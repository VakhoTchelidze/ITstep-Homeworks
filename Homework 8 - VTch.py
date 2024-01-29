
#--------------------1--------------------

# 1.	დაწერე პროგრამა რომელიც გადაამრავლებს სიის ყველა წევრს კონკრეტულ რიცხვზე ლამბდას გამოყენებით.

# mult = lambda sia ,num :[a*num for a in sia]
#
# nums = [1,2,3]
#
# print(mult(nums,5))


#--------------------2--------------------

# 2.	დაწერე პროგრამა ლამბდას გამოყენებით, რომელიც გადაცემული სიის სიგრძეს დააბრუნებს, მას შემდეგ
# რაც წაშლის სიიდან ყველა სახელს რომელიც პატარა სიმბოლოთი იწყება.  (გამოიყენე .isupper() მეთოდი)

#წაშლით როგორ კეთდება?
#sia = ["Dinamiki",'mausi','Klaviatura']
# func_2 = lambda lst: sum(1 for item in lst if str(item[0]).isupper())
# print(func_2(sia))


#--------------------3--------------------

# 3.	დაწერე პროგრამა რომელიც დააჯამებს სიაში არსებულ დადებით და უარყოფით რიცხვებს ცალცალკე.
# გამოიყენე ლამბდა ფუნქცია და filter.

# sia = [1,4,-3,-2]
#
# func = [sum(filter(lambda a: a<0,sia)),sum(filter(lambda a: a>0,sia))]
#
# print(func)


#--------------------4--------------------

# 4.	დაწერე ბანკის ექაუნთის შექმნის, ანგარიშზე თანხის განთავსების და შემდგომ ექაუნთში შესვლის
# პროგრამა, არასწორი ინფორმაციის შეყვანა მომხმარებლისგან დააზღვიე try და except ბლოკის მეშვეობით.

username = ''
password = ''
angarishi = ''

while len(username)<=0:
    username = input('რეგისტრაციისთვის შეიყვანე სახელი: ')

while len(password)<7:
    password = input('რეგისტრაციისთვის შეიყვანე პაროლი(მინიმუმ 8 სიმბოლო): ')

while True:
    try:
        angarishi = int(input('განათავსეთ სასურველი თანხა ანგარიშზე: '))
        break
    except:
        continue

#ექაუნთზე შესვლა
while True:
    log_name = input('შესვლისთვის შეიყვანე სახელი: ')
    if log_name == username:
        while True:
            log_pass = input('შესვლისთვის შეიყვანე პაროლი: ')
            if log_pass == password:
                print(f'მოგესალმები {username}')
                break
            else:
                continue
        break
    else:
        continue

while True:

    try:
        answ = input('გსურთ თანხის გატანა?(კი/არა): ')
        if answ == 'კი':
            withdrawal = int(input('თანხის გატანა: '))

            if withdrawal > angarishi:
                print('შეყვანილი თანხა მეტია ანგარიშზე არსებულ ტანხაზე')
            else:
                angarishi -= withdrawal
                print(f'მიმნდინარე ბალანსი {angarishi}')

        elif answ == 'არა':
            break

    except:
        print('თანხა არასწორია')

    finally:
        print('კუს ტბის ბანკი - მუდამ თქვენთან !')
























