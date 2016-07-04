# 树莓派使用VPN科学上网
我们已经可以把树莓派当做无线路由器来上网，现在我们进行下一阶段的工作。如何科学上网，让连接wifi的所有设备都可以科学上网。
##  网段
tplink wan 192.168.1.2 网关 192.168.1.1 连接光猫，自动获取IP
tplink lan 192.168.0.1
tplink lan dhcp 192.168.0.100~192.168.0.199/255.255.255.0
raspberrypi eth0 192.168.0.101
raspberrypi wlan0 172.24.1.1
raspberrypi wlan0 dhcp 172.24.1.50~172.24.1.150 /255.255.255.0

## 设想
我现在手头上有个VPN，但是连接VPN之后所有的流量都会走VPN导致所有的访问国内网站很慢。所以需要通过路由配置，使国内网站走eth0，不走VPN
## VPN
我购买的是GreenVPN，使用下面的命令配置VPN
```
sudo pptpsetup --create GreenVPN --server jp.greenmobi.net --username xxx --password xxx --encrypt --start
```
启动VPN`sudo pon GreenVPN`，停止`sudo poff GreenVPN`
## freedom-routes
https://github.com/sabersalv/freedom-routes
https://github.com/cqjjjzr/freedom-routes
下载linux.tar.gz，把脚本拷贝到对应的位置，会在VPN连接之前自动添加路由记录，VPN停止的时候自动删除路由记录。
```
sudo cp routes-up.sh /etc/ppp/ip-pre-up
sudo cp routes-down.sh /etc/ppp/ip-down.d/ip-down
```
把VPN重新连接一下，现在可以在树莓派上测试一下是否可以科学上网`w3m www.twitter.com`，`w3m www.baidu.com`。

## ChinaDNS
https://github.com/shadowsocks/ChinaDNS
在某些情况下DNS解析域名会失败，或者解析到不正确的地址上，我们使用ChinaDNS解决掉这个问题。
```
sudo service avahi-daemon stop # 这个服务会占用5353端口，先停止
sudo nohup /home/pi/proxx_env/chinadns-1.3.2/src/chinadns -m -c /home/pi/proxx_env/chinadns-1.3.2/chnroute.txt -b 127.0.0.1 -p 5353 > /dev/null 2>&1 &
```
把dnsmasq 的上级设置为chinaDNS 修改`/etc/dnsmasq.conf`，`server=127.0.0.1#5353`
## iptables
我们在树莓派上可以科学上网，但是连接wifi的设备还是不可以科学上网，这时候我们需要增加nat的配置。
```
sudo iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE  
sudo iptables -A FORWARD -i eth0 -o wlan0 -m state --state RELATED,ESTABLISHED -j ACCEPT  
sudo iptables -A FORWARD -i wlan0 -o eth0 -j ACCEPT
# 上面是我们已经添加过的
sudo iptables -t nat -A POSTROUTING -o ppp0 -j MASQUERADE  
sudo iptables -A FORWARD -i ppp0 -o wlan0 -m state --state RELATED,ESTABLISHED -j ACCEPT  
sudo iptables -A FORWARD -i wlan0 -o ppp0 -j ACCEPT  
```
## ssh
因为GreenVPN服务商禁掉了ssh，所以无法ssh国外的服务器，我们只能手工添加路由，走eth0
```
sudo ip route add 52.91.123.123 via 192.168.0.1
```

## VPN断线自动重连
VPN有时候会断线，我们写一个小脚本让VPN断线之后重新连接
vpn_auto_connect.sh
```shell
#!/bin/sh
VPN=`ifconfig | grep ppp0`
echo $VPN
if [ -z "$VPN" ]
then
sudo pon GreenVPN
fi
```
设置定时任务，每五分钟执行一次，如果发现VPN断了，就会重新连接。`sudo crontab -e`
```crontab
SHELL=/bin/bash
PATH=/sbin:/bin:/usr/sbin:/usr/bin
MAILTO=pi

*/5 * * * * /home/pi/proxx_env/vpn_auto.sh
```

