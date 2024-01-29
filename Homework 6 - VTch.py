
#--------------1--------------

# 1. შექმენი ფუნქცია, რომელიც მომხმარებლისგან მიღებულ ინფორმაციას გაასამმაგებს და დაბეჭდავს შემდეგნაირად:
# input: “ablabdabdab”
# Output: „Tripled: ablabdabdabablabdabdabablabdabdab“

# def word_tripler(word):
#     print(f'Tripled: {word*3}')
#
# word_tripler('amin')


#--------------2--------------

# 2. შექმენი ფუნქცია, რომელიც მიიღებს მომხმარებლის წონას და დააბრუნებს მის წონას მთვარეზე. (მთვარის გრავიტაცია 6_ჯერ ნაკლებია დედამიწისაზე)

# def moon_weight(weight):
#     print(f'Your weight on moon would be: {weight / 6}')
#
# moon_weight(120)


#--------------3--------------



# while True:
#     equation = input('Choose Operation(+-*/^): ')
#     if len(equation.split()) == 3:
#         num1, x, num2 = equation.split()
#         break
# def math_op(num1=num1,x=x,num2=num2):
#
#     if x == "+":
#         return int(num1)+int(num2)
#
#     elif x == "-":
#         return int(num1)-int(num2)
#
#     elif x == "*":
#         return int(num1)*int(num2)
#
#     elif x == "/":
#         return int(num1)/int(num2)
#
#     elif x == "^":
#         return int(num1) ** int(num2)
#
#     else:
#         print('Wrong Format')
# #print(3^2) es simbolo ragac sxva operaciistvisaa
#
# print(math_op())


#--------------4--------------

def morse_translator(word):
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M','N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    morse_code = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---','-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-','..-', '...-', '.--', '-..-', '-.--', '--..']
    morse_word = ''
    for i in word:
        morse_word += morse_code[letters.index(i.upper())]+" "
    return morse_word

print(morse_translator('vaxo'))




