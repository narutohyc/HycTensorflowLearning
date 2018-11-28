Jupyter Notebook介绍、安装及使用教程 - 知乎知乎 \- 有问题上知乎if (window.requestAnimationFrame) { window.requestAnimationFrame(function() { window.FIRST\_ANIMATION\_FRAME = Date.now(); }); }

[](//www.zhihu.com)

写文章

![Jupyter Notebook介绍、安装及使用教程](https://pic3.zhimg.com/v2-637604b9f9fe566bac65ff3f44c184af_1200x500.jpg)

Jupyter Notebook介绍、安装及使用教程
==========================

[![豆豆](https://pic2.zhimg.com/v2-45a1bf36532957955f7ab01a4458cbbc_xs.jpg)](//www.zhihu.com/people/raxxie)

[豆豆](//www.zhihu.com/people/raxxie)

热爱生活。

268 人赞了该文章

![](https://pic1.zhimg.com/v2-ffad61af265d2f2fa0becd65205d3cc4_b.jpg)

![](data:image/svg+xml;utf8,<svg%20xmlns='http://www.w3.org/2000/svg'%20width='10836'%20height='7264'></svg>)

目录

* * *

**一、什么是Jupyter Notebook？**
--------------------------

**1\. 简介**
----------

> Jupyter Notebook是基于网页的用于交互计算的应用程序。其可被应用于全过程计算：开发、文档编写、运行代码和展示结果。——[Jupyter Notebook官方介绍](http://link.zhihu.com/?target=https%3A//jupyter-notebook.readthedocs.io/en/stable/notebook.html)

简而言之，Jupyter Notebook是以网页的形式打开，可以在网页页面中**直接编写代码**和**运行代码**，代码的**运行结果**也会直接在代码块下显示的程序。如在编程过程中需要编写说明文档，可在同一个页面中直接编写，便于作及时的说明和解释。

**2\. 组成部分**
------------

**① 网页应用**
----------

网页应用即基于网页形式的、结合了编写说明文档、数学公式、交互计算和其他富媒体形式的工具。**简言之，网页应用是可以实现各种功能的工具。**

**② 文档**
--------

即Jupyter Notebook中所有交互计算、编写说明文档、数学公式、图片以及其他富媒体形式的输入和输出，都是以文档的形式体现的。

这些文档是保存为后缀名为`.ipynb`的`JSON`格式文件，不仅便于版本控制，也方便与他人共享。

此外，文档还可以导出为：HTML、LaTeX、PDF等格式。

**3\. Jupyter Notebook的主要特点**
-----------------------------

① 编程时具有**语法高亮**、_缩进_、_tab补全_的功能。

② 可直接通过浏览器运行代码，同时在代码块下方展示运行结果。

③ 以富媒体格式展示计算结果。富媒体格式包括：HTML，LaTeX，PNG，SVG等。

④ 对代码编写说明文档或语句时，支持Markdown语法。

⑤ 支持使用LaTeX编写数学性说明。

**二、安装Jupyter Notebook**
------------------------

**0\. 先试用，再决定**
---------------

如果看了以上对Jupyter Notebook的介绍你还是拿不定主意究竟是否适合你，那么不要担心，你可以先**免安装试用体验**一下，[戳这里](http://link.zhihu.com/?target=https%3A//try.jupyter.org/)，然后再做决定。

值得注意的是，官方提供的同时试用是有限的，如果你点击链接之后进入的页面如下图所示，那么不要着急，过会儿再试试看吧。

![](https://pic3.zhimg.com/v2-b33e494528f00be39032485fcafdf942_b.jpg)

![](data:image/svg+xml;utf8,<svg%20xmlns='http://www.w3.org/2000/svg'%20width='1436'%20height='618'></svg>)

试用满线

如果你足够幸运，那么你将看到如下界面，就可以开始体验啦。

![](https://pic3.zhimg.com/v2-d07ddde1d96cd3a71a5ecffe738907c2_b.jpg)

![](data:image/svg+xml;utf8,<svg%20xmlns='http://www.w3.org/2000/svg'%20width='2332'%20height='1378'></svg>)

主界面

![](https://pic2.zhimg.com/v2-8fa489d28f5c0aa29e78dc63116b0591_b.jpg)

![](data:image/svg+xml;utf8,<svg%20xmlns='http://www.w3.org/2000/svg'%20width='2004'%20height='1774'></svg>)

编辑页面

**1\. 安装**
----------

**① 安装前提**
----------

安装Jupyter Notebook的前提是需要安装了Python（3.3版本及以上，或2.7版本）。

**② 使用Anaconda安装**
------------------

如果你是小白，那么建议你通过安装Anaconda来解决Jupyter Notebook的安装问题，因为Anaconda已经自动为你安装了Jupter Notebook及其他工具，还有python中超过180个科学包及其依赖项。

你可以通过进入Anaconda的[官方下载页面](http://link.zhihu.com/?target=https%3A//www.anaconda.com/download/%23macos)自行选择下载；如果你对阅读**英文文档**感到头痛，或者对**安装步骤**一无所知，甚至也想快速了解一下**什么是Anaconda**，那么可以前往我的另一篇文章：

[豆豆：Anaconda介绍、安装及使用教程​zhuanlan.zhihu.com![图标](https://pic2.zhimg.com/v2-4ec3ac92a0051720dbf20f626dd44fb1_180x120.jpg)](https://zhuanlan.zhihu.com/p/32925500)

你想要的，都在里面！

常规来说，安装了Anaconda发行版时已经自动为你安装了Jupyter Notebook的，但如果没有自动安装，那么就在终端（Linux或macOS的“终端”，Windows的“Anaconda Prompt”，以下均简称“终端”）中输入以下命令安装：

    conda install jupyter notebook
    

**③ 使用pip命令安装**
---------------

如果你是有经验的Python玩家，想要尝试用pip命令来安装Jupyter  
Notebook，那么请看以下步骤吧！接下来的命令都输入在终端当中的噢！

**1\. 把pip升级到最新版本**

*   Python 3.x

    pip3 install --upgrade pip
    

*   Python 2.x

    pip install --upgrade pip
    

*   注意：老版本的pip在安装Jupyter Notebook过程中或面临依赖项无法同步安装的问题。因此**强烈建议**先把pip升级到最新版本。

**2\. 安装Jupyter Notebook**

*   Python 3.x

    pip3 install jupyter
    

*   Python 2.x

    pip install jupyter
    

**三、运行Jupyter Notebook**
------------------------

**0\. 帮助**
----------

如果你有任何jupyter notebook命令的疑问，可以考虑查看官方帮助文档，命令如下：

    jupyter notebook --help
    

或

    jupyter notebook -h
    

**1\. 启动**
----------

**① 默认端口启动**
------------

在终端中输入以下命令：

    jupyter notebook
    

执行命令之后，在终端中将会显示一系列notebook的服务器信息，同时浏览器将会自动启动Jupyter Notebook。

启动过程中终端显示内容如下：

    $ jupyter notebook
    [I 08:58:24.417 NotebookApp] Serving notebooks from local directory: /Users/catherine
    [I 08:58:24.417 NotebookApp] 0 active kernels
    [I 08:58:24.417 NotebookApp] The Jupyter Notebook is running at: http://localhost:8888/
    [I 08:58:24.417 NotebookApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
    

*   注意：之后在Jupyter Notebook的所有操作，都请保持终端**不要关闭**，因为一旦关闭终端，就会断开与本地服务器的链接，你将无法在Jupyter Notebook中进行其他操作啦。

浏览器地址栏中默认地将会显示：`http://localhost:8888`。其中，“localhost”指的是本机，“8888”则是端口号。

![](https://pic3.zhimg.com/v2-3e14e522a5634717c566006702ca681e_b.jpg)

![](data:image/svg+xml;utf8,<svg%20xmlns='http://www.w3.org/2000/svg'%20width='1439'%20height='226'></svg>)

URL

如果你**同时**启动了多个Jupyter Notebook，由于默认端口“8888”被占用，因此地址栏中的数字将从“8888”起，每多启动一个Jupyter Notebook数字就加1，如“8889”、“8890”……

**② 指定端口启动**
------------

如果你想自定义端口号来启动Jupyter Notebook，可以在终端中输入以下命令：

    jupyter notebook --port <port_number>
    

其中，“<port_number>”是自定义端口号，直接以数字的形式写在命令当中，数字两边不加尖括号“<>”。如：`jupyter notebook --port 9999`，即在端口号为“9999”的服务器启动Jupyter Notebook。

**③ 启动服务器但不打开浏览器**
------------------

如果你只是想启动Jupyter Notebook的服务器但不打算立刻进入到主页面，那么就无需立刻启动浏览器。在终端中输入：

    jupyter notebook --no-browser
    

此时，将会在终端显示启动的服务器信息，并在服务器启动之后，显示出打开浏览器页面的链接。当你需要启动浏览器页面时，只需要复制链接，并粘贴在浏览器的地址栏中，轻按回车变转到了你的Jupyter Notebook页面。

![](https://pic3.zhimg.com/v2-e43d4ba2c2a8c2cdcb6da3afeb0e1bca_b.jpg)

![](data:image/svg+xml;utf8,<svg%20xmlns='http://www.w3.org/2000/svg'%20width='894'%20height='567'></svg>)

例图中由于在完成上面内容时我同时启动了多个Jupyter Notebook，因此显示我的“8888”端口号被占用，最终分配给我的是“8889”。

**2\. 主页面**
-----------

**① 主页面内容**
-----------

当执行完启动命令之后，浏览器将会进入到Notebook的主页面，如下图所示。

![](https://pic2.zhimg.com/v2-32443bb8f73158ef24acd0c0bdf93ce5_b.jpg)

![](data:image/svg+xml;utf8,<svg%20xmlns='http://www.w3.org/2000/svg'%20width='1440'%20height='789'></svg>)

默认主页面

如果你的主页面里边的文件夹跟我的不同，或者你在疑惑为什么首次启动里边就已经有这么多文件夹，不要担心，这里边的文件夹全都是你的家目录里的目录文件。你可以在终端中执行以下2步来查看：

① `cd` 或 `cd -` 或 `cd ~` 或`cd /Users/<user_name>`

*   这个命令将会进入你的家目录。
*   “<user_name>” 是用户名。用户名两边不加尖括号“<>”。

② `ls`

*   这个命令将会展示你家目录下的文件。

**② 设置Jupyter Notebook文件存放位置**
------------------------------

如果你不想把今后在Jupyter Notebook中编写的所有文档都直接保存在家目录下，那你需要修改Jupyter Notebook的文件存放路径。

**⑴ 创建文件夹/目录**
--------------

*   Windows用户在想要存放Jupyter Notebook文件的**磁盘**中**新建文件夹**并为该文件夹命名；双击进入该文件夹，然后复制地址栏中的路径。
*   Linux/macOS用户在想要存放Jupyter Notebook文件的位置**创建目录**并为目录命名，命令为：`mkdir <directory_name>`；进入目录，命令为：`cd <directory_name>`；查看目录的路径，命令为：`pwd`；复制该路径。
*   注意：“<directory_name>”是自定义的目录名。目录名两边不加尖括号“<>”。

**⑵ 配置文件路径**
------------

*   一个便捷获取配置文件所在路径的命令：

    jupyter notebook --generate-config
    

*   注意： 这条命令虽然可以用于查看配置文件所在的路径，但主要用途是是否将这个路径下的配置文件**替换**为**默认配置文件**。 如果你是第一次查询，那么**或许**不会出现下图的提示；若文件已经存在或被修改，使用这个命令之后会出现询问“Overwrite /Users/raxxie/.jupyter/jupyter\_notebook\_config.py with default config? \[y/N\]”，即“用默认配置文件覆盖此路径下的文件吗？”，如果按“y”，则完成覆盖，那么之前所做的修改都将失效；如果只是为了查询路径，那么一定要输入“N”。

![](https://pic4.zhimg.com/v2-da0d33d371c00fe08985cbce2b23bcc7_b.jpg)

![](data:image/svg+xml;utf8,<svg%20xmlns='http://www.w3.org/2000/svg'%20width='719'%20height='112'></svg>)

配置文件所在路径

常规的情况下，Windows和Linux/macOS的配置文件所在路径和配置文件名如下所述：

*   Windows系统的配置文件路径：`C:\Users\<user_name>\.jupyter\`
*   Linux/macOS系统的配置文件路径：`/Users/<user_name>/.jupyter/` 或 `~/.jupyter/`
*   配置文件名：`jupyter_notebook_config.py`

注意：

① “<user_name>”为你的用户名。用户名两边不加尖括号“<>”。

② Windows和Linux/macOS系统的配置文件存放路径其实是相同的，只是系统不同，表现形式有所不同而已。

③ Windows和Linux/macOS系统的配置文件也是相同的。文件名以“.py”结尾，是Python的可执行文件。

④ 如果你不是通过一步到位的方式前往配置文件所在位置，而是一层一层进入文件夹/目录的，那么当你进入家目录后，用`ls`命令会发现找不到“.jupyter”文件夹/目录。这是因为凡是以“.”开头的目录都是隐藏文件，你可以通过`ls -a`命令查看当前位置下所有的隐藏文件。

**⑶ 修改配置文件**
------------

*   Windows系统的用户可以使用文档编辑工具或IDE打开“jupyter\_notebook\_config.py”文件并进行编辑。常用的文档编辑工具和IDE有记事本、Notepad++、vim、Sublime  
    Text、PyCharm等。其中，vim是没有图形界面的，是一款学习曲线较为陡峭的编辑器，其他工具在此不做使用说明，因为上手相对简单。通过vim修改配置文件的方法请继续往下阅读。
*   Linux/macOS系统的用户建议直接通过终端调用vim来对配置文件进行修改。具体操作步骤如下：

**⒜ 打开配置文件**
------------

打开终端，输入命令：

    vim ~/.jupyter/jupyter_notebook_config.py
    

![](https://pic3.zhimg.com/v2-ec79adec540c62b244bd44df41f6c0ae_b.jpg)

![](data:image/svg+xml;utf8,<svg%20xmlns='http://www.w3.org/2000/svg'%20width='811'%20height='93'></svg>)

命令详解

执行上述命令后便进入到配置文件当中了。

**⒝ 查找关键词**
-----------

进入配置文件后查找关键词“c.NotebookApp.notebook_dir”。查找方法如下：

进入配置文件后不要按其他键，用**英文半角**直接输入`/c.NotebookApp.notebook_dir`，这时搜索的关键词已在文档中高亮显示了，按回车，光标从底部切换到文档正文中被查找关键词的首字母。

**⒞ 编辑配置文件**
------------

按**小写i**进入编辑模式，底部出现“--INSERT--”说明成功进入编辑模式。使用方向键把光标定位在第二个单引号上（光标定位在哪个字符，就在这个字符前开始输入），把“⑴ 创建文件夹/目录”步骤中复制的路径粘贴在此处。

**⒟ 取消注释**
----------

把该行行首的**井号（#）**删除。因为配置文件是Python的可执行文件，在Python中，井号（#）表示注释，即在编译过程中不会执行该行命令，所以为了使修改生效，需要删除井号（#）。

**⒠ 保存配置文件**
------------

先按`esc`键，从编辑模式退出，回到命令模式。

再用**英文半角**直接输入`:wq`，回车即成功保存且退出了配置文件。

注意：

*   **冒号（:）** 一定要有，且也是**英文半角**。
*   w：保存。
*   q：退出。

**⒡ 验证**
--------

在终端中输入命令`jupyter notebook`打开Jupyter Notebook，此时你会看到一个清爽的界面，恭喜！

![](https://pic1.zhimg.com/v2-8d185cb051aea662a829e88ba486dbc4_b.jpg)

![](data:image/svg+xml;utf8,<svg%20xmlns='http://www.w3.org/2000/svg'%20width='1170'%20height='391'></svg>)

配置后主页面

**⒢ 注意**
--------

*   以上所有命令均以**英文半角**格式输入，若有报错，请严格检查这两个条件，**英文**且**半角**。
*   这里仅介绍了vim编辑器修改配置文件的方法，没有对vim编辑器的详细使用进行讲解，所以无需了解vim编辑器的具体使用方法，只需要按照上述步骤一定可以顺利完成修改！
*   推荐有时间和经历时学习一下vim编辑器的使用。这款强大的编辑器将会成为你未来工作中的利器。

**四、Jupyter Notebook的基本使用**
---------------------------

**1\. Files页面**
---------------

![](https://pic1.zhimg.com/v2-cb526cea874c6b91198a742766c44c70_b.jpg)

![](data:image/svg+xml;utf8,<svg%20xmlns='http://www.w3.org/2000/svg'%20width='1437'%20height='451'></svg>)

Files页面

此时你的界面当中应该还没有“Conda”和“Nbextensions”类目。不要着急，这两个类目将分别在“五、拓展功能”中的“[1.关联Jupyter Notebook和conda的环境和包——‘nb_conda’](https://zhuanlan.zhihu.com/p/33105153/edit#conda)”和“[2.Markdown生成目录](https://zhuanlan.zhihu.com/p/33105153/edit#nbextensions)”中安装。

Files页面是用于管理和创建文件相关的类目。

对于现有的文件，可以通过勾选文件的方式，对选中文件进行复制、重命名、移动、下载、查看、编辑和删除的操作。

同时，也可以根据需要，在“New”下拉列表中选择想要创建文件的环境，进行创建“ipynb”格式的笔记本、“txt”格式的文档、终端或文件夹。如果你创建的环境没有在下拉列表中显示，那么你需要依次前往“五、拓展功能”中的“[1.关联Jupyter Notebook和conda的环境和包——‘nb_conda’](https://zhuanlan.zhihu.com/p/33105153/edit#conda)”和“[六、增加内核——‘ipykernel’](https://zhuanlan.zhihu.com/p/33105153/edit#ipykernel)”中解决该问题。

**① 笔记本的基本操作**
--------------

![](https://pic1.zhimg.com/v2-3c250ee0349ff76d869ed80d456487cc_b.jpg)

![](data:image/svg+xml;utf8,<svg%20xmlns='http://www.w3.org/2000/svg'%20width='1440'%20height='424'></svg>)

笔记本页面注解图

上图展示的是笔记本的基本结构和功能。根据图中的注解已经可以解决绝大多数的使用问题了！

工具栏的使用如图中的注解一样直观，在此不过多解释。需要特别说明的是“单元格的状态”，有Code，Markdown，Heading，Raw NBconvert。其中，最常用的是前两个，分别是代码状态，Markdown编写状态。Jupyter Notebook已经取消了Heading状态，即标题单元格。取而代之的是Markdown的一级至六级标题。而Raw NBconvert目前极少用到，此处也不做过多讲解。

菜单栏涵盖了笔记本的所有功能，即便是工具栏的功能，也都可以在菜单栏的类目里找到。然而，并不是所有功能都是常用的，比如Widgets，Navigate。Kernel类目的使用，主要是对内核的操作，比如中断、重启、连接、关闭、切换内核等，由于我们在创建笔记本时已经选择了内核，因此切换内核的操作便于我们在使用笔记本时切换到我们想要的内核环境中去。由于其他的功能相对比较常规，根据图中的注解来尝试使用笔记本的功能已经非常便捷，因此不再做详细讲解。

**② 笔记本重命名的两种方式**
-----------------

**⑴ 笔记本内部重命名**
--------------

在使用笔记本时，可以直接在其内部进行重命名。在左上方“Jupyter”的图标旁有程序默认的标题“Untitled”，点击“Untitled”然后在弹出的对话框中输入自拟的标题，点击“Rename”即完成了重命名。

**⑵ 笔记本外部重命名**
--------------

若在使用笔记本时忘记了重命名，且已经保存并退出至“Files”界面，则在“Files”界面勾选需要重命名的文件，点击“Rename”然后直接输入自拟的标题即可。

**⑶ 演示**
--------

![](https://pic1.zhimg.com/v2-e2504cf777d5c7253a28411e3abb50a4_b.gif)

![](data:image/svg+xml;utf8,<svg%20xmlns='http://www.w3.org/2000/svg'%20width='1438'%20height='567'></svg>)

笔记本重命名演示图

  

  

**2\. Running页面**
-----------------

Running页面主要展示的是当前正在运行当中的终端和“ipynb”格式的笔记本。若想要关闭已经打开的终端和“ipynb”格式的笔记本，仅仅关闭其页面是无法彻底退出程序的，需要在Running页面点击其对应的“Shutdown”。更多关闭方法可以查阅“八、关闭和退出”中的“[1.关闭笔记本和终端](https://zhuanlan.zhihu.com/p/33105153/edit#quit)”。

![](https://pic4.zhimg.com/v2-ca637455e9537c30205e0b85b6901327_b.gif)

![](data:image/svg+xml;utf8,<svg%20xmlns='http://www.w3.org/2000/svg'%20width='1438'%20height='419'></svg>)

Running页面功能演示图

  

  

**3\. Clusters页面**
------------------

> Clusters tab is now provided by IPython parallel. See '[IPython parallel](http://link.zhihu.com/?target=https%3A//github.com/ipython/ipyparallel)' for  
> installation details.

Clusters类目现在已由IPython parallel对接，且由于现阶段使用频率较低，因此在此不做详细说明，想要了解更多可以访问[IPython parallel的官方网站](http://link.zhihu.com/?target=https%3A//github.com/ipython/ipyparallel)。

**4\. Conda页面**
---------------

Conda页面主要是Jupyter Notebook与Conda关联之后对Conda环境和包进行直接操作和管理的页面工具。详细信息请直接查阅“五、拓展功能”中的“[1.关联Jupyter Notebook和conda的环境和包——‘nb_conda’](https://zhuanlan.zhihu.com/p/33105153/edit#conda)”。这是目前使用Jupyter Notebook的必备环节，因此请务必查阅。

**5\. Nbextensions页面**
----------------------

Nbextensions页面提供了多个Jupyter Notebook的插件，使其功能更加强大。该页面中主要使用的插件有nb\_conda，nb\_present，Table of Contents(2)。这些功能我们无需完全掌握，也无需安装所有的扩展功能，根据本文档提供的学习思路，我们只需要安装Talbe of Contents(2)即可，该功能可为Markdown文档提供目录导航，便于我们编写文档。该安装指导请查阅“五、拓展功能”中的“[2.Markdown生成目录](https://zhuanlan.zhihu.com/p/33105153/edit#nbextensions)”。

![](https://pic2.zhimg.com/v2-a7a2f4b1f06aed21df09b6e3b957e191_b.jpg)

![](data:image/svg+xml;utf8,<svg%20xmlns='http://www.w3.org/2000/svg'%20width='1440'%20height='592'></svg>)

Nbextensions页面

**五、拓展功能**
----------

**1\. 关联Jupyter Notebook和conda的环境和包——“nb_conda”☆**
--------------------------------------------------

**① 安装**
--------

    conda install nb_conda
    

执行上述命令能够将你conda创建的环境与Jupyter Notebook相关联，便于你在Jupyter Notebook的使用中，在不同的环境下创建笔记本进行工作。

**② 使用**
--------

*   可以在Conda类目下对conda环境和包进行一系列操作。

![](https://pic2.zhimg.com/v2-75db6aec2cf08a29014679435675f17d_b.jpg)

![](data:image/svg+xml;utf8,<svg%20xmlns='http://www.w3.org/2000/svg'%20width='1439'%20height='716'></svg>)

Conda页面注解图

*   可以在笔记本内的“Kernel”类目里的“Change  
    kernel”切换内核。

![](https://pic2.zhimg.com/v2-6a926273202380b5fd5e51dff7941dfd_b.jpg)

![](data:image/svg+xml;utf8,<svg%20xmlns='http://www.w3.org/2000/svg'%20width='1440'%20height='435'></svg>)

切换内核

**③ 卸载**
--------

    canda remove nb_conda
    

执行上述命令即可卸载nb_conda包。

**2\. Markdown生成目录**
--------------------

*   不同于有道云笔记的Markdown编译器，Jupyter Notebook无法为Markdown文档通过特定语法添加目录，因此需要通过安装扩展来实现目录的添加。

    conda install -c conda-forge jupyter_contrib_nbextensions
    

*   执行上述命令后，启动Jupyter Notebook，你会发现导航栏多了“Nbextensions”的类目，点击“Nbextensions”，勾选“Table  
    of Contents ⑵”

![](https://pic2.zhimg.com/v2-a7a2f4b1f06aed21df09b6e3b957e191_b.jpg)

![](data:image/svg+xml;utf8,<svg%20xmlns='http://www.w3.org/2000/svg'%20width='1440'%20height='592'></svg>)

Nbextensions页面

*   之后再在Jupyter Notebook中使用Markdown，点击下图的图标即可使用啦。

![](https://pic2.zhimg.com/v2-dd9b3a1f62c89570a47c7f6d24bf01a1_b.jpg)

![](data:image/svg+xml;utf8,<svg%20xmlns='http://www.w3.org/2000/svg'%20width='1435'%20height='712'></svg>)

目录

**3\. Markdown在文中设置链接并定位**
--------------------------

在使用Markdown编辑文档时，难免会遇到需要在文中设定链接，定位在文档中的其他位置便于查看。因为Markdown可以完美的兼容html语法，因此这种功能可以通过html语法当中“a标签”的索引用法来实现。

语法格式如下：

    [添加链接的正文](#自定义索引词)
    <a id=自定义索引词>跳转提示</a>
    

注意：

1.  语法格式当中所有的符号均是**英文半角**。
2.  “自定义索引词”最好是英文，较长的词可以用下划线连接。
3.  “a标签”出现在想要被跳转到的文章位置，html标签除了单标签外均要符合“有头（`<a>`）必有尾（`</a>`）”的原则。头尾之间的“跳转提示”是可有可无的。
4.  “a标签”中的“id”值即是为正文中添加链接时设定的“自定义索引值”，这里通过“id”的值实现从正文的链接跳转至指定位置的功能。

例：

![](https://pic3.zhimg.com/v2-33dd1aeea782e414db9b703f75f0f32e_b.gif)

![](data:image/svg+xml;utf8,<svg%20xmlns='http://www.w3.org/2000/svg'%20width='1438'%20height='712'></svg>)

有跳转提示语

  

  

![](https://pic1.zhimg.com/v2-c89c8598922c7077b1570e96e4b57428_b.gif)

![](data:image/svg+xml;utf8,<svg%20xmlns='http://www.w3.org/2000/svg'%20width='1436'%20height='711'></svg>)

无跳转提示语

  

  

**4\. 加载指定网页源代码**
-----------------

**① 使用场景**
----------

想要在Jupyter Notebook中直接加载指定网站的源代码到笔记本中。

**② 方法**
--------

执行以下命令:

    %load URL
    

其中，URL为指定网站的地址。

**③ 例**
-------

![](https://pic2.zhimg.com/v2-69a40fddfacfecb8151bd9e6f60054e9_b.gif)

![](data:image/svg+xml;utf8,<svg%20xmlns='http://www.w3.org/2000/svg'%20width='1438'%20height='763'></svg>)

加载网络代码

  

  

**5\. 加载本地Python文件**
--------------------

**① 使用场景**
----------

想在Jupyter Notebook中加载本地的Python文件并执行文件代码。

**② 方法**
--------

执行以下命令：

    %load Python文件的绝对路径
    

**③ 注意**
--------

1.  Python文件的后缀为“.py”。
2.  “%load”后跟的是Python文件的**绝对路径**。
3.  输入命令后，可以按`CTRL 回车`来执行命令。第一次执行，是将本地的Python文件内容加载到单元格内。此时，Jupyter Notebook会自动将“%load”命令注释掉（即在前边加井号“#”），以便在执行已加载的文件代码时不重复执行该命令；第二次执行，则是执行已加载文件的代码。

**④ 例**
-------

![](https://pic3.zhimg.com/v2-99c16d96c8ffbf0e507ec909fadf416a_b.gif)

![](data:image/svg+xml;utf8,<svg%20xmlns='http://www.w3.org/2000/svg'%20width='1438'%20height='692'></svg>)

加载本地Python文件

  

  

**6\. 直接运行本地Python文件**
----------------------

**① 使用场景**
----------

不想在Jupyter Notebook的单元格中加载本地Python文件，想要直接运行。

**② 方法**
--------

执行命令：

    %run Python文件的绝对路径
    

或

    !python3 Python文件的绝对路径
    

或

    !python Python文件的绝对路径
    

**③ 注意**
--------

1.  Python文件的后缀为“.py”。
2.  “%run”后跟的是Python文件的**绝对路径**。
3.  “!python3”用于执行Python  
    3.x版本的代码。
4.  “!python”用于执行Python  
    2.x版本的代码。
5.  “!python3”和“!python”属于 `!shell命令` 语法的使用，即在Jupyter Notebook中执行shell命令的语法。
6.  输入命令后，可以按 `control return` 来执行命令，执行过程中将不显示本地Python文件的内容，直接显示运行结果。

**④ 例**
-------

![](https://pic2.zhimg.com/v2-353ba4eddf9b935380844200ea398c11_b.gif)

![](data:image/svg+xml;utf8,<svg%20xmlns='http://www.w3.org/2000/svg'%20width='1438'%20height='506'></svg>)

运行本地Python文件

  

  

**7\. 在Jupyter Notebook中获取当前位置**
--------------------------------

**① 使用场景**
----------

想要在Jupyter Notebook中获取当前所在位置的**绝对路径。**

**② 方法**
--------

    %pwd
    

或

    !pwd
    

**③ 注意**
--------

1.  获取的位置是当前Jupyter Notebook中创建的笔记本所在位置，且该位置为**绝对路径**。
2.  “!pwd”属于 `!shell命令` 语法的使用，即在Jupyter  
    Notebook中执行shell命令的语法。

**④ 例**
-------

![](https://pic2.zhimg.com/v2-ca13bbc098e544d0fd53c4d5835f6cfd_b.gif)

![](data:image/svg+xml;utf8,<svg%20xmlns='http://www.w3.org/2000/svg'%20width='1433'%20height='386'></svg>)

获取当前位置的绝对路径

  

  

**8\. 在Jupyter Notebook使用shell命令**
----------------------------------

**① 方法一——在笔记本的单元格中**
--------------------

**⑴ 语法**
--------

    !shell命令
    

  

*   在Jupyter Notebook中的笔记本单元格中用英文感叹号“!”后接shell命令即可执行shell命令。

**⑵ 例**
-------

![](https://pic1.zhimg.com/v2-8b8ec14f44d588674e37ffa57f117674_b.gif)

![](data:image/svg+xml;utf8,<svg%20xmlns='http://www.w3.org/2000/svg'%20width='1438'%20height='524'></svg>)

Shell命令的使用

  

  

**② 方法二——在Jupyter Notebook中新建终端**
---------------------------------

**⑴ 启动方法**
----------

在Jupyter Notebook主界面，即“File”界面中点击“New”；在“New”下拉框中点击“Terminal”即新建了终端。此时终端位置是在你的家目录，可以通过`pwd`命令查询当前所在位置的绝对路径。

**⑵ 关闭方法**
----------

在Jupyter Notebook的“Running”界面中的“Terminals”类目中可以看到正在运行的终端，点击后边的“Shutdown”即可关闭终端。

**⑶ 例**
-------

![](https://pic2.zhimg.com/v2-8318df6fd86b4839d83f0d94004f9191_b.gif)

![](data:image/svg+xml;utf8,<svg%20xmlns='http://www.w3.org/2000/svg'%20width='1437'%20height='699'></svg>)

笔记本中的终端使用

  

  

**9\. 隐藏笔记本输入单元格**
------------------

**① 使用场景**
----------

在Jupyter Notebook的笔记本中无论是编写文档还是编程，都有输入（In \[\]）和输出（Out \[\]）。当我们编写的代码或文档使用的单元格较多时，有时我们只想关注输出的内容而暂时不看输入的内容，这时就需要隐藏输入单元格而只显示输出单元格。

**② 方法一**
---------

**⑴ 代码**
--------

    from IPython.display import display
    from IPython.display import HTML
    import IPython.core.display as di # Example: di.display_html('<h3>%s:</h3>' % str, raw=True)
    
    # 这行代码的作用是：当文档作为HTML格式输出时，将会默认隐藏输入单元格。
    di.display_html('<script>jQuery(function() {if (jQuery("body.notebook_app").length == 0) { jQuery(".input_area").toggle(); jQuery(".prompt").toggle();}});</script>', raw=True)
    
    # 这行代码将会添加“Toggle code”按钮来切换“隐藏/显示”输入单元格。
    di.display_html('''<button onclick="jQuery('.input_area').toggle(); jQuery('.prompt').toggle();">Toggle code</button>''', raw=True)
    

在笔记本第一个单元格中输入以上代码，然后执行，即可在该文档中使用“隐藏/显示”输入单元格功能。

*   缺陷：此方法不能很好的适用于Markdown单元格。

⑵ 例
---

![](https://pic2.zhimg.com/v2-b8847adffd4ebc8ec70694196578524d_b.gif)

![](data:image/svg+xml;utf8,<svg%20xmlns='http://www.w3.org/2000/svg'%20width='1438'%20height='701'></svg>)

方法一：隐藏/显示输入单元格

  

  

**③ 方法二**
---------

**⑴ 代码**
--------

    from IPython.display import HTML
    
    HTML('''<script>
    code_show=true; 
    function code_toggle() {
    if (code_show){
    $('div.input').hide();
    } else {
    $('div.input').show();
    }
    code_show = !code_show
    } 
    $( document ).ready(code_toggle);
    </script>
    <form action="javascript:code_toggle()"><input type="submit" value="Click here to toggle on/off the raw code."></form>''')
    

在笔记本第一个单元格中输入以上代码，然后执行，即可在该文档中使用“隐藏/显示”输入单元格功能。

*   缺陷：此方法不能很好的适用于Markdown单元格。

**⑵ 例**
-------

![](https://pic4.zhimg.com/v2-b4df17ea52642f69ed6f80c2ceb4e3bf_b.gif)

![](data:image/svg+xml;utf8,<svg%20xmlns='http://www.w3.org/2000/svg'%20width='1438'%20height='659'></svg>)

方法二：隐藏/显示输入单元格

  

  

**10\. 魔术命令**
-------------

由于目前暂时用不到过多的魔术命令，因此暂时先参考[官网的文档](http://link.zhihu.com/?target=http%3A//ipython.readthedocs.io/en/stable/interactive/magics.html)。

**六、增加内核——“ipykernel” ☆**
-------------------------

**1\. 使用场景**
------------

*   场景一：同时用不同版本的Python进行工作，在Jupyter Notebook中无法切换，即“New”的下拉菜单中无法使用需要的环境。
*   场景二：创建了不同的虚拟环境（或许具有相同的Python版本但安装的包不同），在Jupyter Notebook中无法切换，即“New”的下拉菜单中无法使用需要的环境。

接下来将分别用“命令行模式”和“图形界面模式”来解决以上两个场景的问题。顾名思义，“命令行模式”即在终端中通过执行命令来一步步解决问题；“图形界面模式”则是通过在Jupyter Notebook的网页中通过鼠标点击的方式解决上述问题。

其中，“图形界面模式”的解决方法相对比较简单快捷，如果对于急于解决问题，不需要知道运行原理的朋友，可以直接进入“3\. 解决方法之图形界面模式”来阅读。

“命令行模式”看似比较复杂，且又划分了使用场景，但通过这种方式来解决问题可以更好的了解其中的工作原理，比如，每进行一步操作对应的命令是什么，而命令的执行是为了达到什么样的目的，这些可能都被封装在图形界面上的一个点击动作来完成了。对于想更深入了解其运作过程的朋友，可以接着向下阅读。

**2\. 解决方法之命令行模式**
------------------

**① 同时使用不同版本的Python**
---------------------

**⑴ 在Python 3中创建Python 2内核**
----------------------------

**⒜ pip安装**
-----------

*   首先安装Python 2的ipykernel包。

    python2 -m pip install ipykernel
    

*   再为**当前用户**安装Python 2的内核（ipykernel）。

    python2 -m ipykernel install --user
    

*   注意：“--user”参数的意思是针对当前用户安装，而非系统范围内安装。

**⒝ conda安装**
-------------

*   首先创建Python版本为2.x且具有ipykernel的新环境，其中“<env_name>”为自定义环境名，环境名两边不加尖括号“<>”。

    conda create -n <env_name> python=2 ipykernel
    

*   然后切换至新创建的环境。

    Windows: activate <env_name>
    Linux/macOS: source activate <env_name>
    

*   为**当前用户**安装Python 2的内核（ipykernel）。

    python2 -m ipykernel install --user
    

*   注意：“--user”参数的意思是针对当前用户安装，而非系统范围内安装。

**⑵ 在Python 2中创建Python 3内核**
----------------------------

**⒜ pip安装**
-----------

*   首先安装Python 3的ipykernel包。

    python3 -m pip install ipykernel
    

*   再为**当前用户**安装Python 2的内核（ipykernel）。

    python3 -m ipykernel install --user
    

*   注意：“--user”参数的意思是针对当前用户安装，而非系统范围内安装。

**⒝ conda安装**
-------------

*   首先创建Python版本为3.x且具有ipykernel的新环境，其中“<env_name>”为自定义环境名，环境名两边不加尖括号“<>”。

    conda create -n <env_name> python=3 ipykernel
    

*   然后切换至新创建的环境。

    Windows: activate <env_name>
    Linux/macOS: source activate <env_name>
    

*   为**当前用户**安装Python 3的内核（ipykernel）。

    python3 -m ipykernel install --user
    

*   注意：“--user”参数的意思是针对当前用户安装，而非系统范围内安装。

**② 为不同环境创建内核**
---------------

**⑴ 切换至需安装内核的环境**
-----------------

    Windows: activate <env_name>
    Linux/macOS: source activate <env_name>
    

*   注意：“<env_name>”是需要安装内核的环境名称，环境名两边不加尖括号“<>”。

**⑵ 检查该环境是否安装了ipykernel包**
--------------------------

    conda list
    

执行上述命令查看当前环境下安装的包，若没有安装ipykernel包，则执行安装命令；否则进行下一步。

    conda install ipykernel
    

**⑶ 为当前环境下的当前用户安装Python内核**
---------------------------

*   若该环境的Python版本为2.x，则执行命令：

    python2 -m ipykernel install --user --name <env_name> --display-name "<notebook_name>"
    

*   若该环境的Python版本为3.x，则执行命令：

    python3 -m ipykernel install --user --name <env_name> --display-name "<notebook_name>"
    

*   注意:

1\. “<env_name>”为当前环境的环境名称。环境名两边不加尖括号“<>”。

2\. “<notebook_name>”为自定义显示在Jupyter Notebook中的名称。名称两边不加尖括号“<>”，但**双引号必须加**。

3\. “--name”参数的值，即“<env_name>”是Jupyter内部使用的，其目录的存放路径为`~/Library/Jupyter/kernels/`。如果定义的名称在该路径已经存在，那么将自动覆盖该名称目录的内容。

4\. “--display-name”参数的值是显示在Jupyter Notebook的菜单中的名称。

**⑷ 检验**
--------

使用命令`jupyter notebook`启动Jupyter Notebook；在“Files”下的“New”下拉框中即可找到你在第⑶步中的自定义名称，此时，你便可以尽情地在Jupyter Notebook中切换环境，在不同的环境中创建笔记本进行工作和学习啦！

**3\. 解决方法之图形界面模式**
-------------------

① 你创建了一个新的环境，但却发现在Jupyter Notebook的“New”中找不到这个环境，无法在该环境中创建笔记本。

![](https://pic3.zhimg.com/v2-5c1dc9640e1bf796c24b9d29c62868aa_b.gif)

![](data:image/svg+xml;utf8,<svg%20xmlns='http://www.w3.org/2000/svg'%20width='1438'%20height='665'></svg>)

问题发现

  

  

② 进入Jupyter Notebook → Conda → 在“Conda  
environment”中点击你要添加ipykernel包的环境 → 左下方搜索框输入“ipykernel”  
→ 勾选“ipykernel” → 点击搜索框旁的“→”箭头 → 安装完毕 → 右下方框内找到“ipykernel”说明已经安装成功

![](https://pic4.zhimg.com/v2-49839a5db0f9108ad13c185a20f958e3_b.gif)

![](data:image/svg+xml;utf8,<svg%20xmlns='http://www.w3.org/2000/svg'%20width='1438'%20height='660'></svg>)

解决方法

  

  

③ 在终端`control c`关闭Jupyter Notebook的服务器然后重启Jupyter Notebook，在“File”的“New”的下拉列表里就可以找到你的环境啦。

![](https://pic1.zhimg.com/v2-9d4fa171b3010a04d3e1229fdfebbbe0_b.gif)

![](data:image/svg+xml;utf8,<svg%20xmlns='http://www.w3.org/2000/svg'%20width='1438'%20height='705'></svg>)

验证

  

  

**七、Jupyter Notebook快捷键**
-------------------------

**1\. Mac与Windows特殊按键对照表**
--------------------------

![](https://pic4.zhimg.com/v2-8eaff7a48cda7cb89fb462f82d464963_b.jpg)

![](data:image/svg+xml;utf8,<svg%20xmlns='http://www.w3.org/2000/svg'%20width='558'%20height='766'></svg>)

Mac和Windows特殊按键对照表

**2\. Jupyter Notebook笔记本的两种模式**
--------------------------------

**① 命令模式**
----------

*   命令模式将键盘命令与Jupyter Notebook笔记本命令相结合，可以通过键盘不同键的组合运行笔记本的命令。
*   按`esc`键进入命令模式。
*   命令模式下，单元格边框为灰色，且左侧边框线为蓝色粗线条。

![](https://pic3.zhimg.com/v2-a93c521c691f10a59f9e3357125e6e66_b.jpg)

![](data:image/svg+xml;utf8,<svg%20xmlns='http://www.w3.org/2000/svg'%20width='1440'%20height='311'></svg>)

命令模式

**② 编辑模式**
----------

*   编辑模式使用户可以在单元格内编辑代码或文档。
*   按`enter`或`return`键进入编辑模式。
*   编辑模式下，单元格边框和左侧边框线均为绿色。

![](https://pic2.zhimg.com/v2-874151e646d6363c1307b13c410234d9_b.jpg)

![](data:image/svg+xml;utf8,<svg%20xmlns='http://www.w3.org/2000/svg'%20width='1440'%20height='294'></svg>)

编辑模式

**3\. 两种模式的快捷键**
----------------

**① 命令模式**
----------

![](https://pic4.zhimg.com/v2-61c3a34252d14a09a6819d213298e5bf_b.jpg)

![](data:image/svg+xml;utf8,<svg%20xmlns='http://www.w3.org/2000/svg'%20width='952'%20height='3302'></svg>)

命令模式快捷键

**② 编辑模式**
----------

![](https://pic4.zhimg.com/v2-8eaff7a48cda7cb89fb462f82d464963_b.jpg)

![](data:image/svg+xml;utf8,<svg%20xmlns='http://www.w3.org/2000/svg'%20width='558'%20height='766'></svg>)

编辑模式快捷键

**4\. 查看和编辑快捷键**
----------------

**① 查看快捷键**
-----------

① 进入Jupyter Notebook主界面“File”中。

② 在“New”的下拉列表中选择环境创建一个笔记本。

③ 点击“Help”。

④ 点击“Keyboard Shortcuts”。

**② 编辑快捷键**
-----------

**⑴ 方法一**
---------

① 进入Jupyter Notebook主界面“File”中。

② 在“New”的下拉列表中选择环境创建一个笔记本。

③ 点击“Help”。

④ 点击“Keyboard Shortcuts”。

⑤ 弹出的对话框中“Command Mode (press Esc to enable)”旁点击“Edit  
Shortcuts”按钮。

**⑵ 方法二**
---------

① 进入Jupyter Notebook主界面“File”中。

② 在“New”的下拉列表中选择环境创建一个笔记本。

③ 点击“Help”。

④ 点击“Edit Keyboard Shortcuts”。

**③ 例**
-------

![](https://pic3.zhimg.com/v2-706e6c1a0364e6d5279f309e0ed5d0f6_b.gif)

![](data:image/svg+xml;utf8,<svg%20xmlns='http://www.w3.org/2000/svg'%20width='1436'%20height='705'></svg>)

查看和编辑快捷键

  

  

**八、关闭和退出**
-----------

**1\. 关闭笔记本和终端**
----------------

当我们在Jupyter Notebook中创建了终端或笔记本时，将会弹出新的窗口来运行终端或笔记本。当我们使用完毕想要退出终端或笔记本时，仅仅**关闭页面**是无法结束程序运行的，因此我们需要通过以下步骤将其完全关闭。

**① 方法一**
---------

⑴ 进入“Files”页面。

⑵ 勾选想要关闭的“ipynb”笔记本。正在运行的笔记本其图标为绿色，且后边标有“Running”的字样；已经关闭的笔记本其图标为灰色。

⑶ 点击上方的黄色的“Shutdown”按钮。

⑷ 成功关闭笔记本。

*   注意：此方法只能关闭笔记本，无法关闭终端。

**② 方法二**
---------

⑴ 进入“Running”页面。

⑵ 第一栏是“Terminals”，即所有正在运行的终端均会在此显示；第二栏是“Notebooks”，即所有正在运行的“ipynb”笔记本均会在此显示。

⑶ 点击想要关闭的终端或笔记本后黄色“Shutdown”按钮。

⑷ 成功关闭终端或笔记本。

*   注意：此方法可以关闭任何正在运行的终端和笔记本。

**③ 注意**
--------

⑴ 只有“ipynb”笔记本和终端需要通过上述方法才能使其结束运行。

⑵  
“txt”文档，即“New”下拉列表中的“Text  
File”，以及“Folder”只要关闭程序运行的页面即结束运行，无需通过上述步骤关闭。

**④ 演示**
--------

![](https://pic4.zhimg.com/v2-05314d41206fbfc5bbe3533709202f23_b.gif)

![](data:image/svg+xml;utf8,<svg%20xmlns='http://www.w3.org/2000/svg'%20width='1438'%20height='451'></svg>)

关闭笔记本或终端程序

  

  

**2\. 退出Jupyter Notebook程序**
----------------------------

如果你想退出Jupyter Notebook程序，仅仅通过关闭网页是无法退出的，因为当你打开Jupyter Notebook时，其实是启动了它的服务器。

你可以尝试关闭页面，并打开新的浏览器页面，把之前的地址输进地址栏，然后跳转页面，你会发现再次进入了刚才“关闭”的Jupyter Notebook页面。

如果你忘记了刚才关闭的页面地址，可以在启动Jupyter Notebook的终端中找到地址，复制并粘贴至新的浏览器页面的地址栏，会发现同样能够进入刚才关闭的页面。

因此，想要彻底退出Jupyter Notebook，需要关闭它的服务器。只需要在它启动的终端上按：

*   Mac用户：`control c`
*   Windows用户：`ctrl c`

然后在终端上会提示：“Shutdown this notebook server (y/\[n\])?”输入`y`即可关闭服务器，这才是彻底退出了Jupyter Notebook程序。此时，如果你想要通过输入刚才关闭网页的网址进行访问Jupyter Notebook便会看到报错页面。

**九、参考资料**
----------

1.知乎：jupyter notebook 可以做哪些事情？[猴子的回答](https://www.zhihu.com/question/46309360/answer/254638807?utm_source=wechat_session&utm_medium=social)

2\. [Jupyter Notebook官方介绍](http://link.zhihu.com/?target=https%3A//jupyter-notebook.readthedocs.io/en/stable/notebook.html)

3\. [Anaconda官方下载页面](http://link.zhihu.com/?target=https%3A//www.anaconda.com/download/%23macos)

4\. [Python·Jupyter Notebook各种使用方法记录](http://link.zhihu.com/?target=http%3A//blog.csdn.net/tina_ttl/article/details/51031113%2321-%25E6%2596%25B9%25E5%25BC%258F%25E4%25B8%2580)

5\. [Stack Overflow中有关如何隐藏/显示输入单元格的问题](http://link.zhihu.com/?target=https%3A//stackoverflow.com/questions/27934885/how-to-hide-code-from-cells-in-ipython-notebook-visualized-with-nbviewer)

6\. [魔术命令官方文档](http://link.zhihu.com/?target=http%3A//ipython.readthedocs.io/en/stable/interactive/magics.html)

7\. [Jupyter Notebook 的快捷键](http://link.zhihu.com/?target=http%3A//blog.csdn.net/lawme/article/details/51034543)

8\. [Jupyter Notebook官方文档](http://link.zhihu.com/?target=http%3A//jupyter.org/documentation)

编辑于 2018-01-22

[

Jupyter Notebook (IPython Notebook)



](//www.zhihu.com/topic/20064574)

[

Python



](//www.zhihu.com/topic/19552832)

[

数据分析



](//www.zhihu.com/topic/19559424)

​赞同 268​​48 条评论

​分享

​收藏

​

{"host":"zhihu.com","protocol":"https:","mainHost":"www.zhihu.com"}{"initialState":{"common":{"ask":{}},"privacy":{"showPrivacy":false},"loading":{"global":{"count":0},"local":{"env\\u002FgetIpinfo\\u002F":false,"article\\u002Fget\\u002F":false,"brand\\u002FgetUrl\\u002F":false}},"entities":{"users":{"raxxie":{"isFollowed":false,"avatarUrlTemplate":"https:\\u002F\\u002Fpic2.zhimg.com\\u002Fv2-45a1bf36532957955f7ab01a4458cbbc_{size}.jpg","type":"people","name":"豆豆","isAdvertiser":false,"url":"http:\\u002F\\u002Fwww.zhihu.com\\u002Fapi\\u002Fv4\\u002Fpeople\\u002Fe7c2d130df5eb242baa4487729f50d09","urlToken":"raxxie","userType":"people","headline":"热爱生活。","avatarUrl":"https:\\u002F\\u002Fpic2.zhimg.com\\u002Fv2-45a1bf36532957955f7ab01a4458cbbc\_is.jpg","isFollowing":false,"isOrg":false,"gender":1,"badge":\[\],"id":"e7c2d130df5eb242baa4487729f50d09"}},"questions":{},"answers":{},"articles":{"33105153":{"trackUrl":\["http:\\u002F\\u002Fsugar.zhihu.com\\u002Fplutus\_adreaper\\u002Fpage\_monitor\_log?si=\_\_SESSIONID\_\_&ti=\_\_ATOKEN\_\_&at=view&pf=\_\_OS\_\_"\],"reviewers":\[\],"topics":\[{"introduction":"","avatarUrl":"https:\\u002F\\u002Fpic4.zhimg.com\\u002Fe82bab09c\_is.jpg","name":"Jupyter Notebook (IPython Notebook)","url":"http:\\u002F\\u002Fwww.zhihu.com\\u002Fapi\\u002Fv4\\u002Ftopics\\u002F20064574","type":"topic","excerpt":"","id":"20064574"},{"introduction":"Python（英国发音：\\u002Fˈpaɪθən\\u002F 美国发音：\\u002Fˈpaɪθɑːn\\u002F）, 是一种面向对象的解释型计算机程序设计语言，由荷兰人Guido van Rossum于1989年发明，第一个公开发行版发行于1991年。Python是纯粹的自由软件， 源代码和解释器CPython遵循 GPL(GNU General Public License)协议。Python语法简洁清晰，特色之一是强制用空白符(white space)作为语句缩进。Python具有丰富和强大的库。它常被昵称为胶水语言，能够把用其他语言制作的各种模块（尤其是C\\u002FC++）很轻松地联结在一起。常见的一种应用情形是，使用Python快速生成程序的原型（有时甚至是程序的最终界面），然后对其中有特别要求的部分，用更合适的语言改写，比如3D游戏中的图形渲染模块，性能要求特别高，就可以用C\\u002FC++重写，而后封装为Python可以调用的扩展类库。需要注意的是在您使用扩展类库时可能需要考虑平台问题，某些可能不提供跨平台的实现。7月20日，IEEE发布2017年编程语言排行榜：Python高居首位。2018年3月，该语言作者在邮件列表上宣布 Python 2.7将于2020年1月1日终止支持。用户如果想要在这个日期之后继续得到与Python 2.7有关的支持，则需要付费给商业供应商。","avatarUrl":"https:\\u002F\\u002Fpic4.zhimg.com\\u002Fv2-1b642f312b0369f240fd6fb494f4acc9\_is.jpg","name":"Python","url":"http:\\u002F\\u002Fwww.zhihu.com\\u002Fapi\\u002Fv4\\u002Ftopics\\u002F19552832","type":"topic","excerpt":"Python（英国发音：\\u002Fˈpaɪθən\\u002F 美国发音：\\u002Fˈpaɪθɑːn\\u002F）, 是一种面向对象的解释型计算机程序设计语言，由荷兰人Guido van Rossum于1989年发明，第一个公开发行版发行于1991年。Python是纯粹的自由软件， 源代码和解释器CPython遵循 GPL(GNU General Public License)协议。Python语法简洁清晰，特色之一是强制用空白符(white space)作为语句缩进。Python具有丰富和强大的库。它常被昵称为胶水语言，能够把用其…","id":"19552832"},{"introduction":"数据分析是指用适当的统计分析方法对收集来的大量数据进行分析，提取有用信息和形成结论而对数据加以详细研究和概括总结的过程。这一过程也是质量管理体系的支持过程。在实用中，数据分析可帮助人们作出判断，以便采取适当行动。数据分析的数学基础在20世纪早期就已确立，但直到计算机的出现才使得实际操作成为可能，并使得数据分析得以推广。数据分析是数学与计算机科学相结合的产物。","avatarUrl":"https:\\u002F\\u002Fpic3.zhimg.com\\u002Fv2-78f4b42d0750ff5cecc0f6ec9453bc5f\_is.jpg","name":"数据分析","url":"http:\\u002F\\u002Fwww.zhihu.com\\u002Fapi\\u002Fv4\\u002Ftopics\\u002F19559424","type":"topic","excerpt":"数据分析是指用适当的统计分析方法对收集来的大量数据进行分析，提取有用信息和形成结论而对数据加以详细研究和概括总结的过程。这一过程也是质量管理体系的支持过程。在实用中，数据分析可帮助人们作出判断，以便采取适当行动。数据分析的数学基础在20世纪早期就已确立，但直到计算机的出现才使得实际操作成为可能，并使得数据分析得以推广。数据分析是数学与计算机科学相结合的产物。","id":"19559424"}\],"excerpt":"\\u003Cb\\u003E一、什么是Jupyter Notebook？\\u003C\\u002Fb\\u003E\\u003Cb\\u003E1. 简介\\u003C\\u002Fb\\u003EJupyter Notebook是基于网页的用于交互计算的应用程序。其可被应用于全过程计算：开发、文档编写、运行代码和展示结果。——\\u003Ca href=\\"https:\\u002F\\u002Fjupyter-notebook.readthedocs.io\\u002Fen\\u002Fstable\\u002Fnotebook.html\\"\\u003EJupyter Notebook官方介绍\\u003C\\u002Fa\\u003E简而言之，Jupyter Notebook是以网页的形式打开，可以在网页页面中\\u003Cb\\u003E…\\u003C\\u002Fb\\u003E","adminClosedComment":false,"canTip":false,"contributions":\[\],"id":33105153,"commercialInfo":{"isCommercial":false},"voteupCount":268,"upvotedFollowees":\[\],"author":{"isFollowed":false,"avatarUrlTemplate":"https:\\u002F\\u002Fpic2.zhimg.com\\u002Fv2-45a1bf36532957955f7ab01a4458cbbc\_{size}.jpg","type":"people","name":"豆豆","isAdvertiser":false,"url":"http:\\u002F\\u002Fwww.zhihu.com\\u002Fapi\\u002Fv4\\u002Fpeople\\u002Fe7c2d130df5eb242baa4487729f50d09","urlToken":"raxxie","userType":"people","headline":"热爱生活。","avatarUrl":"https:\\u002F\\u002Fpic2.zhimg.com\\u002Fv2-45a1bf36532957955f7ab01a4458cbbc\_is.jpg","isFollowing":false,"isOrg":false,"gender":1,"badge":\[\],"id":"e7c2d130df5eb242baa4487729f50d09"},"imageWidth":1920,"content":"\\u003Cp\\u003E\\u003C\\u002Fp\\u003E\\u003Cfigure\\u003E\\u003Cnoscript\\u003E\\u003Cimg src=\\"https:\\u002F\\u002Fpic1.zhimg.com\\u002Fv2-ffad61af265d2f2fa0becd65205d3cc4\_b.jpg\\" data-size=\\"normal\\" data-rawwidth=\\"10836\\" data-rawheight=\\"7264\\" class=\\"origin\_image zh-lightbox-thumb\\" width=\\"10836\\" data-original=\\"https:\\u002F\\u002Fpic1.zhimg.com\\u002Fv2-ffad61af265d2f2fa0becd65205d3cc4\_r.jpg\\"\\u003E\\u003C\\u002Fnoscript\\u003E\\u003Cimg src=\\"data:image\\u002Fsvg+xml;utf8,&lt;svg%20xmlns='http:\\u002F\\u002Fwww.w3.org\\u002F2000\\u002Fsvg'%20width='10836'%20height='7264'&gt;&lt;\\u002Fsvg&gt;\\" data-size=\\"normal\\" data-rawwidth=\\"10836\\" data-rawheight=\\"7264\\" class=\\"origin\_image zh-lightbox-thumb lazy\\" width=\\"10836\\" data-original=\\"https:\\u002F\\u002Fpic1.zhimg.com\\u002Fv2-ffad61af265d2f2fa0becd65205d3cc4\_r.jpg\\" data-actualsrc=\\"https:\\u002F\\u002Fpic1.zhimg.com\\u002Fv2-ffad61af265d2f2fa0becd65205d3cc4\_b.jpg\\"\\u003E\\u003Cfigcaption\\u003E目录\\u003C\\u002Ffigcaption\\u003E\\u003C\\u002Ffigure\\u003E\\u003Chr\\u003E\\u003Ch2\\u003E\\u003Cb\\u003E一、什么是Jupyter Notebook？\\u003C\\u002Fb\\u003E\\u003C\\u002Fh2\\u003E\\u003Ch2\\u003E\\u003Cb\\u003E1. 简介\\u003C\\u002Fb\\u003E\\u003C\\u002Fh2\\u003E\\u003Cblockquote\\u003EJupyter Notebook是基于网页的用于交互计算的应用程序。其可被应用于全过程计算：开发、文档编写、运行代码和展示结果。——\\u003Ca href=\\"http:\\u002F\\u002Flink.zhihu.com\\u002F?target=https%3A\\u002F\\u002Fjupyter-notebook.readthedocs.io\\u002Fen\\u002Fstable\\u002Fnotebook.html\\" class=\\" wrap external\\" target=\\"\_blank\\" rel=\\"nofollow noreferrer\\"\\u003EJupyter Notebook官方介绍\\u003C\\u002Fa\\u003E\\u003C\\u002Fblockquote\\u003E\\u003Cp\\u003E简而言之，Jupyter Notebook是以网页的形式打开，可以在网页页面中\\u003Cb\\u003E直接编写代码\\u003C\\u002Fb\\u003E和\\u003Cb\\u003E运行代码\\u003C\\u002Fb\\u003E，代码的\\u003Cb\\u003E运行结果\\u003C\\u002Fb\\u003E也会直接在代码块下显示的程序。如在编程过程中需要编写说明文档，可在同一个页面中直接编写，便于作及时的说明和解释。\\u003C\\u002Fp\\u003E\\u003Ch2\\u003E\\u003Cb\\u003E2. 组成部分\\u003C\\u002Fb\\u003E\\u003C\\u002Fh2\\u003E\\u003Ch2\\u003E\\u003Cb\\u003E① 网页应用\\u003C\\u002Fb\\u003E\\u003C\\u002Fh2\\u003E\\u003Cp\\u003E网页应用即基于网页形式的、结合了编写说明文档、数学公式、交互计算和其他富媒体形式的工具。\\u003Cb\\u003E简言之，网页应用是可以实现各种功能的工具。\\u003C\\u002Fb\\u003E\\u003C\\u002Fp\\u003E\\u003Ch2\\u003E\\u003Cb\\u003E② 文档\\u003C\\u002Fb\\u003E\\u003C\\u002Fh2\\u003E\\u003Cp\\u003E即Jupyter Notebook中所有交互计算、编写说明文档、数学公式、图片以及其他富媒体形式的输入和输出，都是以文档的形式体现的。\\u003C\\u002Fp\\u003E\\u003Cp\\u003E这些文档是保存为后缀名为\\u003Ccode\\u003E.ipynb\\u003C\\u002Fcode\\u003E的\\u003Ccode\\u003EJSON\\u003C\\u002Fcode\\u003E格式文件，不仅便于版本控制，也方便与他人共享。\\u003C\\u002Fp\\u003E\\u003Cp\\u003E此外，文档还可以导出为：HTML、LaTeX、PDF等格式。\\u003C\\u002Fp\\u003E\\u003Ch2\\u003E\\u003Cb\\u003E3. Jupyter Notebook的主要特点\\u003C\\u002Fb\\u003E\\u003C\\u002Fh2\\u003E\\u003Cp\\u003E① 编程时具有\\u003Cb\\u003E语法高亮\\u003C\\u002Fb\\u003E、\\u003Ci\\u003E缩进\\u003C\\u002Fi\\u003E、\\u003Ci\\u003Etab补全\\u003C\\u002Fi\\u003E的功能。\\u003C\\u002Fp\\u003E\\u003Cp\\u003E② 可直接通过浏览器运行代码，同时在代码块下方展示运行结果。\\u003C\\u002Fp\\u003E\\u003Cp\\u003E③ 以富媒体格式展示计算结果。富媒体格式包括：HTML，LaTeX，PNG，SVG等。\\u003C\\u002Fp\\u003E\\u003Cp\\u003E④ 对代码编写说明文档或语句时，支持Markdown语法。\\u003C\\u002Fp\\u003E\\u003Cp\\u003E⑤ 支持使用LaTeX编写数学性说明。\\u003C\\u002Fp\\u003E\\u003Ch2\\u003E\\u003Cb\\u003E二、安装Jupyter Notebook\\u003C\\u002Fb\\u003E\\u003C\\u002Fh2\\u003E\\u003Ch2\\u003E\\u003Cb\\u003E0. 先试用，再决定\\u003C\\u002Fb\\u003E\\u003C\\u002Fh2\\u003E\\u003Cp\\u003E如果看了以上对Jupyter Notebook的介绍你还是拿不定主意究竟是否适合你，那么不要担心，你可以先\\u003Cb\\u003E免安装试用体验\\u003C\\u002Fb\\u003E一下，\\u003Ca href=\\"http:\\u002F\\u002Flink.zhihu.com\\u002F?target=https%3A\\u002F\\u002Ftry.jupyter.org\\u002F\\" class=\\" wrap external\\" target=\\"\_blank\\" rel=\\"nofollow noreferrer\\"\\u003E戳这里\\u003C\\u002Fa\\u003E，然后再做决定。\\u003C\\u002Fp\\u003E\\u003Cp\\u003E值得注意的是，官方提供的同时试用是有限的，如果你点击链接之后进入的页面如下图所示，那么不要着急，过会儿再试试看吧。 \\u003C\\u002Fp\\u003E\\u003Cfigure\\u003E\\u003Cnoscript\\u003E\\u003Cimg src=\\"https:\\u002F\\u002Fpic3.zhimg.com\\u002Fv2-b33e494528f00be39032485fcafdf942\_b.jpg\\" data-size=\\"normal\\" data-rawwidth=\\"1436\\" data-rawheight=\\"618\\" class=\\"origin\_image zh-lightbox-thumb\\" width=\\"1436\\" data-original=\\"https:\\u002F\\u002Fpic3.zhimg.com\\u002Fv2-b33e494528f00be39032485fcafdf942\_r.jpg\\"\\u003E\\u003C\\u002Fnoscript\\u003E\\u003Cimg src=\\"data:image\\u002Fsvg+xml;utf8,&lt;svg%20xmlns='http:\\u002F\\u002Fwww.w3.org\\u002F2000\\u002Fsvg'%20width='1436'%20height='618'&gt;&lt;\\u002Fsvg&gt;\\" data-size=\\"normal\\" data-rawwidth=\\"1436\\" data-rawheight=\\"618\\" class=\\"origin\_image zh-lightbox-thumb lazy\\" width=\\"1436\\" data-original=\\"https:\\u002F\\u002Fpic3.zhimg.com\\u002Fv2-b33e494528f00be39032485fcafdf942\_r.jpg\\" data-actualsrc=\\"https:\\u002F\\u002Fpic3.zhimg.com\\u002Fv2-b33e494528f00be39032485fcafdf942\_b.jpg\\"\\u003E\\u003Cfigcaption\\u003E试用满线\\u003C\\u002Ffigcaption\\u003E\\u003C\\u002Ffigure\\u003E\\u003Cp\\u003E如果你足够幸运，那么你将看到如下界面，就可以开始体验啦。\\u003C\\u002Fp\\u003E\\u003Cfigure\\u003E\\u003Cnoscript\\u003E\\u003Cimg src=\\"https:\\u002F\\u002Fpic3.zhimg.com\\u002Fv2-d07ddde1d96cd3a71a5ecffe738907c2\_b.jpg\\" data-size=\\"normal\\" data-rawwidth=\\"2332\\" data-rawheight=\\"1378\\" class=\\"origin\_image zh-lightbox-thumb\\" width=\\"2332\\" data-original=\\"https:\\u002F\\u002Fpic3.zhimg.com\\u002Fv2-d07ddde1d96cd3a71a5ecffe738907c2\_r.jpg\\"\\u003E\\u003C\\u002Fnoscript\\u003E\\u003Cimg src=\\"data:image\\u002Fsvg+xml;utf8,&lt;svg%20xmlns='http:\\u002F\\u002Fwww.w3.org\\u002F2000\\u002Fsvg'%20width='2332'%20height='1378'&gt;&lt;\\u002Fsvg&gt;\\" data-size=\\"normal\\" data-rawwidth=\\"2332\\" data-rawheight=\\"1378\\" class=\\"origin\_image zh-lightbox-thumb lazy\\" width=\\"2332\\" data-original=\\"https:\\u002F\\u002Fpic3.zhimg.com\\u002Fv2-d07ddde1d96cd3a71a5ecffe738907c2\_r.jpg\\" data-actualsrc=\\"https:\\u002F\\u002Fpic3.zhimg.com\\u002Fv2-d07ddde1d96cd3a71a5ecffe738907c2\_b.jpg\\"\\u003E\\u003Cfigcaption\\u003E主界面\\u003C\\u002Ffigcaption\\u003E\\u003C\\u002Ffigure\\u003E\\u003Cfigure\\u003E\\u003Cnoscript\\u003E\\u003Cimg src=\\"https:\\u002F\\u002Fpic2.zhimg.com\\u002Fv2-8fa489d28f5c0aa29e78dc63116b0591\_b.jpg\\" data-size=\\"normal\\" data-rawwidth=\\"2004\\" data-rawheight=\\"1774\\" class=\\"origin\_image zh-lightbox-thumb\\" width=\\"2004\\" data-original=\\"https:\\u002F\\u002Fpic2.zhimg.com\\u002Fv2-8fa489d28f5c0aa29e78dc63116b0591\_r.jpg\\"\\u003E\\u003C\\u002Fnoscript\\u003E\\u003Cimg src=\\"data:image\\u002Fsvg+xml;utf8,&lt;svg%20xmlns='http:\\u002F\\u002Fwww.w3.org\\u002F2000\\u002Fsvg'%20width='2004'%20height='1774'&gt;&lt;\\u002Fsvg&gt;\\" data-size=\\"normal\\" data-rawwidth=\\"2004\\" data-rawheight=\\"1774\\" class=\\"origin\_image zh-lightbox-thumb lazy\\" width=\\"2004\\" data-original=\\"https:\\u002F\\u002Fpic2.zhimg.com\\u002Fv2-8fa489d28f5c0aa29e78dc63116b0591\_r.jpg\\" data-actualsrc=\\"https:\\u002F\\u002Fpic2.zhimg.com\\u002Fv2-8fa489d28f5c0aa29e78dc63116b0591\_b.jpg\\"\\u003E\\u003Cfigcaption\\u003E编辑页面\\u003C\\u002Ffigcaption\\u003E\\u003C\\u002Ffigure\\u003E\\u003Ch2\\u003E\\u003Cb\\u003E1. 安装\\u003C\\u002Fb\\u003E\\u003C\\u002Fh2\\u003E\\u003Ch2\\u003E\\u003Cb\\u003E① 安装前提\\u003C\\u002Fb\\u003E\\u003C\\u002Fh2\\u003E\\u003Cp\\u003E安装Jupyter Notebook的前提是需要安装了Python（3.3版本及以上，或2.7版本）。\\u003C\\u002Fp\\u003E\\u003Ch2\\u003E\\u003Cb\\u003E② 使用Anaconda安装\\u003C\\u002Fb\\u003E\\u003C\\u002Fh2\\u003E\\u003Cp\\u003E如果你是小白，那么建议你通过安装Anaconda来解决Jupyter Notebook的安装问题，因为Anaconda已经自动为你安装了Jupter Notebook及其他工具，还有python中超过180个科学包及其依赖项。\\u003C\\u002Fp\\u003E\\u003Cp\\u003E你可以通过进入Anaconda的\\u003Ca href=\\"http:\\u002F\\u002Flink.zhihu.com\\u002F?target=https%3A\\u002F\\u002Fwww.anaconda.com\\u002Fdownload\\u002F%23macos\\" class=\\" wrap external\\" target=\\"\_blank\\" rel=\\"nofollow noreferrer\\"\\u003E官方下载页面\\u003C\\u002Fa\\u003E自行选择下载；如果你对阅读\\u003Cb\\u003E英文文档\\u003C\\u002Fb\\u003E感到头痛，或者对\\u003Cb\\u003E安装步骤\\u003C\\u002Fb\\u003E一无所知，甚至也想快速了解一下\\u003Cb\\u003E什么是Anaconda\\u003C\\u002Fb\\u003E，那么可以前往我的另一篇文章：\\u003C\\u002Fp\\u003E\\u003Ca href=\\"https:\\u002F\\u002Fzhuanlan.zhihu.com\\u002Fp\\u002F32925500\\" data-draft-node=\\"block\\" data-draft-type=\\"link-card\\" data-image=\\"https:\\u002F\\u002Fpic2.zhimg.com\\u002Fv2-4ec3ac92a0051720dbf20f626dd44fb1\_180x120.jpg\\" data-image-width=\\"1000\\" data-image-height=\\"750\\" class=\\"internal\\"\\u003E豆豆：Anaconda介绍、安装及使用教程\\u003C\\u002Fa\\u003E\\u003Cp\\u003E你想要的，都在里面！\\u003C\\u002Fp\\u003E\\u003Cp\\u003E常规来说，安装了Anaconda发行版时已经自动为你安装了Jupyter Notebook的，但如果没有自动安装，那么就在终端（Linux或macOS的“终端”，Windows的“Anaconda Prompt”，以下均简称“终端”）中输入以下命令安装：\\u003C\\u002Fp\\u003E\\u003Cdiv class=\\"highlight\\"\\u003E\\u003Cpre\\u003E\\u003Ccode class=\\"language-text\\"\\u003E\\u003Cspan\\u003E\\u003C\\u002Fspan\\u003Econda install jupyter notebook\\n\\u003C\\u002Fcode\\u003E\\u003C\\u002Fpre\\u003E\\u003C\\u002Fdiv\\u003E\\u003Ch2\\u003E\\u003Cb\\u003E③ 使用pip命令安装\\u003C\\u002Fb\\u003E\\u003C\\u002Fh2\\u003E\\u003Cp\\u003E如果你是有经验的Python玩家，想要尝试用pip命令来安装Jupyter\\u003Cbr\\u003ENotebook，那么请看以下步骤吧！接下来的命令都输入在终端当中的噢！\\u003C\\u002Fp\\u003E\\u003Cp\\u003E\\u003Cb\\u003E1. 把pip升级到最新版本\\u003C\\u002Fb\\u003E\\u003C\\u002Fp\\u003E\\u003Cul\\u003E\\u003Cli\\u003EPython 3.x\\u003C\\u002Fli\\u003E\\u003C\\u002Ful\\u003E\\u003Cdiv class=\\"highlight\\"\\u003E\\u003Cpre\\u003E\\u003Ccode class=\\"language-text\\"\\u003E\\u003Cspan\\u003E\\u003C\\u002Fspan\\u003Epip3 install --upgrade pip\\n\\u003C\\u002Fcode\\u003E\\u003C\\u002Fpre\\u003E\\u003C\\u002Fdiv\\u003E\\u003Cul\\u003E\\u003Cli\\u003EPython 2.x\\u003C\\u002Fli\\u003E\\u003C\\u002Ful\\u003E\\u003Cdiv class=\\"highlight\\"\\u003E\\u003Cpre\\u003E\\u003Ccode class=\\"language-text\\"\\u003E\\u003Cspan\\u003E\\u003C\\u002Fspan\\u003Epip install --upgrade pip\\n\\u003C\\u002Fcode\\u003E\\u003C\\u002Fpre\\u003E\\u003C\\u002Fdiv\\u003E\\u003Cul\\u003E\\u003Cli\\u003E注意：老版本的pip在安装Jupyter Notebook过程中或面临依赖项无法同步安装的问题。因此\\u003Cb\\u003E强烈建议\\u003C\\u002Fb\\u003E先把pip升级到最新版本。\\u003C\\u002Fli\\u003E\\u003C\\u002Ful\\u003E\\u003Cp\\u003E\\u003Cb\\u003E2. 安装Jupyter Notebook\\u003C\\u002Fb\\u003E\\u003C\\u002Fp\\u003E\\u003Cul\\u003E\\u003Cli\\u003EPython 3.x\\u003C\\u002Fli\\u003E\\u003C\\u002Ful\\u003E\\u003Cdiv class=\\"highlight\\"\\u003E\\u003Cpre\\u003E\\u003Ccode class=\\"language-text\\"\\u003E\\u003Cspan\\u003E\\u003C\\u002Fspan\\u003Epip3 install jupyter\\n\\u003C\\u002Fcode\\u003E\\u003C\\u002Fpre\\u003E\\u003C\\u002Fdiv\\u003E\\u003Cul\\u003E\\u003Cli\\u003EPython 2.x\\u003C\\u002Fli\\u003E\\u003C\\u002Ful\\u003E\\u003Cdiv class=\\"highlight\\"\\u003E\\u003Cpre\\u003E\\u003Ccode class=\\"language-text\\"\\u003E\\u003Cspan\\u003E\\u003C\\u002Fspan\\u003Epip install jupyter\\n\\u003C\\u002Fcode\\u003E\\u003C\\u002Fpre\\u003E\\u003C\\u002Fdiv\\u003E\\u003Ch2\\u003E\\u003Cb\\u003E三、运行Jupyter Notebook\\u003C\\u002Fb\\u003E\\u003C\\u002Fh2\\u003E\\u003Ch2\\u003E\\u003Cb\\u003E0. 帮助\\u003C\\u002Fb\\u003E\\u003C\\u002Fh2\\u003E\\u003Cp\\u003E如果你有任何jupyter notebook命令的疑问，可以考虑查看官方帮助文档，命令如下：\\u003C\\u002Fp\\u003E\\u003Cdiv class=\\"highlight\\"\\u003E\\u003Cpre\\u003E\\u003Ccode class=\\"language-text\\"\\u003E\\u003Cspan\\u003E\\u003C\\u002Fspan\\u003Ejupyter notebook --help\\n\\u003C\\u002Fcode\\u003E\\u003C\\u002Fpre\\u003E\\u003C\\u002Fdiv\\u003E\\u003Cp\\u003E或\\u003C\\u002Fp\\u003E\\u003Cdiv class=\\"highlight\\"\\u003E\\u003Cpre\\u003E\\u003Ccode class=\\"language-text\\"\\u003E\\u003Cspan\\u003E\\u003C\\u002Fspan\\u003Ejupyter notebook -h\\n\\u003C\\u002Fcode\\u003E\\u003C\\u002Fpre\\u003E\\u003C\\u002Fdiv\\u003E\\u003Ch2\\u003E\\u003Cb\\u003E1. 启动\\u003C\\u002Fb\\u003E\\u003C\\u002Fh2\\u003E\\u003Ch2\\u003E\\u003Cb\\u003E① 默认端口启动\\u003C\\u002Fb\\u003E\\u003C\\u002Fh2\\u003E\\u003Cp\\u003E在终端中输入以下命令：\\u003C\\u002Fp\\u003E\\u003Cdiv class=\\"highlight\\"\\u003E\\u003Cpre\\u003E\\u003Ccode class=\\"language-bash\\"\\u003E\\u003Cspan\\u003E\\u003C\\u002Fspan\\u003Ejupyter notebook\\n\\u003C\\u002Fcode\\u003E\\u003C\\u002Fpre\\u003E\\u003C\\u002Fdiv\\u003E\\u003Cp\\u003E执行命令之后，在终端中将会显示一系列notebook的服务器信息，同时浏览器将会自动启动Jupyter Notebook。\\u003C\\u002Fp\\u003E\\u003Cp\\u003E启动过程中终端显示内容如下：\\u003C\\u002Fp\\u003E\\u003Cdiv class=\\"highlight\\"\\u003E\\u003Cpre\\u003E\\u003Ccode class=\\"language-text\\"\\u003E\\u003Cspan\\u003E\\u003C\\u002Fspan\\u003E$ jupyter notebook\\n\[I 08:58:24.417 NotebookApp\] Serving notebooks from local directory: \\u002FUsers\\u002Fcatherine\\n\[I 08:58:24.417 NotebookApp\] 0 active kernels\\n\[I 08:58:24.417 NotebookApp\] The Jupyter Notebook is running at: http:\\u002F\\u002Flocalhost:8888\\u002F\\n\[I 08:58:24.417 NotebookApp\] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).\\n\\u003C\\u002Fcode\\u003E\\u003C\\u002Fpre\\u003E\\u003C\\u002Fdiv\\u003E\\u003Cul\\u003E\\u003Cli\\u003E注意：之后在Jupyter Notebook的所有操作，都请保持终端\\u003Cb\\u003E不要关闭\\u003C\\u002Fb\\u003E，因为一旦关闭终端，就会断开与本地服务器的链接，你将无法在Jupyter Notebook中进行其他操作啦。\\u003C\\u002Fli\\u003E\\u003C\\u002Ful\\u003E\\u003Cp\\u003E浏览器地址栏中默认地将会显示：\\u003Ccode\\u003Ehttp:\\u002F\\u002Flocalhost:8888\\u003C\\u002Fcode\\u003E。其中，“localhost”指的是本机，“8888”则是端口号。 \\u003C\\u002Fp\\u003E\\u003Cfigure\\u003E\\u003Cnoscript\\u003E\\u003Cimg src=\\"https:\\u002F\\u002Fpic3.zhimg.com\\u002Fv2-3e14e522a5634717c566006702ca681e\_b.jpg\\" data-size=\\"normal\\" data-rawwidth=\\"1439\\" data-rawheight=\\"226\\" class=\\"origin\_image zh-lightbox-thumb\\" width=\\"1439\\" data-original=\\"https:\\u002F\\u002Fpic3.zhimg.com\\u002Fv2-3e14e522a5634717c566006702ca681e\_r.jpg\\"\\u003E\\u003C\\u002Fnoscript\\u003E\\u003Cimg src=\\"data:image\\u002Fsvg+xml;utf8,&lt;svg%20xmlns='http:\\u002F\\u002Fwww.w3.org\\u002F2000\\u002Fsvg'%20width='1439'%20height='226'&gt;&lt;\\u002Fsvg&gt;\\" data-size=\\"normal\\" data-rawwidth=\\"1439\\" data-rawheight=\\"226\\" class=\\"origin\_image zh-lightbox-thumb lazy\\" width=\\"1439\\" data-original=\\"https:\\u002F\\u002Fpic3.zhimg.com\\u002Fv2-3e14e522a5634717c566006702ca681e\_r.jpg\\" data-actualsrc=\\"https:\\u002F\\u002Fpic3.zhimg.com\\u002Fv2-3e14e522a5634717c566006702ca681e\_b.jpg\\"\\u003E\\u003Cfigcaption\\u003EURL\\u003C\\u002Ffigcaption\\u003E\\u003C\\u002Ffigure\\u003E\\u003Cp\\u003E如果你\\u003Cb\\u003E同时\\u003C\\u002Fb\\u003E启动了多个Jupyter Notebook，由于默认端口“8888”被占用，因此地址栏中的数字将从“8888”起，每多启动一个Jupyter Notebook数字就加1，如“8889”、“8890”……\\u003C\\u002Fp\\u003E\\u003Ch2\\u003E\\u003Cb\\u003E② 指定端口启动\\u003C\\u002Fb\\u003E\\u003C\\u002Fh2\\u003E\\u003Cp\\u003E如果你想自定义端口号来启动Jupyter Notebook，可以在终端中输入以下命令：\\u003C\\u002Fp\\u003E\\u003Cdiv class=\\"highlight\\"\\u003E\\u003Cpre\\u003E\\u003Ccode class=\\"language-text\\"\\u003E\\u003Cspan\\u003E\\u003C\\u002Fspan\\u003Ejupyter notebook --port &lt;port\_number&gt;\\n\\u003C\\u002Fcode\\u003E\\u003C\\u002Fpre\\u003E\\u003C\\u002Fdiv\\u003E\\u003Cp\\u003E其中，“&lt;port\_number&gt;”是自定义端口号，直接以数字的形式写在命令当中，数字两边不加尖括号“&lt;&gt;”。如：\\u003Ccode\\u003Ejupyter notebook --port 9999\\u003C\\u002Fcode\\u003E，即在端口号为“9999”的服务器启动Jupyter Notebook。\\u003C\\u002Fp\\u003E\\u003Ch2\\u003E\\u003Cb\\u003E③ 启动服务器但不打开浏览器\\u003C\\u002Fb\\u003E\\u003C\\u002Fh2\\u003E\\u003Cp\\u003E如果你只是想启动Jupyter Notebook的服务器但不打算立刻进入到主页面，那么就无需立刻启动浏览器。在终端中输入：\\u003C\\u002Fp\\u003E\\u003Cdiv class=\\"highlight\\"\\u003E\\u003Cpre\\u003E\\u003Ccode class=\\"language-text\\"\\u003E\\u003Cspan\\u003E\\u003C\\u002Fspan\\u003Ejupyter notebook --no-browser\\n\\u003C\\u002Fcode\\u003E\\u003C\\u002Fpre\\u003E\\u003C\\u002Fdiv\\u003E\\u003Cp\\u003E此时，将会在终端显示启动的服务器信息，并在服务器启动之后，显示出打开浏览器页面的链接。当你需要启动浏览器页面时，只需要复制链接，并粘贴在浏览器的地址栏中，轻按回车变转到了你的Jupyter Notebook页面。 \\u003C\\u002Fp\\u003E\\u003Cfigure\\u003E\\u003Cnoscript\\u003E\\u003Cimg src=\\"https:\\u002F\\u002Fpic3.zhimg.com\\u002Fv2-e43d4ba2c2a8c2cdcb6da3afeb0e1bca\_b.jpg\\" data-caption=\\"\\" data-size=\\"normal\\" data-rawwidth=\\"894\\" data-rawheight=\\"567\\" class=\\"origin\_image zh-lightbox-thumb\\" width=\\"894\\" data-original=\\"https:\\u002F\\u002Fpic3.zhimg.com\\u002Fv2-e43d4ba2c2a8c2cdcb6da3afeb0e1bca\_r.jpg\\"\\u003E\\u003C\\u002Fnoscript\\u003E\\u003Cimg src=\\"data:image\\u002Fsvg+xml;utf8,&lt;svg%20xmlns='http:\\u002F\\u002Fwww.w3.org\\u002F2000\\u002Fsvg'%20width='894'%20height='567'&gt;&lt;\\u002Fsvg&gt;\\" data-caption=\\"\\" data-size=\\"normal\\" data-rawwidth=\\"894\\" data-rawheight=\\"567\\" class=\\"origin\_image zh-lightbox-thumb lazy\\" width=\\"894\\" data-original=\\"https:\\u002F\\u002Fpic3.zhimg.com\\u002Fv2-e43d4ba2c2a8c2cdcb6da3afeb0e1bca\_r.jpg\\" data-actualsrc=\\"https:\\u002F\\u002Fpic3.zhimg.com\\u002Fv2-e43d4ba2c2a8c2cdcb6da3afeb0e1bca\_b.jpg\\"\\u003E\\u003C\\u002Ffigure\\u003E\\u003Cp\\u003E例图中由于在完成上面内容时我同时启动了多个Jupyter Notebook，因此显示我的“8888”端口号被占用，最终分配给我的是“8889”。\\u003C\\u002Fp\\u003E\\u003Ch2\\u003E\\u003Cb\\u003E2. 主页面\\u003C\\u002Fb\\u003E\\u003C\\u002Fh2\\u003E\\u003Ch2\\u003E\\u003Cb\\u003E① 主页面内容\\u003C\\u002Fb\\u003E\\u003C\\u002Fh2\\u003E\\u003Cp\\u003E当执行完启动命令之后，浏览器将会进入到Notebook的主页面，如下图所示。\\u003C\\u002Fp\\u003E\\u003Cfigure\\u003E\\u003Cnoscript\\u003E\\u003Cimg src=\\"https:\\u002F\\u002Fpic2.zhimg.com\\u002Fv2-32443bb8f73158ef24acd0c0bdf93ce5\_b.jpg\\" data-size=\\"normal\\" data-rawwidth=\\"1440\\" data-rawheight=\\"789\\" class=\\"origin\_image zh-lightbox-thumb\\" width=\\"1440\\" data-original=\\"https:\\u002F\\u002Fpic2.zhimg.com\\u002Fv2-32443bb8f73158ef24acd0c0bdf93ce5\_r.jpg\\"\\u003E\\u003C\\u002Fnoscript\\u003E\\u003Cimg src=\\"data:image\\u002Fsvg+xml;utf8,&lt;svg%20xmlns='http:\\u002F\\u002Fwww.w3.org\\u002F2000\\u002Fsvg'%20width='1440'%20height='789'&gt;&lt;\\u002Fsvg&gt;\\" data-size=\\"normal\\" data-rawwidth=\\"1440\\" data-rawheight=\\"789\\" class=\\"origin\_image zh-lightbox-thumb lazy\\" width=\\"1440\\" data-original=\\"https:\\u002F\\u002Fpic2.zhimg.com\\u002Fv2-32443bb8f73158ef24acd0c0bdf93ce5\_r.jpg\\" data-actualsrc=\\"https:\\u002F\\u002Fpic2.zhimg.com\\u002Fv2-32443bb8f73158ef24acd0c0bdf93ce5\_b.jpg\\"\\u003E\\u003Cfigcaption\\u003E默认主页面\\u003C\\u002Ffigcaption\\u003E\\u003C\\u002Ffigure\\u003E\\u003Cp\\u003E如果你的主页面里边的文件夹跟我的不同，或者你在疑惑为什么首次启动里边就已经有这么多文件夹，不要担心，这里边的文件夹全都是你的家目录里的目录文件。你可以在终端中执行以下2步来查看：\\u003C\\u002Fp\\u003E\\u003Cp\\u003E① \\u003Ccode\\u003Ecd\\u003C\\u002Fcode\\u003E 或 \\u003Ccode\\u003Ecd -\\u003C\\u002Fcode\\u003E 或 \\u003Ccode\\u003Ecd ~\\u003C\\u002Fcode\\u003E 或\\u003Ccode\\u003Ecd \\u002FUsers\\u002F&lt;user\_name&gt;\\u003C\\u002Fcode\\u003E\\u003C\\u002Fp\\u003E\\u003Cul\\u003E\\u003Cli\\u003E这个命令将会进入你的家目录。\\u003C\\u002Fli\\u003E\\u003Cli\\u003E“&lt;user\_name&gt;” 是用户名。用户名两边不加尖括号“&lt;&gt;”。\\u003C\\u002Fli\\u003E\\u003C\\u002Ful\\u003E\\u003Cp\\u003E② \\u003Ccode\\u003Els\\u003C\\u002Fcode\\u003E \\u003C\\u002Fp\\u003E\\u003Cul\\u003E\\u003Cli\\u003E这个命令将会展示你家目录下的文件。\\u003C\\u002Fli\\u003E\\u003C\\u002Ful\\u003E\\u003Ch2\\u003E\\u003Cb\\u003E② 设置Jupyter Notebook文件存放位置\\u003C\\u002Fb\\u003E\\u003C\\u002Fh2\\u003E\\u003Cp\\u003E如果你不想把今后在Jupyter Notebook中编写的所有文档都直接保存在家目录下，那你需要修改Jupyter Notebook的文件存放路径。\\u003C\\u002Fp\\u003E\\u003Ch2\\u003E\\u003Cb\\u003E⑴ 创建文件夹\\u002F目录\\u003C\\u002Fb\\u003E\\u003C\\u002Fh2\\u003E\\u003Cul\\u003E\\u003Cli\\u003EWindows用户在想要存放Jupyter Notebook文件的\\u003Cb\\u003E磁盘\\u003C\\u002Fb\\u003E中\\u003Cb\\u003E新建文件夹\\u003C\\u002Fb\\u003E并为该文件夹命名；双击进入该文件夹，然后复制地址栏中的路径。\\u003C\\u002Fli\\u003E\\u003Cli\\u003ELinux\\u002FmacOS用户在想要存放Jupyter Notebook文件的位置\\u003Cb\\u003E创建目录\\u003C\\u002Fb\\u003E并为目录命名，命令为：\\u003Ccode\\u003Emkdir &lt;directory\_name&gt;\\u003C\\u002Fcode\\u003E；进入目录，命令为：\\u003Ccode\\u003Ecd &lt;directory\_name&gt;\\u003C\\u002Fcode\\u003E；查看目录的路径，命令为：\\u003Ccode\\u003Epwd\\u003C\\u002Fcode\\u003E；复制该路径。\\u003C\\u002Fli\\u003E\\u003Cli\\u003E注意：“&lt;directory\_name&gt;”是自定义的目录名。目录名两边不加尖括号“&lt;&gt;”。\\u003C\\u002Fli\\u003E\\u003C\\u002Ful\\u003E\\u003Ch2\\u003E\\u003Cb\\u003E⑵ 配置文件路径\\u003C\\u002Fb\\u003E\\u003C\\u002Fh2\\u003E\\u003Cul\\u003E\\u003Cli\\u003E一个便捷获取配置文件所在路径的命令：\\u003C\\u002Fli\\u003E\\u003C\\u002Ful\\u003E\\u003Cdiv class=\\"highlight\\"\\u003E\\u003Cpre\\u003E\\u003Ccode class=\\"language-text\\"\\u003E\\u003Cspan\\u003E\\u003C\\u002Fspan\\u003Ejupyter notebook --generate-config\\n\\u003C\\u002Fcode\\u003E\\u003C\\u002Fpre\\u003E\\u003C\\u002Fdiv\\u003E\\u003Cul\\u003E\\u003Cli\\u003E注意： 这条命令虽然可以用于查看配置文件所在的路径，但主要用途是是否将这个路径下的配置文件\\u003Cb\\u003E替换\\u003C\\u002Fb\\u003E为\\u003Cb\\u003E默认配置文件\\u003C\\u002Fb\\u003E。 如果你是第一次查询，那么\\u003Cb\\u003E或许\\u003C\\u002Fb\\u003E不会出现下图的提示；若文件已经存在或被修改，使用这个命令之后会出现询问“Overwrite \\u002FUsers\\u002Fraxxie\\u002F.jupyter\\u002Fjupyter\_notebook\_config.py with default config? \[y\\u002FN\]”，即“用默认配置文件覆盖此路径下的文件吗？”，如果按“y”，则完成覆盖，那么之前所做的修改都将失效；如果只是为了查询路径，那么一定要输入“N”。\\u003C\\u002Fli\\u003E\\u003C\\u002Ful\\u003E\\u003Cfigure\\u003E\\u003Cnoscript\\u003E\\u003Cimg src=\\"https:\\u002F\\u002Fpic4.zhimg.com\\u002Fv2-da0d33d371c00fe08985cbce2b23bcc7\_b.jpg\\" data-size=\\"normal\\" data-rawwidth=\\"719\\" data-rawheight=\\"112\\" class=\\"origin\_image zh-lightbox-thumb\\" width=\\"719\\" data-original=\\"https:\\u002F\\u002Fpic4.zhimg.com\\u002Fv2-da0d33d371c00fe08985cbce2b23bcc7\_r.jpg\\"\\u003E\\u003C\\u002Fnoscript\\u003E\\u003Cimg src=\\"data:image\\u002Fsvg+xml;utf8,&lt;svg%20xmlns='http:\\u002F\\u002Fwww.w3.org\\u002F2000\\u002Fsvg'%20width='719'%20height='112'&gt;&lt;\\u002Fsvg&gt;\\" data-size=\\"normal\\" data-rawwidth=\\"719\\" data-rawheight=\\"112\\" class=\\"origin\_image zh-lightbox-thumb lazy\\" width=\\"719\\" data-original=\\"https:\\u002F\\u002Fpic4.zhimg.com\\u002Fv2-da0d33d371c00fe08985cbce2b23bcc7\_r.jpg\\" data-actualsrc=\\"https:\\u002F\\u002Fpic4.zhimg.com\\u002Fv2-da0d33d371c00fe08985cbce2b23bcc7\_b.jpg\\"\\u003E\\u003Cfigcaption\\u003E配置文件所在路径\\u003C\\u002Ffigcaption\\u003E\\u003C\\u002Ffigure\\u003E\\u003Cp\\u003E常规的情况下，Windows和Linux\\u002FmacOS的配置文件所在路径和配置文件名如下所述：\\u003C\\u002Fp\\u003E\\u003Cul\\u003E\\u003Cli\\u003EWindows系统的配置文件路径：\\u003Ccode\\u003EC:\\\Users\\\&lt;user\_name&gt;\\\.jupyter\\\\\u003C\\u002Fcode\\u003E\\u003C\\u002Fli\\u003E\\u003Cli\\u003ELinux\\u002FmacOS系统的配置文件路径：\\u003Ccode\\u003E\\u002FUsers\\u002F&lt;user\_name&gt;\\u002F.jupyter\\u002F\\u003C\\u002Fcode\\u003E 或 \\u003Ccode\\u003E~\\u002F.jupyter\\u002F\\u003C\\u002Fcode\\u003E\\u003C\\u002Fli\\u003E\\u003Cli\\u003E配置文件名：\\u003Ccode\\u003Ejupyter\_notebook\_config.py\\u003C\\u002Fcode\\u003E\\u003C\\u002Fli\\u003E\\u003C\\u002Ful\\u003E\\u003Cp\\u003E注意：\\u003C\\u002Fp\\u003E\\u003Cp\\u003E① “&lt;user\_name&gt;”为你的用户名。用户名两边不加尖括号“&lt;&gt;”。\\u003C\\u002Fp\\u003E\\u003Cp\\u003E② Windows和Linux\\u002FmacOS系统的配置文件存放路径其实是相同的，只是系统不同，表现形式有所不同而已。\\u003C\\u002Fp\\u003E\\u003Cp\\u003E③ Windows和Linux\\u002FmacOS系统的配置文件也是相同的。文件名以“.py”结尾，是Python的可执行文件。\\u003C\\u002Fp\\u003E\\u003Cp\\u003E④ 如果你不是通过一步到位的方式前往配置文件所在位置，而是一层一层进入文件夹\\u002F目录的，那么当你进入家目录后，用\\u003Ccode\\u003Els\\u003C\\u002Fcode\\u003E命令会发现找不到“.jupyter”文件夹\\u002F目录。这是因为凡是以“.”开头的目录都是隐藏文件，你可以通过\\u003Ccode\\u003Els -a\\u003C\\u002Fcode\\u003E命令查看当前位置下所有的隐藏文件。\\u003C\\u002Fp\\u003E\\u003Ch2\\u003E\\u003Cb\\u003E⑶ 修改配置文件\\u003C\\u002Fb\\u003E\\u003C\\u002Fh2\\u003E\\u003Cul\\u003E\\u003Cli\\u003EWindows系统的用户可以使用文档编辑工具或IDE打开“jupyter\_notebook\_config.py”文件并进行编辑。常用的文档编辑工具和IDE有记事本、Notepad++、vim、Sublime\\u003Cbr\\u003EText、PyCharm等。其中，vim是没有图形界面的，是一款学习曲线较为陡峭的编辑器，其他工具在此不做使用说明，因为上手相对简单。通过vim修改配置文件的方法请继续往下阅读。\\u003C\\u002Fli\\u003E\\u003Cli\\u003ELinux\\u002FmacOS系统的用户建议直接通过终端调用vim来对配置文件进行修改。具体操作步骤如下：\\u003C\\u002Fli\\u003E\\u003C\\u002Ful\\u003E\\u003Ch2\\u003E\\u003Cb\\u003E⒜ 打开配置文件\\u003C\\u002Fb\\u003E\\u003C\\u002Fh2\\u003E\\u003Cp\\u003E打开终端，输入命令：\\u003C\\u002Fp\\u003E\\u003Cdiv class=\\"highlight\\"\\u003E\\u003Cpre\\u003E\\u003Ccode class=\\"language-text\\"\\u003E\\u003Cspan\\u003E\\u003C\\u002Fspan\\u003Evim ~\\u002F.jupyter\\u002Fjupyter\_notebook\_config.py\\n\\u003C\\u002Fcode\\u003E\\u003C\\u002Fpre\\u003E\\u003C\\u002Fdiv\\u003E\\u003Cfigure\\u003E\\u003Cnoscript\\u003E\\u003Cimg src=\\"https:\\u002F\\u002Fpic3.zhimg.com\\u002Fv2-ec79adec540c62b244bd44df41f6c0ae\_b.jpg\\" data-size=\\"normal\\" data-rawwidth=\\"811\\" data-rawheight=\\"93\\" class=\\"origin\_image zh-lightbox-thumb\\" width=\\"811\\" data-original=\\"https:\\u002F\\u002Fpic3.zhimg.com\\u002Fv2-ec79adec540c62b244bd44df41f6c0ae\_r.jpg\\"\\u003E\\u003C\\u002Fnoscript\\u003E\\u003Cimg src=\\"data:image\\u002Fsvg+xml;utf8,&lt;svg%20xmlns='http:\\u002F\\u002Fwww.w3.org\\u002F2000\\u002Fsvg'%20width='811'%20height='93'&gt;&lt;\\u002Fsvg&gt;\\" data-size=\\"normal\\" data-rawwidth=\\"811\\" data-rawheight=\\"93\\" class=\\"origin\_image zh-lightbox-thumb lazy\\" width=\\"811\\" data-original=\\"https:\\u002F\\u002Fpic3.zhimg.com\\u002Fv2-ec79adec540c62b244bd44df41f6c0ae\_r.jpg\\" data-actualsrc=\\"https:\\u002F\\u002Fpic3.zhimg.com\\u002Fv2-ec79adec540c62b244bd44df41f6c0ae\_b.jpg\\"\\u003E\\u003Cfigcaption\\u003E命令详解\\u003C\\u002Ffigcaption\\u003E\\u003C\\u002Ffigure\\u003E\\u003Cp\\u003E执行上述命令后便进入到配置文件当中了。\\u003C\\u002Fp\\u003E\\u003Ch2\\u003E\\u003Cb\\u003E⒝ 查找关键词\\u003C\\u002Fb\\u003E\\u003C\\u002Fh2\\u003E\\u003Cp\\u003E进入配置文件后查找关键词“c.NotebookApp.notebook\_dir”。查找方法如下：\\u003C\\u002Fp\\u003E\\u003Cp\\u003E进入配置文件后不要按其他键，用\\u003Cb\\u003E英文半角\\u003C\\u002Fb\\u003E直接输入\\u003Ccode\\u003E\\u002Fc.NotebookApp.notebook\_dir\\u003C\\u002Fcode\\u003E，这时搜索的关键词已在文档中高亮显示了，按回车，光标从底部切换到文档正文中被查找关键词的首字母。\\u003C\\u002Fp\\u003E\\u003Ch2\\u003E\\u003Cb\\u003E⒞ 编辑配置文件\\u003C\\u002Fb\\u003E\\u003C\\u002Fh2\\u003E\\u003Cp\\u003E按\\u003Cb\\u003E小写i\\u003C\\u002Fb\\u003E进入编辑模式，底部出现“--INSERT--”说明成功进入编辑模式。使用方向键把光标定位在第二个单引号上（光标定位在哪个字符，就在这个字符前开始输入），把“⑴ 创建文件夹\\u002F目录”步骤中复制的路径粘贴在此处。\\u003C\\u002Fp\\u003E\\u003Ch2\\u003E\\u003Cb\\u003E⒟ 取消注释\\u003C\\u002Fb\\u003E\\u003C\\u002Fh2\\u003E\\u003Cp\\u003E把该行行首的\\u003Cb\\u003E井号（#）\\u003C\\u002Fb\\u003E删除。因为配置文件是Python的可执行文件，在Python中，井号（#）表示注释，即在编译过程中不会执行该行命令，所以为了使修改生效，需要删除井号（#）。 \\u003C\\u002Fp\\u003E\\u003Ch2\\u003E\\u003Cb\\u003E⒠ 保存配置文件\\u003C\\u002Fb\\u003E\\u003C\\u002Fh2\\u003E\\u003Cp\\u003E先按\\u003Ccode\\u003Eesc\\u003C\\u002Fcode\\u003E键，从编辑模式退出，回到命令模式。\\u003C\\u002Fp\\u003E\\u003Cp\\u003E再用\\u003Cb\\u003E英文半角\\u003C\\u002Fb\\u003E直接输入\\u003Ccode\\u003E:wq\\u003C\\u002Fcode\\u003E，回车即成功保存且退出了配置文件。\\u003C\\u002Fp\\u003E\\u003Cp\\u003E注意：\\u003C\\u002Fp\\u003E\\u003Cul\\u003E\\u003Cli\\u003E\\u003Cb\\u003E冒号（:）\\u003C\\u002Fb\\u003E 一定要有，且也是\\u003Cb\\u003E英文半角\\u003C\\u002Fb\\u003E。\\u003C\\u002Fli\\u003E\\u003Cli\\u003Ew：保存。\\u003C\\u002Fli\\u003E\\u003Cli\\u003Eq：退出。\\u003C\\u002Fli\\u003E\\u003C\\u002Ful\\u003E\\u003Ch2\\u003E\\u003Cb\\u003E⒡ 验证\\u003C\\u002Fb\\u003E\\u003C\\u002Fh2\\u003E\\u003Cp\\u003E在终端中输入命令\\u003Ccode\\u003Ejupyter notebook\\u003C\\u002Fcode\\u003E打开Jupyter Notebook，此时你会看到一个清爽的界面，恭喜！ \\u003C\\u002Fp\\u003E\\u003Cfigure\\u003E\\u003Cnoscript\\u003E\\u003Cimg src=\\"https:\\u002F\\u002Fpic1.zhimg.com\\u002Fv2-8d185cb051aea662a829e88ba486dbc4\_b.jpg\\" data-size=\\"normal\\" data-rawwidth=\\"1170\\" data-rawheight=\\"391\\" class=\\"origin\_image zh-lightbox-thumb\\" width=\\"1170\\" data-original=\\"https:\\u002F\\u002Fpic1.zhimg.com\\u002Fv2-8d185cb051aea662a829e88ba486dbc4\_r.jpg\\"\\u003E\\u003C\\u002Fnoscript\\u003E\\u003Cimg src=\\"data:image\\u002Fsvg+xml;utf8,&lt;svg%20xmlns='http:\\u002F\\u002Fwww.w3.org\\u002F2000\\u002Fsvg'%20width='1170'%20height='391'&gt;&lt;\\u002Fsvg&gt;\\" data-size=\\"normal\\" data-rawwidth=\\"1170\\" data-rawheight=\\"391\\" class=\\"origin\_image zh-lightbox-thumb lazy\\" width=\\"1170\\" data-original=\\"https:\\u002F\\u002Fpic1.zhimg.com\\u002Fv2-8d185cb051aea662a829e88ba486dbc4\_r.jpg\\" data-actualsrc=\\"https:\\u002F\\u002Fpic1.zhimg.com\\u002Fv2-8d185cb051aea662a829e88ba486dbc4\_b.jpg\\"\\u003E\\u003Cfigcaption\\u003E配置后主页面\\u003C\\u002Ffigcaption\\u003E\\u003C\\u002Ffigure\\u003E\\u003Ch2\\u003E\\u003Cb\\u003E⒢ 注意\\u003C\\u002Fb\\u003E\\u003C\\u002Fh2\\u003E\\u003Cul\\u003E\\u003Cli\\u003E以上所有命令均以\\u003Cb\\u003E英文半角\\u003C\\u002Fb\\u003E格式输入，若有报错，请严格检查这两个条件，\\u003Cb\\u003E英文\\u003C\\u002Fb\\u003E且\\u003Cb\\u003E半角\\u003C\\u002Fb\\u003E。\\u003C\\u002Fli\\u003E\\u003Cli\\u003E这里仅介绍了vim编辑器修改配置文件的方法，没有对vim编辑器的详细使用进行讲解，所以无需了解vim编辑器的具体使用方法，只需要按照上述步骤一定可以顺利完成修改！\\u003C\\u002Fli\\u003E\\u003Cli\\u003E推荐有时间和经历时学习一下vim编辑器的使用。这款强大的编辑器将会成为你未来工作中的利器。\\u003C\\u002Fli\\u003E\\u003C\\u002Ful\\u003E\\u003Ch2\\u003E\\u003Cb\\u003E四、Jupyter Notebook的基本使用\\u003C\\u002Fb\\u003E\\u003C\\u002Fh2\\u003E\\u003Ch2\\u003E\\u003Cb\\u003E1. Files页面\\u003C\\u002Fb\\u003E\\u003C\\u002Fh2\\u003E\\u003Cfigure\\u003E\\u003Cnoscript\\u003E\\u003Cimg src=\\"https:\\u002F\\u002Fpic1.zhimg.com\\u002Fv2-cb526cea874c6b91198a742766c44c70\_b.jpg\\" data-size=\\"normal\\" data-rawwidth=\\"1437\\" data-rawheight=\\"451\\" class=\\"origin\_image zh-lightbox-thumb\\" width=\\"1437\\" data-original=\\"https:\\u002F\\u002Fpic1.zhimg.com\\u002Fv2-cb526cea874c6b91198a742766c44c70\_r.jpg\\"\\u003E\\u003C\\u002Fnoscript\\u003E\\u003Cimg src=\\"data:image\\u002Fsvg+xml;utf8,&lt;svg%20xmlns='http:\\u002F\\u002Fwww.w3.org\\u002F2000\\u002Fsvg'%20width='1437'%20height='451'&gt;&lt;\\u002Fsvg&gt;\\" data-size=\\"normal\\" data-rawwidth=\\"1437\\" data-rawheight=\\"451\\" class=\\"origin\_image zh-lightbox-thumb lazy\\" width=\\"1437\\" data-original=\\"https:\\u002F\\u002Fpic1.zhimg.com\\u002Fv2-cb526cea874c6b91198a742766c44c70\_r.jpg\\" data-actualsrc=\\"https:\\u002F\\u002Fpic1.zhimg.com\\u002Fv2-cb526cea874c6b91198a742766c44c70\_b.jpg\\"\\u003E\\u003Cfigcaption\\u003EFiles页面\\u003C\\u002Ffigcaption\\u003E\\u003C\\u002Ffigure\\u003E\\u003Cp\\u003E此时你的界面当中应该还没有“Conda”和“Nbextensions”类目。不要着急，这两个类目将分别在“五、拓展功能”中的“\\u003Ca href=\\"https:\\u002F\\u002Fzhuanlan.zhihu.com\\u002Fp\\u002F33105153\\u002Fedit#conda\\" class=\\"internal\\"\\u003E1.关联Jupyter Notebook和conda的环境和包——‘nb\_conda’\\u003C\\u002Fa\\u003E”和“\\u003Ca href=\\"https:\\u002F\\u002Fzhuanlan.zhihu.com\\u002Fp\\u002F33105153\\u002Fedit#nbextensions\\" class=\\"internal\\"\\u003E2.Markdown生成目录\\u003C\\u002Fa\\u003E”中安装。\\u003C\\u002Fp\\u003E\\u003Cp\\u003EFiles页面是用于管理和创建文件相关的类目。\\u003C\\u002Fp\\u003E\\u003Cp\\u003E对于现有的文件，可以通过勾选文件的方式，对选中文件进行复制、重命名、移动、下载、查看、编辑和删除的操作。\\u003C\\u002Fp\\u003E\\u003Cp\\u003E同时，也可以根据需要，在“New”下拉列表中选择想要创建文件的环境，进行创建“ipynb”格式的笔记本、“txt”格式的文档、终端或文件夹。如果你创建的环境没有在下拉列表中显示，那么你需要依次前往“五、拓展功能”中的“\\u003Ca href=\\"https:\\u002F\\u002Fzhuanlan.zhihu.com\\u002Fp\\u002F33105153\\u002Fedit#conda\\" class=\\"internal\\"\\u003E1.关联Jupyter Notebook和conda的环境和包——‘nb\_conda’\\u003C\\u002Fa\\u003E”和“\\u003Ca href=\\"https:\\u002F\\u002Fzhuanlan.zhihu.com\\u002Fp\\u002F33105153\\u002Fedit#ipykernel\\" class=\\"internal\\"\\u003E六、增加内核——‘ipykernel’\\u003C\\u002Fa\\u003E”中解决该问题。\\u003C\\u002Fp\\u003E\\u003Ch2\\u003E\\u003Cb\\u003E① 笔记本的基本操作\\u003C\\u002Fb\\u003E\\u003C\\u002Fh2\\u003E\\u003Cfigure\\u003E\\u003Cnoscript\\u003E\\u003Cimg src=\\"https:\\u002F\\u002Fpic1.zhimg.com\\u002Fv2-3c250ee0349ff76d869ed80d456487cc\_b.jpg\\" data-size=\\"normal\\" data-rawwidth=\\"1440\\" data-rawheight=\\"424\\" class=\\"origin\_image zh-lightbox-thumb\\" width=\\"1440\\" data-original=\\"https:\\u002F\\u002Fpic1.zhimg.com\\u002Fv2-3c250ee0349ff76d869ed80d456487cc\_r.jpg\\"\\u003E\\u003C\\u002Fnoscript\\u003E\\u003Cimg src=\\"data:image\\u002Fsvg+xml;utf8,&lt;svg%20xmlns='http:\\u002F\\u002Fwww.w3.org\\u002F2000\\u002Fsvg'%20width='1440'%20height='424'&gt;&lt;\\u002Fsvg&gt;\\" data-size=\\"normal\\" data-rawwidth=\\"1440\\" data-rawheight=\\"424\\" class=\\"origin\_image zh-lightbox-thumb lazy\\" width=\\"1440\\" data-original=\\"https:\\u002F\\u002Fpic1.zhimg.com\\u002Fv2-3c250ee0349ff76d869ed80d456487cc\_r.jpg\\" data-actualsrc=\\"https:\\u002F\\u002Fpic1.zhimg.com\\u002Fv2-3c250ee0349ff76d869ed80d456487cc\_b.jpg\\"\\u003E\\u003Cfigcaption\\u003E笔记本页面注解图\\u003C\\u002Ffigcaption\\u003E\\u003C\\u002Ffigure\\u003E\\u003Cp\\u003E上图展示的是笔记本的基本结构和功能。根据图中的注解已经可以解决绝大多数的使用问题了！\\u003C\\u002Fp\\u003E\\u003Cp\\u003E工具栏的使用如图中的注解一样直观，在此不过多解释。需要特别说明的是“单元格的状态”，有Code，Markdown，Heading，Raw NBconvert。其中，最常用的是前两个，分别是代码状态，Markdown编写状态。Jupyter Notebook已经取消了Heading状态，即标题单元格。取而代之的是Markdown的一级至六级标题。而Raw NBconvert目前极少用到，此处也不做过多讲解。\\u003C\\u002Fp\\u003E\\u003Cp\\u003E菜单栏涵盖了笔记本的所有功能，即便是工具栏的功能，也都可以在菜单栏的类目里找到。然而，并不是所有功能都是常用的，比如Widgets，Navigate。Kernel类目的使用，主要是对内核的操作，比如中断、重启、连接、关闭、切换内核等，由于我们在创建笔记本时已经选择了内核，因此切换内核的操作便于我们在使用笔记本时切换到我们想要的内核环境中去。由于其他的功能相对比较常规，根据图中的注解来尝试使用笔记本的功能已经非常便捷，因此不再做详细讲解。\\u003C\\u002Fp\\u003E\\u003Ch2\\u003E\\u003Cb\\u003E② 笔记本重命名的两种方式\\u003C\\u002Fb\\u003E\\u003C\\u002Fh2\\u003E\\u003Ch2\\u003E\\u003Cb\\u003E⑴ 笔记本内部重命名\\u003C\\u002Fb\\u003E\\u003C\\u002Fh2\\u003E\\u003Cp\\u003E在使用笔记本时，可以直接在其内部进行重命名。在左上方“Jupyter”的图标旁有程序默认的标题“Untitled”，点击“Untitled”然后在弹出的对话框中输入自拟的标题，点击“Rename”即完成了重命名。\\u003C\\u002Fp\\u003E\\u003Ch2\\u003E\\u003Cb\\u003E⑵ 笔记本外部重命名\\u003C\\u002Fb\\u003E\\u003C\\u002Fh2\\u003E\\u003Cp\\u003E若在使用笔记本时忘记了重命名，且已经保存并退出至“Files”界面，则在“Files”界面勾选需要重命名的文件，点击“Rename”然后直接输入自拟的标题即可。\\u003C\\u002Fp\\u003E\\u003Ch2\\u003E\\u003Cb\\u003E⑶ 演示\\u003C\\u002Fb\\u003E\\u003C\\u002Fh2\\u003E\\u003Cfigure\\u003E\\u003Cnoscript\\u003E\\u003Cimg src=\\"https:\\u002F\\u002Fpic1.zhimg.com\\u002Fv2-e2504cf777d5c7253a28411e3abb50a4\_b.gif\\" data-size=\\"normal\\" data-rawwidth=\\"1438\\" data-rawheight=\\"567\\" data-thumbnail=\\"https:\\u002F\\u002Fpic1.zhimg.com\\u002Fv2-e2504cf777d5c7253a28411e3abb50a4\_b.jpg\\" class=\\"origin\_image zh-lightbox-thumb\\" width=\\"1438\\" data-original=\\"https:\\u002F\\u002Fpic1.zhimg.com\\u002Fv2-e2504cf777d5c7253a28411e3abb50a4\_r.jpg\\"\\u003E\\u003C\\u002Fnoscript\\u003E\\u003Cimg src=\\"data:image\\u002Fsvg+xml;utf8,&lt;svg%20xmlns='http:\\u002F\\u002Fwww.w3.org\\u002F2000\\u002Fsvg'%20width='1438'%20height='567'&gt;&lt;\\u002Fsvg&gt;\\" data-size=\\"normal\\" data-rawwidth=\\"1438\\" data-rawheight=\\"567\\" data-thumbnail=\\"https:\\u002F\\u002Fpic1.zhimg.com\\u002Fv2-e2504cf777d5c7253a28411e3abb50a4\_b.jpg\\" class=\\"origin\_image zh-lightbox-thumb lazy\\" width=\\"1438\\" data-original=\\"https:\\u002F\\u002Fpic1.zhimg.com\\u002Fv2-e2504cf777d5c7253a28411e3abb50a4\_r.jpg\\" data-actualsrc=\\"https:\\u002F\\u002Fpic1.zhimg.com\\u002Fv2-e2504cf777d5c7253a28411e3abb50a4\_b.gif\\"\\u003E\\u003Cfigcaption\\u003E笔记本重命名演示图\\u003C\\u002Ffigcaption\\u003E\\u003C\\u002Ffigure\\u003E\\u003Cp\\u003E\\u003Cbr\\u003E\\u003C\\u002Fp\\u003E\\u003Cp\\u003E\\u003Cbr\\u003E\\u003C\\u002Fp\\u003E\\u003Ch2\\u003E\\u003Cb\\u003E2. Running页面\\u003C\\u002Fb\\u003E\\u003C\\u002Fh2\\u003E\\u003Cp\\u003ERunning页面主要展示的是当前正在运行当中的终端和“ipynb”格式的笔记本。若想要关闭已经打开的终端和“ipynb”格式的笔记本，仅仅关闭其页面是无法彻底退出程序的，需要在Running页面点击其对应的“Shutdown”。更多关闭方法可以查阅“八、关闭和退出”中的“\\u003Ca href=\\"https:\\u002F\\u002Fzhuanlan.zhihu.com\\u002Fp\\u002F33105153\\u002Fedit#quit\\" class=\\"internal\\"\\u003E1.关闭笔记本和终端\\u003C\\u002Fa\\u003E”。\\u003C\\u002Fp\\u003E\\u003Cfigure\\u003E\\u003Cnoscript\\u003E\\u003Cimg src=\\"https:\\u002F\\u002Fpic4.zhimg.com\\u002Fv2-ca637455e9537c30205e0b85b6901327\_b.gif\\" data-size=\\"normal\\" data-rawwidth=\\"1438\\" data-rawheight=\\"419\\" data-thumbnail=\\"https:\\u002F\\u002Fpic4.zhimg.com\\u002Fv2-ca637455e9537c30205e0b85b6901327\_b.jpg\\" class=\\"origin\_image zh-lightbox-thumb\\" width=\\"1438\\" data-original=\\"https:\\u002F\\u002Fpic4.zhimg.com\\u002Fv2-ca637455e9537c30205e0b85b6901327\_r.jpg\\"\\u003E\\u003C\\u002Fnoscript\\u003E\\u003Cimg src=\\"data:image\\u002Fsvg+xml;utf8,&lt;svg%20xmlns='http:\\u002F\\u002Fwww.w3.org\\u002F2000\\u002Fsvg'%20width='1438'%20height='419'&gt;&lt;\\u002Fsvg&gt;\\" data-size=\\"normal\\" data-rawwidth=\\"1438\\" data-rawheight=\\"419\\" data-thumbnail=\\"https:\\u002F\\u002Fpic4.zhimg.com\\u002Fv2-ca637455e9537c30205e0b85b6901327\_b.jpg\\" class=\\"origin\_image zh-lightbox-thumb lazy\\" width=\\"1438\\" data-original=\\"https:\\u002F\\u002Fpic4.zhimg.com\\u002Fv2-ca637455e9537c30205e0b85b6901327\_r.jpg\\" data-actualsrc=\\"https:\\u002F\\u002Fpic4.zhimg.com\\u002Fv2-ca637455e9537c30205e0b85b6901327\_b.gif\\"\\u003E\\u003Cfigcaption\\u003ERunning页面功能演示图\\u003C\\u002Ffigcaption\\u003E\\u003C\\u002Ffigure\\u003E\\u003Cp\\u003E\\u003Cbr\\u003E\\u003C\\u002Fp\\u003E\\u003Cp\\u003E\\u003Cbr\\u003E\\u003C\\u002Fp\\u003E\\u003Ch2\\u003E\\u003Cb\\u003E3. Clusters页面\\u003C\\u002Fb\\u003E\\u003C\\u002Fh2\\u003E\\u003Cblockquote\\u003EClusters tab is now provided by IPython parallel. See '\\u003Ca href=\\"http:\\u002F\\u002Flink.zhihu.com\\u002F?target=https%3A\\u002F\\u002Fgithub.com\\u002Fipython\\u002Fipyparallel\\" class=\\" wrap external\\" target=\\"\_blank\\" rel=\\"nofollow noreferrer\\"\\u003EIPython parallel\\u003C\\u002Fa\\u003E' for\\u003Cbr\\u003Einstallation details.\\u003C\\u002Fblockquote\\u003E\\u003Cp\\u003EClusters类目现在已由IPython parallel对接，且由于现阶段使用频率较低，因此在此不做详细说明，想要了解更多可以访问\\u003Ca href=\\"http:\\u002F\\u002Flink.zhihu.com\\u002F?target=https%3A\\u002F\\u002Fgithub.com\\u002Fipython\\u002Fipyparallel\\" class=\\" wrap external\\" target=\\"\_blank\\" rel=\\"nofollow noreferrer\\"\\u003EIPython parallel的官方网站\\u003C\\u002Fa\\u003E。\\u003C\\u002Fp\\u003E\\u003Ch2\\u003E\\u003Cb\\u003E4. Conda页面\\u003C\\u002Fb\\u003E\\u003C\\u002Fh2\\u003E\\u003Cp\\u003EConda页面主要是Jupyter Notebook与Conda关联之后对Conda环境和包进行直接操作和管理的页面工具。详细信息请直接查阅“五、拓展功能”中的“\\u003Ca href=\\"https:\\u002F\\u002Fzhuanlan.zhihu.com\\u002Fp\\u002F33105153\\u002Fedit#conda\\" class=\\"internal\\"\\u003E1.关联Jupyter Notebook和conda的环境和包——‘nb\_conda’\\u003C\\u002Fa\\u003E”。这是目前使用Jupyter Notebook的必备环节，因此请务必查阅。\\u003C\\u002Fp\\u003E\\u003Ch2\\u003E\\u003Cb\\u003E5. Nbextensions页面\\u003C\\u002Fb\\u003E\\u003C\\u002Fh2\\u003E\\u003Cp\\u003ENbextensions页面提供了多个Jupyter Notebook的插件，使其功能更加强大。该页面中主要使用的插件有nb\_conda，nb\_present，Table of Contents(2)。这些功能我们无需完全掌握，也无需安装所有的扩展功能，根据本文档提供的学习思路，我们只需要安装Talbe of Contents(2)即可，该功能可为Markdown文档提供目录导航，便于我们编写文档。该安装指导请查阅“五、拓展功能”中的“\\u003Ca href=\\"https:\\u002F\\u002Fzhuanlan.zhihu.com\\u002Fp\\u002F33105153\\u002Fedit#nbextensions\\" class=\\"internal\\"\\u003E2.Markdown生成目录\\u003C\\u002Fa\\u003E”。\\u003C\\u002Fp\\u003E\\u003Cfigure\\u003E\\u003Cnoscript\\u003E\\u003Cimg src=\\"https:\\u002F\\u002Fpic2.zhimg.com\\u002Fv2-a7a2f4b1f06aed21df09b6e3b957e191\_b.jpg\\" data-size=\\"normal\\" data-rawwidth=\\"1440\\" data-rawheight=\\"592\\" class=\\"origin\_image zh-lightbox-thumb\\" width=\\"1440\\" data-original=\\"https:\\u002F\\u002Fpic2.zhimg.com\\u002Fv2-a7a2f4b1f06aed21df09b6e3b957e191\_r.jpg\\"\\u003E\\u003C\\u002Fnoscript\\u003E\\u003Cimg src=\\"data:image\\u002Fsvg+xml;utf8,&lt;svg%20xmlns='http:\\u002F\\u002Fwww.w3.org\\u002F2000\\u002Fsvg'%20width='1440'%20height='592'&gt;&lt;\\u002Fsvg&gt;\\" data-size=\\"normal\\" data-rawwidth=\\"1440\\" data-rawheight=\\"592\\" class=\\"origin\_image zh-lightbox-thumb lazy\\" width=\\"1440\\" data-original=\\"https:\\u002F\\u002Fpic2.zhimg.com\\u002Fv2-a7a2f4b1f06aed21df09b6e3b957e191\_r.jpg\\" data-actualsrc=\\"https:\\u002F\\u002Fpic2.zhimg.com\\u002Fv2-a7a2f4b1f06aed21df09b6e3b957e191\_b.jpg\\"\\u003E\\u003Cfigcaption\\u003ENbextensions页面\\u003C\\u002Ffigcaption\\u003E\\u003C\\u002Ffigure\\u003E\\u003Ch2\\u003E\\u003Cb\\u003E五、拓展功能\\u003C\\u002Fb\\u003E\\u003C\\u002Fh2\\u003E\\u003Ch2\\u003E\\u003Cb\\u003E1. 关联Jupyter Notebook和conda的环境和包——“nb\_conda”☆\\u003C\\u002Fb\\u003E\\u003C\\u002Fh2\\u003E\\u003Ch2\\u003E\\u003Cb\\u003E① 安装\\u003C\\u002Fb\\u003E\\u003C\\u002Fh2\\u003E\\u003Cdiv class=\\"highlight\\"\\u003E\\u003Cpre\\u003E\\u003Ccode class=\\"language-text\\"\\u003E\\u003Cspan\\u003E\\u003C\\u002Fspan\\u003Econda install nb\_conda\\n\\u003C\\u002Fcode\\u003E\\u003C\\u002Fpre\\u003E\\u003C\\u002Fdiv\\u003E\\u003Cp\\u003E执行上述命令能够将你conda创建的环境与Jupyter Notebook相关联，便于你在Jupyter Notebook的使用中，在不同的环境下创建笔记本进行工作。\\u003C\\u002Fp\\u003E\\u003Ch2\\u003E\\u003Cb\\u003E② 使用\\u003C\\u002Fb\\u003E\\u003C\\u002Fh2\\u003E\\u003Cul\\u003E\\u003Cli\\u003E可以在Conda类目下对conda环境和包进行一系列操作。 \\u003C\\u002Fli\\u003E\\u003C\\u002Ful\\u003E\\u003Cfigure\\u003E\\u003Cnoscript\\u003E\\u003Cimg src=\\"https:\\u002F\\u002Fpic2.zhimg.com\\u002Fv2-75db6aec2cf08a29014679435675f17d\_b.jpg\\" data-size=\\"normal\\" data-rawwidth=\\"1439\\" data-rawheight=\\"716\\" class=\\"origin\_image zh-lightbox-thumb\\" width=\\"1439\\" data-original=\\"https:\\u002F\\u002Fpic2.zhimg.com\\u002Fv2-75db6aec2cf08a29014679435675f17d\_r.jpg\\"\\u003E\\u003C\\u002Fnoscript\\u003E\\u003Cimg src=\\"data:image\\u002Fsvg+xml;utf8,&lt;svg%20xmlns='http:\\u002F\\u002Fwww.w3.org\\u002F2000\\u002Fsvg'%20width='1439'%20height='716'&gt;&lt;\\u002Fsvg&gt;\\" data-size=\\"normal\\" data-rawwidth=\\"1439\\" data-rawheight=\\"716\\" class=\\"origin\_image zh-lightbox-thumb lazy\\" width=\\"1439\\" data-original=\\"https:\\u002F\\u002Fpic2.zhimg.com\\u002Fv2-75db6aec2cf08a29014679435675f17d\_r.jpg\\" data-actualsrc=\\"https:\\u002F\\u002Fpic2.zhimg.com\\u002Fv2-75db6aec2cf08a29014679435675f17d\_b.jpg\\"\\u003E\\u003Cfigcaption\\u003EConda页面注解图\\u003C\\u002Ffigcaption\\u003E\\u003C\\u002Ffigure\\u003E\\u003Cul\\u003E\\u003Cli\\u003E可以在笔记本内的“Kernel”类目里的“Change\\u003Cbr\\u003Ekernel”切换内核。 \\u003C\\u002Fli\\u003E\\u003C\\u002Ful\\u003E\\u003Cfigure\\u003E\\u003Cnoscript\\u003E\\u003Cimg src=\\"https:\\u002F\\u002Fpic2.zhimg.com\\u002Fv2-6a926273202380b5fd5e51dff7941dfd\_b.jpg\\" data-size=\\"normal\\" data-rawwidth=\\"1440\\" data-rawheight=\\"435\\" class=\\"origin\_image zh-lightbox-thumb\\" width=\\"1440\\" data-original=\\"https:\\u002F\\u002Fpic2.zhimg.com\\u002Fv2-6a926273202380b5fd5e51dff7941dfd\_r.jpg\\"\\u003E\\u003C\\u002Fnoscript\\u003E\\u003Cimg src=\\"data:image\\u002Fsvg+xml;utf8,&lt;svg%20xmlns='http:\\u002F\\u002Fwww.w3.org\\u002F2000\\u002Fsvg'%20width='1440'%20height='435'&gt;&lt;\\u002Fsvg&gt;\\" data-size=\\"normal\\" data-rawwidth=\\"1440\\" data-rawheight=\\"435\\" class=\\"origin\_image zh-lightbox-thumb lazy\\" width=\\"1440\\" data-original=\\"https:\\u002F\\u002Fpic2.zhimg.com\\u002Fv2-6a926273202380b5fd5e51dff7941dfd\_r.jpg\\" data-actualsrc=\\"https:\\u002F\\u002Fpic2.zhimg.com\\u002Fv2-6a926273202380b5fd5e51dff7941dfd\_b.jpg\\"\\u003E\\u003Cfigcaption\\u003E切换内核\\u003C\\u002Ffigcaption\\u003E\\u003C\\u002Ffigure\\u003E\\u003Ch2\\u003E\\u003Cb\\u003E③ 卸载\\u003C\\u002Fb\\u003E\\u003C\\u002Fh2\\u003E\\u003Cdiv class=\\"highlight\\"\\u003E\\u003Cpre\\u003E\\u003Ccode class=\\"language-text\\"\\u003E\\u003Cspan\\u003E\\u003C\\u002Fspan\\u003Ecanda remove nb\_conda\\n\\u003C\\u002Fcode\\u003E\\u003C\\u002Fpre\\u003E\\u003C\\u002Fdiv\\u003E\\u003Cp\\u003E执行上述命令即可卸载nb\_conda包。\\u003C\\u002Fp\\u003E\\u003Ch2\\u003E\\u003Cb\\u003E2. Markdown生成目录\\u003C\\u002Fb\\u003E\\u003C\\u002Fh2\\u003E\\u003Cul\\u003E\\u003Cli\\u003E不同于有道云笔记的Markdown编译器，Jupyter Notebook无法为Markdown文档通过特定语法添加目录，因此需要通过安装扩展来实现目录的添加。\\u003C\\u002Fli\\u003E\\u003C\\u002Ful\\u003E\\u003Cdiv class=\\"highlight\\"\\u003E\\u003Cpre\\u003E\\u003Ccode class=\\"language-text\\"\\u003E\\u003Cspan\\u003E\\u003C\\u002Fspan\\u003Econda install -c conda-forge jupyter\_contrib\_nbextensions\\n\\u003C\\u002Fcode\\u003E\\u003C\\u002Fpre\\u003E\\u003C\\u002Fdiv\\u003E\\u003Cul\\u003E\\u003Cli\\u003E执行上述命令后，启动Jupyter Notebook，你会发现导航栏多了“Nbextensions”的类目，点击“Nbextensions”，勾选“Table\\u003Cbr\\u003Eof Contents ⑵”\\u003C\\u002Fli\\u003E\\u003C\\u002Ful\\u003E\\u003Cfigure\\u003E\\u003Cnoscript\\u003E\\u003Cimg src=\\"https:\\u002F\\u002Fpic2.zhimg.com\\u002Fv2-a7a2f4b1f06aed21df09b6e3b957e191\_b.jpg\\" data-size=\\"normal\\" data-rawwidth=\\"1440\\" data-rawheight=\\"592\\" class=\\"origin\_image zh-lightbox-thumb\\" width=\\"1440\\" data-original=\\"https:\\u002F\\u002Fpic2.zhimg.com\\u002Fv2-a7a2f4b1f06aed21df09b6e3b957e191\_r.jpg\\"\\u003E\\u003C\\u002Fnoscript\\u003E\\u003Cimg src=\\"data:image\\u002Fsvg+xml;utf8,&lt;svg%20xmlns='http:\\u002F\\u002Fwww.w3.org\\u002F2000\\u002Fsvg'%20width='1440'%20height='592'&gt;&lt;\\u002Fsvg&gt;\\" data-size=\\"normal\\" data-rawwidth=\\"1440\\" data-rawheight=\\"592\\" class=\\"origin\_image zh-lightbox-thumb lazy\\" width=\\"1440\\" data-original=\\"https:\\u002F\\u002Fpic2.zhimg.com\\u002Fv2-a7a2f4b1f06aed21df09b6e3b957e191\_r.jpg\\" data-actualsrc=\\"https:\\u002F\\u002Fpic2.zhimg.com\\u002Fv2-a7a2f4b1f06aed21df09b6e3b957e191\_b.jpg\\"\\u003E\\u003Cfigcaption\\u003ENbextensions页面\\u003C\\u002Ffigcaption\\u003E\\u003C\\u002Ffigure\\u003E\\u003Cul\\u003E\\u003Cli\\u003E之后再在Jupyter Notebook中使用Markdown，点击下图的图标即可使用啦。\\u003C\\u002Fli\\u003E\\u003C\\u002Ful\\u003E\\u003Cfigure\\u003E\\u003Cnoscript\\u003E\\u003Cimg src=\\"https:\\u002F\\u002Fpic2.zhimg.com\\u002Fv2-dd9b3a1f62c89570a47c7f6d24bf01a1\_b.jpg\\" data-size=\\"normal\\" data-rawwidth=\\"1435\\" data-rawheight=\\"712\\" class=\\"origin\_image zh-lightbox-thumb\\" width=\\"1435\\" data-original=\\"https:\\u002F\\u002Fpic2.zhimg.com\\u002Fv2-dd9b3a1f62c89570a47c7f6d24bf01a1\_r.jpg\\"\\u003E\\u003C\\u002Fnoscript\\u003E\\u003Cimg src=\\"data:image\\u002Fsvg+xml;utf8,&lt;svg%20xmlns='http:\\u002F\\u002Fwww.w3.org\\u002F2000\\u002Fsvg'%20width='1435'%20height='712'&gt;&lt;\\u002Fsvg&gt;\\" data-size=\\"normal\\" data-rawwidth=\\"1435\\" data-rawheight=\\"712\\" class=\\"origin\_image zh-lightbox-thumb lazy\\" width=\\"1435\\" data-original=\\"https:\\u002F\\u002Fpic2.zhimg.com\\u002Fv2-dd9b3a1f62c89570a47c7f6d24bf01a1\_r.jpg\\" data-actualsrc=\\"https:\\u002F\\u002Fpic2.zhimg.com\\u002Fv2-dd9b3a1f62c89570a47c7f6d24bf01a1\_b.jpg\\"\\u003E\\u003Cfigcaption\\u003E目录\\u003C\\u002Ffigcaption\\u003E\\u003C\\u002Ffigure\\u003E\\u003Ch2\\u003E\\u003Cb\\u003E3. Markdown在文中设置链接并定位\\u003C\\u002Fb\\u003E\\u003C\\u002Fh2\\u003E\\u003Cp\\u003E在使用Markdown编辑文档时，难免会遇到需要在文中设定链接，定位在文档中的其他位置便于查看。因为Markdown可以完美的兼容html语法，因此这种功能可以通过html语法当中“a标签”的索引用法来实现。\\u003C\\u002Fp\\u003E\\u003Cp\\u003E语法格式如下：\\u003C\\u002Fp\\u003E\\u003Cdiv class=\\"highlight\\"\\u003E\\u003Cpre\\u003E\\u003Ccode class=\\"language-text\\"\\u003E\\u003Cspan\\u003E\\u003C\\u002Fspan\\u003E\[添加链接的正文\](#自定义索引词)\\n&lt;a id=自定义索引词&gt;跳转提示&lt;\\u002Fa&gt;\\n\\u003C\\u002Fcode\\u003E\\u003C\\u002Fpre\\u003E\\u003C\\u002Fdiv\\u003E\\u003Cp\\u003E注意：\\u003C\\u002Fp\\u003E\\u003Col\\u003E\\u003Col\\u003E\\u003Cli\\u003E语法格式当中所有的符号均是\\u003Cb\\u003E英文半角\\u003C\\u002Fb\\u003E。\\u003C\\u002Fli\\u003E\\u003Cli\\u003E“自定义索引词”最好是英文，较长的词可以用下划线连接。\\u003C\\u002Fli\\u003E\\u003Cli\\u003E“a标签”出现在想要被跳转到的文章位置，html标签除了单标签外均要符合“有头（\\u003Ccode\\u003E&lt;a&gt;\\u003C\\u002Fcode\\u003E）必有尾（\\u003Ccode\\u003E&lt;\\u002Fa&gt;\\u003C\\u002Fcode\\u003E）”的原则。头尾之间的“跳转提示”是可有可无的。\\u003C\\u002Fli\\u003E\\u003Cli\\u003E“a标签”中的“id”值即是为正文中添加链接时设定的“自定义索引值”，这里通过“id”的值实现从正文的链接跳转至指定位置的功能。\\u003C\\u002Fli\\u003E\\u003C\\u002Fol\\u003E\\u003C\\u002Fol\\u003E\\u003Cp\\u003E例：\\u003C\\u002Fp\\u003E\\u003Cfigure\\u003E\\u003Cnoscript\\u003E\\u003Cimg src=\\"https:\\u002F\\u002Fpic3.zhimg.com\\u002Fv2-33dd1aeea782e414db9b703f75f0f32e\_b.gif\\" data-size=\\"normal\\" data-rawwidth=\\"1438\\" data-rawheight=\\"712\\" data-thumbnail=\\"https:\\u002F\\u002Fpic3.zhimg.com\\u002Fv2-33dd1aeea782e414db9b703f75f0f32e\_b.jpg\\" class=\\"origin\_image zh-lightbox-thumb\\" width=\\"1438\\" data-original=\\"https:\\u002F\\u002Fpic3.zhimg.com\\u002Fv2-33dd1aeea782e414db9b703f75f0f32e\_r.jpg\\"\\u003E\\u003C\\u002Fnoscript\\u003E\\u003Cimg src=\\"data:image\\u002Fsvg+xml;utf8,&lt;svg%20xmlns='http:\\u002F\\u002Fwww.w3.org\\u002F2000\\u002Fsvg'%20width='1438'%20height='712'&gt;&lt;\\u002Fsvg&gt;\\" data-size=\\"normal\\" data-rawwidth=\\"1438\\" data-rawheight=\\"712\\" data-thumbnail=\\"https:\\u002F\\u002Fpic3.zhimg.com\\u002Fv2-33dd1aeea782e414db9b703f75f0f32e\_b.jpg\\" class=\\"origin\_image zh-lightbox-thumb lazy\\" width=\\"1438\\" data-original=\\"https:\\u002F\\u002Fpic3.zhimg.com\\u002Fv2-33dd1aeea782e414db9b703f75f0f32e\_r.jpg\\" data-actualsrc=\\"https:\\u002F\\u002Fpic3.zhimg.com\\u002Fv2-33dd1aeea782e414db9b703f75f0f32e\_b.gif\\"\\u003E\\u003Cfigcaption\\u003E有跳转提示语\\u003C\\u002Ffigcaption\\u003E\\u003C\\u002Ffigure\\u003E\\u003Cp\\u003E\\u003Cbr\\u003E\\u003C\\u002Fp\\u003E\\u003Cp\\u003E\\u003Cbr\\u003E\\u003C\\u002Fp\\u003E\\u003Cfigure\\u003E\\u003Cnoscript\\u003E\\u003Cimg src=\\"https:\\u002F\\u002Fpic1.zhimg.com\\u002Fv2-c89c8598922c7077b1570e96e4b57428\_b.gif\\" data-size=\\"normal\\" data-rawwidth=\\"1436\\" data-rawheight=\\"711\\" data-thumbnail=\\"https:\\u002F\\u002Fpic1.zhimg.com\\u002Fv2-c89c8598922c7077b1570e96e4b57428\_b.jpg\\" class=\\"origin\_image zh-lightbox-thumb\\" width=\\"1436\\" data-original=\\"https:\\u002F\\u002Fpic1.zhimg.com\\u002Fv2-c89c8598922c7077b1570e96e4b57428\_r.jpg\\"\\u003E\\u003C\\u002Fnoscript\\u003E\\u003Cimg src=\\"data:image\\u002Fsvg+xml;utf8,&lt;svg%20xmlns='http:\\u002F\\u002Fwww.w3.org\\u002F2000\\u002Fsvg'%20width='1436'%20height='711'&gt;&lt;\\u002Fsvg&gt;\\" data-size=\\"normal\\" data-rawwidth=\\"1436\\" data-rawheight=\\"711\\" data-thumbnail=\\"https:\\u002F\\u002Fpic1.zhimg.com\\u002Fv2-c89c8598922c7077b1570e96e4b57428\_b.jpg\\" class=\\"origin\_image zh-lightbox-thumb lazy\\" width=\\"1436\\" data-original=\\"https:\\u002F\\u002Fpic1.zhimg.com\\u002Fv2-c89c8598922c7077b1570e96e4b57428\_r.jpg\\" data-actualsrc=\\"https:\\u002F\\u002Fpic1.zhimg.com\\u002Fv2-c89c8598922c7077b1570e96e4b57428\_b.gif\\"\\u003E\\u003Cfigcaption\\u003E无跳转提示语\\u003C\\u002Ffigcaption\\u003E\\u003C\\u002Ffigure\\u003E\\u003Cp\\u003E\\u003Cbr\\u003E\\u003C\\u002Fp\\u003E\\u003Cp\\u003E\\u003Cbr\\u003E\\u003C\\u002Fp\\u003E\\u003Ch2\\u003E\\u003Cb\\u003E4. 加载指定网页源代码\\u003C\\u002Fb\\u003E\\u003C\\u002Fh2\\u003E\\u003Ch2\\u003E\\u003Cb\\u003E① 使用场景\\u003C\\u002Fb\\u003E\\u003C\\u002Fh2\\u003E\\u003Cp\\u003E想要在Jupyter Notebook中直接加载指定网站的源代码到笔记本中。\\u003C\\u002Fp\\u003E\\u003Ch2\\u003E\\u003Cb\\u003E② 方法\\u003C\\u002Fb\\u003E\\u003C\\u002Fh2\\u003E\\u003Cp\\u003E执行以下命令:\\u003C\\u002Fp\\u003E\\u003Cdiv class=\\"highlight\\"\\u003E\\u003Cpre\\u003E\\u003Ccode class=\\"language-text\\"\\u003E\\u003Cspan\\u003E\\u003C\\u002Fspan\\u003E%load URL\\n\\u003C\\u002Fcode\\u003E\\u003C\\u002Fpre\\u003E\\u003C\\u002Fdiv\\u003E\\u003Cp\\u003E其中，URL为指定网站的地址。\\u003C\\u002Fp\\u003E\\u003Ch2\\u003E\\u003Cb\\u003E③ 例\\u003C\\u002Fb\\u003E\\u003C\\u002Fh2\\u003E\\u003Cfigure\\u003E\\u003Cnoscript\\u003E\\u003Cimg src=\\"https:\\u002F\\u002Fpic2.zhimg.com\\u002Fv2-69a40fddfacfecb8151bd9e6f60054e9\_b.gif\\" data-size=\\"normal\\" data-rawwidth=\\"1438\\" data-rawheight=\\"763\\" data-thumbnail=\\"https:\\u002F\\u002Fpic2.zhimg.com\\u002Fv2-69a40fddfacfecb8151bd9e6f60054e9\_b.jpg\\" class=\\"origin\_image zh-lightbox-thumb\\" width=\\"1438\\" data-original=\\"https:\\u002F\\u002Fpic2.zhimg.com\\u002Fv2-69a40fddfacfecb8151bd9e6f60054e9\_r.jpg\\"\\u003E\\u003C\\u002Fnoscript\\u003E\\u003Cimg src=\\"data:image\\u002Fsvg+xml;utf8,&lt;svg%20xmlns='http:\\u002F\\u002Fwww.w3.org\\u002F2000\\u002Fsvg'%20width='1438'%20height='763'&gt;&lt;\\u002Fsvg&gt;\\" data-size=\\"normal\\" data-rawwidth=\\"1438\\" data-rawheight=\\"763\\" data-thumbnail=\\"https:\\u002F\\u002Fpic2.zhimg.com\\u002Fv2-69a40fddfacfecb8151bd9e6f60054e9\_b.jpg\\" class=\\"origin\_image zh-lightbox-thumb lazy\\" width=\\"1438\\" data-original=\\"https:\\u002F\\u002Fpic2.zhimg.com\\u002Fv2-69a40fddfacfecb8151bd9e6f60054e9\_r.jpg\\" data-actualsrc=\\"https:\\u002F\\u002Fpic2.zhimg.com\\u002Fv2-69a40fddfacfecb8151bd9e6f60054e9\_b.gif\\"\\u003E\\u003Cfigcaption\\u003E加载网络代码\\u003C\\u002Ffigcaption\\u003E\\u003C\\u002Ffigure\\u003E\\u003Cp\\u003E\\u003Cbr\\u003E\\u003C\\u002Fp\\u003E\\u003Cp\\u003E\\u003Cbr\\u003E\\u003C\\u002Fp\\u003E\\u003Ch2\\u003E\\u003Cb\\u003E5. 加载本地Python文件\\u003C\\u002Fb\\u003E\\u003C\\u002Fh2\\u003E\\u003Ch2\\u003E\\u003Cb\\u003E① 使用场景\\u003C\\u002Fb\\u003E\\u003C\\u002Fh2\\u003E\\u003Cp\\u003E想在Jupyter Notebook中加载本地的Python文件并执行文件代码。\\u003C\\u002Fp\\u003E\\u003Ch2\\u003E\\u003Cb\\u003E② 方法\\u003C\\u002Fb\\u003E\\u003C\\u002Fh2\\u003E\\u003Cp\\u003E执行以下命令：\\u003C\\u002Fp\\u003E\\u003Cdiv class=\\"highlight\\"\\u003E\\u003Cpre\\u003E\\u003Ccode class=\\"language-text\\"\\u003E\\u003Cspan\\u003E\\u003C\\u002Fspan\\u003E%load Python文件的绝对路径\\n\\u003C\\u002Fcode\\u003E\\u003C\\u002Fpre\\u003E\\u003C\\u002Fdiv\\u003E\\u003Ch2\\u003E\\u003Cb\\u003E③ 注意\\u003C\\u002Fb\\u003E\\u003C\\u002Fh2\\u003E\\u003Col\\u003E\\u003Cli\\u003EPython文件的后缀为“.py”。\\u003C\\u002Fli\\u003E\\u003Cli\\u003E“%load”后跟的是Python文件的\\u003Cb\\u003E绝对路径\\u003C\\u002Fb\\u003E。\\u003C\\u002Fli\\u003E\\u003Cli\\u003E输入命令后，可以按\\u003Ccode\\u003ECTRL 回车\\u003C\\u002Fcode\\u003E来执行命令。第一次执行，是将本地的Python文件内容加载到单元格内。此时，Jupyter Notebook会自动将“%load”命令注释掉（即在前边加井号“#”），以便在执行已加载的文件代码时不重复执行该命令；第二次执行，则是执行已加载文件的代码。\\u003C\\u002Fli\\u003E\\u003C\\u002Fol\\u003E\\u003Ch2\\u003E\\u003Cb\\u003E④ 例\\u003C\\u002Fb\\u003E\\u003C\\u002Fh2\\u003E\\u003Cfigure\\u003E\\u003Cnoscript\\u003E\\u003Cimg src=\\"https:\\u002F\\u002Fpic3.zhimg.com\\u002Fv2-99c16d96c8ffbf0e507ec909fadf416a\_b.gif\\" data-size=\\"normal\\" data-rawwidth=\\"1438\\" data-rawheight=\\"692\\" data-thumbnail=\\"https:\\u002F\\u002Fpic3.zhimg.com\\u002Fv2-99c16d96c8ffbf0e507ec909fadf416a\_b.jpg\\" class=\\"origin\_image zh-lightbox-thumb\\" width=\\"1438\\" data-original=\\"https:\\u002F\\u002Fpic3.zhimg.com\\u002Fv2-99c16d96c8ffbf0e507ec909fadf416a\_r.jpg\\"\\u003E\\u003C\\u002Fnoscript\\u003E\\u003Cimg src=\\"data:image\\u002Fsvg+xml;utf8,&lt;svg%20xmlns='http:\\u002F\\u002Fwww.w3.org\\u002F2000\\u002Fsvg'%20width='1438'%20height='692'&gt;&lt;\\u002Fsvg&gt;\\" data-size=\\"normal\\" data-rawwidth=\\"1438\\" data-rawheight=\\"692\\" data-thumbnail=\\"https:\\u002F\\u002Fpic3.zhimg.com\\u002Fv2-99c16d96c8ffbf0e507ec909fadf416a\_b.jpg\\" class=\\"origin\_image zh-lightbox-thumb lazy\\" width=\\"1438\\" data-original=\\"https:\\u002F\\u002Fpic3.zhimg.com\\u002Fv2-99c16d96c8ffbf0e507ec909fadf416a\_r.jpg\\" data-actualsrc=\\"https:\\u002F\\u002Fpic3.zhimg.com\\u002Fv2-99c16d96c8ffbf0e507ec909fadf416a\_b.gif\\"\\u003E\\u003Cfigcaption\\u003E加载本地Python文件\\u003C\\u002Ffigcaption\\u003E\\u003C\\u002Ffigure\\u003E\\u003Cp\\u003E\\u003Cbr\\u003E\\u003C\\u002Fp\\u003E\\u003Cp\\u003E\\u003Cbr\\u003E\\u003C\\u002Fp\\u003E\\u003Ch2\\u003E\\u003Cb\\u003E6. 直接运行本地Python文件\\u003C\\u002Fb\\u003E\\u003C\\u002Fh2\\u003E\\u003Ch2\\u003E\\u003Cb\\u003E① 使用场景\\u003C\\u002Fb\\u003E\\u003C\\u002Fh2\\u003E\\u003Cp\\u003E不想在Jupyter Notebook的单元格中加载本地Python文件，想要直接运行。\\u003C\\u002Fp\\u003E\\u003Ch2\\u003E\\u003Cb\\u003E② 方法\\u003C\\u002Fb\\u003E\\u003C\\u002Fh2\\u003E\\u003Cp\\u003E执行命令：\\u003C\\u002Fp\\u003E\\u003Cdiv class=\\"highlight\\"\\u003E\\u003Cpre\\u003E\\u003Ccode class=\\"language-text\\"\\u003E\\u003Cspan\\u003E\\u003C\\u002Fspan\\u003E%run Python文件的绝对路径\\n\\u003C\\u002Fcode\\u003E\\u003C\\u002Fpre\\u003E\\u003C\\u002Fdiv\\u003E\\u003Cp\\u003E或\\u003C\\u002Fp\\u003E\\u003Cdiv class=\\"highlight\\"\\u003E\\u003Cpre\\u003E\\u003Ccode class=\\"language-text\\"\\u003E\\u003Cspan\\u003E\\u003C\\u002Fspan\\u003E!python3 Python文件的绝对路径\\n\\u003C\\u002Fcode\\u003E\\u003C\\u002Fpre\\u003E\\u003C\\u002Fdiv\\u003E\\u003Cp\\u003E或\\u003C\\u002Fp\\u003E\\u003Cdiv class=\\"highlight\\"\\u003E\\u003Cpre\\u003E\\u003Ccode class=\\"language-text\\"\\u003E\\u003Cspan\\u003E\\u003C\\u002Fspan\\u003E!python Python文件的绝对路径\\n\\u003C\\u002Fcode\\u003E\\u003C\\u002Fpre\\u003E\\u003C\\u002Fdiv\\u003E\\u003Ch2\\u003E\\u003Cb\\u003E③ 注意\\u003C\\u002Fb\\u003E\\u003C\\u002Fh2\\u003E\\u003Col\\u003E\\u003Cli\\u003EPython文件的后缀为“.py”。\\u003C\\u002Fli\\u003E\\u003Cli\\u003E“%run”后跟的是Python文件的\\u003Cb\\u003E绝对路径\\u003C\\u002Fb\\u003E。\\u003C\\u002Fli\\u003E\\u003Cli\\u003E“!python3”用于执行Python\\u003Cbr\\u003E 3.x版本的代码。\\u003C\\u002Fli\\u003E\\u003Cli\\u003E“!python”用于执行Python\\u003Cbr\\u003E 2.x版本的代码。\\u003C\\u002Fli\\u003E\\u003Cli\\u003E“!python3”和“!python”属于 \\u003Ccode\\u003E!shell命令\\u003C\\u002Fcode\\u003E 语法的使用，即在Jupyter Notebook中执行shell命令的语法。\\u003C\\u002Fli\\u003E\\u003Cli\\u003E输入命令后，可以按 \\u003Ccode\\u003Econtrol return\\u003C\\u002Fcode\\u003E 来执行命令，执行过程中将不显示本地Python文件的内容，直接显示运行结果。\\u003C\\u002Fli\\u003E\\u003C\\u002Fol\\u003E\\u003Ch2\\u003E\\u003Cb\\u003E④ 例\\u003C\\u002Fb\\u003E\\u003C\\u002Fh2\\u003E\\u003Cfigure\\u003E\\u003Cnoscript\\u003E\\u003Cimg src=\\"https:\\u002F\\u002Fpic2.zhimg.com\\u002Fv2-353ba4eddf9b935380844200ea398c11\_b.gif\\" data-size=\\"normal\\" data-rawwidth=\\"1438\\" data-rawheight=\\"506\\" data-thumbnail=\\"https:\\u002F\\u002Fpic2.zhimg.com\\u002Fv2-353ba4eddf9b935380844200ea398c11\_b.jpg\\" class=\\"origin\_image zh-lightbox-thumb\\" width=\\"1438\\" data-original=\\"https:\\u002F\\u002Fpic2.zhimg.com\\u002Fv2-353ba4eddf9b935380844200ea398c11\_r.jpg\\"\\u003E\\u003C\\u002Fnoscript\\u003E\\u003Cimg src=\\"data:image\\u002Fsvg+xml;utf8,&lt;svg%20xmlns='http:\\u002F\\u002Fwww.w3.org\\u002F2000\\u002Fsvg'%20width='1438'%20height='506'&gt;&lt;\\u002Fsvg&gt;\\" data-size=\\"normal\\" data-rawwidth=\\"1438\\" data-rawheight=\\"506\\" data-thumbnail=\\"https:\\u002F\\u002Fpic2.zhimg.com\\u002Fv2-353ba4eddf9b935380844200ea398c11\_b.jpg\\" class=\\"origin\_image zh-lightbox-thumb lazy\\" width=\\"1438\\" data-original=\\"https:\\u002F\\u002Fpic2.zhimg.com\\u002Fv2-353ba4eddf9b935380844200ea398c11\_r.jpg\\" data-actualsrc=\\"https:\\u002F\\u002Fpic2.zhimg.com\\u002Fv2-353ba4eddf9b935380844200ea398c11\_b.gif\\"\\u003E\\u003Cfigcaption\\u003E运行本地Python文件\\u003C\\u002Ffigcaption\\u003E\\u003C\\u002Ffigure\\u003E\\u003Cp\\u003E\\u003Cbr\\u003E\\u003C\\u002Fp\\u003E\\u003Cp\\u003E\\u003Cbr\\u003E\\u003C\\u002Fp\\u003E\\u003Ch2\\u003E\\u003Cb\\u003E7. 在Jupyter Notebook中获取当前位置\\u003C\\u002Fb\\u003E\\u003C\\u002Fh2\\u003E\\u003Ch2\\u003E\\u003Cb\\u003E① 使用场景\\u003C\\u002Fb\\u003E\\u003C\\u002Fh2\\u003E\\u003Cp\\u003E想要在Jupyter Notebook中获取当前所在位置的\\u003Cb\\u003E绝对路径。\\u003C\\u002Fb\\u003E\\u003C\\u002Fp\\u003E\\u003Ch2\\u003E\\u003Cb\\u003E② 方法\\u003C\\u002Fb\\u003E\\u003C\\u002Fh2\\u003E\\u003Cdiv class=\\"highlight\\"\\u003E\\u003Cpre\\u003E\\u003Ccode class=\\"language-text\\"\\u003E\\u003Cspan\\u003E\\u003C\\u002Fspan\\u003E%pwd\\n\\u003C\\u002Fcode\\u003E\\u003C\\u002Fpre\\u003E\\u003C\\u002Fdiv\\u003E\\u003Cp\\u003E或\\u003C\\u002Fp\\u003E\\u003Cdiv class=\\"highlight\\"\\u003E\\u003Cpre\\u003E\\u003Ccode class=\\"language-text\\"\\u003E\\u003Cspan\\u003E\\u003C\\u002Fspan\\u003E!pwd\\n\\u003C\\u002Fcode\\u003E\\u003C\\u002Fpre\\u003E\\u003C\\u002Fdiv\\u003E\\u003Ch2\\u003E\\u003Cb\\u003E③ 注意\\u003C\\u002Fb\\u003E\\u003C\\u002Fh2\\u003E\\u003Col\\u003E\\u003Cli\\u003E获取的位置是当前Jupyter Notebook中创建的笔记本所在位置，且该位置为\\u003Cb\\u003E绝对路径\\u003C\\u002Fb\\u003E。\\u003C\\u002Fli\\u003E\\u003Cli\\u003E“!pwd”属于 \\u003Ccode\\u003E!shell命令\\u003C\\u002Fcode\\u003E 语法的使用，即在Jupyter\\u003Cbr\\u003E Notebook中执行shell命令的语法。\\u003C\\u002Fli\\u003E\\u003C\\u002Fol\\u003E\\u003Ch2\\u003E\\u003Cb\\u003E④ 例\\u003C\\u002Fb\\u003E\\u003C\\u002Fh2\\u003E\\u003Cfigure\\u003E\\u003Cnoscript\\u003E\\u003Cimg src=\\"https:\\u002F\\u002Fpic2.zhimg.com\\u002Fv2-ca13bbc098e544d0fd53c4d5835f6cfd\_b.gif\\" data-size=\\"normal\\" data-rawwidth=\\"1433\\" data-rawheight=\\"386\\" data-thumbnail=\\"https:\\u002F\\u002Fpic2.zhimg.com\\u002Fv2-ca13bbc098e544d0fd53c4d5835f6cfd\_b.jpg\\" class=\\"origin\_image zh-lightbox-thumb\\" width=\\"1433\\" data-original=\\"https:\\u002F\\u002Fpic2.zhimg.com\\u002Fv2-ca13bbc098e544d0fd53c4d5835f6cfd\_r.jpg\\"\\u003E\\u003C\\u002Fnoscript\\u003E\\u003Cimg src=\\"data:image\\u002Fsvg+xml;utf8,&lt;svg%20xmlns='http:\\u002F\\u002Fwww.w3.org\\u002F2000\\u002Fsvg'%20width='1433'%20height='386'&gt;&lt;\\u002Fsvg&gt;\\" data-size=\\"normal\\" data-rawwidth=\\"1433\\" data-rawheight=\\"386\\" data-thumbnail=\\"https:\\u002F\\u002Fpic2.zhimg.com\\u002Fv2-ca13bbc098e544d0fd53c4d5835f6cfd\_b.jpg\\" class=\\"origin\_image zh-lightbox-thumb lazy\\" width=\\"1433\\" data-original=\\"https:\\u002F\\u002Fpic2.zhimg.com\\u002Fv2-ca13bbc098e544d0fd53c4d5835f6cfd\_r.jpg\\" data-actualsrc=\\"https:\\u002F\\u002Fpic2.zhimg.com\\u002Fv2-ca13bbc098e544d0fd53c4d5835f6cfd\_b.gif\\"\\u003E\\u003Cfigcaption\\u003E获取当前位置的绝对路径\\u003C\\u002Ffigcaption\\u003E\\u003C\\u002Ffigure\\u003E\\u003Cp\\u003E\\u003Cbr\\u003E\\u003C\\u002Fp\\u003E\\u003Cp\\u003E\\u003Cbr\\u003E\\u003C\\u002Fp\\u003E\\u003Ch2\\u003E\\u003Cb\\u003E8. 在Jupyter Notebook使用shell命令\\u003C\\u002Fb\\u003E\\u003C\\u002Fh2\\u003E\\u003Ch2\\u003E\\u003Cb\\u003E① 方法一——在笔记本的单元格中\\u003C\\u002Fb\\u003E\\u003C\\u002Fh2\\u003E\\u003Ch2\\u003E\\u003Cb\\u003E⑴ 语法\\u003C\\u002Fb\\u003E\\u003C\\u002Fh2\\u003E\\u003Cdiv class=\\"highlight\\"\\u003E\\u003Cpre\\u003E\\u003Ccode class=\\"language-text\\"\\u003E\\u003Cspan\\u003E\\u003C\\u002Fspan\\u003E!shell命令\\n\\u003C\\u002Fcode\\u003E\\u003C\\u002Fpre\\u003E\\u003C\\u002Fdiv\\u003E\\u003Cp\\u003E\\u003Cbr\\u003E\\u003C\\u002Fp\\u003E\\u003Cul\\u003E\\u003Cli\\u003E在Jupyter Notebook中的笔记本单元格中用英文感叹号“!”后接shell命令即可执行shell命令。\\u003C\\u002Fli\\u003E\\u003C\\u002Ful\\u003E\\u003Ch2\\u003E\\u003Cb\\u003E⑵ 例\\u003C\\u002Fb\\u003E\\u003C\\u002Fh2\\u003E\\u003Cfigure\\u003E\\u003Cnoscript\\u003E\\u003Cimg src=\\"https:\\u002F\\u002Fpic1.zhimg.com\\u002Fv2-8b8ec14f44d588674e37ffa57f117674\_b.gif\\" data-size=\\"normal\\" data-rawwidth=\\"1438\\" data-rawheight=\\"524\\" data-thumbnail=\\"https:\\u002F\\u002Fpic1.zhimg.com\\u002Fv2-8b8ec14f44d588674e37ffa57f117674\_b.jpg\\" class=\\"origin\_image zh-lightbox-thumb\\" width=\\"1438\\" data-original=\\"https:\\u002F\\u002Fpic1.zhimg.com\\u002Fv2-8b8ec14f44d588674e37ffa57f117674\_r.jpg\\"\\u003E\\u003C\\u002Fnoscript\\u003E\\u003Cimg src=\\"data:image\\u002Fsvg+xml;utf8,&lt;svg%20xmlns='http:\\u002F\\u002Fwww.w3.org\\u002F2000\\u002Fsvg'%20width='1438'%20height='524'&gt;&lt;\\u002Fsvg&gt;\\" data-size=\\"normal\\" data-rawwidth=\\"1438\\" data-rawheight=\\"524\\" data-thumbnail=\\"https:\\u002F\\u002Fpic1.zhimg.com\\u002Fv2-8b8ec14f44d588674e37ffa57f117674\_b.jpg\\" class=\\"origin\_image zh-lightbox-thumb lazy\\" width=\\"1438\\" data-original=\\"https:\\u002F\\u002Fpic1.zhimg.com\\u002Fv2-8b8ec14f44d588674e37ffa57f117674\_r.jpg\\" data-actualsrc=\\"https:\\u002F\\u002Fpic1.zhimg.com\\u002Fv2-8b8ec14f44d588674e37ffa57f117674\_b.gif\\"\\u003E\\u003Cfigcaption\\u003EShell命令的使用\\u003C\\u002Ffigcaption\\u003E\\u003C\\u002Ffigure\\u003E\\u003Cp\\u003E\\u003Cbr\\u003E\\u003C\\u002Fp\\u003E\\u003Cp\\u003E\\u003Cbr\\u003E\\u003C\\u002Fp\\u003E\\u003Ch2\\u003E\\u003Cb\\u003E② 方法二——在Jupyter Notebook中新建终端\\u003C\\u002Fb\\u003E\\u003C\\u002Fh2\\u003E\\u003Ch2\\u003E\\u003Cb\\u003E⑴ 启动方法\\u003C\\u002Fb\\u003E\\u003C\\u002Fh2\\u003E\\u003Cp\\u003E在Jupyter Notebook主界面，即“File”界面中点击“New”；在“New”下拉框中点击“Terminal”即新建了终端。此时终端位置是在你的家目录，可以通过\\u003Ccode\\u003Epwd\\u003C\\u002Fcode\\u003E命令查询当前所在位置的绝对路径。\\u003C\\u002Fp\\u003E\\u003Ch2\\u003E\\u003Cb\\u003E⑵ 关闭方法\\u003C\\u002Fb\\u003E\\u003C\\u002Fh2\\u003E\\u003Cp\\u003E在Jupyter Notebook的“Running”界面中的“Terminals”类目中可以看到正在运行的终端，点击后边的“Shutdown”即可关闭终端。\\u003C\\u002Fp\\u003E\\u003Ch2\\u003E\\u003Cb\\u003E⑶ 例\\u003C\\u002Fb\\u003E\\u003C\\u002Fh2\\u003E\\u003Cfigure\\u003E\\u003Cnoscript\\u003E\\u003Cimg src=\\"https:\\u002F\\u002Fpic2.zhimg.com\\u002Fv2-8318df6fd86b4839d83f0d94004f9191\_b.gif\\" data-size=\\"normal\\" data-rawwidth=\\"1437\\" data-rawheight=\\"699\\" data-thumbnail=\\"https:\\u002F\\u002Fpic2.zhimg.com\\u002Fv2-8318df6fd86b4839d83f0d94004f9191\_b.jpg\\" class=\\"origin\_image zh-lightbox-thumb\\" width=\\"1437\\" data-original=\\"https:\\u002F\\u002Fpic2.zhimg.com\\u002Fv2-8318df6fd86b4839d83f0d94004f9191\_r.jpg\\"\\u003E\\u003C\\u002Fnoscript\\u003E\\u003Cimg src=\\"data:image\\u002Fsvg+xml;utf8,&lt;svg%20xmlns='http:\\u002F\\u002Fwww.w3.org\\u002F2000\\u002Fsvg'%20width='1437'%20height='699'&gt;&lt;\\u002Fsvg&gt;\\" data-size=\\"normal\\" data-rawwidth=\\"1437\\" data-rawheight=\\"699\\" data-thumbnail=\\"https:\\u002F\\u002Fpic2.zhimg.com\\u002Fv2-8318df6fd86b4839d83f0d94004f9191\_b.jpg\\" class=\\"origin\_image zh-lightbox-thumb lazy\\" width=\\"1437\\" data-original=\\"https:\\u002F\\u002Fpic2.zhimg.com\\u002Fv2-8318df6fd86b4839d83f0d94004f9191\_r.jpg\\" data-actualsrc=\\"https:\\u002F\\u002Fpic2.zhimg.com\\u002Fv2-8318df6fd86b4839d83f0d94004f9191\_b.gif\\"\\u003E\\u003Cfigcaption\\u003E笔记本中的终端使用\\u003C\\u002Ffigcaption\\u003E\\u003C\\u002Ffigure\\u003E\\u003Cp\\u003E\\u003Cbr\\u003E\\u003C\\u002Fp\\u003E\\u003Cp\\u003E\\u003Cbr\\u003E\\u003C\\u002Fp\\u003E\\u003Ch2\\u003E\\u003Cb\\u003E9. 隐藏笔记本输入单元格\\u003C\\u002Fb\\u003E\\u003C\\u002Fh2\\u003E\\u003Ch2\\u003E\\u003Cb\\u003E① 使用场景\\u003C\\u002Fb\\u003E\\u003C\\u002Fh2\\u003E\\u003Cp\\u003E在Jupyter Notebook的笔记本中无论是编写文档还是编程，都有输入（In \[\]）和输出（Out \[\]）。当我们编写的代码或文档使用的单元格较多时，有时我们只想关注输出的内容而暂时不看输入的内容，这时就需要隐藏输入单元格而只显示输出单元格。\\u003C\\u002Fp\\u003E\\u003Ch2\\u003E\\u003Cb\\u003E② 方法一\\u003C\\u002Fb\\u003E\\u003C\\u002Fh2\\u003E\\u003Ch2\\u003E\\u003Cb\\u003E⑴ 代码\\u003C\\u002Fb\\u003E\\u003C\\u002Fh2\\u003E\\u003Cdiv class=\\"highlight\\"\\u003E\\u003Cpre\\u003E\\u003Ccode class=\\"language-text\\"\\u003E\\u003Cspan\\u003E\\u003C\\u002Fspan\\u003Efrom IPython.display import display\\nfrom IPython.display import HTML\\nimport IPython.core.display as di # Example: di.display\_html('&lt;h3&gt;%s:&lt;\\u002Fh3&gt;' % str, raw=True)\\n\\n# 这行代码的作用是：当文档作为HTML格式输出时，将会默认隐藏输入单元格。\\ndi.display\_html('&lt;script&gt;jQuery(function() {if (jQuery(\\"body.notebook\_app\\").length == 0) { jQuery(\\".input\_area\\").toggle(); jQuery(\\".prompt\\").toggle();}});&lt;\\u002Fscript&gt;', raw=True)\\n\\n# 这行代码将会添加“Toggle code”按钮来切换“隐藏\\u002F显示”输入单元格。\\ndi.display\_html('''&lt;button onclick=\\"jQuery('.input\_area').toggle(); jQuery('.prompt').toggle();\\"&gt;Toggle code&lt;\\u002Fbutton&gt;''', raw=True)\\n\\u003C\\u002Fcode\\u003E\\u003C\\u002Fpre\\u003E\\u003C\\u002Fdiv\\u003E\\u003Cp\\u003E在笔记本第一个单元格中输入以上代码，然后执行，即可在该文档中使用“隐藏\\u002F显示”输入单元格功能。\\u003C\\u002Fp\\u003E\\u003Cul\\u003E\\u003Cli\\u003E缺陷：此方法不能很好的适用于Markdown单元格。\\u003C\\u002Fli\\u003E\\u003C\\u002Ful\\u003E\\u003Ch2\\u003E⑵ 例\\u003C\\u002Fh2\\u003E\\u003Cfigure\\u003E\\u003Cnoscript\\u003E\\u003Cimg src=\\"https:\\u002F\\u002Fpic2.zhimg.com\\u002Fv2-b8847adffd4ebc8ec70694196578524d\_b.gif\\" data-size=\\"normal\\" data-rawwidth=\\"1438\\" data-rawheight=\\"701\\" data-thumbnail=\\"https:\\u002F\\u002Fpic2.zhimg.com\\u002Fv2-b8847adffd4ebc8ec70694196578524d\_b.jpg\\" class=\\"origin\_image zh-lightbox-thumb\\" width=\\"1438\\" data-original=\\"https:\\u002F\\u002Fpic2.zhimg.com\\u002Fv2-b8847adffd4ebc8ec70694196578524d\_r.jpg\\"\\u003E\\u003C\\u002Fnoscript\\u003E\\u003Cimg src=\\"data:image\\u002Fsvg+xml;utf8,&lt;svg%20xmlns='http:\\u002F\\u002Fwww.w3.org\\u002F2000\\u002Fsvg'%20width='1438'%20height='701'&gt;&lt;\\u002Fsvg&gt;\\" data-size=\\"normal\\" data-rawwidth=\\"1438\\" data-rawheight=\\"701\\" data-thumbnail=\\"https:\\u002F\\u002Fpic2.zhimg.com\\u002Fv2-b8847adffd4ebc8ec70694196578524d\_b.jpg\\" class=\\"origin\_image zh-lightbox-thumb lazy\\" width=\\"1438\\" data-original=\\"https:\\u002F\\u002Fpic2.zhimg.com\\u002Fv2-b8847adffd4ebc8ec70694196578524d\_r.jpg\\" data-actualsrc=\\"https:\\u002F\\u002Fpic2.zhimg.com\\u002Fv2-b8847adffd4ebc8ec70694196578524d\_b.gif\\"\\u003E\\u003Cfigcaption\\u003E方法一：隐藏\\u002F显示输入单元格\\u003C\\u002Ffigcaption\\u003E\\u003C\\u002Ffigure\\u003E\\u003Cp\\u003E\\u003Cbr\\u003E\\u003C\\u002Fp\\u003E\\u003Cp\\u003E\\u003Cbr\\u003E\\u003C\\u002Fp\\u003E\\u003Ch2\\u003E\\u003Cb\\u003E③ 方法二\\u003C\\u002Fb\\u003E\\u003C\\u002Fh2\\u003E\\u003Ch2\\u003E\\u003Cb\\u003E⑴ 代码\\u003C\\u002Fb\\u003E\\u003C\\u002Fh2\\u003E\\u003Cdiv class=\\"highlight\\"\\u003E\\u003Cpre\\u003E\\u003Ccode class=\\"language-text\\"\\u003E\\u003Cspan\\u003E\\u003C\\u002Fspan\\u003Efrom IPython.display import HTML\\n\\nHTML('''&lt;script&gt;\\ncode\_show=true; \\nfunction code\_toggle() {\\nif (code\_show){\\n$('div.input').hide();\\n} else {\\n$('div.input').show();\\n}\\ncode\_show = !code\_show\\n} \\n$( document ).ready(code\_toggle);\\n&lt;\\u002Fscript&gt;\\n&lt;form action=\\"javascript:code\_toggle()\\"&gt;&lt;input type=\\"submit\\" value=\\"Click here to toggle on\\u002Foff the raw code.\\"&gt;&lt;\\u002Fform&gt;''')\\n\\u003C\\u002Fcode\\u003E\\u003C\\u002Fpre\\u003E\\u003C\\u002Fdiv\\u003E\\u003Cp\\u003E在笔记本第一个单元格中输入以上代码，然后执行，即可在该文档中使用“隐藏\\u002F显示”输入单元格功能。\\u003C\\u002Fp\\u003E\\u003Cul\\u003E\\u003Cli\\u003E缺陷：此方法不能很好的适用于Markdown单元格。\\u003C\\u002Fli\\u003E\\u003C\\u002Ful\\u003E\\u003Ch2\\u003E\\u003Cb\\u003E⑵ 例\\u003C\\u002Fb\\u003E\\u003C\\u002Fh2\\u003E\\u003Cfigure\\u003E\\u003Cnoscript\\u003E\\u003Cimg src=\\"https:\\u002F\\u002Fpic4.zhimg.com\\u002Fv2-b4df17ea52642f69ed6f80c2ceb4e3bf\_b.gif\\" data-size=\\"normal\\" data-rawwidth=\\"1438\\" data-rawheight=\\"659\\" data-thumbnail=\\"https:\\u002F\\u002Fpic4.zhimg.com\\u002Fv2-b4df17ea52642f69ed6f80c2ceb4e3bf\_b.jpg\\" class=\\"origin\_image zh-lightbox-thumb\\" width=\\"1438\\" data-original=\\"https:\\u002F\\u002Fpic4.zhimg.com\\u002Fv2-b4df17ea52642f69ed6f80c2ceb4e3bf\_r.jpg\\"\\u003E\\u003C\\u002Fnoscript\\u003E\\u003Cimg src=\\"data:image\\u002Fsvg+xml;utf8,&lt;svg%20xmlns='http:\\u002F\\u002Fwww.w3.org\\u002F2000\\u002Fsvg'%20width='1438'%20height='659'&gt;&lt;\\u002Fsvg&gt;\\" data-size=\\"normal\\" data-rawwidth=\\"1438\\" data-rawheight=\\"659\\" data-thumbnail=\\"https:\\u002F\\u002Fpic4.zhimg.com\\u002Fv2-b4df17ea52642f69ed6f80c2ceb4e3bf\_b.jpg\\" class=\\"origin\_image zh-lightbox-thumb lazy\\" width=\\"1438\\" data-original=\\"https:\\u002F\\u002Fpic4.zhimg.com\\u002Fv2-b4df17ea52642f69ed6f80c2ceb4e3bf\_r.jpg\\" data-actualsrc=\\"https:\\u002F\\u002Fpic4.zhimg.com\\u002Fv2-b4df17ea52642f69ed6f80c2ceb4e3bf\_b.gif\\"\\u003E\\u003Cfigcaption\\u003E方法二：隐藏\\u002F显示输入单元格\\u003C\\u002Ffigcaption\\u003E\\u003C\\u002Ffigure\\u003E\\u003Cp\\u003E\\u003Cbr\\u003E\\u003C\\u002Fp\\u003E\\u003Cp\\u003E\\u003Cbr\\u003E\\u003C\\u002Fp\\u003E\\u003Ch2\\u003E\\u003Cb\\u003E10. 魔术命令\\u003C\\u002Fb\\u003E\\u003C\\u002Fh2\\u003E\\u003Cp\\u003E由于目前暂时用不到过多的魔术命令，因此暂时先参考\\u003Ca href=\\"http:\\u002F\\u002Flink.zhihu.com\\u002F?target=http%3A\\u002F\\u002Fipython.readthedocs.io\\u002Fen\\u002Fstable\\u002Finteractive\\u002Fmagics.html\\" class=\\" wrap external\\" target=\\"\_blank\\" rel=\\"nofollow noreferrer\\"\\u003E官网的文档\\u003C\\u002Fa\\u003E。\\u003C\\u002Fp\\u003E\\u003Ch2\\u003E\\u003Cb\\u003E六、增加内核——“ipykernel” ☆\\u003C\\u002Fb\\u003E\\u003C\\u002Fh2\\u003E\\u003Ch2\\u003E\\u003Cb\\u003E1. 使用场景\\u003C\\u002Fb\\u003E\\u003C\\u002Fh2\\u003E\\u003Cul\\u003E\\u003Cli\\u003E场景一：同时用不同版本的Python进行工作，在Jupyter Notebook中无法切换，即“New”的下拉菜单中无法使用需要的环境。\\u003C\\u002Fli\\u003E\\u003Cli\\u003E场景二：创建了不同的虚拟环境（或许具有相同的Python版本但安装的包不同），在Jupyter Notebook中无法切换，即“New”的下拉菜单中无法使用需要的环境。\\u003C\\u002Fli\\u003E\\u003C\\u002Ful\\u003E\\u003Cp\\u003E接下来将分别用“命令行模式”和“图形界面模式”来解决以上两个场景的问题。顾名思义，“命令行模式”即在终端中通过执行命令来一步步解决问题；“图形界面模式”则是通过在Jupyter Notebook的网页中通过鼠标点击的方式解决上述问题。\\u003C\\u002Fp\\u003E\\u003Cp\\u003E其中，“图形界面模式”的解决方法相对比较简单快捷，如果对于急于解决问题，不需要知道运行原理的朋友，可以直接进入“3. 解决方法之图形界面模式”来阅读。\\u003C\\u002Fp\\u003E\\u003Cp\\u003E“命令行模式”看似比较复杂，且又划分了使用场景，但通过这种方式来解决问题可以更好的了解其中的工作原理，比如，每进行一步操作对应的命令是什么，而命令的执行是为了达到什么样的目的，这些可能都被封装在图形界面上的一个点击动作来完成了。对于想更深入了解其运作过程的朋友，可以接着向下阅读。\\u003C\\u002Fp\\u003E\\u003Ch2\\u003E\\u003Cb\\u003E2. 解决方法之命令行模式\\u003C\\u002Fb\\u003E\\u003C\\u002Fh2\\u003E\\u003Ch2\\u003E\\u003Cb\\u003E① 同时使用不同版本的Python\\u003C\\u002Fb\\u003E\\u003C\\u002Fh2\\u003E\\u003Ch2\\u003E\\u003Cb\\u003E⑴ 在Python 3中创建Python 2内核\\u003C\\u002Fb\\u003E\\u003C\\u002Fh2\\u003E\\u003Ch2\\u003E\\u003Cb\\u003E⒜ pip安装\\u003C\\u002Fb\\u003E\\u003C\\u002Fh2\\u003E\\u003Cul\\u003E\\u003Cli\\u003E首先安装Python 2的ipykernel包。\\u003C\\u002Fli\\u003E\\u003C\\u002Ful\\u003E\\u003Cdiv class=\\"highlight\\"\\u003E\\u003Cpre\\u003E\\u003Ccode class=\\"language-text\\"\\u003E\\u003Cspan\\u003E\\u003C\\u002Fspan\\u003Epython2 -m pip install ipykernel\\n\\u003C\\u002Fcode\\u003E\\u003C\\u002Fpre\\u003E\\u003C\\u002Fdiv\\u003E\\u003Cul\\u003E\\u003Cli\\u003E再为\\u003Cb\\u003E当前用户\\u003C\\u002Fb\\u003E安装Python 2的内核（ipykernel）。\\u003C\\u002Fli\\u003E\\u003C\\u002Ful\\u003E\\u003Cdiv class=\\"highlight\\"\\u003E\\u003Cpre\\u003E\\u003Ccode class=\\"language-text\\"\\u003E\\u003Cspan\\u003E\\u003C\\u002Fspan\\u003Epython2 -m ipykernel install --user\\n\\u003C\\u002Fcode\\u003E\\u003C\\u002Fpre\\u003E\\u003C\\u002Fdiv\\u003E\\u003Cul\\u003E\\u003Cli\\u003E注意：“--user”参数的意思是针对当前用户安装，而非系统范围内安装。\\u003C\\u002Fli\\u003E\\u003C\\u002Ful\\u003E\\u003Ch2\\u003E\\u003Cb\\u003E⒝ conda安装\\u003C\\u002Fb\\u003E\\u003C\\u002Fh2\\u003E\\u003Cul\\u003E\\u003Cli\\u003E首先创建Python版本为2.x且具有ipykernel的新环境，其中“&lt;env\_name&gt;”为自定义环境名，环境名两边不加尖括号“&lt;&gt;”。\\u003C\\u002Fli\\u003E\\u003C\\u002Ful\\u003E\\u003Cdiv class=\\"highlight\\"\\u003E\\u003Cpre\\u003E\\u003Ccode class=\\"language-text\\"\\u003E\\u003Cspan\\u003E\\u003C\\u002Fspan\\u003Econda create -n &lt;env\_name&gt; python=2 ipykernel\\n\\u003C\\u002Fcode\\u003E\\u003C\\u002Fpre\\u003E\\u003C\\u002Fdiv\\u003E\\u003Cul\\u003E\\u003Cli\\u003E然后切换至新创建的环境。\\u003C\\u002Fli\\u003E\\u003C\\u002Ful\\u003E\\u003Cdiv class=\\"highlight\\"\\u003E\\u003Cpre\\u003E\\u003Ccode class=\\"language-text\\"\\u003E\\u003Cspan\\u003E\\u003C\\u002Fspan\\u003EWindows: activate &lt;env\_name&gt;\\nLinux\\u002FmacOS: source activate &lt;env\_name&gt;\\n\\u003C\\u002Fcode\\u003E\\u003C\\u002Fpre\\u003E\\u003C\\u002Fdiv\\u003E\\u003Cul\\u003E\\u003Cli\\u003E为\\u003Cb\\u003E当前用户\\u003C\\u002Fb\\u003E安装Python 2的内核（ipykernel）。\\u003C\\u002Fli\\u003E\\u003C\\u002Ful\\u003E\\u003Cdiv class=\\"highlight\\"\\u003E\\u003Cpre\\u003E\\u003Ccode class=\\"language-text\\"\\u003E\\u003Cspan\\u003E\\u003C\\u002Fspan\\u003Epython2 -m ipykernel install --user\\n\\u003C\\u002Fcode\\u003E\\u003C\\u002Fpre\\u003E\\u003C\\u002Fdiv\\u003E\\u003Cul\\u003E\\u003Cli\\u003E注意：“--user”参数的意思是针对当前用户安装，而非系统范围内安装。\\u003C\\u002Fli\\u003E\\u003C\\u002Ful\\u003E\\u003Ch2\\u003E\\u003Cb\\u003E⑵ 在Python 2中创建Python 3内核\\u003C\\u002Fb\\u003E\\u003C\\u002Fh2\\u003E\\u003Ch2\\u003E\\u003Cb\\u003E⒜ pip安装\\u003C\\u002Fb\\u003E\\u003C\\u002Fh2\\u003E\\u003Cul\\u003E\\u003Cli\\u003E首先安装Python 3的ipykernel包。\\u003C\\u002Fli\\u003E\\u003C\\u002Ful\\u003E\\u003Cdiv class=\\"highlight\\"\\u003E\\u003Cpre\\u003E\\u003Ccode class=\\"language-text\\"\\u003E\\u003Cspan\\u003E\\u003C\\u002Fspan\\u003Epython3 -m pip install ipykernel\\n\\u003C\\u002Fcode\\u003E\\u003C\\u002Fpre\\u003E\\u003C\\u002Fdiv\\u003E\\u003Cul\\u003E\\u003Cli\\u003E再为\\u003Cb\\u003E当前用户\\u003C\\u002Fb\\u003E安装Python 2的内核（ipykernel）。\\u003C\\u002Fli\\u003E\\u003C\\u002Ful\\u003E\\u003Cdiv class=\\"highlight\\"\\u003E\\u003Cpre\\u003E\\u003Ccode class=\\"language-text\\"\\u003E\\u003Cspan\\u003E\\u003C\\u002Fspan\\u003Epython3 -m ipykernel install --user\\n\\u003C\\u002Fcode\\u003E\\u003C\\u002Fpre\\u003E\\u003C\\u002Fdiv\\u003E\\u003Cul\\u003E\\u003Cli\\u003E注意：“--user”参数的意思是针对当前用户安装，而非系统范围内安装。\\u003C\\u002Fli\\u003E\\u003C\\u002Ful\\u003E\\u003Ch2\\u003E\\u003Cb\\u003E⒝ conda安装\\u003C\\u002Fb\\u003E\\u003C\\u002Fh2\\u003E\\u003Cul\\u003E\\u003Cli\\u003E首先创建Python版本为3.x且具有ipykernel的新环境，其中“&lt;env\_name&gt;”为自定义环境名，环境名两边不加尖括号“&lt;&gt;”。\\u003C\\u002Fli\\u003E\\u003C\\u002Ful\\u003E\\u003Cdiv class=\\"highlight\\"\\u003E\\u003Cpre\\u003E\\u003Ccode class=\\"language-text\\"\\u003E\\u003Cspan\\u003E\\u003C\\u002Fspan\\u003Econda create -n &lt;env\_name&gt; python=3 ipykernel\\n\\u003C\\u002Fcode\\u003E\\u003C\\u002Fpre\\u003E\\u003C\\u002Fdiv\\u003E\\u003Cul\\u003E\\u003Cli\\u003E然后切换至新创建的环境。\\u003C\\u002Fli\\u003E\\u003C\\u002Ful\\u003E\\u003Cdiv class=\\"highlight\\"\\u003E\\u003Cpre\\u003E\\u003Ccode class=\\"language-text\\"\\u003E\\u003Cspan\\u003E\\u003C\\u002Fspan\\u003EWindows: activate &lt;env\_name&gt;\\nLinux\\u002FmacOS: source activate &lt;env\_name&gt;\\n\\u003C\\u002Fcode\\u003E\\u003C\\u002Fpre\\u003E\\u003C\\u002Fdiv\\u003E\\u003Cul\\u003E\\u003Cli\\u003E为\\u003Cb\\u003E当前用户\\u003C\\u002Fb\\u003E安装Python 3的内核（ipykernel）。\\u003C\\u002Fli\\u003E\\u003C\\u002Ful\\u003E\\u003Cdiv class=\\"highlight\\"\\u003E\\u003Cpre\\u003E\\u003Ccode class=\\"language-text\\"\\u003E\\u003Cspan\\u003E\\u003C\\u002Fspan\\u003Epython3 -m ipykernel install --user\\n\\u003C\\u002Fcode\\u003E\\u003C\\u002Fpre\\u003E\\u003C\\u002Fdiv\\u003E\\u003Cul\\u003E\\u003Cli\\u003E注意：“--user”参数的意思是针对当前用户安装，而非系统范围内安装。\\u003C\\u002Fli\\u003E\\u003C\\u002Ful\\u003E\\u003Ch2\\u003E\\u003Cb\\u003E② 为不同环境创建内核\\u003C\\u002Fb\\u003E\\u003C\\u002Fh2\\u003E\\u003Ch2\\u003E\\u003Cb\\u003E⑴ 切换至需安装内核的环境\\u003C\\u002Fb\\u003E\\u003C\\u002Fh2\\u003E\\u003Cdiv class=\\"highlight\\"\\u003E\\u003Cpre\\u003E\\u003Ccode class=\\"language-text\\"\\u003E\\u003Cspan\\u003E\\u003C\\u002Fspan\\u003EWindows: activate &lt;env\_name&gt;\\nLinux\\u002FmacOS: source activate &lt;env\_name&gt;\\n\\u003C\\u002Fcode\\u003E\\u003C\\u002Fpre\\u003E\\u003C\\u002Fdiv\\u003E\\u003Cul\\u003E\\u003Cli\\u003E注意：“&lt;env\_name&gt;”是需要安装内核的环境名称，环境名两边不加尖括号“&lt;&gt;”。\\u003C\\u002Fli\\u003E\\u003C\\u002Ful\\u003E\\u003Ch2\\u003E\\u003Cb\\u003E⑵ 检查该环境是否安装了ipykernel包\\u003C\\u002Fb\\u003E\\u003C\\u002Fh2\\u003E\\u003Cdiv class=\\"highlight\\"\\u003E\\u003Cpre\\u003E\\u003Ccode class=\\"language-text\\"\\u003E\\u003Cspan\\u003E\\u003C\\u002Fspan\\u003Econda list\\n\\u003C\\u002Fcode\\u003E\\u003C\\u002Fpre\\u003E\\u003C\\u002Fdiv\\u003E\\u003Cp\\u003E执行上述命令查看当前环境下安装的包，若没有安装ipykernel包，则执行安装命令；否则进行下一步。\\u003C\\u002Fp\\u003E\\u003Cdiv class=\\"highlight\\"\\u003E\\u003Cpre\\u003E\\u003Ccode class=\\"language-text\\"\\u003E\\u003Cspan\\u003E\\u003C\\u002Fspan\\u003Econda install ipykernel\\n\\u003C\\u002Fcode\\u003E\\u003C\\u002Fpre\\u003E\\u003C\\u002Fdiv\\u003E\\u003Ch2\\u003E\\u003Cb\\u003E⑶ 为当前环境下的当前用户安装Python内核\\u003C\\u002Fb\\u003E\\u003C\\u002Fh2\\u003E\\u003Cul\\u003E\\u003Cli\\u003E若该环境的Python版本为2.x，则执行命令：\\u003C\\u002Fli\\u003E\\u003C\\u002Ful\\u003E\\u003Cdiv class=\\"highlight\\"\\u003E\\u003Cpre\\u003E\\u003Ccode class=\\"language-text\\"\\u003E\\u003Cspan\\u003E\\u003C\\u002Fspan\\u003Epython2 -m ipykernel install --user --name &lt;env\_name&gt; --display-name \\"&lt;notebook\_name&gt;\\"\\n\\u003C\\u002Fcode\\u003E\\u003C\\u002Fpre\\u003E\\u003C\\u002Fdiv\\u003E\\u003Cul\\u003E\\u003Cli\\u003E若该环境的Python版本为3.x，则执行命令：\\u003C\\u002Fli\\u003E\\u003C\\u002Ful\\u003E\\u003Cdiv class=\\"highlight\\"\\u003E\\u003Cpre\\u003E\\u003Ccode class=\\"language-text\\"\\u003E\\u003Cspan\\u003E\\u003C\\u002Fspan\\u003Epython3 -m ipykernel install --user --name &lt;env\_name&gt; --display-name \\"&lt;notebook\_name&gt;\\"\\n\\u003C\\u002Fcode\\u003E\\u003C\\u002Fpre\\u003E\\u003C\\u002Fdiv\\u003E\\u003Cul\\u003E\\u003Cli\\u003E注意: \\u003C\\u002Fli\\u003E\\u003C\\u002Ful\\u003E\\u003Cp\\u003E1. “&lt;env\_name&gt;”为当前环境的环境名称。环境名两边不加尖括号“&lt;&gt;”。\\u003C\\u002Fp\\u003E\\u003Cp\\u003E2. “&lt;notebook\_name&gt;”为自定义显示在Jupyter Notebook中的名称。名称两边不加尖括号“&lt;&gt;”，但\\u003Cb\\u003E双引号必须加\\u003C\\u002Fb\\u003E。\\u003C\\u002Fp\\u003E\\u003Cp\\u003E3. “--name”参数的值，即“&lt;env\_name&gt;”是Jupyter内部使用的，其目录的存放路径为\\u003Ccode\\u003E~\\u002FLibrary\\u002FJupyter\\u002Fkernels\\u002F\\u003C\\u002Fcode\\u003E。如果定义的名称在该路径已经存在，那么将自动覆盖该名称目录的内容。\\u003C\\u002Fp\\u003E\\u003Cp\\u003E4. “--display-name”参数的值是显示在Jupyter Notebook的菜单中的名称。\\u003C\\u002Fp\\u003E\\u003Ch2\\u003E\\u003Cb\\u003E⑷ 检验\\u003C\\u002Fb\\u003E\\u003C\\u002Fh2\\u003E\\u003Cp\\u003E使用命令\\u003Ccode\\u003Ejupyter notebook\\u003C\\u002Fcode\\u003E启动Jupyter Notebook；在“Files”下的“New”下拉框中即可找到你在第⑶步中的自定义名称，此时，你便可以尽情地在Jupyter Notebook中切换环境，在不同的环境中创建笔记本进行工作和学习啦！\\u003C\\u002Fp\\u003E\\u003Ch2\\u003E\\u003Cb\\u003E3. 解决方法之图形界面模式\\u003C\\u002Fb\\u003E\\u003C\\u002Fh2\\u003E\\u003Cp\\u003E① 你创建了一个新的环境，但却发现在Jupyter Notebook的“New”中找不到这个环境，无法在该环境中创建笔记本。 \\u003C\\u002Fp\\u003E\\u003Cfigure\\u003E\\u003Cnoscript\\u003E\\u003Cimg src=\\"https:\\u002F\\u002Fpic3.zhimg.com\\u002Fv2-5c1dc9640e1bf796c24b9d29c62868aa\_b.gif\\" data-size=\\"normal\\" data-rawwidth=\\"1438\\" data-rawheight=\\"665\\" data-thumbnail=\\"https:\\u002F\\u002Fpic3.zhimg.com\\u002Fv2-5c1dc9640e1bf796c24b9d29c62868aa\_b.jpg\\" class=\\"origin\_image zh-lightbox-thumb\\" width=\\"1438\\" data-original=\\"https:\\u002F\\u002Fpic3.zhimg.com\\u002Fv2-5c1dc9640e1bf796c24b9d29c62868aa\_r.jpg\\"\\u003E\\u003C\\u002Fnoscript\\u003E\\u003Cimg src=\\"data:image\\u002Fsvg+xml;utf8,&lt;svg%20xmlns='http:\\u002F\\u002Fwww.w3.org\\u002F2000\\u002Fsvg'%20width='1438'%20height='665'&gt;&lt;\\u002Fsvg&gt;\\" data-size=\\"normal\\" data-rawwidth=\\"1438\\" data-rawheight=\\"665\\" data-thumbnail=\\"https:\\u002F\\u002Fpic3.zhimg.com\\u002Fv2-5c1dc9640e1bf796c24b9d29c62868aa\_b.jpg\\" class=\\"origin\_image zh-lightbox-thumb lazy\\" width=\\"1438\\" data-original=\\"https:\\u002F\\u002Fpic3.zhimg.com\\u002Fv2-5c1dc9640e1bf796c24b9d29c62868aa\_r.jpg\\" data-actualsrc=\\"https:\\u002F\\u002Fpic3.zhimg.com\\u002Fv2-5c1dc9640e1bf796c24b9d29c62868aa\_b.gif\\"\\u003E\\u003Cfigcaption\\u003E问题发现\\u003C\\u002Ffigcaption\\u003E\\u003C\\u002Ffigure\\u003E\\u003Cp\\u003E\\u003Cbr\\u003E\\u003C\\u002Fp\\u003E\\u003Cp\\u003E\\u003Cbr\\u003E\\u003C\\u002Fp\\u003E\\u003Cp\\u003E② 进入Jupyter Notebook → Conda → 在“Conda\\u003Cbr\\u003Eenvironment”中点击你要添加ipykernel包的环境 → 左下方搜索框输入“ipykernel”\\u003Cbr\\u003E→ 勾选“ipykernel” → 点击搜索框旁的“→”箭头 → 安装完毕 → 右下方框内找到“ipykernel”说明已经安装成功\\u003C\\u002Fp\\u003E\\u003Cfigure\\u003E\\u003Cnoscript\\u003E\\u003Cimg src=\\"https:\\u002F\\u002Fpic4.zhimg.com\\u002Fv2-49839a5db0f9108ad13c185a20f958e3\_b.gif\\" data-size=\\"normal\\" data-rawwidth=\\"1438\\" data-rawheight=\\"660\\" data-thumbnail=\\"https:\\u002F\\u002Fpic4.zhimg.com\\u002Fv2-49839a5db0f9108ad13c185a20f958e3\_b.jpg\\" class=\\"origin\_image zh-lightbox-thumb\\" width=\\"1438\\" data-original=\\"https:\\u002F\\u002Fpic4.zhimg.com\\u002Fv2-49839a5db0f9108ad13c185a20f958e3\_r.jpg\\"\\u003E\\u003C\\u002Fnoscript\\u003E\\u003Cimg src=\\"data:image\\u002Fsvg+xml;utf8,&lt;svg%20xmlns='http:\\u002F\\u002Fwww.w3.org\\u002F2000\\u002Fsvg'%20width='1438'%20height='660'&gt;&lt;\\u002Fsvg&gt;\\" data-size=\\"normal\\" data-rawwidth=\\"1438\\" data-rawheight=\\"660\\" data-thumbnail=\\"https:\\u002F\\u002Fpic4.zhimg.com\\u002Fv2-49839a5db0f9108ad13c185a20f958e3\_b.jpg\\" class=\\"origin\_image zh-lightbox-thumb lazy\\" width=\\"1438\\" data-original=\\"https:\\u002F\\u002Fpic4.zhimg.com\\u002Fv2-49839a5db0f9108ad13c185a20f958e3\_r.jpg\\" data-actualsrc=\\"https:\\u002F\\u002Fpic4.zhimg.com\\u002Fv2-49839a5db0f9108ad13c185a20f958e3\_b.gif\\"\\u003E\\u003Cfigcaption\\u003E解决方法\\u003C\\u002Ffigcaption\\u003E\\u003C\\u002Ffigure\\u003E\\u003Cp\\u003E\\u003Cbr\\u003E\\u003C\\u002Fp\\u003E\\u003Cp\\u003E\\u003Cbr\\u003E\\u003C\\u002Fp\\u003E\\u003Cp\\u003E③ 在终端\\u003Ccode\\u003Econtrol c\\u003C\\u002Fcode\\u003E关闭Jupyter Notebook的服务器然后重启Jupyter Notebook，在“File”的“New”的下拉列表里就可以找到你的环境啦。\\u003C\\u002Fp\\u003E\\u003Cfigure\\u003E\\u003Cnoscript\\u003E\\u003Cimg src=\\"https:\\u002F\\u002Fpic1.zhimg.com\\u002Fv2-9d4fa171b3010a04d3e1229fdfebbbe0\_b.gif\\" data-size=\\"normal\\" data-rawwidth=\\"1438\\" data-rawheight=\\"705\\" data-thumbnail=\\"https:\\u002F\\u002Fpic1.zhimg.com\\u002Fv2-9d4fa171b3010a04d3e1229fdfebbbe0\_b.jpg\\" class=\\"origin\_image zh-lightbox-thumb\\" width=\\"1438\\" data-original=\\"https:\\u002F\\u002Fpic1.zhimg.com\\u002Fv2-9d4fa171b3010a04d3e1229fdfebbbe0\_r.jpg\\"\\u003E\\u003C\\u002Fnoscript\\u003E\\u003Cimg src=\\"data:image\\u002Fsvg+xml;utf8,&lt;svg%20xmlns='http:\\u002F\\u002Fwww.w3.org\\u002F2000\\u002Fsvg'%20width='1438'%20height='705'&gt;&lt;\\u002Fsvg&gt;\\" data-size=\\"normal\\" data-rawwidth=\\"1438\\" data-rawheight=\\"705\\" data-thumbnail=\\"https:\\u002F\\u002Fpic1.zhimg.com\\u002Fv2-9d4fa171b3010a04d3e1229fdfebbbe0\_b.jpg\\" class=\\"origin\_image zh-lightbox-thumb lazy\\" width=\\"1438\\" data-original=\\"https:\\u002F\\u002Fpic1.zhimg.com\\u002Fv2-9d4fa171b3010a04d3e1229fdfebbbe0\_r.jpg\\" data-actualsrc=\\"https:\\u002F\\u002Fpic1.zhimg.com\\u002Fv2-9d4fa171b3010a04d3e1229fdfebbbe0\_b.gif\\"\\u003E\\u003Cfigcaption\\u003E验证\\u003C\\u002Ffigcaption\\u003E\\u003C\\u002Ffigure\\u003E\\u003Cp\\u003E\\u003Cbr\\u003E\\u003C\\u002Fp\\u003E\\u003Cp\\u003E\\u003Cbr\\u003E\\u003C\\u002Fp\\u003E\\u003Ch2\\u003E\\u003Cb\\u003E七、Jupyter Notebook快捷键\\u003C\\u002Fb\\u003E\\u003C\\u002Fh2\\u003E\\u003Ch2\\u003E\\u003Cb\\u003E1. Mac与Windows特殊按键对照表\\u003C\\u002Fb\\u003E\\u003C\\u002Fh2\\u003E\\u003Cfigure\\u003E\\u003Cnoscript\\u003E\\u003Cimg src=\\"https:\\u002F\\u002Fpic4.zhimg.com\\u002Fv2-8eaff7a48cda7cb89fb462f82d464963\_b.jpg\\" data-size=\\"normal\\" data-rawwidth=\\"558\\" data-rawheight=\\"766\\" class=\\"origin\_image zh-lightbox-thumb\\" width=\\"558\\" data-original=\\"https:\\u002F\\u002Fpic4.zhimg.com\\u002Fv2-8eaff7a48cda7cb89fb462f82d464963\_r.jpg\\"\\u003E\\u003C\\u002Fnoscript\\u003E\\u003Cimg src=\\"data:image\\u002Fsvg+xml;utf8,&lt;svg%20xmlns='http:\\u002F\\u002Fwww.w3.org\\u002F2000\\u002Fsvg'%20width='558'%20height='766'&gt;&lt;\\u002Fsvg&gt;\\" data-size=\\"normal\\" data-rawwidth=\\"558\\" data-rawheight=\\"766\\" class=\\"origin\_image zh-lightbox-thumb lazy\\" width=\\"558\\" data-original=\\"https:\\u002F\\u002Fpic4.zhimg.com\\u002Fv2-8eaff7a48cda7cb89fb462f82d464963\_r.jpg\\" data-actualsrc=\\"https:\\u002F\\u002Fpic4.zhimg.com\\u002Fv2-8eaff7a48cda7cb89fb462f82d464963\_b.jpg\\"\\u003E\\u003Cfigcaption\\u003EMac和Windows特殊按键对照表\\u003C\\u002Ffigcaption\\u003E\\u003C\\u002Ffigure\\u003E\\u003Ch2\\u003E\\u003Cb\\u003E2. Jupyter Notebook笔记本的两种模式\\u003C\\u002Fb\\u003E\\u003C\\u002Fh2\\u003E\\u003Ch2\\u003E\\u003Cb\\u003E① 命令模式\\u003C\\u002Fb\\u003E\\u003C\\u002Fh2\\u003E\\u003Cul\\u003E\\u003Cli\\u003E命令模式将键盘命令与Jupyter Notebook笔记本命令相结合，可以通过键盘不同键的组合运行笔记本的命令。\\u003C\\u002Fli\\u003E\\u003Cli\\u003E按\\u003Ccode\\u003Eesc\\u003C\\u002Fcode\\u003E键进入命令模式。\\u003C\\u002Fli\\u003E\\u003Cli\\u003E命令模式下，单元格边框为灰色，且左侧边框线为蓝色粗线条。\\u003C\\u002Fli\\u003E\\u003C\\u002Ful\\u003E\\u003Cfigure\\u003E\\u003Cnoscript\\u003E\\u003Cimg src=\\"https:\\u002F\\u002Fpic3.zhimg.com\\u002Fv2-a93c521c691f10a59f9e3357125e6e66\_b.jpg\\" data-size=\\"normal\\" data-rawwidth=\\"1440\\" data-rawheight=\\"311\\" class=\\"origin\_image zh-lightbox-thumb\\" width=\\"1440\\" data-original=\\"https:\\u002F\\u002Fpic3.zhimg.com\\u002Fv2-a93c521c691f10a59f9e3357125e6e66\_r.jpg\\"\\u003E\\u003C\\u002Fnoscript\\u003E\\u003Cimg src=\\"data:image\\u002Fsvg+xml;utf8,&lt;svg%20xmlns='http:\\u002F\\u002Fwww.w3.org\\u002F2000\\u002Fsvg'%20width='1440'%20height='311'&gt;&lt;\\u002Fsvg&gt;\\" data-size=\\"normal\\" data-rawwidth=\\"1440\\" data-rawheight=\\"311\\" class=\\"origin\_image zh-lightbox-thumb lazy\\" width=\\"1440\\" data-original=\\"https:\\u002F\\u002Fpic3.zhimg.com\\u002Fv2-a93c521c691f10a59f9e3357125e6e66\_r.jpg\\" data-actualsrc=\\"https:\\u002F\\u002Fpic3.zhimg.com\\u002Fv2-a93c521c691f10a59f9e3357125e6e66\_b.jpg\\"\\u003E\\u003Cfigcaption\\u003E命令模式\\u003C\\u002Ffigcaption\\u003E\\u003C\\u002Ffigure\\u003E\\u003Ch2\\u003E\\u003Cb\\u003E② 编辑模式\\u003C\\u002Fb\\u003E\\u003C\\u002Fh2\\u003E\\u003Cul\\u003E\\u003Cli\\u003E编辑模式使用户可以在单元格内编辑代码或文档。\\u003C\\u002Fli\\u003E\\u003Cli\\u003E按\\u003Ccode\\u003Eenter\\u003C\\u002Fcode\\u003E或\\u003Ccode\\u003Ereturn\\u003C\\u002Fcode\\u003E键进入编辑模式。\\u003C\\u002Fli\\u003E\\u003Cli\\u003E编辑模式下，单元格边框和左侧边框线均为绿色。\\u003C\\u002Fli\\u003E\\u003C\\u002Ful\\u003E\\u003Cfigure\\u003E\\u003Cnoscript\\u003E\\u003Cimg src=\\"https:\\u002F\\u002Fpic2.zhimg.com\\u002Fv2-874151e646d6363c1307b13c410234d9\_b.jpg\\" data-size=\\"normal\\" data-rawwidth=\\"1440\\" data-rawheight=\\"294\\" class=\\"origin\_image zh-lightbox-thumb\\" width=\\"1440\\" data-original=\\"https:\\u002F\\u002Fpic2.zhimg.com\\u002Fv2-874151e646d6363c1307b13c410234d9\_r.jpg\\"\\u003E\\u003C\\u002Fnoscript\\u003E\\u003Cimg src=\\"data:image\\u002Fsvg+xml;utf8,&lt;svg%20xmlns='http:\\u002F\\u002Fwww.w3.org\\u002F2000\\u002Fsvg'%20width='1440'%20height='294'&gt;&lt;\\u002Fsvg&gt;\\" data-size=\\"normal\\" data-rawwidth=\\"1440\\" data-rawheight=\\"294\\" class=\\"origin\_image zh-lightbox-thumb lazy\\" width=\\"1440\\" data-original=\\"https:\\u002F\\u002Fpic2.zhimg.com\\u002Fv2-874151e646d6363c1307b13c410234d9\_r.jpg\\" data-actualsrc=\\"https:\\u002F\\u002Fpic2.zhimg.com\\u002Fv2-874151e646d6363c1307b13c410234d9\_b.jpg\\"\\u003E\\u003Cfigcaption\\u003E编辑模式\\u003C\\u002Ffigcaption\\u003E\\u003C\\u002Ffigure\\u003E\\u003Ch2\\u003E\\u003Cb\\u003E3. 两种模式的快捷键\\u003C\\u002Fb\\u003E\\u003C\\u002Fh2\\u003E\\u003Ch2\\u003E\\u003Cb\\u003E① 命令模式\\u003C\\u002Fb\\u003E\\u003C\\u002Fh2\\u003E\\u003Cfigure\\u003E\\u003Cnoscript\\u003E\\u003Cimg src=\\"https:\\u002F\\u002Fpic4.zhimg.com\\u002Fv2-61c3a34252d14a09a6819d213298e5bf\_b.jpg\\" data-size=\\"normal\\" data-rawwidth=\\"952\\" data-rawheight=\\"3302\\" class=\\"origin\_image zh-lightbox-thumb\\" width=\\"952\\" data-original=\\"https:\\u002F\\u002Fpic4.zhimg.com\\u002Fv2-61c3a34252d14a09a6819d213298e5bf\_r.jpg\\"\\u003E\\u003C\\u002Fnoscript\\u003E\\u003Cimg src=\\"data:image\\u002Fsvg+xml;utf8,&lt;svg%20xmlns='http:\\u002F\\u002Fwww.w3.org\\u002F2000\\u002Fsvg'%20width='952'%20height='3302'&gt;&lt;\\u002Fsvg&gt;\\" data-size=\\"normal\\" data-rawwidth=\\"952\\" data-rawheight=\\"3302\\" class=\\"origin\_image zh-lightbox-thumb lazy\\" width=\\"952\\" data-original=\\"https:\\u002F\\u002Fpic4.zhimg.com\\u002Fv2-61c3a34252d14a09a6819d213298e5bf\_r.jpg\\" data-actualsrc=\\"https:\\u002F\\u002Fpic4.zhimg.com\\u002Fv2-61c3a34252d14a09a6819d213298e5bf\_b.jpg\\"\\u003E\\u003Cfigcaption\\u003E命令模式快捷键\\u003C\\u002Ffigcaption\\u003E\\u003C\\u002Ffigure\\u003E\\u003Ch2\\u003E\\u003Cb\\u003E② 编辑模式\\u003C\\u002Fb\\u003E\\u003C\\u002Fh2\\u003E\\u003Cfigure\\u003E\\u003Cnoscript\\u003E\\u003Cimg src=\\"https:\\u002F\\u002Fpic4.zhimg.com\\u002Fv2-8eaff7a48cda7cb89fb462f82d464963\_b.jpg\\" data-size=\\"normal\\" data-rawwidth=\\"558\\" data-rawheight=\\"766\\" class=\\"origin\_image zh-lightbox-thumb\\" width=\\"558\\" data-original=\\"https:\\u002F\\u002Fpic4.zhimg.com\\u002Fv2-8eaff7a48cda7cb89fb462f82d464963\_r.jpg\\"\\u003E\\u003C\\u002Fnoscript\\u003E\\u003Cimg src=\\"data:image\\u002Fsvg+xml;utf8,&lt;svg%20xmlns='http:\\u002F\\u002Fwww.w3.org\\u002F2000\\u002Fsvg'%20width='558'%20height='766'&gt;&lt;\\u002Fsvg&gt;\\" data-size=\\"normal\\" data-rawwidth=\\"558\\" data-rawheight=\\"766\\" class=\\"origin\_image zh-lightbox-thumb lazy\\" width=\\"558\\" data-original=\\"https:\\u002F\\u002Fpic4.zhimg.com\\u002Fv2-8eaff7a48cda7cb89fb462f82d464963\_r.jpg\\" data-actualsrc=\\"https:\\u002F\\u002Fpic4.zhimg.com\\u002Fv2-8eaff7a48cda7cb89fb462f82d464963\_b.jpg\\"\\u003E\\u003Cfigcaption\\u003E编辑模式快捷键\\u003C\\u002Ffigcaption\\u003E\\u003C\\u002Ffigure\\u003E\\u003Ch2\\u003E\\u003Cb\\u003E4. 查看和编辑快捷键\\u003C\\u002Fb\\u003E\\u003C\\u002Fh2\\u003E\\u003Ch2\\u003E\\u003Cb\\u003E① 查看快捷键\\u003C\\u002Fb\\u003E\\u003C\\u002Fh2\\u003E\\u003Cp\\u003E① 进入Jupyter Notebook主界面“File”中。\\u003C\\u002Fp\\u003E\\u003Cp\\u003E② 在“New”的下拉列表中选择环境创建一个笔记本。\\u003C\\u002Fp\\u003E\\u003Cp\\u003E③ 点击“Help”。\\u003C\\u002Fp\\u003E\\u003Cp\\u003E④ 点击“Keyboard Shortcuts”。\\u003C\\u002Fp\\u003E\\u003Ch2\\u003E\\u003Cb\\u003E② 编辑快捷键\\u003C\\u002Fb\\u003E\\u003C\\u002Fh2\\u003E\\u003Ch2\\u003E\\u003Cb\\u003E⑴ 方法一\\u003C\\u002Fb\\u003E\\u003C\\u002Fh2\\u003E\\u003Cp\\u003E① 进入Jupyter Notebook主界面“File”中。\\u003C\\u002Fp\\u003E\\u003Cp\\u003E② 在“New”的下拉列表中选择环境创建一个笔记本。\\u003C\\u002Fp\\u003E\\u003Cp\\u003E③ 点击“Help”。\\u003C\\u002Fp\\u003E\\u003Cp\\u003E④ 点击“Keyboard Shortcuts”。\\u003C\\u002Fp\\u003E\\u003Cp\\u003E⑤ 弹出的对话框中“Command Mode (press Esc to enable)”旁点击“Edit\\u003Cbr\\u003EShortcuts”按钮。\\u003C\\u002Fp\\u003E\\u003Ch2\\u003E\\u003Cb\\u003E⑵ 方法二\\u003C\\u002Fb\\u003E\\u003C\\u002Fh2\\u003E\\u003Cp\\u003E① 进入Jupyter Notebook主界面“File”中。\\u003C\\u002Fp\\u003E\\u003Cp\\u003E② 在“New”的下拉列表中选择环境创建一个笔记本。\\u003C\\u002Fp\\u003E\\u003Cp\\u003E③ 点击“Help”。\\u003C\\u002Fp\\u003E\\u003Cp\\u003E④ 点击“Edit Keyboard Shortcuts”。\\u003C\\u002Fp\\u003E\\u003Ch2\\u003E\\u003Cb\\u003E③ 例\\u003C\\u002Fb\\u003E\\u003C\\u002Fh2\\u003E\\u003Cfigure\\u003E\\u003Cnoscript\\u003E\\u003Cimg src=\\"https:\\u002F\\u002Fpic3.zhimg.com\\u002Fv2-706e6c1a0364e6d5279f309e0ed5d0f6\_b.gif\\" data-size=\\"normal\\" data-rawwidth=\\"1436\\" data-rawheight=\\"705\\" data-thumbnail=\\"https:\\u002F\\u002Fpic3.zhimg.com\\u002Fv2-706e6c1a0364e6d5279f309e0ed5d0f6\_b.jpg\\" class=\\"origin\_image zh-lightbox-thumb\\" width=\\"1436\\" data-original=\\"https:\\u002F\\u002Fpic3.zhimg.com\\u002Fv2-706e6c1a0364e6d5279f309e0ed5d0f6\_r.jpg\\"\\u003E\\u003C\\u002Fnoscript\\u003E\\u003Cimg src=\\"data:image\\u002Fsvg+xml;utf8,&lt;svg%20xmlns='http:\\u002F\\u002Fwww.w3.org\\u002F2000\\u002Fsvg'%20width='1436'%20height='705'&gt;&lt;\\u002Fsvg&gt;\\" data-size=\\"normal\\" data-rawwidth=\\"1436\\" data-rawheight=\\"705\\" data-thumbnail=\\"https:\\u002F\\u002Fpic3.zhimg.com\\u002Fv2-706e6c1a0364e6d5279f309e0ed5d0f6\_b.jpg\\" class=\\"origin\_image zh-lightbox-thumb lazy\\" width=\\"1436\\" data-original=\\"https:\\u002F\\u002Fpic3.zhimg.com\\u002Fv2-706e6c1a0364e6d5279f309e0ed5d0f6\_r.jpg\\" data-actualsrc=\\"https:\\u002F\\u002Fpic3.zhimg.com\\u002Fv2-706e6c1a0364e6d5279f309e0ed5d0f6\_b.gif\\"\\u003E\\u003Cfigcaption\\u003E查看和编辑快捷键\\u003C\\u002Ffigcaption\\u003E\\u003C\\u002Ffigure\\u003E\\u003Cp\\u003E\\u003Cbr\\u003E\\u003C\\u002Fp\\u003E\\u003Cp\\u003E\\u003Cbr\\u003E\\u003C\\u002Fp\\u003E\\u003Ch2\\u003E\\u003Cb\\u003E八、关闭和退出\\u003C\\u002Fb\\u003E\\u003C\\u002Fh2\\u003E\\u003Ch2\\u003E\\u003Cb\\u003E1. 关闭笔记本和终端\\u003C\\u002Fb\\u003E\\u003C\\u002Fh2\\u003E\\u003Cp\\u003E当我们在Jupyter Notebook中创建了终端或笔记本时，将会弹出新的窗口来运行终端或笔记本。当我们使用完毕想要退出终端或笔记本时，仅仅\\u003Cb\\u003E关闭页面\\u003C\\u002Fb\\u003E是无法结束程序运行的，因此我们需要通过以下步骤将其完全关闭。\\u003C\\u002Fp\\u003E\\u003Ch2\\u003E\\u003Cb\\u003E① 方法一\\u003C\\u002Fb\\u003E\\u003C\\u002Fh2\\u003E\\u003Cp\\u003E⑴ 进入“Files”页面。\\u003C\\u002Fp\\u003E\\u003Cp\\u003E⑵ 勾选想要关闭的“ipynb”笔记本。正在运行的笔记本其图标为绿色，且后边标有“Running”的字样；已经关闭的笔记本其图标为灰色。\\u003C\\u002Fp\\u003E\\u003Cp\\u003E⑶ 点击上方的黄色的“Shutdown”按钮。\\u003C\\u002Fp\\u003E\\u003Cp\\u003E⑷ 成功关闭笔记本。\\u003C\\u002Fp\\u003E\\u003Cul\\u003E\\u003Cli\\u003E注意：此方法只能关闭笔记本，无法关闭终端。\\u003C\\u002Fli\\u003E\\u003C\\u002Ful\\u003E\\u003Ch2\\u003E\\u003Cb\\u003E② 方法二\\u003C\\u002Fb\\u003E\\u003C\\u002Fh2\\u003E\\u003Cp\\u003E⑴ 进入“Running”页面。\\u003C\\u002Fp\\u003E\\u003Cp\\u003E⑵ 第一栏是“Terminals”，即所有正在运行的终端均会在此显示；第二栏是“Notebooks”，即所有正在运行的“ipynb”笔记本均会在此显示。\\u003C\\u002Fp\\u003E\\u003Cp\\u003E⑶ 点击想要关闭的终端或笔记本后黄色“Shutdown”按钮。\\u003C\\u002Fp\\u003E\\u003Cp\\u003E⑷ 成功关闭终端或笔记本。\\u003C\\u002Fp\\u003E\\u003Cul\\u003E\\u003Cli\\u003E注意：此方法可以关闭任何正在运行的终端和笔记本。\\u003C\\u002Fli\\u003E\\u003C\\u002Ful\\u003E\\u003Ch2\\u003E\\u003Cb\\u003E③ 注意\\u003C\\u002Fb\\u003E\\u003C\\u002Fh2\\u003E\\u003Cp\\u003E⑴ 只有“ipynb”笔记本和终端需要通过上述方法才能使其结束运行。\\u003C\\u002Fp\\u003E\\u003Cp\\u003E⑵\\u003Cbr\\u003E“txt”文档，即“New”下拉列表中的“Text\\u003Cbr\\u003EFile”，以及“Folder”只要关闭程序运行的页面即结束运行，无需通过上述步骤关闭。\\u003C\\u002Fp\\u003E\\u003Ch2\\u003E\\u003Cb\\u003E④ 演示\\u003C\\u002Fb\\u003E\\u003C\\u002Fh2\\u003E\\u003Cfigure\\u003E\\u003Cnoscript\\u003E\\u003Cimg src=\\"https:\\u002F\\u002Fpic4.zhimg.com\\u002Fv2-05314d41206fbfc5bbe3533709202f23\_b.gif\\" data-size=\\"normal\\" data-rawwidth=\\"1438\\" data-rawheight=\\"451\\" data-thumbnail=\\"https:\\u002F\\u002Fpic4.zhimg.com\\u002Fv2-05314d41206fbfc5bbe3533709202f23\_b.jpg\\" class=\\"origin\_image zh-lightbox-thumb\\" width=\\"1438\\" data-original=\\"https:\\u002F\\u002Fpic4.zhimg.com\\u002Fv2-05314d41206fbfc5bbe3533709202f23\_r.jpg\\"\\u003E\\u003C\\u002Fnoscript\\u003E\\u003Cimg src=\\"data:image\\u002Fsvg+xml;utf8,&lt;svg%20xmlns='http:\\u002F\\u002Fwww.w3.org\\u002F2000\\u002Fsvg'%20width='1438'%20height='451'&gt;&lt;\\u002Fsvg&gt;\\" data-size=\\"normal\\" data-rawwidth=\\"1438\\" data-rawheight=\\"451\\" data-thumbnail=\\"https:\\u002F\\u002Fpic4.zhimg.com\\u002Fv2-05314d41206fbfc5bbe3533709202f23\_b.jpg\\" class=\\"origin\_image zh-lightbox-thumb lazy\\" width=\\"1438\\" data-original=\\"https:\\u002F\\u002Fpic4.zhimg.com\\u002Fv2-05314d41206fbfc5bbe3533709202f23\_r.jpg\\" data-actualsrc=\\"https:\\u002F\\u002Fpic4.zhimg.com\\u002Fv2-05314d41206fbfc5bbe3533709202f23\_b.gif\\"\\u003E\\u003Cfigcaption\\u003E关闭笔记本或终端程序\\u003C\\u002Ffigcaption\\u003E\\u003C\\u002Ffigure\\u003E\\u003Cp\\u003E\\u003Cbr\\u003E\\u003C\\u002Fp\\u003E\\u003Cp\\u003E\\u003Cbr\\u003E\\u003C\\u002Fp\\u003E\\u003Ch2\\u003E\\u003Cb\\u003E2. 退出Jupyter Notebook程序\\u003C\\u002Fb\\u003E\\u003C\\u002Fh2\\u003E\\u003Cp\\u003E如果你想退出Jupyter Notebook程序，仅仅通过关闭网页是无法退出的，因为当你打开Jupyter Notebook时，其实是启动了它的服务器。\\u003C\\u002Fp\\u003E\\u003Cp\\u003E你可以尝试关闭页面，并打开新的浏览器页面，把之前的地址输进地址栏，然后跳转页面，你会发现再次进入了刚才“关闭”的Jupyter Notebook页面。\\u003C\\u002Fp\\u003E\\u003Cp\\u003E如果你忘记了刚才关闭的页面地址，可以在启动Jupyter Notebook的终端中找到地址，复制并粘贴至新的浏览器页面的地址栏，会发现同样能够进入刚才关闭的页面。\\u003C\\u002Fp\\u003E\\u003Cp\\u003E因此，想要彻底退出Jupyter Notebook，需要关闭它的服务器。只需要在它启动的终端上按：\\u003C\\u002Fp\\u003E\\u003Cul\\u003E\\u003Cli\\u003EMac用户：\\u003Ccode\\u003Econtrol c\\u003C\\u002Fcode\\u003E\\u003C\\u002Fli\\u003E\\u003Cli\\u003EWindows用户：\\u003Ccode\\u003Ectrl c\\u003C\\u002Fcode\\u003E\\u003C\\u002Fli\\u003E\\u003C\\u002Ful\\u003E\\u003Cp\\u003E然后在终端上会提示：“Shutdown this notebook server (y\\u002F\[n\])?”输入\\u003Ccode\\u003Ey\\u003C\\u002Fcode\\u003E即可关闭服务器，这才是彻底退出了Jupyter Notebook程序。此时，如果你想要通过输入刚才关闭网页的网址进行访问Jupyter Notebook便会看到报错页面。\\u003C\\u002Fp\\u003E\\u003Ch2\\u003E\\u003Cb\\u003E九、参考资料\\u003C\\u002Fb\\u003E\\u003C\\u002Fh2\\u003E\\u003Cp\\u003E1.知乎：jupyter notebook 可以做哪些事情？\\u003Ca href=\\"https:\\u002F\\u002Fwww.zhihu.com\\u002Fquestion\\u002F46309360\\u002Fanswer\\u002F254638807?utm\_source=wechat\_session&amp;utm\_medium=social\\" class=\\"internal\\"\\u003E猴子的回答\\u003C\\u002Fa\\u003E\\u003C\\u002Fp\\u003E\\u003Cp\\u003E2. \\u003Ca href=\\"http:\\u002F\\u002Flink.zhihu.com\\u002F?target=https%3A\\u002F\\u002Fjupyter-notebook.readthedocs.io\\u002Fen\\u002Fstable\\u002Fnotebook.html\\" class=\\" wrap external\\" target=\\"\_blank\\" rel=\\"nofollow noreferrer\\"\\u003EJupyter Notebook官方介绍\\u003C\\u002Fa\\u003E\\u003C\\u002Fp\\u003E\\u003Cp\\u003E3. \\u003Ca href=\\"http:\\u002F\\u002Flink.zhihu.com\\u002F?target=https%3A\\u002F\\u002Fwww.anaconda.com\\u002Fdownload\\u002F%23macos\\" class=\\" wrap external\\" target=\\"\_blank\\" rel=\\"nofollow noreferrer\\"\\u003EAnaconda官方下载页面\\u003C\\u002Fa\\u003E\\u003C\\u002Fp\\u003E\\u003Cp\\u003E4. \\u003Ca href=\\"http:\\u002F\\u002Flink.zhihu.com\\u002F?target=http%3A\\u002F\\u002Fblog.csdn.net\\u002Ftina\_ttl\\u002Farticle\\u002Fdetails\\u002F51031113%2321-%25E6%2596%25B9%25E5%25BC%258F%25E4%25B8%2580\\" class=\\" wrap external\\" target=\\"\_blank\\" rel=\\"nofollow noreferrer\\"\\u003EPython·Jupyter Notebook各种使用方法记录\\u003C\\u002Fa\\u003E\\u003C\\u002Fp\\u003E\\u003Cp\\u003E5. \\u003Ca href=\\"http:\\u002F\\u002Flink.zhihu.com\\u002F?target=https%3A\\u002F\\u002Fstackoverflow.com\\u002Fquestions\\u002F27934885\\u002Fhow-to-hide-code-from-cells-in-ipython-notebook-visualized-with-nbviewer\\" class=\\" wrap external\\" target=\\"\_blank\\" rel=\\"nofollow noreferrer\\"\\u003EStack Overflow中有关如何隐藏\\u002F显示输入单元格的问题\\u003C\\u002Fa\\u003E\\u003C\\u002Fp\\u003E\\u003Cp\\u003E6. \\u003Ca href=\\"http:\\u002F\\u002Flink.zhihu.com\\u002F?target=http%3A\\u002F\\u002Fipython.readthedocs.io\\u002Fen\\u002Fstable\\u002Finteractive\\u002Fmagics.html\\" class=\\" wrap external\\" target=\\"\_blank\\" rel=\\"nofollow noreferrer\\"\\u003E魔术命令官方文档\\u003C\\u002Fa\\u003E\\u003C\\u002Fp\\u003E\\u003Cp\\u003E7. \\u003Ca href=\\"http:\\u002F\\u002Flink.zhihu.com\\u002F?target=http%3A\\u002F\\u002Fblog.csdn.net\\u002Flawme\\u002Farticle\\u002Fdetails\\u002F51034543\\" class=\\" wrap external\\" target=\\"\_blank\\" rel=\\"nofollow noreferrer\\"\\u003EJupyter Notebook 的快捷键\\u003C\\u002Fa\\u003E\\u003C\\u002Fp\\u003E\\u003Cp\\u003E8. \\u003Ca href=\\"http:\\u002F\\u002Flink.zhihu.com\\u002F?target=http%3A\\u002F\\u002Fjupyter.org\\u002Fdocumentation\\" class=\\" wrap external\\" target=\\"\_blank\\" rel=\\"nofollow noreferrer\\"\\u003EJupyter Notebook官方文档\\u003C\\u002Fa\\u003E\\u003C\\u002Fp\\u003E","commentCount":48,"linkbox":{"url":"","category":"","pic":"","title":""},"isTitleImageFullScreen":false,"type":"article","suggestEdit":{"status":false,"url":"","reason":"","tip":"","title":""},"tipjarorsCount":0,"status":0,"updated":1516595036,"isLabeled":false,"reason":"","voting":0,"created":1516357181,"url":"http:\\u002F\\u002Fzhuanlan.zhihu.com\\u002Fp\\u002F33105153","commentPermission":"all","title":"Jupyter Notebook介绍、安装及使用教程","annotationAction":\[\],"hasPublishingDraft":false,"paging":{},"imageUrl":"https:\\u002F\\u002Fpic3.zhimg.com\\u002Fv2-637604b9f9fe566bac65ff3f44c184af\_r.jpg","isFavorited":false,"excerptTitle":"","canComment":{"status":true,"reason":""},"isNormal":true}},"columns":{},"topics":{},"roundtables":{},"favlists":{},"comments":{},"notifications":{},"ebooks":{},"activities":{},"feeds":{},"pins":{},"positions":{},"promotions":{},"drafts":{}},"currentUser":"","account":{"lockLevel":{},"unlockTicketStatus":false,"unlockTicket":null,"challenge":\[\],"errorStatus":false,"message":"","isFetching":false,"accountInfo":{},"urlToken":{"loading":false}},"settings":{"socialBind":null,"inboxMsg":null,"notification":{},"email":{},"privacyFlag":null,"blockedUsers":{"isFetching":false,"paging":{"pageNo":1,"pageSize":6},"data":\[\]},"blockedFollowees":{"isFetching":false,"paging":{"pageNo":1,"pageSize":6},"data":\[\]},"ignoredTopics":{"isFetching":false,"paging":{"pageNo":1,"pageSize":6},"data":\[\]},"restrictedTopics":null,"laboratory":{}},"notification":{},"people":{"profileStatus":{},"activitiesByUser":{},"answersByUser":{},"answersSortByVotesByUser":{},"answersIncludedByUser":{},"votedAnswersByUser":{},"thankedAnswersByUser":{},"voteAnswersByUser":{},"thankAnswersByUser":{},"topicAnswersByUser":{},"articlesByUser":{},"articlesSortByVotesByUser":{},"articlesIncludedByUser":{},"pinsByUser":{},"positionsByUser":{},"questionsByUser":{},"commercialQuestionsByUser":{},"favlistsByUser":{},"followingByUser":{},"followersByUser":{},"mutualsByUser":{},"followingColumnsByUser":{},"followingQuestionsByUser":{},"followingFavlistsByUser":{},"followingTopicsByUser":{},"publicationsByUser":{},"columnsByUser":{},"allFavlistsByUser":{},"brands":null,"creationsByUser":{},"creationsSortByVotesByUser":{}},"env":{"ab":{"config":{"experiments":\[{"expId":"launch-ad\_ios\_lans-2","expPrefix":"ad\_ios\_lans","isDynamicallyUpdated":true,"isRuntime":true,"includeTriggerInfo":false},{"expId":"launch-gw\_adr\_dkts-11","expPrefix":"gw\_adr\_dkts","isDynamicallyUpdated":true,"isRuntime":false,"includeTriggerInfo":false},{"expId":"launch-gw\_adr\_mini-2","expPrefix":"gw\_adr\_mini","isDynamicallyUpdated":true,"isRuntime":false,"includeTriggerInfo":false},{"expId":"launch-gw\_adr\_wbtp-2","expPrefix":"gw\_adr\_wbtp","isDynamicallyUpdated":true,"isRuntime":false,"includeTriggerInfo":false},{"expId":"launch-gw\_adr\_wxfb-2","expPrefix":"gw\_adr\_wxfb","isDynamicallyUpdated":true,"isRuntime":false,"includeTriggerInfo":false},{"expId":"launch-gw\_anr\_wxbk-2","expPrefix":"gw\_anr\_wxbk","isDynamicallyUpdated":true,"isRuntime":false,"includeTriggerInfo":false},{"expId":"launch-gw\_ios\_dkts-8","expPrefix":"gw\_ios\_dkts","isDynamicallyUpdated":true,"isRuntime":false,"includeTriggerInfo":false},{"expId":"launch-gw\_ios\_mini-2","expPrefix":"gw\_ios\_mini","isDynamicallyUpdated":true,"isRuntime":false,"includeTriggerInfo":false},{"expId":"launch-gw\_ios\_wxb-2","expPrefix":"gw\_ios\_wxb","isDynamicallyUpdated":true,"isRuntime":false,"includeTriggerInfo":false},{"expId":"launch-gw\_ios\_wxfb-1","expPrefix":"gw\_ios\_wxfb","isDynamicallyUpdated":true,"isRuntime":false,"includeTriggerInfo":false},{"expId":"launch-gw\_wbtp-2","expPrefix":"gw\_wbtp","isDynamicallyUpdated":true,"isRuntime":false,"includeTriggerInfo":false},{"expId":"launch-mp\_amap\_ios-1","expPrefix":"mp\_amap\_ios","isDynamicallyUpdated":true,"isRuntime":false,"includeTriggerInfo":false},{"expId":"launch-mp\_apm-1","expPrefix":"mp\_apm","isDynamicallyUpdated":true,"isRuntime":false,"includeTriggerInfo":false},{"expId":"launch-mp\_hb\_si-3","expPrefix":"mp\_hb\_si","isDynamicallyUpdated":true,"isRuntime":false,"includeTriggerInfo":false},{"expId":"launch-mp\_ios\_webp-2","expPrefix":"mp\_ios\_webp","isDynamicallyUpdated":true,"isRuntime":false,"includeTriggerInfo":false},{"expId":"launch-mp\_video\_feed-2","expPrefix":"mp\_video\_feed","isDynamicallyUpdated":false,"isRuntime":false,"includeTriggerInfo":false},{"expId":"launch-se\_ios\_topsearch-2","expPrefix":"se\_ios\_topsearch","isDynamicallyUpdated":false,"isRuntime":false,"includeTriggerInfo":false},{"expId":"launch-top\_dtmt-10","expPrefix":"top\_dtmt","isDynamicallyUpdated":true,"isRuntime":false,"includeTriggerInfo":false},{"expId":"launch-top\_feed\_card-1","expPrefix":"top\_feed\_card","isDynamicallyUpdated":true,"isRuntime":false,"includeTriggerInfo":false},{"expId":"launch-vd\_adrupload\_cdn-2","expPrefix":"vd\_adrupload\_cdn","isDynamicallyUpdated":false,"isRuntime":false,"includeTriggerInfo":false},{"expId":"launch-vd\_player\_agent-2","expPrefix":"vd\_player\_agent","isDynamicallyUpdated":true,"isRuntime":false,"includeTriggerInfo":false},{"expId":"launch-vd\_ppt\_enter\_2-2","expPrefix":"vd\_ppt\_enter\_2","isDynamicallyUpdated":true,"isRuntime":false,"includeTriggerInfo":false},{"expId":"launch-vd\_upload\_cdn-2","expPrefix":"vd\_upload\_cdn","isDynamicallyUpdated":false,"isRuntime":false,"includeTriggerInfo":false},{"expId":"launch-vd\_zm\_core-2","expPrefix":"vd\_zm\_core","isDynamicallyUpdated":false,"isRuntime":false,"includeTriggerInfo":false},{"expId":"vd\_challenge\_p-1","expPrefix":"vd\_challenge\_p","isDynamicallyUpdated":true,"isRuntime":false,"includeTriggerInfo":false},{"expId":"top\_rfsh\_all-7","expPrefix":"top\_rfsh\_all","isDynamicallyUpdated":true,"isRuntime":false,"includeTriggerInfo":false}\],"params":\[{"id":"top\_multi\_model","type":"String","value":"0","chainId":"\_all\_"},{"id":"adr\_article\_misc","type":"String","value":"0"},{"id":"ios\_mini","type":"String","value":"1"},{"id":"se\_cm","type":"String","value":"1","chainId":"\_all\_"},{"id":"top\_fqai","type":"String","value":"0","chainId":"\_all_"},{"id":"se\_daxuechuisou","type":"String","value":"new","chainId":"\_all_"},{"id":"adr\_ps","type":"String","value":"0"},{"id":"adr\_task\_statistics","type":"String","value":"false"},{"id":"hb\_live\_btn\_color","type":"String","value":"default\_color"},{"id":"se\_ad\_index","type":"String","value":"10","chainId":"\_all_"},{"id":"top\_quality","type":"String","value":"0","chainId":"\_all_"},{"id":"adr\_guest\_refresh","type":"String","value":"1"},{"id":"hb\_new\_label","type":"String","value":"0"},{"id":"ios\_article\_new\_comment","type":"String","value":"0"},{"id":"ios\_real\_time\_launch\_http","type":"String","value":"http\_off"},{"id":"adr\_audio\_enable\_exo","type":"String","value":"0"},{"id":"se\_billboard","type":"String","value":"3","chainId":"\_all\_"},{"id":"top\_recall\_tb\_long","type":"String","value":"51","chainId":"\_all_"},{"id":"top\_root\_web","type":"String","value":"0","chainId":"\_all\_"},{"id":"top\_test\_4\_liguangyi","type":"String","value":"1","chainId":"\_all_"},{"id":"web\_heifetz\_grow\_ad","type":"String","value":"0"},{"id":"ios\_consultation","type":"String","value":"0"},{"id":"se\_entity","type":"String","value":"on","chainId":"\_all_"},{"id":"se\_wiki\_box","type":"String","value":"1","chainId":"\_all\_"},{"id":"top\_rerank\_reweight","type":"String","value":"-1","chainId":"\_all\_"},{"id":"tp\_favsku","type":"String","value":"a","chainId":"\_all_"},{"id":"ios\_hybrid\_intercepting","type":"String","value":"1"},{"id":"se\_cq","type":"String","value":"1","chainId":"\_all_"},{"id":"se\_time\_search","type":"String","value":"origin","chainId":"\_all\_"},{"id":"top\_universalebook","type":"String","value":"1","chainId":"\_all_"},{"id":"ios\_lans","type":"String","value":"close"},{"id":"ios\_pdf","type":"String","value":"n"},{"id":"top\_is\_gr","type":"String","value":"0","chainId":"\_all\_"},{"id":"ios\_adr\_vid\_vol","type":"String","value":"0"},{"id":"ios\_ad\_cta","type":"String","value":"0"},{"id":"top\_billvideo","type":"String","value":"0","chainId":"\_all\_"},{"id":"top\_nid","type":"String","value":"0","chainId":"\_all_"},{"id":"adr\_prt","type":"String","value":"false"},{"id":"hb\_active\_answerer","type":"String","value":"0"},{"id":"hb\_billboard","type":"String","value":"0"},{"id":"hb\_stream\_render","type":"String","value":"0"},{"id":"top\_recall\_follow\_user","type":"String","value":"91","chainId":"\_all_"},{"id":"adr\_rlp","type":"String","value":"0"},{"id":"top\_f\_r\_nb","type":"String","value":"1","chainId":"\_all\_"},{"id":"adr\_cashier\_color","type":"String","value":"0"},{"id":"adr\_invite","type":"String","value":"false"},{"id":"adr\_ques\_comment","type":"String","value":"0"},{"id":"adr\_recommend\_column","type":"String","value":"0"},{"id":"ios\_wxbk","type":"String","value":"1"},{"id":"top\_mt","type":"String","value":"0","chainId":"\_all_"},{"id":"top\_vds\_alb\_pos","type":"String","value":"0","chainId":"\_all_"},{"id":"top\_wonderful","type":"String","value":"1","chainId":"\_all_"},{"id":"hb\_majorob\_style","type":"String","value":"0"},{"id":"top\_alt","type":"String","value":"0","chainId":"\_all_"},{"id":"top\_roundtable","type":"String","value":"1","chainId":"\_all_"},{"id":"top\_vd\_rt\_int","type":"String","value":"0","chainId":"\_all_"},{"id":"top\_tuner\_refactor","type":"String","value":"-1","chainId":"\_all\_"},{"id":"adr\_bugly","type":"String","value":"n"},{"id":"adr\_consultation","type":"String","value":"0"},{"id":"adr\_preload\_question","type":"String","value":"0"},{"id":"ls\_new\_score","type":"String","value":"0","chainId":"\_all\_"},{"id":"adr\_comment\_new\_editor","type":"String","value":"0"},{"id":"ios\_question\_invite\_v2","type":"String","value":"0"},{"id":"pin\_efs","type":"String","value":"orig","chainId":"\_all_"},{"id":"top\_raf","type":"String","value":"n","chainId":"\_all_"},{"id":"ios\_next\_ans","type":"String","value":"N"},{"id":"ios\_question\_answer\_preload","type":"String","value":"0"},{"id":"top\_free\_content","type":"String","value":"-1","chainId":"\_all_"},{"id":"top\_tr","type":"String","value":"0","chainId":"\_all_"},{"id":"top\_vdio\_rew","type":"String","value":"0","chainId":"\_all\_"},{"id":"adr\_anp","type":"String","value":"android\_answer\_pager\_off"},{"id":"adr\_member\_switch","type":"String","value":"0"},{"id":"ios\_comment","type":"String","value":"0"},{"id":"top\_sjre","type":"String","value":"0","chainId":"\_all\_"},{"id":"se\_tf","type":"String","value":"1","chainId":"\_all_"},{"id":"top\_feedre\_cpt","type":"String","value":"101","chainId":"\_all\_"},{"id":"adr\_question\_invite\_v2","type":"String","value":"0"},{"id":"adr\_video\_upload\_cdn","type":"String","value":"1"},{"id":"adr\_zmcore","type":"String","value":"1"},{"id":"ls\_new\_video","type":"String","value":"0","chainId":"\_all_"},{"id":"top\_nszt","type":"String","value":"0","chainId":"\_all_"},{"id":"top\_slot\_ad\_pos","type":"String","value":"1","chainId":"\_all_"},{"id":"top\_video\_fix\_position","type":"String","value":"0","chainId":"\_all_"},{"id":"top\_video\_rew","type":"String","value":"0","chainId":"\_all\_"},{"id":"adr\_android\_gdt","type":"String","value":"open"},{"id":"ios\_searchbox","type":"String","value":"0"},{"id":"ios\_topsearch","type":"String","value":"1"},{"id":"top\_adpar","type":"String","value":"0","chainId":"\_all_"},{"id":"ios\_vm\_subject\_type","type":"String","value":"0"},{"id":"adr\_ans\_video","type":"String","value":"N"},{"id":"adr\_real\_time\_launch\_http","type":"String","value":"http\_off"},{"id":"ios\_asp","type":"String","value":"off"},{"id":"ios\_spic","type":"String","value":"0"},{"id":"top\_billread","type":"String","value":"1","chainId":"\_all_"},{"id":"top\_rank","type":"String","value":"0","chainId":"\_all_"},{"id":"tp\_ios\_topic\_write\_pin\_guide","type":"String","value":"1","chainId":"\_all_"},{"id":"adr\_q\_bar","type":"String","value":"NO"},{"id":"adr\_sqtc","type":"String","value":"1"},{"id":"ios\_launch\_timeout","type":"String","value":"-1"},{"id":"top\_ac\_merge","type":"String","value":"0","chainId":"\_all_"},{"id":"adr\_new\_answer\_pager","type":"String","value":"false"},{"id":"ios\_quill\_editor","type":"String","value":"0"},{"id":"top\_recall\_tb\_follow","type":"String","value":"71","chainId":"\_all\_"},{"id":"top\_retagg","type":"String","value":"0","chainId":"\_all_"},{"id":"ios\_q\_a\_c","type":"String","value":"0"},{"id":"se\_minor\_onebox","type":"String","value":"d","chainId":"\_all_"},{"id":"top\_ntr","type":"String","value":"1","chainId":"\_all_"},{"id":"top\_recommend\_topic\_card","type":"String","value":"0","chainId":"\_all_"},{"id":"adr\_profile\_label","type":"String","value":"1"},{"id":"ios\_apm","type":"String","value":"1"},{"id":"se\_backsearch","type":"String","value":"0","chainId":"\_all\_"},{"id":"ios\_wxfb","type":"String","value":"0"},{"id":"se\_consulting\_price","type":"String","value":"n","chainId":"\_all_"},{"id":"top\_newfollowans","type":"String","value":"0","chainId":"\_all_"},{"id":"adr\_comment","type":"String","value":"false"},{"id":"adr\_editor\_version","type":"String","value":"V2"},{"id":"adr\_mqtt\_5\_24\_0","type":"String","value":"0"},{"id":"ios\_video\_continuous","type":"String","value":"0"},{"id":"top\_ebook","type":"String","value":"0","chainId":"\_all\_"},{"id":"top\_recall\_core\_interest","type":"String","value":"81","chainId":"\_all_"},{"id":"top\_root\_ac","type":"String","value":"1","chainId":"\_all\_"},{"id":"top\_video\_score","type":"String","value":"1","chainId":"\_all\_"},{"id":"adr\_consult","type":"String","value":"0"},{"id":"adr\_perm","type":"String","value":"0"},{"id":"ios\_ge4","type":"String","value":"3"},{"id":"se\_ingress","type":"String","value":"on","chainId":"\_all\_"},{"id":"se\_dl","type":"String","value":"1","chainId":"\_all_"},{"id":"adr\_medal","type":"String","value":"0"},{"id":"hb\_best\_answerer","type":"String","value":"0"},{"id":"ios\_q\_o\_b","type":"String","value":"0"},{"id":"ios\_video\_upload\_cdn","type":"String","value":"1"},{"id":"top\_new\_user\_gift","type":"String","value":"0","chainId":"\_all\_"},{"id":"adr\_spic","type":"String","value":"0"},{"id":"hb\_consulting\_price","type":"String","value":"np"},{"id":"ios\_db\_n\_e","type":"String","value":"0"},{"id":"ios\_video\_agent\_4\_28","type":"String","value":"false"},{"id":"hb\_unfollow\_reason","type":"String","value":"0"},{"id":"ios\_amap","type":"String","value":"y"},{"id":"ios\_profile\_badge","type":"String","value":"true"},{"id":"top\_rerank\_repos","type":"String","value":"-1","chainId":"\_all_"},{"id":"se\_sltr","type":"String","value":"0","chainId":"\_all_"},{"id":"top\_30","type":"String","value":"0","chainId":"\_all_"},{"id":"top\_fqa","type":"String","value":"0","chainId":"\_all_"},{"id":"top\_login\_card","type":"String","value":"1","chainId":"\_all\_"},{"id":"adr\_android\_launch\_ad\_mp4","type":"String","value":"open"},{"id":"adr\_traffic\_leak","type":"String","value":"false"},{"id":"ios\_ff\_cardtype","type":"String","value":"A"},{"id":"se\_product\_rank\_list","type":"String","value":"0","chainId":"\_all_"},{"id":"ios\_x\_z\_c0","type":"String","value":"1"},{"id":"top\_nuc","type":"String","value":"0","chainId":"\_all\_"},{"id":"web\_new\_comment","type":"String","value":"0"},{"id":"top\_v\_album","type":"String","value":"1","chainId":"\_all\_"},{"id":"zr\_ans\_rec","type":"String","value":"gbrank","chainId":"\_all\_"},{"id":"ios\_more\_editcard","type":"String","value":"true"},{"id":"top\_an","type":"String","value":"0","chainId":"\_all_"},{"id":"top\_tagore","type":"String","value":"1","chainId":"\_all_"},{"id":"top\_tffrt","type":"String","value":"0","chainId":"\_all_"},{"id":"adr\_guest\_login","type":"String","value":"0"},{"id":"hb\_entity\_ui","type":"String","value":"origin"},{"id":"top\_bill","type":"String","value":"0","chainId":"\_all_"},{"id":"top\_mlt\_model","type":"String","value":"0","chainId":"\_all\_"},{"id":"hb\_liguangyi\_test","type":"String","value":"1"},{"id":"ios\_dkts","type":"String","value":"20"},{"id":"top\_root\_mg","type":"String","value":"1","chainId":"\_all_"},{"id":"web\_heifetz\_column\_api2","type":"String","value":"0"},{"id":"hb\_report","type":"String","value":"0"},{"id":"ios\_profile\_sig","type":"String","value":"true"},{"id":"ios\_vid\_qt","type":"String","value":"0"},{"id":"se\_qc","type":"String","value":"0","chainId":"\_all_"},{"id":"adr\_dkts","type":"String","value":"20"},{"id":"adr\_pdf","type":"String","value":"n"},{"id":"top\_local","type":"String","value":"1","chainId":"\_all_"},{"id":"web\_stream\_render","type":"String","value":"0"},{"id":"adr\_enable\_agent","type":"String","value":"1"},{"id":"ios\_telecom\_login","type":"String","value":"1"},{"id":"top\_new\_feed","type":"String","value":"1","chainId":"\_all\_"},{"id":"top\_promo","type":"String","value":"1","chainId":"\_all_"},{"id":"ios\_medal\_badge\_view","type":"String","value":"false"},{"id":"se\_auto\_syn","type":"String","value":"0","chainId":"\_all_"},{"id":"adr\_profile\_medal","type":"String","value":"0"},{"id":"ios\_book\_is\_card","type":"String","value":"0"},{"id":"ios\_input\_image","type":"String","value":"1"},{"id":"ios\_km\_center","type":"String","value":"0"},{"id":"top\_root\_few\_topic","type":"String","value":"0","chainId":"\_all\_"},{"id":"top\_vd\_gender","type":"String","value":"0","chainId":"\_all\_"},{"id":"web\_new\_label","type":"String","value":"0"},{"id":"adr\_ppt\_enter","type":"String","value":"1"},{"id":"ios\_article\_recommend\_column","type":"String","value":"0"},{"id":"ios\_magitab","type":"String","value":"0"},{"id":"top\_feedtopiccard","type":"String","value":"0","chainId":"\_all_"},{"id":"ios\_ad\_web\_cache","type":"String","value":"0"},{"id":"se\_merger","type":"String","value":"1","chainId":"\_all\_"},{"id":"top\_gif","type":"String","value":"0","chainId":"\_all_"},{"id":"top\_nucc","type":"String","value":"0","chainId":"\_all_"},{"id":"tp\_discussion\_feed\_type\_android","type":"String","value":"0","chainId":"\_all\_"},{"id":"adr\_anr\_watch","type":"String","value":"false"},{"id":"adr\_next\_answer\_btn","type":"String","value":"0"},{"id":"ios\_7324","type":"String","value":"0"},{"id":"se\_gi","type":"String","value":"0","chainId":"\_all_"},{"id":"se\_dt","type":"String","value":"1","chainId":"\_all_"},{"id":"top\_cc\_at","type":"String","value":"1","chainId":"\_all\_"},{"id":"top\_retag","type":"String","value":"0","chainId":"\_all_"},{"id":"top\_videos\_priority","type":"String","value":"-1","chainId":"\_all\_"},{"id":"adr\_launch\_ad\_new\_strategy","type":"String","value":"open"},{"id":"ios\_answer\_hybrid\_preload","type":"String","value":"0"},{"id":"ios\_invite\_ans","type":"String","value":"A"},{"id":"ios\_vid\_home","type":"String","value":"0"},{"id":"se\_consulting\_switch","type":"String","value":"off","chainId":"\_all_"},{"id":"top\_ab\_validate","type":"String","value":"0","chainId":"\_all\_"},{"id":"top\_dtmt","type":"String","value":"2","chainId":"\_all_"},{"id":"top\_recall\_tb","type":"String","value":"1","chainId":"\_all\_"},{"id":"adr\_mini","type":"String","value":"1"},{"id":"adr\_use\_gd","type":"String","value":"n"},{"id":"adr\_wbtp","type":"String","value":"1"},{"id":"pf\_creator\_card","type":"String","value":"0","chainId":"\_all\_"},{"id":"top\_tagore\_topic","type":"String","value":"0","chainId":"\_all\_"},{"id":"ls\_is\_use\_zrec","type":"String","value":"0","chainId":"\_all_"},{"id":"top\_followtop","type":"String","value":"1","chainId":"\_all_"},{"id":"top\_rerank\_breakin","type":"String","value":"-1","chainId":"\_all\_"},{"id":"top\_rerank\_isolation","type":"String","value":"-1","chainId":"\_all\_"},{"id":"adr\_new\_roundtable","type":"String","value":"true"},{"id":"adr\_wxfb","type":"String","value":"0"},{"id":"ios\_cashier\_color","type":"String","value":"0"},{"id":"ios\_roundtable","type":"String","value":"B"},{"id":"top\_tmt","type":"String","value":"0","chainId":"\_all_"},{"id":"adr\_android\_video\_continuous","type":"String","value":"0"},{"id":"ios\_pay\_view","type":"String","value":"new"},{"id":"web\_card\_style","type":"String","value":"b"},{"id":"se\_filter","type":"String","value":"0","chainId":"\_all\_"},{"id":"se\_rescore","type":"String","value":"1","chainId":"\_all_"},{"id":"top\_follow\_reason","type":"String","value":"0","chainId":"\_all\_"},{"id":"top\_gr\_topic\_reweight","type":"String","value":"0","chainId":"\_all_"},{"id":"ios\_1752","type":"String","value":"0"},{"id":"ios\_ad\_skip\_pos","type":"String","value":"up"},{"id":"ios\_new\_player","type":"String","value":"0"},{"id":"ios\_question\_new\_comment","type":"String","value":"0"},{"id":"top\_sj","type":"String","value":"2","chainId":"\_all\_"},{"id":"top\_vd\_op","type":"String","value":"0","chainId":"\_all\_"},{"id":"top\_yhgc","type":"String","value":"0","chainId":"\_all_"},{"id":"web\_column\_auto\_invite","type":"String","value":"0"},{"id":"adr\_pre\_load\_html","type":"String","value":"0"},{"id":"ios\_ios\_launch\_mp4","type":"String","value":"1"},{"id":"top\_no\_weighing","type":"String","value":"1","chainId":"\_all_"},{"id":"top\_recall\_deep\_user","type":"String","value":"1","chainId":"\_all_"},{"id":"top\_user\_gift","type":"String","value":"0","chainId":"\_all\_"},{"id":"adr\_feed\_video\_continuous","type":"String","value":"0"},{"id":"adr\_liguangi\_test","type":"String","value":"1"},{"id":"adr\_refresh\_token","type":"String","value":"1"},{"id":"top\_ad\_slot","type":"String","value":"1","chainId":"\_all_"},{"id":"ios\_notif\_new\_invite","type":"String","value":"off"},{"id":"top\_recall\_tb\_short","type":"String","value":"61","chainId":"\_all\_"},{"id":"tp\_discussion\_feed\_card\_type","type":"String","value":"0","chainId":"\_all\_"},{"id":"top\_memberfree","type":"String","value":"1","chainId":"\_all_"},{"id":"web\_question\_invite","type":"String","value":"N"},{"id":"adr\_telecom\_login","type":"String","value":"1"},{"id":"ios\_hybrid\_editor\_v3","type":"String","value":"0"},{"id":"ios\_video\_feed","type":"String","value":"1"},{"id":"top\_billab","type":"String","value":"0","chainId":"\_all\_"},{"id":"ios\_q\_bar","type":"String","value":"NO"},{"id":"top\_feedre\_rtt","type":"String","value":"41","chainId":"\_all\_"},{"id":"adr\_sdk\_data\_switch","type":"String","value":"0"},{"id":"adr\_video\_ne\_comment","type":"String","value":"0"},{"id":"se\_ltr","type":"String","value":"1","chainId":"\_all_"},{"id":"top\_hweb","type":"String","value":"0","chainId":"\_all_"},{"id":"top\_card","type":"String","value":"-1","chainId":"\_all_"},{"id":"top\_feedre\_itemcf","type":"String","value":"31","chainId":"\_all\_"},{"id":"top\_hqt","type":"String","value":"0","chainId":"\_all_"},{"id":"top\_newfollow","type":"String","value":"0","chainId":"\_all_"},{"id":"adr\_wxbk","type":"String","value":"1"},{"id":"ios\_add\_question\_v2","type":"String","value":"0"},{"id":"ios\_article\_misc\_panel","type":"String","value":"0"},{"id":"se\_majorob\_style","type":"String","value":"0","chainId":"\_all_"},{"id":"top\_tag\_isolation","type":"String","value":"0","chainId":"\_all\_"},{"id":"tp\_sft","type":"String","value":"a","chainId":"\_all_"},{"id":"adr\_cta","type":"String","value":"0"},{"id":"adr\_mbv","type":"String","value":"false"},{"id":"top\_yc","type":"String","value":"0","chainId":"\_all_"},{"id":"top\_billboard\_count","type":"String","value":"1","chainId":"\_all\_"},{"id":"top\_lowup","type":"String","value":"1","chainId":"\_all_"},{"id":"top\_topic\_feedre","type":"String","value":"21","chainId":"\_all\_"},{"id":"adr\_android\_medal\_badge\_view","type":"String","value":"false"},{"id":"ios\_psn","type":"String","value":"n"},{"id":"ios\_wbtp","type":"String","value":"1"},{"id":"se\_major\_onebox","type":"String","value":"major","chainId":"\_all\_"},{"id":"adr\_traffic\_threshold","type":"String","value":"314572800"},{"id":"hb\_new\_upvote","type":"String","value":"online\_upvote"},{"id":"ios\_answer\_preload","type":"String","value":"0"},{"id":"ios\_lssq","type":"String","value":"0"},{"id":"top\_hca","type":"String","value":"0","chainId":"\_all_"},{"id":"top\_nmt","type":"String","value":"0","chainId":"\_all_"},{"id":"adr\_unif","type":"String","value":"off"},{"id":"hb\_major\_onebox","type":"String","value":"0"},{"id":"se\_relevant\_query","type":"String","value":"new","chainId":"\_all_"},{"id":"top\_distinction","type":"String","value":"0","chainId":"\_all_"},{"id":"ios\_le\_nav","type":"String","value":"0"},{"id":"ios\_video\_agent\_4\_22","type":"String","value":"false"},{"id":"se\_refactored\_search\_index","type":"String","value":"0","chainId":"\_all_"},{"id":"tp\_write\_pin\_guide","type":"String","value":"3","chainId":"\_all_"},{"id":"adr\_article\_new\_comment","type":"String","value":"0"},{"id":"adr\_grow\_guide\_login\_4","type":"String","value":"3"},{"id":"se\_correct\_ab","type":"String","value":"0","chainId":"\_all_"},{"id":"se\_new\_market\_search","type":"String","value":"off","chainId":"\_all_"},{"id":"top\_pfq","type":"String","value":"0","chainId":"\_all_"},{"id":"top\_root","type":"String","value":"0","chainId":"\_all_"},{"id":"top\_spec\_promo","type":"String","value":"1","chainId":"\_all\_"},{"id":"adr\_test\_delete","type":"String","value":"0"},{"id":"ios\_mlssq","type":"String","value":"0"},{"id":"pin\_ef","type":"String","value":"orig","chainId":"\_all\_"},{"id":"top\_gr\_model","type":"String","value":"0","chainId":"\_all\_"},{"id":"se\_engine","type":"String","value":"0","chainId":"\_all_"},{"id":"top\_deep\_promo","type":"String","value":"0","chainId":"\_all\_"},{"id":"top\_feedre","type":"String","value":"1","chainId":"\_all_"},{"id":"adr\_edit\_question","type":"String","value":"0"},{"id":"adr\_topsearch","type":"String","value":"2"},{"id":"ios\_qtoc","type":"String","value":"0"},{"id":"se\_billboardsearch","type":"String","value":"0","chainId":"\_all_"},{"id":"top\_gr\_auto\_model","type":"String","value":"0","chainId":"\_all_"},{"id":"top\_nad","type":"String","value":"1","chainId":"\_all_"},{"id":"top\_recall","type":"String","value":"1","chainId":"\_all_"},{"id":"adr\_book\_is\_card","type":"String","value":"0"},{"id":"ios\_ps","type":"String","value":"0"},{"id":"ios\_webp","type":"String","value":"1"},{"id":"se\_websearch","type":"String","value":"0","chainId":"\_all\_"},{"id":"se\_gemini\_service","type":"String","value":"content","chainId":"\_all\_"},{"id":"top\_billpic","type":"String","value":"0","chainId":"\_all_"},{"id":"top\_billupdate1","type":"String","value":"2","chainId":"\_all_"},{"id":"top\_uit","type":"String","value":"0","chainId":"\_all_"},{"id":"adr\_more\_hyb\_card","type":"String","value":"0"},{"id":"adr\_mqtt","type":"String","value":"0"},{"id":"adr\_osen\_label","type":"String","value":"old"},{"id":"hb\_recommend\_column","type":"String","value":"1"},{"id":"adr\_challenge\_plan","type":"String","value":"3"},{"id":"adr\_hybrid\_dns","type":"String","value":"0"},{"id":"top\_manual\_tag","type":"String","value":"1","chainId":"\_all\_"},{"id":"adr\_video\_topic\_volume\_control","type":"String","value":"0"},{"id":"ios\_search\_tab","type":"String","value":"0"},{"id":"adr\_new\_hybrid","type":"String","value":"0"},{"id":"adr\_traffic\_monitor","type":"String","value":"false"},{"id":"adr\_unfollow\_reason","type":"String","value":"0"},{"id":"adr\_use\_cashier","type":"String","value":"new"}\],"chains":\[{"chainId":"\_all\_"}\]},"triggers":{}},"userAgent":{"Edge":false,"Wechat":false,"Weibo":false,"QQ":false,"Qzone":false,"Mobile":false,"Android":false,"iOS":false,"isAppleDevice":false,"Zhihu":false,"ZhihuHybrid":false,"isBot":false,"Tablet":false,"UC":false,"Sogou":false,"Qihoo":false,"Baidu":false,"BaiduApp":false,"isWebView":false,"origin":"Mozilla\\u002F5.0 (Windows NT 10.0; Win64; x64) AppleWebKit\\u002F537.36 (KHTML, like Gecko) Chrome\\u002F70.0.3538.110 Safari\\u002F537.36"},"trafficSource":"production","edition":{"baidu":false,"sogou":false,"baiduBeijing":false,"yidianzixun":false},"theme":"light","referer":"","conf":{},"ipInfo":{"cityName":"Fuzhou","countryName":"China","regionName":"Fujian","countryCode":"CN"},"logged":false,"tdkInfo":{}},"me":{"accountInfoLoadStatus":{},"organizationProfileStatus":{},"columnContributions":\[\]},"label":{},"comments":{"stickers":\[\],"commentWithPicPermission":{},"notificationsComments":{},"pagination":{},"collapsed":{},"reverse":{},"reviewing":{},"conversation":{},"conversationMore":{},"parent":{}},"pushNotifications":{"default":{"isFetching":false,"isDrained":false,"ids":\[\]},"follow":{"isFetching":false,"isDrained":false,"ids":\[\]},"vote\_thank":{"isFetching":false,"isDrained":false,"ids":\[\]},"currentTab":"default","notificationsCount":{"default":0,"follow":0,"vote\_thank":0}},"messages":{"data":{},"currentTab":"common","messageCount":0},"register":{"registerValidateSucceeded":null,"registerValidateErrors":{},"registerConfirmError":null,"sendDigitsError":null,"registerConfirmSucceeded":null},"login":{"loginUnregisteredError":false,"loginBindWechatError":false,"loginConfirmError":null,"sendDigitsError":null,"validateDigitsError":false,"loginConfirmSucceeded":null,"qrcodeLoginToken":"","qrcodeLoginScanStatus":0,"qrcodeLoginError":null,"qrcodeLoginReturnNewToken":false},"active":{"sendDigitsError":null,"activeConfirmSucceeded":null,"activeConfirmError":null},"switches":{},"captcha":{"captchaNeeded":false,"captchaValidated":false,"captchaBase64String":null,"captchaValidationMessage":null,"loginCaptchaExpires":false},"sms":{"supportedCountries":\[\]},"recommendation":{},"shareTexts":{},"articles":{"voters":{}},"previewPost":{},"favlists":{"relations":{}},"columns":{"voters":{}},"reward":{"answer":{},"article":{},"question":{}},"video":{"data":{}},"topstory":{"topstorys":{"isFetching":false,"isDrained":false,"afterId":0,"items":\[\],"next":null},"recommend":{"isFetching":false,"isDrained":false,"afterId":0,"items":\[\],"next":null},"follow":{"isFetching":false,"isDrained":false,"afterId":0,"items":\[\],"next":null},"followWonderful":{"isFetching":false,"isDrained":false,"afterId":0,"items":\[\],"next":null},"sidebar":null,"announcement":{},"hotList":\[\],"guestFeeds":{"isFetching":false,"isDrained":false,"afterId":0,"items":\[\],"next":null},"followExtra":{"isNewUser":null,"isFetched":false,"followCount":0,"followers":\[\]}},"readStatus":{},"column":{},"articleContribution":{"contributeRequests":\[\],"deleteContributeIdList":\[\],"handledContributeIdList":\[\],"recommendedColumns":\[\],"pinnedColumns":\[\],"sentContributeRequestsIdList":\[null,null,null,null,null,null,null,null,null,null,null,null,null,null,null\]},"columnContribution":{"autoInviteEnabled":false,"recommendedContributors":\[\],"contributionInvitation":null}},"fetchHost":"www.zhihu.com","subAppName":"column"}
