from konlpy.tag import Okt
import time
okt = Okt()
print(type(okt))

text = '세일즈우먼인아름다운그녀가아버지가방에들어가시나욬ㅎㅎ'

# result = okt.pos(text,norm=True, stem=True) # 원형 :('아름답다', 'Adjective')
# print(result)
# print('-'*50)
#
# result = okt.pos(text,norm=True, stem=False) # ('아름다운', 'Adjective')
# print(result)
# print('-'*50)
#
# result = okt.pos(text,norm=False, stem=True) # 정규화
# print(result)
# print('-'*50)
#
# result = okt.pos(text,norm=False, stem=False)
# print(result)
# print('-'*50)

# print('전체 확인 하기')
# for myitem in result :
#     somedata = '단어 : %s, 품사 : %s' %(myitem[0],myitem[1])
#     print(somedata)
#
# print('KoreanParticle , Noun 확인 하기')
# for myitem in result :
#     if myitem[1] in ('KoreanParticle','Noun') :
#         if len(myitem[0]) >= 2:
#             somedata = '단어 : %s, 품사 : %s' %(myitem[0],myitem[1])
#             print(somedata)
#         else :
#             print(f'"{myitem[0]}"는 한 글자라서 제외합니다.')

print('명사만 추출하기')
time_s = time.time()
print(time_s)
nouns = okt.nouns(text)
time_e = time.time()
print(time_e)
print(nouns)
print('-'*40)