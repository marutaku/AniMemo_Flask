
class AbstractDB(object):
    def __init__(self, connection):
        self.connection = connection

    def execute_sql(self, sql, context=None):
        """
        SQLの実行
        :param sql text:
        :param context  tuple:
        :return:
        """

        # Check context is tuple
        if context and isinstance(context, tuple):
            pass
        elif context and isinstance(context, list):
            context = tuple(context)
        elif context:
            return TypeError('Unexpected type object is passed')

        with self.connection.cursor() as cursor:
            cursor.execute(sql, context)
            return cursor.fetchall()


