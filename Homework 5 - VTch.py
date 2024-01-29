# 1. ციკლის მეშვეობით 3 მომხმარებელს შეაყვანინე ინფორმაცია საკუთარი სახელის, გვარის და ასაკის შესახებ.
# თითოეული მომხმარებლის ინფორმაცია შეინახე ინდივიდუალურ სიაში. შემდეგ კი სამივე სია დაამატე საერთო ცალრიელ
# სიას სახელად consumer_info. Input_ის მეშვეობით მომხმარებლის ინდექსის შეყვანის შემთხვევაში პროგრამამ უნდა
# დაბრუნოს არჩეულ მომხმარებელზე ინფორმაცია შემდეგნაირად:
# Name: Elene
# Lastname: Khardava
# Age: 21

#---------------1---------------

# count = 1
# consumer_info = [" "]
# while count < 4:
#     name = input(f'Enter consumer {count} name: ')
#     lastname = input(f'Enter consumer {count} lastname: ')
#     age = input(f'Enter consumer {count} age: ')
#     user_info = [name,lastname,age]
#     consumer_info.append(user_info)
#     count += 1
#
# index = int(input('Enter consumer index(1-3): '))
#
# print(f'''
# Name: {consumer_info[index][0]}
# Lastname: {consumer_info[index][1]}
# Age: {consumer_info[index][2]}
# ''')


# 2. მომხმარებელი დაარეგისტრირე ონლაინ პლატფორმაზე თუ სახელის ველი არ იქნება ცარიელი, ხოლო პაროლი 8 სიმბოლოზე მეტი ან ტოლია.
# მისი მონაცემები შეინახე ლისთში. შემდეგ მიეცი საშუალება სცადოს პლატფორმაზე შესვლა და შეადარე მის მიერ შემოყვანილი ინფორმაცია სიაში
# შენახულ ინფორმაციას. დაბეჭდე შესაბამისი მესიჯი.

#---------------2---------------

# username = ''
# password = ''
# userlist = []
#
# while len(password) < 8 or len(username) < 1:
#
#     username = input('Enter username: ')
#     if len(username) >= 1:
#         while len(password) < 8:
#             password = input('Enter password: ')
#             if len(password) >= 8:
#                 userlist.append(username)
#                 userlist.append(password)
#                 break
#             else:
#                 print('არასწორი ფორმატის პაროლი')
#     else:
#         print('არასწორი ფორმატის სახელი')
#         continue
#
# while True:
#     print('პლატფორმაზე შესვლა: ')
#     uname = input('Enter username: ')
#     pssw = input('Enter password: ')
#
#     if (uname in userlist) and (pssw in userlist):
#         print('Logged in successfully !')
#         break
#
#     elif (uname in userlist) and (pssw not in userlist):
#         print('Wrong password!')
#
#     elif (uname not in userlist) and (pssw in userlist):
#         print('Wrong username!')
#
#     else:
#         print('Wrong username and password!')


# 3. შექმენი ჩაშენებული სია, რომელშიც იქნება შენახული ცნობილი მსახიობების შესახებ ინფორმაცია.
# მომხმარებელს შემოჰყავს მსახიობის სახელი ან გვარი. თუ სიაში მოიძებნა მსახიობი, დაბეჭდა მის შესახებ
# არსებული ინფორმაცია რეზუმის სახით.

#---------------3---------------

#Siashi 3 msaxiobia veriko anjafaridze, al pacino da robert deniro, Dictionrebitac sheidzleboda tumca ar gagvivlia
# actorlist = ['al pacino - born April 25, 1940. Al is an American actor. Considered one of the greatest and most influential actors of the 20th century','robert deniro - born August 17, 1943, is an American actor and filmmaker.', 'veriko anjafaridze was a Soviet and Georgian stage and film actress.',]
#
# while True:
#     actor = input('Ente actor name or lastname: ')
#     nocounter = 0
#     for i,x in enumerate(actorlist):
#         for o in x.split():
#             if actor.lower() == o.lower():
#                 print(actorlist[i])
#                 nocounter = 1
#                 break
#     if nocounter == 0:
#         print('No such actor in our database')