1. slim
  http://blog.csdn.net/mao_xiao_feng/article/details/73409975
  slim中实现一个层：

  首先让我们看看tensorflow怎么实现一个层，例如卷积层：

  [python] view plain copy
  input = ...  
  with tf.name_scope('conv1_1') as scope:  
    kernel = tf.Variable(tf.truncated_normal([3, 3, 64, 128], dtype=tf.float32,  
                                             stddev=1e-1), name='weights')  
    conv = tf.nn.conv2d(input, kernel, [1, 1, 1, 1], padding='SAME')  
    biases = tf.Variable(tf.constant(0.0, shape=[128], dtype=tf.float32),  
                         trainable=True, name='biases')  
    bias = tf.nn.bias_add(conv, biases)  
    conv1 = tf.nn.relu(bias, name=scope)  

  然后slim的实现：
  [python] view plain copy
  input = ...  
  net = slim.conv2d(input, 128, [3, 3], scope='conv1_1')  

  但这个不是重要的，因为tenorflow目前也有大部分层的简单实现，这里比较吸引人的是slim中的repeat和stack操作：
  假设定义三个相同的卷积层：

  [python] view plain copy
  net = ...  
  net = slim.conv2d(net, 256, [3, 3], scope='conv3_1')  
  net = slim.conv2d(net, 256, [3, 3], scope='conv3_2')  
  net = slim.conv2d(net, 256, [3, 3], scope='conv3_3')  
  net = slim.max_pool2d(net, [2, 2], scope='pool2')  

  在slim中的repeat操作可以减少代码量：
  [python] view plain copy
  net = slim.repeat(net, 3, slim.conv2d, 256, [3, 3], scope='conv3')  
  net = slim.max_pool2d(net, [2, 2], scope='pool2')  

  而stack是处理卷积核或者输出不一样的情况：
  假设定义三层FC：

  [python] view plain copy
  # Verbose way:  
  x = slim.fully_connected(x, 32, scope='fc/fc_1')  
  x = slim.fully_connected(x, 64, scope='fc/fc_2')  
  x = slim.fully_connected(x, 128, scope='fc/fc_3')  

  使用stack操作：
  [python] view plain copy
  slim.stack(x, slim.fully_connected, [32, 64, 128], scope='fc')  

  同理卷积层也一样：
  [python] view plain copy
  # 普通方法:  
  x = slim.conv2d(x, 32, [3, 3], scope='core/core_1')  
  x = slim.conv2d(x, 32, [1, 1], scope='core/core_2')  
  x = slim.conv2d(x, 64, [3, 3], scope='core/core_3')  
  x = slim.conv2d(x, 64, [1, 1], scope='core/core_4')  

  # 简便方法:  
  slim.stack(x, slim.conv2d, [(32, [3, 3]), (32, [1, 1]), (64, [3, 3]), (64, [1, 1])], scope='core')
  
  
  
  
  
  
  
2.Tensorflow一些常用基本概念与函数（1）
  http://blog.csdn.net/lenbow/article/details/52152766
  

