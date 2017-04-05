#conding:utf8

import hashlib

#将url转换为md5节省存储空间
def url_to_md5(url):
    if isinstance(url,str):         #hashlib中update()不能接受uniocde，需转换为utf8
        url = url.encode('utf8')
    md5 = hashlib.md5()
    md5.update(url)
    return md5.hexdigest()