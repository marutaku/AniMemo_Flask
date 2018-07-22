from lib.database.AbstractDB import AbstractDB

class Works(AbstractDB):
    def __init__(self):
        super(Works, self).__init__()

    def get_works_by_id(self, works_id):
        sql = 'SELECT * FROM works WHERE id = {id}'.format(id=works_id)
        return self._request(sql)

    def insert_work(self, title, image_path, title_short1, title_short2, title_short3, year, cours, public_url, twitter_account, twitter_hash_tag):
        sql = 'INSERT INTO works(title, image_path, title_short1, title_short2, title_short3, year, cours, public_url, twitter_account, twitter_hash_tag) VALUES("{title}", "{image_path}", "{title_short1}", "{title_short2}", "{title_short3}", {year}, {cours}, "{public_url}", "{twitter_account}", "{twitter_hash_tag}")'.format(title=title,
                                                                                                              image_path=image_path,
                                                                                                              title_short1=title_short1,
                                                                                                              title_short2=title_short2,
                                                                                                              title_short3=title_short3,
                                                                                                              year=year,
                                                                                                              cours=cours,
                                                                                                              puclic_url=puclic_url,
                                                                                                              twitter_account=twitter_account,
                                                                                                              twitter_hash_tag=twitter_hash_tag)
        return self._request(sql)

