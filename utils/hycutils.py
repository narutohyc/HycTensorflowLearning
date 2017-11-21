# -*- coding: utf-8 -*-

""" 17 Category Flower Dataset

Credits: Maria-Elena Nilsback and Andrew Zisserman.
http://www.robots.ox.ac.uk/~vgg/data/flowers/17/

"""
from __future__ import absolute_import, print_function

import os
import sys
from six.moves import urllib
import tarfile
import math
from skimage import color
import cv2
import time
import numpy as np
import pickle
from tflearn.data_utils import *
import matplotlib.pyplot as plt
from os.path import join


def shuffledata(*arrs):
    """ shuffle.
    Shuffle given arrays at unison, along first axis.
    Arguments:
        *arrs: Each array to shuffle at unison.
    Returns:
        Tuple of shuffled arrays.
    """
    arrs = list(arrs)
    for i, arr in enumerate(arrs):
        assert len(arrs[0]) == len(arrs[i])
        arrs[i] = np.array(arr)
    p = np.random.permutation(len(arrs[0]))
    return tuple(arr[p] for arr in arrs)


# dirname is the path of your images
def load_data_old(dirname=None, resize_pics=(227, 227), shuffle=True,
                  one_hot=False, pklname='default.pkl'):
    dataset_file = os.path.join(dirname, pklname)
    # if not os.path.exists(dataset_file):
    #    tarpath = maybe_download("17flowers.tgz",
    #                             "http://www.robots.ox.ac.uk/~vgg/data/flowers/17/",
    #                             dirname)
    image_path = dirname  # os.path.join(dirname, 'jpg/')
    X, Y = build_image_dataset_from_dir(image_path,
                                        dataset_file=dataset_file,
                                        resize=resize_pics,
                                        filetypes=['.jpg', '.jpeg'],
                                        convert_gray=False,
                                        shuffle_data=shuffle,
                                        categorical_Y=one_hot)
    return X, Y


# dirname is the path of your images
def load_data(dirname=None, resize_pics=(227, 227), shuffle=True,
              one_hot=False, pklname='default.pkl'):
    '''
    Args:
        dirname:图像父路径，默认images  例如：path/1/1.img   path/1/2.img   path/2/4.img
        resize_pics:图像resize尺寸
        shuffle:是否乱序，默认乱序
        one_hot:是否one_hot编码，默认否
        pklname:生成数据集的名称，默认default.pkl，会放在dirname路径下
    Returns:X,Y表示分割好图像与对应标签，可在tensorflow中使用的数据格式
    '''
    dataset_file = os.path.join(dirname, pklname)
    # if not os.path.exists(dataset_file):
    #    tarpath = maybe_download("17flowers.tgz",
    #                             "http://www.robots.ox.ac.uk/~vgg/data/flowers/17/",
    #                             dirname)
    image_path = dirname  # os.path.join(dirname, 'jpg/')
    X, Y = build_image_dataset_from_dir(image_path,
                                        dataset_file=dataset_file,
                                        resize=resize_pics,
                                        filetypes=['.jpg', '.jpeg'],
                                        convert_gray=False,
                                        shuffle_data=shuffle,
                                        categorical_Y=one_hot)
    return X, Y


def load_data_nopkl(dirname=None, resize_pics=(227, 227), shuffle=True, one_hot=False, pklname='default.pkl',
                    istag=False):
    '''
    :param dirname: 图像数据的路径
    :param resize_pics: 图像resize尺寸
    :param shuffle: 是否乱序
    :param one_hot: 是否进行one_hot编码
    :param pklname: pkl文件名，此处没有使用
    :param istag: 是否进行抽样测试，默认每类数据集取张图像
    :return: 图像数据，图像便签，图像数量
    '''
    X = []
    Y = []
    imgnum = 0
    imgdic = os.listdir(dirname)
    classnum = 0
    for imgd in imgdic:
        # 防止计算pkl文件
        if imgd[-1] != 'l':
            classnum = classnum + 1

    for imgd in imgdic:
        if imgd[-1] != 'l':
            imgpath = join(dirname, imgd)
            imglist = os.listdir(imgpath)
            tag = 0
            for imgl in imglist:
                imgnum = imgnum + 1
                # 读取图像
                img = plt.imread(join(imgpath, imgl))
                # 图像预处理
                img = cv2.resize(img, resize_pics) / 255.0
                # 获取当前图像的标签
                label = int(os.path.splitext(join(imgpath, imgl).split('/')[-2])[0])
                X.append(img)
                if one_hot == True:
                    temp = [0 for _ in range(classnum)]
                    temp[label] = 1
                    Y.append(temp)
                else:
                    Y.append(label)
                tag = tag + 1
                if tag == 5 and istag == True:
                    break
    if shuffle == True:
        X, Y = shuffledata(X, Y)
    return X, Y, imgnum


