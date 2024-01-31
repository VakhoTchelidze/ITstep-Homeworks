
# ------------------1------------------

# 1.	შექმენი წრის კლასი, რომელსაც ექნება მეთოდები საკუთარი პერიმეტრისა და ფართობის გამოსათვლელად.

# class Circle():
#     pi = 3.14
#
#     def __init__(self, radius=1):
#         self.radius = radius
#
#     def Area(self):
#         return self.radius * self.radius * self.pi
#
#     def Perimeter(self):
#         return self.radius * self.pi * 2
#
#
# c = Circle(10)
#
# print(c.Area())
# print(c.Perimeter())


# ------------------2------------------

# 2.	შექმენი კალკულატორის კლასი, საბაზისო არითმეტიკული ოპერაციების მეთოდებით.

# class Calculator:
#
#     def __init__(self,num1,num2):
#         self.num1 = num1
#         self.num2 = num2
#
#     def multiplication(self):
#         return self.num1 * self.num2
#
#     def sum(self):
#         return self.num1 + self.num2
#
#     def subtraction(self):
#         return self.num1 - self.num2
#
#     def division(self):
#         return self.num1 / self.num2
#
#
# print(Calculator(2,2).multiplication())
# print(Calculator(2,2).sum())
# print(Calculator(2,2).subtraction())
# print(Calculator(2,2).division())


# ------------------3------------------

# არასავალდებულო დავალება:
# შექმენი შოფინგის კალათის კლასი, რომელსაც ექნება მეთოდები სასურველი ნივთის დასამატებლად და ამოსაშლელად,
# ასევე კალათაში არსებული პროდუქტების სიისა და ჯამური ღირებულების გამოსატანად.

class Basket:

    def __init__(self):

        self.items = {}

    def add_item(self,item,quantity = 1):
        if item in self.items:
            self.items[item] += quantity
        else:
            self.items[item] = quantity

    def remove_item(self, item, quantity = 1):
        if item in self.items:
            self.items[item] = max(0, self.items[item] - quantity)
            if self.items[item] == 0:
                del self.items[item]


    def total_price(self,price_list):
        total_cost = 0
        for i in self.items.keys():
            if i in price_list:
                try:
                    print(f'{i} --- Q: {self.items[i]} , Price: {price_list[i]}, Total cost: {price_list[i]*self.items[i]} ')
                    total_cost += price_list[i]*self.items[i]
                except:
                    pass
            else:
                print(f'{i} --- not in price list')
        print(f'Total cost: {round(total_cost, 2)}')

    def list(self):
        print('Product list in basket:')
        for key, val in self.items.items():
            print(f'{key} ----- {val}')


prices = {"apple": 0.5, "banana": 0.3, "orange": 0.4}


basket = Basket()

basket.add_item("apple", 3)
basket.add_item("banana", 2)
basket.add_item("pomodoro", 2)

basket.remove_item("apple", 1)

basket.total_price(prices)

basket.list()




















