small tips
==========

����Ĺ���������һЩ���⣬��¼��������ϣ���������˲�Ҫ�ٲȿ��ˡ�

all()
-----

all()��python��һ�����ú������ٷ��ĵ�����˵������е�Ԫ�ض�ΪTrue��all()�ŷ���True��::

    def all(iterable):
        for element in iterable:
            if not element:
                return False
        return True


��һЩ�����Ҫע�⣬��listΪ��ʱ������True�����ַ�����None��0 �Ľ������False��::

    >>> all([])
    True
    >>> all(['a', 'b', 'c'])
    True
    >>> all(['a', 'b', ''])
    False
    >>> all(['a', 'b', None])
    False
    >>> all(['a', 'b', 0])
    False


ע����������ĵ�����
----------

��windows�ϰ�װpython package����ʱ��������� UnicodeDecodeError����::

    mimetypes.init() # try to read system mime.types
    File "C:\Python27\lib\mimetypes.py", line 358, in init
    db.read_windows_registry()
    File "C:\Python27\lib\mimetypes.py", line 258, in read_windows_registry
    for subkeyname in enum_types(hkcr):
    File "C:\Python27\lib\mimetypes.py", line 249, in enum_types
    ctype = ctype.encode(default_encoding) # omit in 3.x!
    UnicodeDecodeError: 'ascii' codec can't decode byte 0x88 in position 1: ordinal not in range(128)


������Ϊpython��ע�����HKEY_CLASSES_ROOT��ȡmimetypeʱ���а������ĵ��ļ�����׺��һ�㶼�ǰ���Ͱ͵ġ�::

    HKEY_CLASSES_ROOT\.�����������յĿ����ļ�


������ɾ���˾Ͳ����ٳ���UnicodeDecodeError��������Python 2.7.7���Ժ�İ汾�޸���������⡣


python setup.py develop
-----------------------

developģʽ������������install�������������site-packages�ļ����н���һ��.egg-link�ļ��������ڲ���ϵͳ��������
������Ϳ�������༭��Ĵ��룬������Ҫÿ�β��Ե�ʱ��reinstallһ�顣��Ȼ��ĳ���Ҫ��python������������֯���й���


������Ϣ���ο��ĵ� http://pythonhosted.org//setuptools/setuptools.html#development-mode




json ��ʽ�е������ǲ��Ϸ���
----------------

��json��ʽ�е������ǲ��Ϸ����ַ���������replace('\'', '\"')�滻����::

    >>> json.loads("['a', 'b', 'c']")
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "D:\Python27\lib\json\__init__.py", line 338, in loads
        return _default_decoder.decode(s)
      File "D:\Python27\lib\json\decoder.py", line 365, in decode
        obj, end = self.raw_decode(s, idx=_w(s, 0).end())
      File "D:\Python27\lib\json\decoder.py", line 383, in raw_decode
        raise ValueError("No JSON object could be decoded")
    ValueError: No JSON object could be decoded


redis.Redis �� redis.StrictRedis zadd�Ĳ���˳��һ����
---------------------------------------------

redis.Redis.zadd(name, *args, **kwargs)  value��ǰ�������ں�

*args, ��: name1, score1, name2, score2, ... ������ **kwargs, ��: name1=score1, name2=score2


redis.StrictRedis.zadd(name, *args, **kwargs) ������ǰ��value�ں�

*args, ��: score1, name1, score2, name2, ... ������ **kwargs, ��: name1=score1, name2=score2,
