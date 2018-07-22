from bs4 import BeautifulSoup
from lib.database.Works import Works
from lib.api.ShangriLa import ShangriLa
from lib.models.Utils import Utils
import requests
from time import sleep



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
                if link:
                    if link.get("src").endswith(".jpg"):
                        image = link.get("src")
                    elif link.get("src").endswith(".png"):
                        image = link.get("src")

                if image:
                    image_path = work['public_url'] + image
                else:
                    image_path = None
                self.work_db.insert_work(work['title'], image_path, work['title_short1'], work['title_short2'], work['title_short3'], year, work['cours_id'], work['public_url'], work['twitter_account'], work['twitter_hash_tag'])
                sleep(1)
        return True
