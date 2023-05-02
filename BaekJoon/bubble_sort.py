# def bubblesort(data):

#     for index in range(len(data)-1):
#         swap=False
#         for index2 in range(len(data)-index-1):
#             if data[index2]>data[index2+1]:
#                 data[index2],data[index2+1] = data[index2+1],data[index2]
#                 swap=True
#         if swap == False:
#             break
    
#     return data

# import random

# a = random.sample(range(100),10)

# print(bubblesort(a))

def bubblesort(data):

    for index in range(len(data)-1):
        swap=False
        for index2 in range(len(data)-index-1):
            if data[index2]>data[index2+1]:
                swap=True
                data[index2],data[index2+1] = data[index2+1],data[index2]
        if swap ==False:
            break
    return data

import random

a = random.sample(range(100),10)
print(bubblesort(a))       