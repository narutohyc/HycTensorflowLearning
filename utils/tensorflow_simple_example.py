import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

mnist = input_data.read_data_sets("MINIST_data/",one_hot=True)
sess = tf.InteractiveSession()

def weight_variable(shape):
	inital = tf.truncated_normal(shape,stddev=0.1)
	return inital
	
def bias_variable(shape):
	inital = tf.constant(0.1,shape=shape)
	return tf.Variable(inital)
	
def conv2d(x,W):
	return tf.nn.conv2d(x,W,strides=[1,1,1,1],padding='SAME')
	
def max_pool_2x2(x):
	return tf.nn.max_pool(x,ksize=[1,2,2,1],strides=[1,2,2,1],padding='SAME')
	
if __name__ == "__main__":
	x = tf.placeholder(tf.float32,[None,784])
	y_ = tf.placeholder(tf.float32,[None,10])
	x_image = tf.reshape(x,[-1,28,28,1])    # 28*28
	
	# first floor
	w_conv1 = weight_variable([5,5,1,32])
	b_conv1 = bias_variable([32])
	h_conv1 = tf.nn.relu(conv2d(x_image,w_conv1)+b_conv1)	# 28*28*32
	h_pool1 = max_pool_2x2(h_conv1)   #14*14*32
	
	# second floor
	w_conv2 = weight_variable([5,5,32,64])   
	b_conv2 = bias_variable([64])
	h_conv2 = tf.nn.relu(conv2d(h_pool1,w_conv2)+b_conv2)  # 14*14*64
	h_pool2 = max_pool_2x2(h_conv2)    # 7*7*64
	
	# full connection
	w_fc1 = weight_variable([7*7*64,1024])  
	b_fc1 = bias_variable([1024])
	h_bool2_flat = tf.reshape(h_pool2,[-1,7*7*64])
	h_fc1 = tf.nn.relu(tf.matmul(h_bool2_flat,w_fc1)+b_fc1)
	
	# dropout
	keep_prob = tf.placeholder(tf.float32)
	h_fc1_drop = tf.nn.dropout(h_fc1,keep_prob)
	
	# softmax
	w_fc2 = weight_variable([1024,10])
	b_fc2 = bias_variable([10])
	y_conv = tf.nn.softmax(tf.matmul(h_fc1_drop,w_fc2)+b_fc2)
	
	# cost function
	cross_entropy = tf.reduce_mean(-tf.reduce_sum(y_*tf.log(y_conv),reduction_indices=[1]))
	train_step = tf.train.AdamOptimizer(1e-4).minimize(cross_entropy)
	y_conv = tf.nn.softmax(tf.matmul(h_fc1_drop,w_fc2)+b_fc2)
	
	correct_prediction = tf.equal(tf.argmax(y_conv,1),tf.argmax(y_,1))
	accuracy = tf.reduce_mean(tf.cast(correct_prediction,tf.float32))
	
	tf.global_variables_initializer().run()
	
	for i in range(20000):
		batch = mnist.train.next_batch(50)
		if i%50 == 0:
			train_accuracy = accuracy.eval(feed_dict={x:batch[0],y_:batch[1],keep_prob:1})
			print("step %d,training accuracy %g" % (i,train_accuracy))
		train_step.run(feed_dict={x:batch[0],y_:batch[1],keep_prob:0.5})
	
	print("test accuracy %g" % accuracy.eval(feed_dict={x:mnist.test.images,y_:mnist.test.labels,keep_prob:1.0}))
