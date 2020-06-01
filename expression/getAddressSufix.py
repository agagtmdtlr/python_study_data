import re
# 주소지 정보에서 마지막 번지와 관련된
# 정보를 추출해 보기로 합니다.
# 힌트) 외따옴표를 표현하려면 \'를 사용하면 됩니다.

mylist = ["('강원원주시웅비2길8');",
"('강원도철원군서면와수로181번길7-16');",
"('강원평창군봉평면태기로68');",
"('강원강릉시강변로410번길36');"]
regex ='\d+[번길]*\d+-?\d*'
pattern = re.compile(regex)
for address in mylist:
    result = pattern.search(address)
    print(result.group())