mylist = [('sale 무료 배송 할인', '스팸'),
          ('일정 변경', '일반'),
          ('세일 변경', '일반')]

# 단어를 저장할 집합
words = set()
# 카테고리별 각 단어들의 빈도수를 저장할 중첩 사전
word_dict = {}
# 카테고리별 빈도수 저장할 사전
category_dict = {}


for i in [x[0] for x in mylist ]:
    for j in i.split(' '):
        words.add(j)
print(words)
for i in [x[1] for x in mylist ]:
    if i in category_dict:
        category_dict[i] = category_dict[i]+1
    else:
        category_dict[i] = 1
print(category_dict)

for word,category in mylist:
    if category not in word_dict:
        word_dict[category] = dict()
    for x in word.split():
        temp = word_dict[category]
        if x in temp:
            word_dict[category][x] = word_dict[category][x] + 1
        else:
            word_dict[category][x] = 1
print(word_dict)