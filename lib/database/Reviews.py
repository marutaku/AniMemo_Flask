from lib.database.AbstractDB import AbstractDB


class Review(AbstractDB):
    def __init__(self):
        super(Review, self).__init__()

    def get_review_by_work_id(self, work_id):
        sql = 'SELECT * FROM reviews WHERE work_id={work_id} ORDER BY id DESC'.format(work_id=work_id)
        return self._request(sql)

    def get_review_by_user_id(self, user_id):
        sql = 'SELECT * FROM reviews INNER JOIN works on works.id = reviews.work_id WHERE user_id={user_id} ORDER BY reviews.id DESC'.format(
            user_id=user_id)
        return self._request(sql)

    def insert_review(self, user_id, work_id, text):
        sql = 'INSERT INTO reviews(user_id, work_id, text) VALUES({user_id}, {work_id}, "{text}")'.format(user_id=user_id,
                                                                                                              work_id=work_id,
                                                                                                              text=text)
        return self._request(sql)
