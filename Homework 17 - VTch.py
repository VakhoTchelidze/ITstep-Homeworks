
#--------------------1--------------------

# 1.	შექმენი კლასი რომელსაც ექნება public, protected და private პარამეტრები. გამოიყენე @property დეკორატორი
# და ასევე შექმენი setter და  getter დეკორატორებიანი ფუნქციები პარამეტრებზე წვდომისა და რედაქტირებისთვის.

class Animal:

    def __init__(self,name, legs, color):

        assert type(legs) is int, "Enter integer in legs field"

        self._name = name
        self.legs = legs
        self.__color = color

    @staticmethod
    def speak():
        print('Aaahhhhhhhh!')
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        assert type(value) is str, "Enter string in model field"
        print("Name changed")
        self._name = value

    @name.getter
    def name(self):
        print("Getting name info")
        return self._name


dog = Animal('Bombora',4,'red')
dog.name = 'Chapa'
print(dog.name)


#--------------------2--------------------

# 2.	შექმენი მისი შვილობილი კლასი და შეუცვალე რაიმე არსებული მეთოდი.

class Dog(Animal):

    def __init__(self,name, legs, color):
        super().__init__(name, legs, color)

    def speak(self):
        print(f'Woof! my name is {self.name}')

dog2 = Dog('Max',4,'Black')

dog2.speak()



















