# 백준 1700. 멀티탭 스케줄링
# https://www.acmicpc.net/problem/1700
import sys
N, K = map(int, sys.stdin.readline().split())
devices = list(map(int, sys.stdin.readline().split()))
def sol(N, K, devices):
    multitap = []
    cnt = 0
    
    for i in range(K):
        current_device = devices[i]
        
        if current_device in multitap:
            continue
        
        if len(multitap) < N:
            multitap.append(current_device)
            continue
        
        not_used_in_future = -1
        far_index = -1
        
        for device in devices:
            # 미래에 다시 사용하지 않을 전기 용품
            if device not in devices[i + 1:]:
                not_used_in_future = device
                break
            # 미래에 다시 사용할 전기 용품
            else:
                index = devices[i + 1:].index(device)
                if index > far_index:
                    far_index = index
                    not_used_in_future = device
        multitap.remove(not_used_in_future)
        cnt += 1
        multitap.append(current_device)
    return cnt
print(sol(N=N, K=K, devices=devices))

        
                
        