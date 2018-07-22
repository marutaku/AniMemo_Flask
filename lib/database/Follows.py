from lib.database.AbstractDB import AbstractDB


class Follows(AbstractDB):
    def __init__(self):
        super(Follows, self).__init__()

    def insert_follows(self, from_id, to_id):
        sql = 'INSERT INTO follows(user_id, followed_user_id) VALUES({from_id}, {to_id})'.format(from_id=from_id,
                                                                                                 to_id=to_id)
        return self._request(sql)

    def get_all_followers(self, user_id):
        sql = 'SELECT * FROM follows WHERE user_id = {user_id}'.format(user_id=user_id)
        return self._request(sql)

    def delete_followers(self, user_id, followed_user_id):
        sql = 'DELETE FROM follows WHERE user_id = {user_id} AND followed_user_id = {followed_user_id}'.format(
            user_id=user_id, followed_user_id=followed_user_id)
        return self._request(sql)
