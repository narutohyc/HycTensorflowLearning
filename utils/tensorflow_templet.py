# -*- coding: utf-8 -*-
'''
1.運行writeTfrecord2()，生成tensorflow的TFRecord格式的數據

2.運行train()，訓練模型
   
3.運行test()，測試訓練好的模型

'''


from __future__ import division, print_function, absolute_import
from tflearn.layers.core import input_data, dropout, fully_connected
from tflearn.layers.normalization import local_response_normalization
from tflearn.layers.estimator import regression
import os
from os.path import join
import datetime
from tflearn.layers.merge_ops import merge
import tensorflow as tf
from tflearn.layers.conv import conv_2d, max_pool_2d, avg_pool_2d, upsample_2d
from matplotlib.pyplot import savefig
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import skimage.io as io


def print_time(seconds=0):
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    print("      %02d:%02d:%02d" % (h, m, s))


# 二進位資料
def _bytes_feature(value):
    return tf.train.Feature(bytes_list=tf.train.BytesList(value=[value]))


# 整數資料
def _int64_feature(value):
    return tf.train.Feature(int64_list=tf.train.Int64List(value=[value]))


# 浮點數資料
def _float32_feature(value):
    return tf.train.Feature(float_list=tf.train.FloatList(value=value))


# 講數據寫入到tfrdcord文件
def writeTfrecord2(image_file=None, label_file=None, tfrecord_file=None):
    writer = tf.python_io.TFRecordWriter(tfrecord_file)
    image_list = os.listdir(image_file)
    label_list = os.listdir(label_file)
    step = 0
    for image_filename, label_filename in zip(image_list, label_list):
        # 圖取圖檔,io.imread讀出的圖像是uint8 type，此處必須是uint8
        image = io.imread(join(image_file, image_filename))
        height, width, depth = image.shape
        image_string = image.tostring()

        label = io.imread(join(label_file, image_filename[:-4] + '.jpg'))  # deep_img
        label_string = label.tostring()

        # 建立包含多個 Features 的 Example
        example = tf.train.Example(features=tf.train.Features(feature={
            'height': _int64_feature(height),
            'width': _int64_feature(width),
            'depth': _int64_feature(depth),
            'image_string': _bytes_feature(image_string),
            'label_string': _bytes_feature(label_string)}))
        writer.write(example.SerializeToString())
        step = step + 1
        if step % 100 == 0:
            print('%d   write %s sucessful!!!' % (step, join(image_file, image_filename)))
    writer.close()


# 解析單個的數據信息
def read_and_decode(filenames=None, batch_size=2):
    tfrecord_file_queue = tf.train.string_input_producer([filenames], name='queue')
    reader = tf.TFRecordReader()
    _, tfrecord_serialized = reader.read(tfrecord_file_queue)
    tfrecord_features = tf.parse_single_example(tfrecord_serialized,
                                                features={
                                                    'height': tf.FixedLenFeature([], tf.int64),
                                                    'width': tf.FixedLenFeature([], tf.int64),
                                                    'depth': tf.FixedLenFeature([], tf.int64),
                                                    'image_string': tf.FixedLenFeature([], tf.string),
                                                    'label_string': tf.FixedLenFeature([], tf.string)}, name='features')
    # If image was saved as uint8, so we have to decode as uint8.
    image = tf.decode_raw(tfrecord_features['image_string'], tf.uint8)
    label = tf.decode_raw(tfrecord_features['label_string'], tf.uint8)
    width = tf.cast(tfrecord_features['width'], tf.int32)
    height = tf.cast(tfrecord_features['height'], tf.int32)
    depth = tf.cast(tfrecord_features['depth'], tf.int32)

    width_m, height_m, depth_m = 240, 320, 3
    # 此處必須填寫常量數值
    image = tf.reshape(image, (width_m, height_m, depth_m))
    label = tf.reshape(label, (width_m, height_m))
    ##########################################################
    # you can put data augmentation here, I didn't use it
    ##########################################################

    # 打散資料順序
    images, labels = tf.train.shuffle_batch(
            [image, label],
            batch_size=batch_size,
            capacity=30,
            num_threads=1,
            min_after_dequeue=10)
    return images, labels, width, height, depth


