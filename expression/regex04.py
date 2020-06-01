import re

# raw String 규칙
regex = '\\\\hello' # escape sequence : \\hello 문자를 찾아라
regex = r'\\hello'

mystr= '\\hello how \\world'
regex = '\\\\[a-z]+'

pattern = re.compile(regex)
mymatch = pattern.findall(mystr)
print(mymatch)

print('# raw string 규칙')
regex = r'\\[a-z]+'

pattern = re.compile(regex)
mymatch = pattern.findall(mystr)
print(mymatch)