def maybe_download(filename, source_url, work_directory):
    if not os.path.exists(work_directory):
        os.mkdir(work_directory)
    filepath = os.path.join(work_directory, filename)
    if not os.path.exists(filepath):
        print("Downloading Oxford 17 category Flower Dataset, Please "
              "wait...")
        filepath, _ = urllib.request.urlretrieve(source_url + filename,
                                                 filepath, reporthook)
        statinfo = os.stat(filepath)
        print('Succesfully downloaded', filename, statinfo.st_size, 'bytes.')

        untar(filepath, work_directory)
        build_class_directories(os.path.join(work_directory, 'jpg'))
    return filepath


# reporthook from stackoverflow #13881092
def reporthook(blocknum, blocksize, totalsize):
    readsofar = blocknum * blocksize
    if totalsize > 0:
        percent = readsofar * 1e2 / totalsize
        s = "\r%5.1f%% %*d / %d" % (
            percent, len(str(totalsize)), readsofar, totalsize)
        sys.stderr.write(s)
        if readsofar >= totalsize:  # near the end
            sys.stderr.write("\n")
    else:  # total size is unknown
        sys.stderr.write("read %d\n" % (readsofar,))


# 构建图像分类文件夹 每80张为一类
def build_class_directories(dir):
    dir_id = 0
    class_dir = os.path.join(dir, str(dir_id))
    if not os.path.exists(class_dir):
        os.mkdir(class_dir)
    for i in range(1, 1361):
        fname = "image_" + ("%.4i" % i) + ".jpg"
        # this operation can move image_a to /num/image_a, maybe it looks like rename, but actually it do move
        os.rename(os.path.join(dir, fname), os.path.join(class_dir, fname))
        if i % 80 == 0 and dir_id < 16:
            dir_id += 1
            class_dir = os.path.join(dir, str(dir_id))
            os.mkdir(class_dir)


# untar tarfile
def untar(fname, extract_dir):
    if fname.endswith("tar.gz") or fname.endswith("tgz"):
        tar = tarfile.open(fname)
        tar.extractall(extract_dir)
        tar.close()
        print("File Extracted")
    else:
        print("Not a tar.gz/tgz file: '%s '" % sys.argv[0])


# 将在同一文件夹下的图像移动到各自的文件夹下，如c0_img_104.jpg -> 0/img_104.jpg
def images2Class(imagesPath='/home/hyc/tflearn/examples/images/alexNetDriver/imgtest/test5000_256'):
    images = os.listdir(imagesPath)
    for image in images:
        class_dir = os.path.join(imagesPath, image[1])
        if not os.path.exists(class_dir):
            os.mkdir(class_dir)
        os.rename(os.path.join(imagesPath, image), os.path.join(class_dir, image[3:]))


