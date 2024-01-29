#დავალება 1 - დაწერე პროგრამა რომელიც გეკითხება ჯერ სახელს, შემდეგ გვარს და ინფორმაციის მიღების შემდეგ ტერმინალში ბეჭდავს ერთმანეთის გვერდით.

fname = input('Enter your firstname: ')
lname = input('Enter your lastname: ')
print(fname,lname, sep=' ')

#დავალება 2 - დაწერე პროგრამა რომელიც ითხოვს ორ რიცხვს, პირველი რიცხვი აჰყავს მეორის ხარისხში და შედეგი იბეჭდება ტერმინალში.

a = int(input('Enter the first number: '))
b = int(input('Enter the second number: '))
print(a**b)

#დავალება 3 - დაწერე პროგრამა რომელიც გეკითხება სახელს, გვარს, ასაკს და ქალაქს დაბეჭდავს ინფორმაციას შემდეგი სახით:

finame = input('Enter your firstname: ')
laname = input('Enter your lastname: ')
age = input('Enter your age: ')
city = input('Enter your city name: ')

print(f'''
Name: {finame}
Surname: {laname}
Age: {age}
City: {city}
''')

#დავალება 4 - დაწერე პროგრამა, რომელიც გთხოვს შეიყვანო ნებისმიერი სამი სხვადასხვა ხილის დასახელება ცალ-ცალკე. რეზულტატი კი იბეჭდება შემდეგი სახით:

fruit1 = input('Enter fruit 1: ')
fruit2 = input('Enter fruit 2: ')
fruit3 = input('Enter fruit 3: ')

print('{0}//{1}%%{2}'.format(fruit1,fruit2,fruit3))

#დავალება 5 - დაწერე პროგრამა, რომელიც გთხოვს შეიყვანო ტექსტი, დათვლის მასში არსებული სიმბოლოების რაოდენობას და გამოიტანს შედეგს შემდეგნაირად:

text = input('Enter the text: ')

print(f'Number of symbols: {len(text)}')