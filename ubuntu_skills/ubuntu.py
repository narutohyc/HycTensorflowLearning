1)查看本機安裝軟件（管道過濾）：
ubuntu@ubuntu:~$ dpkg --list | grep xrd
ii  xrdp             0.6.1-2           amd64        Remote Desktop Protocol (RDP) server
卸載安裝軟件：
sudo apt-get --purge remove xrdp

2)ubuntu好看主題安裝及使用：
安裝：
sudo apt-get install unity-tweak-tool
打開：
unity-tweak-tool

3)ubuntu下配置路徑文件：
~/.bashrc
source ~/.bashrc  #生效
或
/etc/profile
source /etc/profile  #生效

4）ubuntu backup
/home/hyc/.cache/dconf
/home/hyc/.dbus
system setting:
backup

5)windows重装系统时，格式化硬盘，并进行格式转换
问题描述：
windows 无法安装到这个磁盘。 选中的磁盘具有MBR分区表。 在EFI系统上，Windows只能安装到GPT 磁盘

方案：
按Shift + F10组合键打开命令提示符窗口（有些笔记本可能需要同时按住Fn键）
X:>\Sources> diskpart    #输入diskpart命令后回车即可打开Microsoft DiskPart分区工具。
DISKPART> list disk
DISKPART> select disk 0     #输入命令 select disk 0 后回车，这样就选中了第一块硬盘
DISKPART> clean
DISKPART> convert gpt     #输入 convert gpt 命令后回车，即可把当前选中硬盘转换为GPT格式
DiskPart 已将所选磁盘成功地更换为 GPT 格式
运行 list partition 命令查看已经创建的分区信息

-----------------------------------------------------------我是分割线-------------------------------------------------------------------

6）Ubuntu死机解决方法汇总
http://www.jianshu.com/p/36fb9eed82a3
  可尝试的解决方法
  1. 进入TTY终端
  Ctrl+Alt+F1进入TTY1终端字符界面, 输入用户名和密码以登录
  输入top命令, 找到可能造成假死的进程, 用kill命令结束掉进程。然后Ctrl+Alt+F7回到桌面

  2. 直接注销用户
  Ctrl+Alt+F1进入TTY1终端字符界面, 输入用户名和密码以登录。
  然后执行以下的任意一个命令注销桌面重新登录。
  sudo pkill Xorg
  或者
  sudo restart lightdm

  3. 底层方法
  如果上面两种方法不成功, 那有可能是比较底层的软件出现问题。
  可以试试 :** reisub 方法**。
  说具体一点, 是一种系统请求, 直接交给内核处理。
  键盘上一般都有一个键SysRq, 和PrintScreen(截屏)在一个键位上，这就是系统请求的键。
  这个方法可以在死机的情况下安全地重启计算机, 数据不会丢失。
  
  
7）Ubuntu中设置静态IP的方法介绍
  1、修改网络配置文件 
  网络配置信息存储在/etc/network/interfaces 文件中 
  sudo vi /etc/network/interfaces 
  我用vi打开，我的文件显示如下内容： 
  # This file describes the network interfaces available on your system 
  # and how to activate them. For more information, see interfaces(5). 
  # The loopback network interface 
  auto lo 
  iface lo inet loopback 
  我的网络配置文件中只有一个环回地址，即127.0.0.1。在下面添加： 
  auto eth0 #指明网卡eth0在系统启动时自动加载 
  iface eth0 inet static #指明eth0采用ipv4地址，inet表示ipv4地址，inet6表示ipv6地址; static表示静态，dhcp表示动态 
  address 172.22.112.13 #静态ip 
  netmask 255.255.255.128 #子网掩码 
  gateway 172.22.112.1 #网关地址 
  
  
  例子：
  # interfaces(5) file used by ifup(8) and ifdown(8)
  auto lo
  iface lo inet loopback

  auto enp0s31f6
  iface enp0s31f6 inet static
  address 140.138.152.236
  netmask 255.255.255.0
  gateway 140.138.152.254

  dns-nameservers 8.8.8.8
  
  2、重新啓動
  sudo /etc/init.d/networking restart
  reboot
  
  
8）ubuntu16.04修改用戶密碼
  passwd username
  
  
9）硬盘复制
  硬盘数据克隆——“再生龙”
  http://www.jianshu.com/p/2db596571db3
    
10）使用sudo apt-get update命令时出现如下错误：
    E: Could not get lock /var/lib/apt/lists/lock - open (11: Resource temporarily unavailable)
    Unable to lock directory /var/lib/apt/lists
    
  错误：
    hyc@hyc:~$ sudo apt update
    [sudo] password for hyc:    
    Reading package lists... Done
    E: Could not get lock /var/lib/apt/lists/lock - open (11: Resource temporarily unavailable)
    E: Unable to lock directory /var/lib/apt/lists/
  解决方案：
    sudo rm /var/lib/apt/lists/lock
  
11）修改源列表
  sudo gedit /etc/apt/source.list

12）移除过时或错误源
  Err:27 http://ppa.launchpad.net/fcitx-team/nightly/ubuntu xenial Release       
    404  Not Found
  Reading package lists... Done
  E: The repository 'http://ppa.launchpad.net/fcitx-team/nightly/ubuntu xenial Release' does not have a Release file.
  hyc@hyc:/var/lib/apt/lists$  sudo add-apt-repository --remove ppa:fcitx-team/nightly

13）ubuntu無法進入桌面，循環登錄
  原因：顯卡驅動沒裝好，卸載顯卡驅動
  
14）ubuntu failed to load kernel modules
  kernel version is too higher, please dowmgrade it.
  
15）ubuntu查看cpu、內存信息
  主界面搜索：  System Monitor
  
16）ubuntu切換jdk版本
  sudo add-apt-repository ppa:openjdk-r/ppa  
  sudo apt-get update   
  sudo apt-get install openjdk-7-jdk 
  sudo update-alternatives --config java
  sudo update-alternatives --config javac
 
17）ubuntu pip 提示 AttributeError: 'module' object has no attribute 'SSL_ST_INIT'
  sudo python -m easy_install --upgrade pyOpenSSL
  
18）ubuntu下matlab 出现问题:matlab has encountered an internal problem and needs to close
  相信有不少人在Ubuntu系统下会遇到这个问题, 原因是较新的Ubuntu系统(15.04或者更高)使用的libstdc++.so.6比Matlab默认采用的库版本高, 
  当Matlab加载这个库的时候,操作系统检测到不兼容的调用于是产生崩溃并给予退出提示框,差不多是这个样子的输出:
  
  解决方法:强制Matlab使用操作系统提供的库即可, 进入Matlab的安装目录,继续导航到该目录下的sys/os/glnxa64目录, 然后重命名该目录下的
  文件libstdc++.so.6为libstdc++.so.6.old, 问题解决. 此问题会出现在15.04或更高版本的Ubuntu系统上, 比如我就是从14.10升级到15.04后
  就出现这个问题.
19）