# 调整imagespath文件夹下，各分类子文件下所有图像的亮度，并保存为img_104.jpg -> img_104_x.jpg
def brightnessAdjustment(imagespath=None, scale=None):
    '''
    imagespath：图像路径
    scale：亮度比例，需要一个数组[0.4,0.7,2]

    调用案例：
    trainImagePath = '/home/hyc/tflearn/examples/images/alexNetDriver/train17408_256_l_2368'
    scale = [0.4,0.7,2]
    brightnessAdjustment(imagespath=trainImagePath,scale=scale)
    '''
    imageFirst = os.listdir(imagespath)
    for imagefirst in imageFirst:
        imageSecond = os.listdir(os.path.join(imagespath, imagefirst))
        for imagesecond in imageSecond:
            imagepath = os.path.join(imagespath, imagefirst, imagesecond)
            # 读取图片B，G，R，返回一个ndarray类型，此处理解有误，个人认为读入应该为R,G,B，建议显示看看
            img = cv2.imread(imagepath, cv2.IMREAD_COLOR)
            # rgb2hsv
            img_hsv = color.rgb2hsv(img)
            for i in range(len(scale)):
                # 调整亮度，注意！！！此处矩阵应进行深拷贝
                temp_img_hsv = img_hsv.copy()
                temp_img_hsv[:, :, 2] = temp_img_hsv[:, :, 2] * scale[i]
                # hsv2rgb
                img_rgb = color.hsv2rgb(temp_img_hsv) * 255
                # 保存文件
                cv2.imwrite('%s_%s.jpg' % (imagepath[:len(imagepath) - 4], i), img_rgb)
                print(imagepath + '  sucessful!!!')
        print(imagefirst + '  sucessful!!!')
    print('1')


# 调整imagespath文件夹下，各分类子文件下所有图像的亮度，并保存为img_104.jpg -> curpath+scale[i]/0/img_104_x.jpg
def brightnessAdByOneself(imagespath=None, scale=None, curpath=None):
    '''
    imagespath：图像路径
    scale：亮度比例，需要一个数组[0.4,0.7,2]
    curpath:表示当前图像处理完要保存的父路径

    调用案例：
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    trainImagePath = join(curpath, 'alexNetDriver/train17408cr')
    scale = [0.4, 0.7, 1.5, 2]
    brightnessAdByOneself(imagespath=trainImagePath, scale=scale, curpath=curpath)
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    print('end')
    '''
    imageFirst = os.listdir(imagespath)
    for imagefirst in imageFirst:
        imageSecond = os.listdir(os.path.join(imagespath, imagefirst))
        for imagesecond in imageSecond:
            imagepath = os.path.join(imagespath, imagefirst, imagesecond)
            # 读取图片B，G，R，返回一个ndarray类型，此处理解有误，个人认为读入应该为R,G,B，建议显示看看
            img = cv2.imread(imagepath, cv2.IMREAD_COLOR)
            # rgb2hsv
            img_hsv = color.rgb2hsv(img)
            for i in range(len(scale)):
                # 调整亮度，注意！！！此处矩阵应进行深拷贝
                temp_img_hsv = img_hsv.copy()
                temp_img_hsv[:, :, 2] = temp_img_hsv[:, :, 2] * scale[i]
                # hsv2rgb
                img_rgb = color.hsv2rgb(temp_img_hsv) * 255

                if not os.path.exists(join(curpath, 'alexNetDriver/train17408cr' + str(scale[i]))):
                    os.mkdir(join(curpath, 'alexNetDriver/train17408cr' + str(scale[i])))
                if not os.path.exists(join(join(curpath, 'alexNetDriver/train17408cr' + str(scale[i])), imagefirst)):
                    os.mkdir(join(join(curpath, 'alexNetDriver/train17408cr' + str(scale[i])), imagefirst))

                # 保存文件
                savepath = join(join(join(curpath, 'alexNetDriver/train17408cr' + str(scale[i])), imagefirst),
                                imagesecond)
                cv2.imwrite(savepath, img_rgb)
                print(imagepath + '  sucessful!!!')
        print(imagefirst + '  sucessful!!!')
    print('1')


