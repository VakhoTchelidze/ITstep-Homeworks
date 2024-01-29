# -----------------1-----------------

# 1.	დაწერე კოდი რომელიც article.txt _დოკუმენტში იპოვის რიგით მეორე ყველაზე ხშირად განმეორებად სიტყვას.

#ფაილიდან ინფორმაციას ვინახავთ ცვლადში
with open('article.txt', '+r') as file:
    text = file.readlines()

#სიიდან ტექსტის ვაერთიანებთ
full_text = ''
for i in text:
    full_text += i

#სასვენი ნიშნებიდან ვასუფთავებთ
cleaned_text = ''
for i in full_text:
    if i.isalnum() or i.isspace():
        cleaned_text += i

#ვეძებთ ყველაზე ხშირად გამეორებად სიტყვებს
unique_words = set(cleaned_text.split())
word_dict = {}

for item in unique_words:
    word_dict[item] = cleaned_text.count(item)

#სორტირება
sorted_dict = dict(sorted(word_dict.items(), key=lambda i: i[1], reverse=True))

#ამ ფუნქციაში ვუთითებთ ტოპ რომელი სიტყვა წამოიღოს
def top_word(top):
    for num,key in enumerate(sorted_dict):
        try:
            if num == top:
                print(key)
        except:
            print('Entered value is not correct')
print(sorted_dict)
top_word(1)


# -----------------2-----------------

# 2.	names.csv ფაილში არსებული ინფორმაცია გადმოაკოპირე names.txt ფაილში.
#
# import csv
#
# with open("names.csv", "r") as file:
#     csv_reader = csv.reader(file)
#
#     with open("new_names.txt", "w", newline="") as new_file:
#         csv_writer = csv.writer(new_file)
#
#         for line in csv_reader:
#             csv_writer.writerow(line)









