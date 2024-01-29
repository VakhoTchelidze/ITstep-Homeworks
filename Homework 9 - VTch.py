#---------1---------

#1.	დაალაგე შემთხვევით დაგენერირებული 10 ელემენტიანი სია sort() მეთოდის გამოყენებით (ზრდადობით).

# import random
#
# rand_list = [random.randint(1, 100) for _ in range(10)]
# print(rand_list)
# rand_list.sort()
# print(rand_list)


#---------2---------

#2.	დაალაგე შემთხვევით დაგენერირებული 10 ელემენტიანი სია sorted() ფუნქციის გამოყენებით (კლებადობით).

# import random
#
# rand_list = [random.randint(1, 100) for _ in range(10)]
# print(rand_list)
# rand_list.sort(reverse=True)
rand_list = sorted(rand_list, reverse=True)
# print(rand_list)


#---------3---------
#
# 3.	დაწერე პროგრამა რომელიც შეადგენს შემთხვევით მთელ რიცხვთა სიას და შექმნილი სიის სორტირება სცადე ორი განსხვავებული
# მეთოდით (მაგ. Bubble და Selection). დათვალე თითოეული მეთოდისთვის სორტირებისთვის საჭირო დრო და დააკვირდი რომელი
# უფრო ეფექტურია მცირე(1000 ელემენტი), საშუალო(2000 ელემენტი) და გრძელი(3000 ელემენტი) სიის შემთხვევებში.

import time
import random

rand_list_small = [random.randint(1, 100) for _ in range(1000)]
rand_list_mid = [random.randint(1, 100) for _ in range(2000)]
rand_list_large = [random.randint(1, 100) for _ in range(3000)]

list_size = ['Small','Mid','Large']
list_of_lists = [rand_list_large, rand_list_mid, rand_list_small]

def timer_decorator(function):
    def inner(*args):
        start = time.time()
        function(*args)
        end = time.time()
        result = end - start
        #print(f'Result: {result}')
        return result
    return inner

def list_clasifier(lista):
    if len(lista) == 1000:
        return 'Small'
    elif len(lista) == 2000:
        return 'Mid'
    else:
        return 'Large'

#Bubble Sort
@timer_decorator
def bubble(list_a):
    indexing_length = len(list_a)-1
    sorteed = False

    while not sorteed:
        sorteed = True

        for i in range(0, indexing_length):
            if list_a[i] > list_a[i+1]:
                sorteed = False
                list_a[i], list_a[i+1] = list_a[i+1], list_a[i]
    #list_clasifier(list_a)
    return list_a

# Selection Sort
@timer_decorator
def selection_sort(some_arr):
    arr = some_arr
    indexing_length = range(0, len(arr) - 1)

    for i in indexing_length:
        min_value = i

        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_value]:
                min_value = j

        if min_value != i:
            arr[min_value], arr[i] = arr[i], arr[min_value]

    size = list_clasifier(some_arr)
    return arr


def measure_func(list):
    for i in list:
        size = list_clasifier(i)
        bubble_result = bubble(i)
        selection_result = selection_sort(i)
        print(f'For The {size} of List Performance Result is {bubble_result} for Bubble Sort and {selection_result} for Selection Sort')

        if bubble_result > selection_result:
            print(f'Bubble Sort performs better then Selection Sort for {size} lists')
        elif bubble_result == selection_result:
            print('Both method has same result')
        else:
            print(f'Selection Sort performs better then Bubble Sort for {size} lists')
        print()

measure_func(list_of_lists)

