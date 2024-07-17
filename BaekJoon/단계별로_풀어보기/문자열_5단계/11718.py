import sys
s = sys.stdin.read()
print(s)


# sys.stdin.readline() : 문자열 형태로 개행문자(\n)를 포함한 한 줄만 입력된다.
# sys.stdin.readlines() : 파일의 끝까지 한 번에 읽어온다. 각 줄이 개행 문자(\n)가 포함되어 리스트로 저장된다.
# sys.stdin.read() : 파일의 끝까지 한 번에 읽어오고 읽은대로 출력된다.