# 把curdir下每個文件夾下的圖像剪切和縮放，並放到imagepath+'cr'下
# curdir/0/img->imagepath+'cr'/0/img
def imgcutAndresize(curdir=None, imagepath=None):
    # get current path
    # curpath = os.getcwd()
    # curpath = '/home/hyc/code/driverdataset/train'
    # imagepath = 'train17408'
    # imgcutAndresize(curpath, imagepath)

    # imagepath = 'test5000'
    # imgcutAndresize(curpath, imagepath)
    # create curpath/train17408cut
    savedir = imagepath + 'cr'
    if not os.path.exists(join(curdir, savedir)):
        os.mkdir(join(curdir, savedir))

    imgdir = join(curdir, imagepath)
    imglist = os.listdir(imgdir)
    for imgl in imglist:
        tuxiang = join(imgdir, imgl)
        tlist = os.listdir(tuxiang)
        if not os.path.exists(join(join(curdir, savedir), imgl)):
            os.mkdir(join(join(curdir, savedir), imgl))
        for t in tlist:
            image = cv2.imread(join(tuxiang, t))
            w = image.shape[0]
            h = image.shape[1]
            if w > h:
                t = w
                w = h
                h = t
            # 剪切圖像爲正方形
            image = image[:, (h - w) / 2:h - 80, ]
            savepath = join(join(join(curdir, savedir), imgl), t)
            # 圖像做resize，並保存圖像
            cv2.imwrite(savepath, cv2.resize(image, (256, 256)))


# 把curdir下每個文件夾下的圖像剪切和縮放，並放到imagepath+'cr'下
# curdir/imgs->imagepath+'cr'/imgs
def testimgcutAndresize(curdir=None, imagepath=None):
    # curpath = '/home/hyc/code/driverdataset'
    # imagepath = 'test'
    # testimgcutAndresize(curpath, imagepath)
    # create curpath/train17408cut
    savedir = imagepath + 'cr'
    if not os.path.exists(join(curdir, savedir)):
        os.mkdir(join(curdir, savedir))

    imgdir = join(curdir, imagepath)
    imglist = os.listdir(imgdir)
    for imgl in imglist:
        tuxiang = join(imgdir, imgl)
        image = cv2.imread(tuxiang)
        w = image.shape[0]
        h = image.shape[1]
        if w > h:
            t = w
            w = h
            h = t
        # 剪切圖像爲正方形
        image = image[:, (h - w) / 2:h - 80, ]
        savepath = join(join(curdir, savedir), imgl)
        # 圖像做resize，並保存圖像
        cv2.imwrite(savepath, cv2.resize(image, (256, 256)))


def valNet(size=227, pad=0, kernel=1, stride=1):
    net = []
    net.append([1, 227, 227, 3])
    '''
    net.append([ ])
    for i in range(net):
        size =
        pad =
        stride =
        kernel =
        print(round((size+2*pad-kernel)/1.0/stride-0.5)+1)
    '''
    return round((size + 2 * pad - kernel) / 1.0 / stride - 0.5) + 1


# 將秒數轉換成hh:mm:ss的形式
def secondsToDate(senconds):
    day = 24 * 60 * 60
    hour = 60 * 60
    min = 60
    if senconds < 60:
        return "%d sec" % math.ceil(senconds)
    elif senconds > day:
        days = divmod(senconds, day)
        return "%d days, %s" % (int(days[0]), secondsToDate(days[1]))
    elif senconds > hour:
        hours = divmod(senconds, hour)
        return '%d hours, %s' % (int(hours[0]), secondsToDate(hours[1]))
    else:
        mins = divmod(senconds, min)
        return "%d mins, %d sec" % (int(mins[0]), math.ceil(mins[1]))


if __name__ == '__main__':
    pass
    valNet()

    # get current path
    curpath = os.getcwd()
    # curpath = '/home/hyc/code/driverdataset/train'
    # imagepath = 'train17408'
    # imgcutAndresize(curpath, imagepath)

    # imagepath = 'test5000'
    # imgcutAndresize(curpath, imagepath)


    # curpath = '/home/hyc/code/driverdataset'
    # imagepath = 'test'
    # testimgcutAndresize(curpath, imagepath)



    # testImagePath = '/home/hyc/tflearn/examples/images/alexNetDriver/test5000_256'
    # images2Class(testImagePath)
    # print('over!')

    # trainImagePath = '/home/hyc/tflearn/examples/images/alexNetDriver/train17408_256'
    # images2Class(trainImagePath)
    # print('over!')


    # print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    # trainImagePath = join(curpath, 'alexNetDriver/train17408cr')
    # scale = [0.4, 0.7, 1.5, 2]
    # brightnessAdByOneself(imagespath=trainImagePath, scale=scale, curpath=curpath)
    # print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    # print('end')

    # '''
