import math
import sys

from bs4 import BeautifulSoup
from konlpy.tag import Komoran

max_score = - sys.maxsize
print(max_score)
# print(math.log(1))
# print(math.log(0.00000001))
text = open('data/mydict.dict', 'rt', encoding='utf-8')
komo = Komoran(userdic='concat_data/mydict.dict')
text = '세일즈 우먼 대한민국 만세 박승식'
result = komo.pos(text)
print(result)

class BayesianFilter:
    def __init__(self):
        # 형태소 단어들을 저장할 집합
        self.words = set() # 형태소 단어들을 저장할 집합
        self.word_dict = dict() # 카테고리별 각각의 단어를 저장하고 있는 중첩 사전
        self.category_dict = dict() # 카테고리별 빈도 수 를 저장하고 있는 사진

    # 예측
    def predict(self,email):
        # email : 점검을 하기 위한 신규 이메일 제목
        best_category = None # 일반인지 스팸인지 모름

        score_list = [] # 점수 정보를 저장하고 있는 리스트
        max_score = -sys.maxsize
        words = self.bayes_split(email)

        for category in self.category_dict.keys():

            score = self.score(words, category)
            score_list.append(score)
            if score > max_score :
                max_score = score
                best_category = category

        return str(best_category),score_list

    # 확률 계산산
    def score(self,words,category):
        # 예시 : words(['무료','배송']), category('광고')
        # 점수(확률) = (1) + (2)
        # (1) : 전체 카테고리에 대한 해당 카테고리의 비율 category_dict 사용
        score = math.log(self.category_prob(category))

        # (2) : 해당 카테고리 내에서 words 각각의 단어들에 대한 비율
        for word in words:
            print(word)
            score += math.log(self.word_prob(word, category))

        return score

    def category_prob(self,category):
        sum_cate = sum(self.category_dict.values())
        cate_value = self.category_dict[category]
        result = cate_value/sum_cate
        return result

    def word_prob(self, word, category):
        bunja = 0
        if word in self.word_dict[category]:
            bunja = self.word_dict[category][word]+1
        else: # 해당 단어가 없는 경우 입니다.
            # 없는 경우에는 확률이 0이 되므로 의도적으로 +1을 수행합니다.
            bunja = 1
        bunmo = sum(self.word_dict[category].values()) # 가중치
        bunmo += len(self.words)
        # print(bunja,bunmo,word)
        return bunja/bunmo

    def bayes_split(self,text):
        # 형태소 분석을 한 결과를 리스트로 반환해주는 함수입니다.
        results = []
        result =komo.pos(text)
        # print(result)
        for word in result:
            # 'NNP','SL','NNG'인 항목들만 추려 내기
            if word[1] in ['NNP','SL','NNG']:
                results.append(word[0])
        return results
    def fit(self,oneline):
        mydata = oneline.split(',')
        text = mydata[0]
        category = mydata[1]
        # print('제목 : ' + text)
        # print('카테고리 : '+category)
        # print('-'*20)
        word_list = self.bayes_split(text)
        # print(word_list)

        # 카테고리
        if not category in self.category_dict:
            self.category_dict[category] = 0
        self.category_dict[category] += 1
        # print(self.category_dict)

        # word_dict 살펴 보기
        if not category in self.word_dict:
            self.word_dict[category] = dict()
        # print(self.word_dict)

        # 단어를 해당 카테고리에 추가히기
        for word in word_list:
            if not word in self.word_dict[category]:
                self.word_dict[category][word] = 0
            self.word_dict[category][word] += 1
            # print(self.word_dict)
            # 각 형태소들을 워드집합에 추가하기
            self.words.add(word)
        # print(self.words)
# end class

komo = Komoran(userdic='concat_data/mydict.txt')
bf = BayesianFilter()
train_file = 'data/bayes_train.txt'
mytrain = open(train_file,'rt',encoding='utf-8')
train_list = [one.strip() for one in mytrain.readlines()]

# 메일 1개씩 fit() 함수에 추가하기
for oneline in train_list:
    bf.fit(oneline)

# 샘플 데이터에 대한 예측
test_file = 'data/bayes_test.txt'
mytest = open(test_file,'rt',encoding='utf-8')
test_list = [one.strip() for one in mytest.readlines()]
print(test_list)

for onemail in test_list :
    # predict : 예측 값, scorelist : log(확률 값) 예측 점수
    predict, scorelist = bf.predict(onemail)
    message = f'\n메일 제목이 [{onemail}]인 메일은 [{predict}] 메일 입니다.'
    print(message)
    print(scorelist)
    print('-'*20)
