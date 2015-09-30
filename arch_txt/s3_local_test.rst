s3 本地测试环境的搭建
============

s3 ninja
--------
http://s3ninja.net/ s3 ninja 在本地模拟S3 API, 而且自带一个管理界面, 但是需要修改代码,把endpoint_url指定为 http://localhost:9444/s3

如果我们不想修改代码,可以通过一些简单的配置把请求导向本地 s3 ninja


s3 virtual hosted-style and path-style access
---------------------------------------------
访问s3 bucket上的文件,有两种方式.::

    # example bucket名字 johnsmith  文件 homepage.html

    # Path Style
    http://s3.amazonaws.com/johnsmith/homepage.html

    # Virtual Hosted–Style
    http://johnsmith.s3.amazonaws.com/homepage.html


更多信息参考
http://docs.aws.amazon.com/zh_cn/AmazonS3/latest/dev/UsingBucket.html#access-bucket-intro
http://docs.aws.amazon.com/zh_cn/AmazonS3/latest/dev/VirtualHosting.html

如何配置
----

我们要达到的目的如下

mybucket.s3.amazonaws.com -> localhost:9444:s3/mybucket

/etc/hosts
^^^^^^^^^^
添加一行::

    127.0.0.1 mybucket.s3.amazonaws.com

nginx
^^^^^


配置多个bucket
----------







1. nginx
2. s3 ninja
3. gas mask

