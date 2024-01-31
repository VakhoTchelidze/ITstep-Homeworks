
# ------------------1------------------

# 1.	შექმენი წრის კლასი, რომელსაც ექნება მეთოდები საკუთარი პერიმეტრისა და ფართობის გამოსათვლელად.

class Circle():
    pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius

    def Area(self):
        return self.radius * self.radius * self.pi

    def Perimeter(self):
        return self.radius * self.pi * 2


c = Circle(10)

print(c.Area())
print(c.Perimeter())


# ------------------2------------------

# 2.	შექმენი კალკულატორის კლასი, საბაზისო არითმეტიკული ოპერაციების მეთოდებით.