def getNet(network=None):
    network = conv_2d(network, 96, 11, strides=4, activation='relu')
    network = max_pool_2d(network, 3, strides=2)
    network = local_response_normalization(network)
    network = conv_2d(network, 256, 5, activation='relu')
    network = max_pool_2d(network, 3, strides=2)
    network = local_response_normalization(network)
    network = conv_2d(network, 384, 3, activation='relu')
    network = conv_2d(network, 384, 3, activation='relu')
    network = conv_2d(network, 256, 3, activation='relu')
    network = max_pool_2d(network, 3, strides=2)
    network = local_response_normalization(network)
    network = fully_connected(network, 200, activation='tanh')
    network = dropout(network, 0.5)
    network = fully_connected(network, 200, activation='tanh')
    network = dropout(network, 0.5)
    network = fully_connected(network, 240 * 320, activation='softmax')
    return network


def train(tfrecord_file=None, model_path=None, log_path=None):
    batch_size = 1
    nSteps = 1000

    images, labels, width, height, depth = read_and_decode(filenames=tfrecord_file, batch_size=batch_size)

    x = tf.placeholder(tf.float32, [None, 240, 320, 3])
    tf.summary.image('input', tf.reshape(x, [-1, 240, 320, 3]))
    y_ = tf.placeholder(tf.float32, [None, 240 * 320])  # writeTfrecord2
    tf.summary.image('label', tf.reshape(y_, [-1, 240, 320, 1]))

    network = getNet(network=x)
    y = tf.nn.softmax(network)

    # loss
    cross_entropy = tf.reduce_mean(-tf.reduce_sum(y_ * tf.log(y), reduction_indices=[1]))
    tf.summary.scalar('loss', cross_entropy)

    # define training step which minimises cross entropy
    train_step = tf.train.GradientDescentOptimizer(1e-4).minimize(cross_entropy)
    # argmax gives index of highest entry in vector (1st axis of 1D tensor)
    correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))

    # get mean of all entries in correct prediction, the higher the better
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
    tf.summary.scalar('accuracy', accuracy)
    summary_op = tf.summary.merge_all()

    # Saver 对象用于保存检查点
    saver = tf.train.Saver(max_to_keep=2)

    if not os.path.exists(model_path):
        os.mkdir(model_path)

    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())
        # summary_writer = tf.summary.FileWriter(join(log_path, 'main_v3'), sess.graph)
        tra_summary_writer = tf.summary.FileWriter(join(log_path, 'train'), sess.graph)
        val_summary_writer = tf.summary.FileWriter(join(log_path, 'val'), sess.graph)
        coord = tf.train.Coordinator()
        threads = tf.train.start_queue_runners(coord=coord)

        initial_step = 0
        ckpt = tf.train.get_checkpoint_state(model_path)
        if ckpt and ckpt.model_checkpoint_path:
            saver.restore(sess, ckpt.model_checkpoint_path)
            initial_step = int(ckpt.model_checkpoint_path.rsplit('-', 1)[1])
            print('Loading model success, global_step is %s' % initial_step)
        else:
            print('No checkpoint file found, so train from initial')

        MAX_STEP = initial_step + nSteps
        try:
            print('training......')
            starttime = datetime.datetime.now()
            for step in range(initial_step, MAX_STEP):
                imgs, labs, wid, hgt, dep = sess.run([images, labels, width, height, depth])
                labs = np.reshape(labs, [-1, 240 * 320])
                _, train_loss, train_acc = sess.run([train_step, cross_entropy, accuracy],
                                                    feed_dict={x: imgs, y_: labs})

                if (step + 1) % 10 == 0 or (step + 1) == MAX_STEP:  # then perform training
                    summary_str = sess.run(summary_op, feed_dict={x: imgs, y_: labs})
                    tra_summary_writer.add_summary(summary_str, step)
                    # summary_writer.add_summary(summary_str)

                if (step + 1) % 20 == 0 or (step + 1) == MAX_STEP:  # then perform validation
                    vimageBatch, vlabelBatch, _, _, _ = sess.run([images, labels, width, height, depth])
                    vlabelBatch = np.reshape(vlabelBatch, [-1, 240 * 320])
                    val_loss, val_acc, summary_str = sess.run([cross_entropy, accuracy, summary_op],
                                                              feed_dict={x: vimageBatch, y_: vlabelBatch})
                    # summary_writer.add_summary(summary_str)
                    val_summary_writer.add_summary(summary_str, step)
                    print("step %d, training accuracy %s    loss %s" % (step + 1, float(val_acc), float(val_loss)))
                # 每 1000 次训练保存检查点一次
                if (step + 1) % 100 == 0 or (step + 1) == MAX_STEP:
                    saver.save(sess, join(model_path, 'dehaze_model.ckpt'), global_step=step)
                    print('Saveing model success, global_step is %s' % step)
            endtime = datetime.datetime.now()
            print('traing time is:')
            print_time((endtime - starttime).seconds)
        except Exception as e:
            coord.request_stop(e)
        finally:
            coord.request_stop()
            coord.join(threads)

    #######################   print images and labels   ######################
    # 展示讀取到的數據
    # da, db = 6, 8
    # f, a = plt.subplots(da, db, figsize=(100, 100))
    # ina = 0
    # inb = 0
    # with tf.Session() as sess:
    #     # sess.run(tf.global_variables_initializer())
    #     coord = tf.train.Coordinator()
    #     threads = tf.train.start_queue_runners(coord=coord)
    #     for _ in range(int(da * db / 2)):
    #         imgs, labs, wid, hgt, dep = sess.run([images, labels, width, height, depth])
    #         print('%d  %d  %d' % (wid, hgt, dep))
    #
    #
    #         a[ina][inb].imshow(np.reshape(labs[0], (240, 320)))
    #         a[ina][inb].set_xticks([])
    #         a[ina][inb].set_yticks([])
    #         inb = inb + 1
    #         if inb % db == 0:
    #             inb = 0
    #             ina = ina + 1
    #
    #         a[ina][inb].imshow(np.reshape(imgs[0], (240, 320, 3)))
    #         a[ina][inb].set_xticks([])
    #         a[ina][inb].set_yticks([])
    #         inb = inb + 1
    #         if inb % db == 0:
    #             inb = 0
    #             ina = ina + 1
    #
    #     coord.request_stop()
    #     coord.join(threads)
    # f.show()
    # plt.draw()
    # plt.waitforbuttonpress()
    ############################################################################
    print('train end!!!')


