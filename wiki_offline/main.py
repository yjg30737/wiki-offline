import certifi
import urllib3
from bs4 import BeautifulSoup
import re, os

def convertWikiToText(url):
    m = re.search(r'\.wikipedia\.org', url)
    if m:
        http = urllib3.PoolManager(ca_certs=certifi.where())
        resp = http.request('GET', url)
        resp_data = resp.data.decode('utf-8')
        if resp.status == 200:
            soup = BeautifulSoup(resp_data, features='lxml')
            link_list = soup.findAll('link')
            for link in link_list:
                if link['rel'][0] == 'canonical':
                    pass
                    # print(link['href'])
            title = soup.find('title').text.split(' - ')[0]
            content_tag = soup.find(id='bodyContent')
            content = content_tag.text
            filename = title + '.txt'
            f = open(filename, 'w', encoding='utf-8')
            f.write(content)
            f.close()
            os.startfile(filename)
    else:
        raise Exception('This is not the right URL')
