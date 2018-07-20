from lib.database.AbstractDB import AbstractDB


class User(AbstractDB):
    def __init__(self):
        super(User, self).__init__()

    def get_user(self, user_name):
        sql = 'SELECT * FROM users WHERE name="{name}"'.format(name=user_name)
        return self._request(sql)

    def insert_user(self, name, email, password, image_path=None):
        sql = 'INSERT INTO users(name, password, email, image_path) VALUES("{name}", "{password}", "{email}", "{image_path}")'.format(name=name,
                                                                                                              password=password,
                                                                                                              email=email,
                                                                                                              image_path=image_path)
        return self._request(sql)

    def get_user_status(self, user_id):
        sql = 'SELECT * FROM users WHERE id = {id}'.format(id=user_id)
        return self._request(sql)