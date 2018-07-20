import hashlib

class Utils(object):
    @staticmethod
    def hash_password(password):
        md5 = hashlib.md5()
        md5.update(password.encode('utf-8'))
        return md5.hexdigest()

