# def insertionsort(data):
#     for index in range(len(data)-1):
#         for index2 in range(index+1,0,-1):
#             if data[index2]<data[index2-1]:
#                 data[index2],data[index2-1] = data[index2-1],data[index2]
#             else:
#                 break
#     return data
    
# import random
# a = random.sample(range(100),10)
# print(insertionsort(a))

def insertion_sort(data):
    for index in range(len(data)-1):
        for index2 in range(index+1,0,-1):
            if data[index2]<data[index2-1]:
                data[index2],data[index2-1] = data[index2-1],data[index2]
            else:
                break
    return data
import random
a = random.sample(range(100),10)
print(insertion_sort(a))