import sys

print('글자를 많이 입력하세요')
inputData = sys.stdin.readline()
print(inputData)

print('입력하시면 5글자만 챙길게요')
inputData = sys.stdin.readline(5)
print(inputData)

# sys.exit() # 작업을 끝낼때

sys.stdout.write('호호호')

print('-'*20)
print(sys.version)

print('-'*20)
print(sys.path)