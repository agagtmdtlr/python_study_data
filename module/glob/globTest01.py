import glob
import os
mydir = 'c:\\windows'
print(os.curdir) # current directory : .
print(os.getcwd())
os.chdir(mydir) # 경로를 바꾸어 준다.
print(os.curdir)
print(os.getcwd())

findfile = '*[0-9].*' #파일명이 숫자로 끝나는 파일들
print(glob.glob(findfile))

findfile = '*.exe' # 확장자 exe 파일들
print(glob.glob(findfile))

findfile = '?i*.*' # 두번째 글자가 i인 파일들
print(glob.glob(findfile))