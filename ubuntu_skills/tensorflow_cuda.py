1）安装tensorflow、cuda、显卡驱动等
  http://city.shaform.com/blog/2016/10/31/install-tensorflow-with-cuda.html
  http://coldmooon.github.io/2015/08/03/caffe_install/
  

2）tensorflow1.3版本
  https://www.tensorflow.org/versions/r1.3/install/install_linux
  sudo pip install tensorflow-gpu==1.3.0

3）
  http://darren1231.pixnet.net/blog/post/328443879-deep-learning-model--caffe-%E4%BD%BF%E7%94%A8%E6%95%99%E5%AD%B8
  
4）Ubuntu 16.04 安装英伟达（Nvidia）显卡驱动
  https://gist.github.com/dangbiao1991/7825db1d17df9231f4101f034ecd5a2b  
  好像可以直接安装cuda

5）pycharm添加环境变量
  pycharm add system Environment Variables:
  Preferences > Console > Python Console > Environment Variables, setting
  sys.path.extend('/usr/local/cuda/lib64')



6）python install opencv
  pip install opencv-python


7）tensorflow讀取大數據
  https://zhuanlan.zhihu.com/p/27238630
  http://blog.csdn.net/qiaohan12345/article/details/52343568
  https://wxinlong.github.io/2017/05/13/tfrecords/
  https://www.zixundingzhi.com/bianchengyuyan/9dd30be9a727b673.html
    
8）如何查看ubuntu下显卡驱动是否已经成功安装
  首先得安装mesa-utils，在终端输入命令：sudo apt-get install mesa-utils
  然后再运行命令：glxinfo | grep rendering
  如果结果是“yes”，证明显卡 驱动已经成功安装。


9）手动挂载U盘
  sudo fdisk -l查看插入的U盘位置，比如 /dev/sdb4
  执行挂载
  sudo mount /dev/sdb4 /media
  cd /media   就可以查看



10）



