from konlpy.tag import Okt

# 사용자 정의 사전(user_dict.txt)
# 싸이월드 NNP ... 사전 만들고
# userdic 이라는 매개 변수를 이용하면 된다.


okt = Okt()
print(type(okt))
text = '명사만을 추출하여 워드 클라우드를 그려 봅니다.'

# 명사
result = okt.nouns(text)
print(result)
print(type(result))

# tuple( 단어 , 품사 )
result = okt.pos(text)
print(result)
print(type(result))

# 단어
result = okt.morphs(text)
print(result)
print(type(result))