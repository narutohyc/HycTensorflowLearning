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
  
2018-03-09	15:00	性功能障礙與前列腺肥大保養	鍾旭東醫師 亞東紀念醫院

2018-03-16	14:00	這堂課上的叫掙錢	周正哲 經理 芸享科技有限公司

2018-03-23	14:00	世界網路戰部隊簡介	郭凡彬 課長 網路戰聯隊
軍方負責網路攻防、駭客滲透防護的「網路戰大隊」，向來被視為軍方極機密的軍事單位之一，但在新政府規劃設立資電「第四軍種」政策目標下，「網路戰大隊」已在軍方巧妙的安排下亮相，測試社會各界對「台灣網軍」的支持程度。





2018-03-30	14:00	The Tor Network - 這些年我們一起走過的不為人知的網路	廖威捷 工程師 IBM Security
暗网这个原本局限在IT行业和部分非法业务群体中的名词，在2017年因为中国访美学者章莹颖遇害第一次如此广泛的被大众所认知。对于多数人而言，暗网是一个可怕的地方，它甚至一定程度上导致了犯罪行为的发生。
暗网和深网实际上都是从英文翻译来的，暗网即dark Darknet或Dark Web；深网则译为Deep Web、Dark Web。从概念来讲，暗网是指需要通过特殊软件、特殊授权、或对电脑做特殊设置才能连上的网络；深网的概念是指互联网上那些不能被标准搜索引擎索引的非表面网络内容。简单来说，暗网是深网的一个子集。
对暗网有过了解的人应该都听过类似的表述：在网络世界也有着一套冰山理论。即我们平时能看到的网络（或者说互联网）只占整个网络中的4%-5%，也可以称之为"明网"，超过整个数据量的95%都隐藏在冰山之下，在冰山之下，存在着很多见不得光的东西，包括暴力、犯罪……
暗网也被称作"隐藏的服务器"，其域名数量达到表层网络的400-500倍。像纸牌屋中形容的那样："96%的互联网数据无法通过标准搜索引擎访问，虽然其中的大部分属于无用信息，但那上面有一切东西，儿童贩卖、比特币洗钱、致幻剂、大麻、赏金黑客……"
Deep Web这个称呼开始并不是这样，由于普通的途径看不到，而对于有办法的人又能看到，所以最开始的称呼叫不可见网络，这个称呼不太准确，在2001年的时候，博格曼第一次用了Deep Web这个词来形容，中文一般来说叫暗网
1996年，美国海军研究试验所的科学家们提交了一篇论文，题目是《隐藏路径信息》，提出打造一个隐秘系统的构想，这个系统会让任何使用者在连接互联网时都会实时处于匿名状态，而不会向服务器泄露身份。这个系统建设十分有必要，一来可以保护各个国家的政见异己者，逃脱各个国家的专制压迫，普及美国人眼中的普世民主；二来能够为美国的情报人员提供信息交流的安全之所。

2003年10月，这一想法开始正式实施，为使用者提供免费的匿名网上场所。由于保护数据的密码就像洋葱一样层层包裹，这个系统最终被称为Tor（The Onion Router）。直到2011年，其60%资金仍来自美国政府。刚开始，它也的确为持不同政见者提供了庇护，但让美国政府尴尬的是，这个系统很快就开始堕落，成为了犯罪分子的天堂。2006年初，一个名叫“农贸市场”的网站开始出售大麻和克他命；臭名昭著的“丝绸之路”网站也是于2011年发源于Tor，用户可以在这里购买毒品、枪支和各种其他非法物品，最终由美国FBI亲自出面，花了一年多时间才剿灭。





2018-04-20	14:00	Maybe five years later...	謝長鴻工程師 新思科技股份有限公司(Synopsys)

2018-05-04	19:00	Reducing IC aging: From Circuit to System	林英超博士 國立成功大學資工系
电子产品长时间使用就会老化，这是由于许多环境因素造成的，如潮湿、灰尘、温度、振动、光照、昆虫等等。从而会有使用障碍，造成失效。
    电子产品中机壳大部分为塑料制品，当受到各种环境因素影响时，老化也是必然的了。线路板长期不通电使用，当受到环境中湿度、灰尘、昆虫等影响，如电线就会老化，焊接点极易腐蚀，电阻和电容等元件内部也会发生变化，产生失效。
    所以，人们会对一些不常用的电器产品时不时通电运行一下，这也是有一定道理的。另外，电子产品制造过成中，厂家也会针对产品进行全方位的老化测试，掌握其老化时间，为提高产量及质量，降低器件成本，提高产品的竟争力等打下坚实的基础。
    东西都是有使用寿命的，基本理论上的使用寿命比实际使用寿命时间长，理论上的参数都是在理想环境下的损耗时长。而在实际使用中，影响因素有很多，灰尘，杂物，温度，湿度。每一种电子元件都是有温度的工作范围。长期在工作温度范围以外工作，整体电路的性能没有保证，器件的参数会发生变化甚至失去其原有的功能（就是烧了）。电路板很坚强基本上都能坚持到有些元件先坏。基本上电路板上的元件也分级别有工业级，商业级，军品。质量好的会用的时间长点，配一块板子不一定都用好的元件。除非特殊情况，质量差的肯定坏在前面。








https://github.com/sekilab/RoadDamageDetector/blob/master/RoadDamageDatasetTutorial.ipynb
https://bdc2018.mycityreport.net/data/
https://www.kdnuggets.com/2018/02/ieee-2018-big-data-cup.html



