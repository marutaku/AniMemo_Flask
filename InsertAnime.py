import requests, sys, ssl, urllib3
from time import sleep
from bs4 import BeautifulSoup
from lib.database.Works import Works
from lib.api.ShangriLa import ShangriLa

work_db = Works()
def main(years):
    shangrila_api = ShangriLa()
    for year in years:
        for cours in [1, 2, 3, 4]:
            print('=' * 30)
            print('Getting year: {}, cours: {}'.format(year, cours))
            works = shangrila_api.get_by_year_and_cours(year, cours)
            for work in works:
                try:
                    # get image_path by public_url
                    soup = BeautifulSoup(requests.get(work['public_url']).content, 'html.parser')
                    link = soup.find("img")
                    image = None
                    if link:
                        if link.get("src"):
                            if link.get("src").endswith(".jpg"):
                                image = link.get("src")
                            elif link.get("src").endswith(".png"):
                                image = link.get("src")
                    if image:
                        image_path = work['public_url'] + image
                    else:
                        image_path = '/static/white.png'
                    work_db.insert_work(work['title'], image_path, work['title_short1'], work['title_short2'],
                                             work['title_short3'], year, cours, work['public_url'],
                                             work['twitter_account'], work['twitter_hash_tag'])
                    sleep(1)
                except requests.exceptions.SSLError:
                    print('SSL error happen.  work: {}'.format(work))
                    continue
                except ssl.CertificateError:
                    print('SSL error happen.  work: {}'.format(work))
                    continue
                except urllib3.exceptions.MaxRetryError:
                    print('Over max retry count. work: {}'.format(work))
                    continue
                except requests.exceptions.ConnectionError:
                    continue
                except urllib3.exceptions.NewConnectionError:
                    continue
                except TimeoutError:
                    continue

if __name__ == '__main__':
    main(range(2014, 2019))

