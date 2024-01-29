
#-------------------------1-------------------------


# 1.	დაწერე ფუნქცია რომელიც მომხმარებელს ჩააწერინებს ტექსტურ ფაილში
# ინფორმაციას Input ფუნქციის დახმარებით, მანამ სანამ მომხმარებელი არ შეიყვანს
# სიტყვას _ “enough”.

# def file_writer():
#     filename = input('Enter file name: ')
#
#     while True:
#         text = input('Enter text: ')
#         if text.lower() == 'enough':
#             break
#         else:
#             with open(filename+'.txt', 'a') as file:
#                 file.write(text+'\n')
#
# file_writer()


#-------------------------2-------------------------


# 2.	დაწერე ფუნქცია რომელიც input ფუნქციის დახმარებით მომხმარებლისგან მიიღებს საქაღალდის
# ლოკაციას და შესაქმნელი ფაილის სახელს, შემდეგ მიღებულ ლოკაციაზე შექმნის შესაბამის ფაილს და
# ამოპრინტავს საქაღალდეში არსებულ ყველა ფაილის სიას.

import os


def file_creator():
    location = input('Enter location where you want to create file: ')
    filename = input('Enter name of file you want to create: ')

    with open(f"{location}\\{filename}.txt", "x") as file:
        pass

    for i in os.listdir(location):
        print(i)


file_creator()













