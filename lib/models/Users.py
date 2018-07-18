

class User(object):
    def __init__(self, connection):
        self.connection = connection

    def get_user_by_id(self, id):
        sql = 'SELECT * FROM User WHERE id = %s'
        with self.connection.cursor() as cursor:
            pass

    def _execute_sql(self, sql):
        pass


