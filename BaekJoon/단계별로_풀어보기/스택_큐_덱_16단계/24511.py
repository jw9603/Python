'''
한가롭게 방학에 놀고 있던 도현이는 갑자기 재밌는 자료구조를 생각해냈다. 그 자료구조의 이름은 queuestack이다.

queuestack의 구조는 다음과 같다. 
$1$번, 
$2$번, ... , 
$N$번의 자료구조(queue 혹은 stack)가 나열되어있으며, 각각의 자료구조에는 한 개의 원소가 들어있다.

queuestack의 작동은 다음과 같다.

$x_0$을 입력받는다.
$x_0$을 
$1$번 자료구조에 삽입한 뒤 
$1$번 자료구조에서 원소를 pop한다. 그때 pop된 원소를 
$x_1$이라 한다.
$x_1$을 
$2$번 자료구조에 삽입한 뒤 
$2$번 자료구조에서 원소를 pop한다. 그때 pop된 원소를 
$x_2$이라 한다.
...
$x_{N-1}$을 
$N$번 자료구조에 삽입한 뒤 
$N$번 자료구조에서 원소를 pop한다. 그때 pop된 원소를 
$x_N$이라 한다.
$x_N$을 리턴한다.
도현이는 길이 
$M$의 수열 
$C$를 가져와서 수열의 원소를 앞에서부터 차례대로 queuestack에 삽입할 것이다. 이전에 삽입한 결과는 남아 있다. (예제 
$1$ 참고)

queuestack에 넣을 원소들이 주어졌을 때, 해당 원소를 넣은 리턴값을 출력하는 프로그램을 작성해보자.

'''
import sys
from collections import deque

N = int(sys.stdin.readline().strip())

list_a = list(map(int,sys.stdin.readline().split())) # 0 1 1 0, 0 : 큐, 1 : 스택
list_b = list(map(int,sys.stdin.readline().split())) # 1 2 3 4

M =int(sys.stdin.readline().strip())

list_c = list(map(int,sys.stdin.readline().split()))

res = deque()

for i in range(N):
    if list_a[i] == 0: # 큐
        res.appendleft(list_b[i])
        
for i in range(M):
    res.append(list_c[i])
    print(res.popleft(),end=' ')

