#-----------------------1-----------------------
# 1. ჯეირანის პროგრამა
# დაასრულე ჯეირანის თამაშის პროგრამა ციკლის გამოყენებით. თამაშის დასასრულებლად რომელიმე მოთამაშემ უნდა დააგროვოს 3 ქულა.


# import random
#
# human_point = 0
# comp_point = 0
#
# while True:
#     human_choice = int(input('''
#     აირჩიე რიცხვი:
#     1. ქვა
#     2. მაკრატელი
#     3. ფურცელი
#
#     შეიყვანე ციფრი(1-3):
#     '''))
#
#     computer_choice = random.randint(1, 3)
#     print(f'ანგარიში: {human_point} : {comp_point}')
#     if human_point != 3 and comp_point != 3:
#         if human_choice == computer_choice:
#             continue
#         elif (human_choice == 1 and computer_choice == 2) or (human_choice == 2 and computer_choice == 3) or (human_choice == 3 and computer_choice == 1):
#             human_point += 1
#         else:
#             comp_point += 1
#
#     elif human_point == 3:
#         print('გილოცავ მოიგე!')
#         break
#     else:
#         print('წააგე')
#         break


#-----------------------2-----------------------
# 2. გამრავლების ტაბულა ორმაგი for ციკლის_ის დახმარებით დაბეჭდე გამრავლების ტაბულა 1_დან მომხმარებლის მიერ შეყვანილი მთელი რიცხვის ჩათვლით.

#I ვარიანტი

# number = int(input('Enter number: '))
#
# for num in range(1,number+1):
#     for i in range(1,number+1):
#         print(f'{num}*{i}={num*1}')
#     print()

#II ვარიანტი

# number = int(input('Enter number: '))
#
# for num in range(1,number+1):
#     for i in range(1,number+1):
#ეს იფი ორნიშნებმა კვადრატის ფორმა როარ დაარღვიონ მაგიტოა
#         if len(str(num*i)) == 1:
#             print(num*i, end="  ")
#         else:
#             print(num * i, end=" ")
#     print()



#-----------------------3-----------------------
# 3. საბანკო ანგარიში
# შეადგინე პროგრამა რომელიც განასახიერებს საბანკო ანგარიშს. მასზე განთავსებულია თანხა 3000 ლარის ოდენობით.
# პროგრამა გეკითხება გაწეულ ხარჯს და აკლებს ანგარიშს მანამ, სანამ არ შეიყვან 0_ს.
# შემდეგ გიბეჭდავს ანგარიშზე დარჩენილ თანხას და წყვეტს ფუნქციონირებას. თუ ანგარიშზე არსებული თანხა ნაკლებია დანახარჯის თანხაზე,
# პროგრამამ უნდა დაბეჭდოს, რომ ანგარიშზე არ არის საკმარისი თანხა და გააგრძელოს ფუნქციონირება.

# angarishi = 3000
#
# while True:
#     withdrawal = int(input('რა თანხის განაღდება გსურთ: '))
#
#     if withdrawal < angarishi and withdrawal != 0:
#         angarishi = angarishi - withdrawal
#         print(f'მიმდინარე ნაშთი - {angarishi}')
#     elif withdrawal == 0 or angarishi==0:
#         print(f'მიმდინარე ნაშთი - {angarishi}')
#         break
#     else:
#         print('ანგარიშზე არ არის საკმარისი თანხა')
#         print(f'მიმდინარე ნაშთი - {angarishi}')
#         continue


#-----------------------4-----------------------
# 4. თუთიყუშის პროგრამა
# დაწერე პროგრამა _ თუთიყუში. პროგრამამ უნდა გაიმეოროს რასაც ეტყვი მანამ სანამ არ შეიყვან სიტყვას quit, თუმცა წინ დაურთოს კითხვა „User Said Whaaat!?”
# თუ შევიყვანეთ სიტყვა Hello დაიბეჭდება
# „User Said Whaaat!?”
# “User Said Hello”

# while True:
#     answer = input('User Said Whaaat!? ')
#
#     if answer.lower() != 'quit':
#         print(f'User Said {answer}')
#     else:
#         print('End!')
#         break


