

# -----------------1-----------------


# 1. შექმენი ფუნქცია რომელიც მიიღებს სიას და დააბრუნებს ასევე სიას, თუმცა უნიკალური ელემენტებით (გამოიყენე set მონაცემთა ტიპი).

# def unique_list(lst):
#     lst = set(lst)
#     lst = list(lst)
#     return lst
#
# listi = [1,2,3,3,4,5,5,6,5,5]
#
# print(unique_list(listi))


# -----------------2-----------------


# 2. შექმენი ფუნქცია რომელიც მიიღებს სიას და დააბრუნებს ასევე set ტიპის მონაცემს უნიკალური ელემენტებით, რომლის
# შეცვლაც შეუძლებელი იქნება (გამოიყენე frozenset).

# def immutable_set(lst):
#     lst = set(lst)
#     lst.add(100)
#     lst = frozenset(lst)
#
#     #frozensetis test -vcdilobt chavamarot elementi
#     try:
#         lst.add(99999999)
#     except:
#         pass
#
#     return lst
#
# listi = [1,2,3,3,4,5,5,6,5,5]
#
# print(immutable_set(listi))


# -----------------3-----------------


# 3. შექმენი ფუნქცია რომელიც მიიღებს ორ set ტიპის მონაცემს, გააერთიანებს მათ, შემდეგ კი გადააქცევს tuple ტიპის მონაცემად და დააბრუნებს შედეგს.

def set_to_tuple(set1,set2):
    new_set = set1.union(set2)
    return new_set

set_1 = {11,12,13}
set_2 = {21,22,23}

print(set_to_tuple(set_1,set_2))

