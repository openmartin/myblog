# 树莓派3第一次开机过程
最近买了一个raspberry Pi 3，打算用来做一个科学上网的路由器，第一篇记录一下第一次点亮的过程。
[官方视频](https://www.raspberrypi.org/help/noobs-setup/)记录了整个过程，照着视频一点一点的做就可以，基本没有难度，动作快的话一个小时就可以搞定。
## 下载NOOBS
NOOBS 表示 noob(小白，等于newbie) system，新手选择这个最方便，下载包含Raspbian 镜像包的，1G左右。
https://www.raspberrypi.org/downloads/noobs/
## 格式化SD Card
有很多格式化SD Card的工具，不过官网上推荐的SD Formatter 4.0下载不了，在Mac系统下可以使用磁盘工具来格式化，
记住选择FAT（不要选择exFAT，启动不了），还有可启动的主分区，
## 解压NOOBS_v1_9_2.zip
把NOOBS_v1_9_2目录下的文件直接拖到SD Card 的根分区，不包含NOOBS_v1_9_2目录
## 开机
第一次开机需要显示器，键盘和鼠标，我看网上还有其他方法，貌似很高深，都看不懂。
开机装完系统之后就不需要显示器，键鼠了，但是第一次开机时一定需要，显示器需要支持HDMI口，树莓派并没VGA口，如果显示器是VGA口的，可以买一个HDMI转VGA的转接头。
整个过程有点像ubuntu 的LiveCD，详细可以去看官方的视频。
## 修改apt-get source
启动系统之后，我们进入了Raspbian系统，就是一个Debian系统，所有的配置和Ubuntu很像，在搜索一些资料的时候可以直接用Debian或Ubuntu关键词来搜索。
连接树莓派官方的源比较慢，我们可以改成国内的镜像源。
```shell
# /etc/apt.d/source.list
deb http://mirrors.ustc.edu.cn/raspbian/raspbian/ jessie main non-free contrib
deb-src http://mirrors.ustc.edu.cn/raspbian/raspbian/ jessie main non-free contrib
```
## rasp-config
可以修改配置，启动的时候不启动图形界面。
出于安全考虑，可以修改默认的用户名密码(pi:raspberry)

参考：
1. https://www.raspberrypi.org/help/noobs-setup/
2. https://lug.ustc.edu.cn/wiki/mirrors/help/raspbian
