mylist = [('sale 무료 배송 할인', '스팸'),
          ('일정 변경', '일반'),
          ('세일 변경', '일반')]

# 단어를 저장할 집합
words = set()
# 카테고리별 각 단어들의 빈도수를 저장할 중첩 사전
word_dict = {}
# 카테고리별 빈도수 저장할 사전
category_dict = {}

words = {j for i in mylist for j in i}
print(words)
words = {k for i in mylist for j in i for k in j.split()}
print(words)
for i in mylist:
    for j in i:
        if word_dict.get(j) is not None:
            word_dict[j] = word_dict.get(j)+1
        else :
            word_dict[j] = 1
print(word_dict)
word_dict = {}
for i in mylist:
    for j in i:
        for k in j.split():
            if word_dict.get(k) is not None:
                word_dict[k] = word_dict.get(k)+1
            else :
                word_dict[k] = 1
print(word_dict)

