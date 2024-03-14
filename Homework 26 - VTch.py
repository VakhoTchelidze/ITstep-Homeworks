
# 1.	მოცემულ კლასს მოარგე Single Responsibility პრინციპი და შესაბამისად შეცვალე კოდი.
# (კერძოდ დაშალე 4 კლასად User,  Storage,  HttpConnection,  Logger)

# class  User:
#     def __init__(self, name):
#         self.name = name
#
#     def get_name(self):
#         return self.name
#
# class Storage():
#     def save(self,user, data):
#         #აქ დასეივდება მონაცემები ბაზაში
#         pass
#
# class HttpConnection():
#     def send(self,user,message,reciever):
#         #აქ მოცემული ელემენტების გამოყენებით გავაგზავნით იმეილს
#         პასს
# class Logger():
#     def log(self,user, data):
#         #აქ დავლოგავთ მონაცემებს
#         pass


# 2.	მოცემული გვაქვს Discount კლასი. Open-Closed პრინციპის გამოყენებით საჭიროა სწორად
# დავნერგოთ 40%_იანი ფასდაკლების ფუნქციონალი VIP კლიენტებისთვის. (შექმენი VIPDiscount კლასი)

from abc import ABC, abstractmethod

class Discount(ABC):
    @abstractmethod
    def give_discount(self):

class VipDiscoundt(Discount):
    def __init__(self, customer, price):
        self.customer = customer
        self.price = price

    def give_discount(self):
        if self.customer == 'favourite':
            return self.price * 0.2
        if self.customer == 'vip':
            return self.price * 0.4
        else:
            return self.price






