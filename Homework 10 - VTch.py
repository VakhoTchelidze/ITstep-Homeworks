
#----------------1----------------

#1.	დაწერე ფუნქცია რომელიც შეადგენს შემთხვევით მთელ რიცხვთა სიას.

from random import randint

# #V1
# def list_generator(n, k):
#     from random import randint
#     arr = []
#     for _ in range(1, n):
#         arr.append(randint(1, k))
#     return arr

# new_list_2 = list_generator(100,1000)
# print(new_list_2)

# #V2
# new_list = [randint(1, 1000) for _ in range(1,101)]
#
# print(new_list)



#----------------2----------------

#2.	დაასორტირე შექმნილი სია რომელიმე ოპტიმალური მეთოდით.

#new_list = [randint(1, 1000) for _ in range(1,101)]

# def shell_sort(some_arr):
#     a = len(some_arr)
#     gap = a // 2
#     while gap > 0:
#         for i in range(gap, a):
#             anchor = some_arr[i]
#             j = i
#             while j >= gap and some_arr[j-gap] > anchor:
#                 some_arr[j] = some_arr[j-gap]
#                 j -= gap
#
#             some_arr[j] = anchor
#         gap //= 2
#
#     return some_arr
#
# new_list = shell_sort(new_list)
#
# print(new_list)


#----------------3----------------

#3.	დასორტირებულ სიაში ელემენტის მოსაძებნად გამოიყენე ხაზობრივი და ბინარული ძიება.

#new_list = [randint(1, 1000) for _ in range(1,101)]

# def search(arr, x):
#     for i in range(len(arr)):
#         if arr[i] == x:
#             return i
#     return -1
#
# print(search(new_list, 1))
#
# def binary_search(arr,low, high, x):
#     if high >= low:
#         mid = (high + low) // 2
#         if arr[mid] == x:
#             return mid
#
#         elif arr[mid] > x:
#             return binary_search(arr, low, mid-1, x)
#
#         else:
#             return binary_search(arr, mid+1, high, x)
#     else:
#         return -1
#
#
# print(binary_search(new_list,0,len(new_list)-1,1))


#----------------4----------------

#4.	დათვალე ძიების თითოეული მეთოდისთვის საჭირო დრო
# (დეკორატორის გამოყენებით) და დააკვირდი დროში სხვაობას მცირე, საშუალო და გრძელი სიის შემთხვევებში.

import time
import random

rand_list_small = [random.randint(1, 100) for _ in range(1000)]
rand_list_mid = [random.randint(1, 100) for _ in range(2000)]
rand_list_large = [random.randint(1, 100) for _ in range(3000)]

list_size = ['Small','Mid','Large']
list_of_lists = [rand_list_large, rand_list_mid, rand_list_small]

#binary serchistvis
def shell_sort(some_arr):
    a = len(some_arr)
    gap = a // 2
    while gap > 0:
        for i in range(gap, a):
            anchor = some_arr[i]
            j = i
            while j >= gap and some_arr[j-gap] > anchor:
                some_arr[j] = some_arr[j-gap]
                j -= gap

            some_arr[j] = anchor
        gap //= 2

    return some_arr
def timer_decorator(function):
    def inner(*args):
        start = time.time()
        function(*args)
        end = time.time()
        result = end - start
        return result
    return inner

def list_clasifier(lista):
    if len(lista) == 1000:
        return 'Small'
    elif len(lista) == 2000:
        return 'Mid'
    else:
        return 'Large'

#binary search
@timer_decorator
def binary_search(arr,low, high, x):
    arr = shell_sort(arr)
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == x:
            return mid

        elif arr[mid] > x:
            return binary_search(arr, low, mid-1, x)

        else:
            return binary_search(arr, mid+1, high, x)
    else:
        return -1

# linear search
@timer_decorator
def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1


def measure_func(list,x):
    for i in list:
        size = list_clasifier(i)
        binary_result = binary_search(i,0,len(i)-1,x)
        linear_result = linear_search(i, x)
        print(f'For The {size} of List Performance Result is {binary_result} for Binary Search and {linear_result} for Linear Search')

        if binary_result < linear_result:
            print(f'Bubble Search performs better then Linear Search for {size} lists')
        elif binary_result == linear_result:
            print('Both method has same result')
        else:
            print(f'Linear Search performs better then Bubble Search for {size} lists')
        print()

measure_func(list_of_lists,1)