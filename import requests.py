import requests
from bs4 import BeautifulSoup
ur1 =""
response = requests.get(ur1)
if response.status_code == 200:
    soup = BeautifulSoup(reseponse.text,'')#''解析网页内容
    title = soup.title.string#网页标题
    print('网页标题；',title)
    linke = soup.find_all('a')
    for link in linke:
        print('连接：'，link.get('href'))
              else:
              print('请求失败，状态码：'，response.sttus_code)
                    
