# 성적이 낮은 순서로 학생 출력하기
import sys
N = int(sys.stdin.readline().strip())
students = [list(sys.stdin.readline().split()) for _ in range(N)]
students.sort(key=lambda x:(int(x[1])))
print(*[student[0] for student in students])