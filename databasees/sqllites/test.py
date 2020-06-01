import os
#경로 근간 이 되는 놈을 찾는다??
print(os.path.basename('wow/command/power')) # power
# 공통 경로 찾기
print(os.path.commonpath(['hello/wow/command/power','hello/wow/command/sold','hello/wow/damm'])) # hello\wow
# directory 뽑아내기
print(os.path.dirname('hello/wow/command/power.exe')) # hello/wow/command

print(os.path.commonpath(['hello/']))