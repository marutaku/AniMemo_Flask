from lib.database.AbstractDB import AbstractDB


class Works(AbstractDB):
    def __init__(self):
        super(Works, self).__init__()

    def get_works(self):
        sql = 'SELECT * FROM works'
        return self._request(sql)

    def get_works_by_title(self, title):
        sql = 'SELECT * FROM works WHERE title like %"{title}"%'.format(title=title)
        return self._request(sql)

    def get_works_by_year(self, year):
        sql = 'SELECT * FROM works WHERE year = {year}'.format(year=year)
        return self._request(sql)

    def get_works_by_cours(self, cours):
        sql = 'SELECT * FROM works WHERE cours = {cours}'.format(cours=cours)
        return self._request(sql)

    def get_works_by_title_and_year(self, title, year):
        sql = 'SELECT * FROM works WHERE like %"{title}"% AND year = {year}'.format(title=title, year=year)
        return self._request(sql)

    def get_works_by_title_and_cours(self, title, cours):
        sql = 'SELECT * FROM works WHERE like %"{title}"% AND cours = {cours}'.format(title=title, cours=cours)
        return self._request(sql)

    def get_works_by_year_and_cours(self, year, cours):
        sql = 'SELECT * FROM works WHERE year = {year} AND cours = {cours}'.format(year=year, cours=cours)
        return self._request(sql)

    def get_works_by_title_and_year_and_cours(self, title, year, cours):
        sql = 'SELECT * FROM works WHERE like %"{title}"% AND year = {year} AND cours = {cours}'.format(title=title, year=year, cours=cours)
        return self._request(sql)

    def insert_work(self, title, image_path, title_short1, title_short2, title_short3, year, cours, public_url,
                    twitter_account, twitter_hash_tag):
        sql = 'INSERT INTO works(title, image_path, title_short1, title_short2, title_short3, year, cours, public_url, twitter_account, twitter_hash_tag) VALUES("{title}", "{image_path}", "{title_short1}", "{title_short2}", "{title_short3}", {year}, {cours}, "{public_url}", "{twitter_account}", "{twitter_hash_tag}")'.format(
            title=title,
            image_path=image_path,
            title_short1=title_short1,
            title_short2=title_short2,
            title_short3=title_short3,
            year=year,
            cours=cours,
            public_url=public_url,
            twitter_account=twitter_account,
            twitter_hash_tag=twitter_hash_tag)
        return self._request(sql)
