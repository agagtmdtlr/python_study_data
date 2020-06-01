import urllib.request
from selenium import webdriver
from bs4 import BeautifulSoup
import json

# driver = webdriver.Chrome('d:/chromedriver.exe')
url = 'http://webtoon.daum.net/data/gateway/comments/list/webtoon_ep/86079?page=%s&pageSize=5&isBest=true&sortType=Recommend'%(1)

# driver.get(url)
# page = driver.page_source
# print(type(page))
# print(page.read())
response = urllib.request.urlopen(url)
print(type(response))
# page = response.read()
# print('page : ',type(page))
soup = BeautifulSoup(response,'html.parser')
jsonObj = json.loads(str(soup))
print('jsonObj : ',type(jsonObj))
data = jsonObj['concat_data']['comments']
type(data)
for id in data:
    print(id['content'])

# {"result":{"status":"200","message":""},
#  "metaData":null,
#  "concat_data":
#      {"totalCommentCount":1482,
#       "totalPage":741,
#       "user":
#           {"daumName":"-",
#            "login":false},
#       "comments":
#           [{"commentId":19116908,
#             "parentCommentId":0,
#             "articleId":86079,
#             "articleType":"webtoon_ep",
#             "subject":"강호표사 예고",
#             "viewUrl":"http://webtoon.daum.net/webtoon/viewer/86079",
#             "encryptedUserId":"gbQqKHhQxW90",
#             "daumName":"악어고기",
#             "childCount":0,
#             "recommendCount":6,
#             "disagreeCount":1,
#             "status":"S",
#             "regDate":"2020-04-05 22:14:06",
#             "content":"ozi 님의 작품을  또 보다니 기대가 되네요!",
#             "spoiler":false,
#             "isWithdraw":false,
#             "isParent":true,
#             "isBest":false,
#             "isMine":false}

# http://webtoon.daum.net/data/gateway/comments/list/webtoon_ep/40160?page=2&pageSize=10&isBest=true&sortType=Recommend&1586165911706
# http://webtoon.daum.net/data/gateway/comments/list/webtoon_ep/86079?page=1&pageSize=2&isBest=true&sortType=Recommend&1586155683043