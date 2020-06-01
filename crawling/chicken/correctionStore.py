# 'allstore.csv' 파일을 이용한 보정처리를 위한 파일
# 보정 처리 후에 'allStoreModified.csv' 파일로 저장하기

from pyy.crawling.chicken.chickenCorrection import Chickencorrection

filename = 'studydata/allstore.csv'
chknstore = Chickencorrection(filename)

print('finished')