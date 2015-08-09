���������ѷec2�ϲ���djangoӦ��
=================================

�ܶ�ʱ�����ǻ��ڻ��������ϻ�������ʱ�䣬�����Ҽ�¼��һ�������õĹ��̣�ϣ���ܽ�ʡ���һЩ��ʱ�䡣


�ҵĻ�����amazon ec2��ѡ��Ĳ���ϵͳ��Amazon Linux AMI 2015.03 (HVM) ��ѡ�������Ĳ��𷽰� nginx + gunicorn + django + mysql

mysql
------------------

���Ȱ�װmysql-sever::

    $sudo yum install mysql-server mysql mysql-devel
    $sudo chown mysql.mysql -R /var/lib/mysql

�޸������ļ�/etc/my.cnf::

    [mysqld]
    datadir=/var/lib/mysql # �����ļ���ŵ�λ�ã��޸ĳ��ʺϵ�λ��
    ......
    port=3306
    character-set-server=utf8 #����Ĭ�ϱ���

    [client]
    default-character-set=utf8 #����Ĭ�ϱ���

����mysql::

    $sudo service mysqld start

����root���룬ִ��/usr/bin/mysql_secure_installation

�����Ҫͨ���ͻ��˹��߹���MySQL����Ҫ���Զ������MySQLȨ��::

    $mysql -u root -p

    mysql>GRANT ALL PRIVILEGES ON *.* TO root@"%" IDENTIFIED BY '<password>' WITH GRANT OPTION;
    mysql>FLUSH PRIVILEGES;

һ�㲻����root�û�����MySQL��������Ҫ���һ����ͨ�û�::

    create user 'blog'@'localhost' identified by '<password>';
    flush privileges;
    grant all privileges on blog.* to blog@localhost identified  by '<password>';


����python����
------------------

��Ŀǰ��python�汾��2.7.9�����Բ���Ҫ��װpip

pip
^^^^^^^^^^^^^^^^^^

���Python�汾��2.7.9������3.4 ���ϣ�pipĬ�ϰ�����Python�İ�װ����

��ô��װpip���ο����� https://pip.pypa.io/en/latest/installing.html

virtualenv
^^^^^^^^^^^^^^^^^^

virtualenv ���ڴ���������Python���������Բ���ȫ�ֵ�site-packages���а�װ�İ���Ӱ�졣::

    pip install virtualenv
    # �������⻷��
    virtualenv ENV
    cd ENV
    source ./bin/activate

ĥ�����󿳲񹤣���������ʼ��չ��������

��װ�����python��
^^^^^^^^^^^^^^^^^^^^^^^^^^^

�����Ŀ����requirements.txt�ļ�����ֱ��ִ�У��Զ���װ����������ϵ��û�еĻ�����п��Դӿ�����������һ��::

    $pip freeze >> requirements.txt # �ڿ���������ִ��
    $pip install -r requirements.txt


�����������г�һЩ������Ҫ��������::

    $pip install gunicorn # gunicorn
    $pip install gevent   # ��gunicornʹ��gevent worker����߲�������
    $pip install django
    $pip install MySQL-python # ���Ҫ����mysql���ݿ⣬��Ҫ��װ
    $pip install Pillow   # ����Python Image Library


���ʹ��gunicron����djangoӦ�ã���ҪСС�޸�settings.pyһ�£�������INSTALLED_APPS��������gunicorn��

gunicron �����ű�::

    nohup gunicorn --worker-class=gevent myblog.wsgi:application --bind 127.0.0.1:8001 >gunicorn.log 2>&1 &

����Ĳ������֮�����ǵ�Ӧ�þͿ��������ˣ���������һ����gunicorn֮ǰʹ��ngnix����������������ô���һ�Ǿ�̬�ļ�����nginx�������Լ�����Ӧʱ�䣬�������һ���������ϲ�����վ�㣬������gunicorn�޷��ﵽĿ�ģ���ʱ������Ҫ��apache����nginx��������������ܡ�

nginx
------------------------------------

��ͬ��Linux���а��ϰ�װ�ķ����������ļ���λ�ÿ��ܲ�̫һ��������������������õ�˼·֮��Ϳ��Ծ�һ������::

    $sudo yum install nginx
    $sudo service start nginx

�༭ /etc/nginx/conf.d/virtual.conf::

    server {
        listen       80;

        server_name  blog.dailyastrology.info;

        access_log /var/log/nginx/blog.dailyastrology.info-access.log;
        error_log /var/log/nginx/blog.dailyastrology.info-error.log;

        location / {
            proxy_pass http://127.0.0.1:8001;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        }
        location /static {
            root /home/ec2-user/blogenv/myblog;
        }
    }

���������Ϊ���˵�վ�㣬����������Ӧ�þ͹��õģ��������Ҫ�߼��Ĺ��ܾ���Ҫ�Լ�ȥ�о�ÿ����������ú���ά������

