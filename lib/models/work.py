from bs4 import BeautifulSoup
from lib.database.Works import Works
from lib.database.Reviews import Review
from lib.api.ShangriLa import ShangriLa
from lib.models.Utils import Utils
import requests
from time import sleep


class WorkModel():
    work_db = Works()
    review_db = Review()
    shangrila_api = ShangriLa()
    
    def is_stored(self, year):
        print('he')
        if self.work_db.count_works_by_year(year)[0]['count(*)'] == "0":
        # if self.work_db.count_works_by_year(year)[0]['count(*)'] == 0:
            self.store_works(year)
        else:
            print('hello')
            print(self.work_db.count_works_by_year(year)[0])
            print(self.work_db.count_works_by_year(year)[0]['count(*)'])
            print('hello')


    def store_works(self, year):
        for cours in [1, 2, 3, 4]:
            works = self.shangrila_api.get_by_year_and_cours(year, cours)
            for work in works:
                # get image_path by public_url
                soup = BeautifulSoup(requests.get(work['public_url']).content, 'html.parser')
                link = soup.find("img")
                image = None
                if link:
                    if link.get("src").endswith(".jpg"):
                        image = link.get("src")
                    elif link.get("src").endswith(".png"):
                        image = link.get("src")

                if image:
                    image_path = work['public_url'] + image
                else:
                    image_path = None
                self.work_db.insert_work(work['title'], image_path, work['title_short1'], work['title_short2'],
                                         work['title_short3'], year, cours, work['public_url'],
                                         work['twitter_account'], work['twitter_hash_tag'])
                sleep(1)
        return True

    def get_works(self, title, year, cours):
        if (title is None and year is None and cours is None) or (title == "" and year == "" and cours == ""):
            return self.work_db.get_works()
        if title != "" and year != "" and cours != "":
            return self.work_db.get_works_by_title_and_year_and_cours(title, year, cours)
        if title != "" and year != "":
            return self.work_db.get_works_by_title_and_year(title, year)
        if title != "" and cours != "":
            return self.work_db.get_works_by_title_and_cours(title, cours)
        if year != "" and cours != "":
            return self.work_db.get_works_by_year_and_cours(year, cours)
        if title != "":
            return self.work_db.get_works_by_title(title)
        if year != "":
            return self.work_db.get_works_by_year(year)
        if cours != "":
            return self.work_db.get_works_by_cours(cours)
    
    def show_work(self, id):
        return self.work_db.get_work_by_id(id)

    def post_review(self, user_id, work_id, text):
        self.review_db.insert_review(user_id, work_id, text)

    def get_reviews_by_work(self, work_id):
        return self.review_db.get_review_by_work_id(work_id)
    # user_id版もここに書く？

