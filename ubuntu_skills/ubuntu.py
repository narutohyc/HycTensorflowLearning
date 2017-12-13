1)
查看本機安裝軟件（管道過濾）： 
ubuntu@ubuntu:~$ dpkg --list | grep xrd
ii  xrdp                                       0.6.1-2                                      amd64        Remote Desktop Protocol (RDP) server
卸載安裝軟件：
sudo apt-get --purge remove xrdp

2)
ubuntu好看主題安裝及使用：
安裝：
sudo apt-get install unity-tweak-tool
打開：
unity-tweak-tool

3)
ubuntu下配置路徑文件：
~/.bashrc
source ~/.bashrc  #生效
或
/etc/profile
source /etc/profile  #生效

4）
ubuntu backup
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

6）









