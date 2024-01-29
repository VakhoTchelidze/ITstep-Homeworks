#---------------------1---------------------
# 1. მომხმარებელს შემოაყვანინე ინფორმაცია და დათვალე რამდენი რიცხვი, ანბანის ასო და სხვა სიმბოლოა მოცემული წინადადებაში.
# შედეგი დაბეჭდე. გამოიყენე for ციკლი, isalpha და isdigit ფუნქციები.

# word = input('Enter word: ')
# digcount = 0
# letcount = 0
# simbol = 0
# space = 0
#
# for i in word:
#     if i.isalpha():
#         letcount += 1
#     elif i.isdigit():
#         digcount += 1
#     elif i == ' ':
#         space+=1
#     else:
#         simbol += 1
# print(f'''
# Letter: {letcount}
# Digit: {digcount}
# Simbol: {simbol}
# Space: {space}
# ''')


#---------------------2---------------------
# 2. მომხმარებელს შეაყვანინე ორი წინადადება და მათგან შეადგინე მესამე შემდეგ წესებზე დაყრდნობით.
# შექმნილი წინადადება უნდა იწყებოდეს პირველი წინადადების პირველი სიმბოლოთი, რომელსაც ჯერ მოჰყვება
# მეორე წინადადების ბოლო სიმბოლო, შემდეგ კი პირველი წინადადების მეორე სიმბოლო და მეორე წინადადების
# ბოლოდან მეორე სიმბოლო.

# word1 = input('Enter text 1: ')
# word2 = input('Enter text 2: ')
# new_word = word1[0]+word2[-1]+word1[1]+word2[-2]
# print(f'New word: {new_word}')


#---------------------3---------------------
# 3. მომხმარებელს შეაყვანინე ორი წინადადება და შეამოწმე, პირველ წინადადებაში არსებული ყველა სიმბოლო თუ შედის მეორე
# წინადადებაში და პირიქით, მეორე წინადადებაში შემავალი ყველა სიმბოლო თუ შედის პირველ წინადადებაში.
# თუ ეს ორი პირობა დაკმაყოფილდა, დაბეჭდე:
# „Strings are balanced!“
# თუ რომელიმე პირობა დაირღვა, დაბეჭდე:
#„Strings are not balanced!“

# import re
#
# word1 = input('Enter text 1: ')
# word2 = input('Enter text 2: ')
# var = 0
#
# for i in word2:
#     ans = re.findall(i, word1)
#     if len(ans) == 0:
#         print('Strings are not balanced!')
#         var += 1
#         break
#
# for i in word1:
#     ans = re.findall(i, word2)
#     if len(ans) == 0:
#         print('Strings are not balanced!')
#         var += 1
#         break
# if var == 0:
#     print('Strings are balanced!')