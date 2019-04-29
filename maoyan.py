'''
@author maqiuping
maoyan.com
'''
import requests
from requests.exceptions import RequestException
from bs4 import BeautifulSoup


headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
}
def get_one_page(url):
    try:
        response = requests.get(url,headers=headers)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None


def parser_one_page(html):
    doc = BeautifulSoup(html, 'lxml')
    dd_list = doc.find_all('dd')
    with open('movie.txt','a') as f:
        for item in dd_list:
            for i in item.find_all(class_="board-img"):
                f.write(i['alt'])
            for i in item.find_all(class_="star"):
                f.write(i.string+'\n')





def main():
    for i in range(10):
        if i ==0:
            url = 'https://maoyan.com/board/4'
        else:
            url = 'https://maoyan.com/board/4?offset='+str(i*10)
        html = get_one_page(url)
        parser_one_page(html)


if __name__ == "__main__":
    main()

