
#--------------------1--------------------


# 1. დაწერე ფუნქცია რომელიც ლექსიკონიდან დუბლიკატებს ამოშლის და ყველა უნიკალური value_ს მქონე ლექსიკონს დააბრუნებს.


#ორნაირად შეიძლება ამის გაკეთება, პირველი ვარიანტი რომ მარტო უნიკალურებს ტოვებს და მეორე დუბლიკატებს შლის დატოვებს იმას
# რომელიც პირველია სიაში(ესე გავაკეთე მე)  - and i not in list_duplicates ამ პირობას ამოვუშლით და მარტო იმას დატოვებს რაც უნიკალურია

# my_dict = {'k1': 'v1','k2': 'v2','k3': 'v1', 'k4': 'v3','k5': 'v2'}
#
# def duplicate_remover(dict):
#     list_duplicates = []
#     for i, val_i in dict.items():
#         for j, val_j in dict.items():
#             if val_i == val_j and i != j and j not in list_duplicates and i not in list_duplicates:
#                 list_duplicates.append(j)
#
#     for key in list_duplicates:
#         dict.pop(key)
#
#     return dict
#
#
# print(duplicate_remover(my_dict))


#--------------------2--------------------


# 2.დაწერე ფუნქცია რომელიც შეამოწმებს გადაცემული ლექსიკონი ცარიელია თუ არა და დააბრუნებს შესაბამის პასუხს.

# my_dict = {}
#
# def empt_checker(dict):
#
#     if len(dict.items()) == 0:
#         print('Dictionary is empty')
#     else:
#         if len(dict.items()) == 1:
#             print(f'Dictionary is not empty there is only {len(dict.items())} item')
#         else:
#             print(f'Dictionary is not empty there are {len(dict.items())} item')
#
# empt_checker(my_dict)


#--------------------3--------------------


# 3. დაწერე ფუნქცია, რომელიც გადაცემული სტრიქონისგან ლექსიკონს შექმნის და დააბრუნებს.
# ვთქვათ გადავეცით ფუნქციას სტრიქონი, უნდა დააბრუნოს სიმბოლოები key_ს ადგილას და მათი რაოდენობა value_ს ადგილას.
# მაგალითად გადავეცით სტრიქონი : 'racoon'
# უნდა დააბრუნოს ლექსიკონი: {'r': 1, 'a': 1, ‘c': 1, 'o': 2, ‘n': 1}


def counter(text):

    lst = []
    for i in text:
        if i not in lst:
            lst.append(i)

    dicti = {}

    for item in lst:
        dicti[item] = text.count(item)

    return dicti

print(counter('racoon'))