def test(tfrecord_file=None, model_path=None, log_path=None):
    batch_size = 1
    images, labels, width, height, depth = read_and_decode(filenames=tfrecord_file, batch_size=batch_size)

    x = tf.placeholder(tf.float32, [None, 240, 320, 3])
    tf.summary.image('input', tf.reshape(x, [-1, 240, 320, 3]))

    y_ = tf.placeholder(tf.float32, [None, 240 * 320])  # writeTfrecord2
    tf.summary.image('label', tf.reshape(y_, [-1, 240, 320, 1]))

    network = getNet(network=x)
    y = tf.nn.softmax(network)
    saver = tf.train.Saver(max_to_keep=2)

    da, db = 6, 8
    f, a = plt.subplots(da, db, figsize=(100, 100))
    ina, inb = 0, 0
    nSteps = da * db
    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())
        coord = tf.train.Coordinator()
        threads = tf.train.start_queue_runners(coord=coord)

        ckpt = tf.train.get_checkpoint_state(model_path)
        if ckpt and ckpt.model_checkpoint_path:
            saver.restore(sess, ckpt.model_checkpoint_path)
            print('Loading model success')
        else:
            print('No checkpoint file found, so train from initial')
        try:
            print('testing......')
            for step in range(int(nSteps / 2)):
                imgs, labs, wid, hgt, dep = sess.run([images, labels, width, height, depth])
                predict = sess.run(y, feed_dict={x: imgs})
                labs = np.reshape(labs, [-1, 240 * 320])

                a[ina][inb].imshow(np.reshape(labs[0], (240, 320)))
                a[ina][inb].set_xticks([])
                a[ina][inb].set_yticks([])
                inb = inb + 1
                if inb % db == 0:
                    inb = 0
                    ina = ina + 1

                a[ina][inb].imshow(np.reshape(predict[0], (240, 320)))
                a[ina][inb].set_xticks([])
                a[ina][inb].set_yticks([])
                inb = inb + 1
                if inb % db == 0:
                    inb = 0
                    ina = ina + 1
            f.show()
            plt.draw()
            plt.waitforbuttonpress()
        except Exception as e:
            coord.request_stop(e)
        finally:
            coord.request_stop()
            coord.join(threads)
    print('test end!!!')

def main():
    curpath = os.getcwd()
    himgpath = join(curpath, 'gt_haze_image')
    cimgpath = join(curpath, 'gt_image')
    dimgpath = join(curpath, 'gt_deep_image')
    tfrecord_file = join(curpath, 'main_v3_nyu.tfrecord')
    save_path = join(curpath, 'savedmodel/dehaze')
    log_path = join(curpath, 'log')
    predict_out = join(curpath, 'main_v3_img_predict')

    # writeTfrecord2(image_file=himgpath, label_file=dimgpath, tfrecord_file=tfrecord_file)
    train(tfrecord_file=tfrecord_file, model_path=save_path, log_path=log_path)
    # test(tfrecord_file=tfrecord_file, model_path=save_path, log_path=log_path)

if __name__ == '__main__':
    main()



