from lib.database.AbstractDB import AbstractDB


class Status(AbstractDB):
    def __init__(self):
        super(Status, self).__init__()

    def insert_status(self, state, user_id, word_id):
        sql = 'INSERT INTO states(state, user_id. work_id) VALUES ({state}, {user_id}, {work_id})'.format(state=state,
                                                                                                          user_id=user_id,
                                                                                                          word_id=word_id)
        return self._request(sql)

    def get_all_status(self, user_id):
        sql = 'SELECT * FROM states WHERE user_id = {user_id}'.format(user_id=user_id)
        return self._request(sql)
