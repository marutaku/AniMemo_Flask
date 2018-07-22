from bs4 import BeautifulSoup
from lib.database.Works import Works
from lib.api.ShangriLa import ShangriLa
from lib.models.Utils import Utils
import requests



class WorkModel():
    work_db = Works()
    shangrila_api = ShangriLa()

    def store_works(self, year):
        for cours in [1, 2, 3, 4]:
            works = self.shangrila_api.get_by_year_and_cours(year, cours)
            for work in works:
                # get image_path by public_url
                soup = BeautifulSoup(requests.get(work['public_url']).content,'html.parser')
                link = soup.find("img")
                image = None
                if link.get("src").endswith(".jpg"):
                    image = link.get("src")
                elif link.get("src").endswith(".png"):
                    image = link.get("src")
                image_path = work['image_path'] + image
                self.work_db.insert_work(work['title'], image_path, work['title_short1'], work['title_short2'], work['title_short3'], work['year'], work['cours_id'], work['public_url'], work['twitter_account'], work['twitter_hash_tag'])
        return True
