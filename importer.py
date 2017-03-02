import urllib2
from bs4 import BeautifulSoup
import bs4
from helper import parse_date
from model import Competitor


def import_results():
    url = "http://www.triathlon-service.de/ergebnisse/liste.php?nr=5680"
    webpage = urllib2.urlopen(url).read()
    soup = BeautifulSoup(webpage)
    for tr in soup.body.table.table:
        if tr.__class__ != bs4.element.NavigableString:
            tds = tr.find_all('td')
            if tds[3].text != 'Stnr.':
                competitor_data = {
                    'id': tds[3].text,
                    'name': tds[4].text,
                    'total': parse_date(tds[9].text),
                    'swimming': parse_date(tds[10].text),
                    'biking': parse_date(tds[11].text),
                    'running': parse_date(tds[13].text)
                }
                c = Competitor(competitor_data)
                c.save()
