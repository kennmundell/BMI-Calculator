class Person:
    def __init__(self, age, weight, height, first_name, last_name, catch_phrase):
        self.age = age
        self.weight = weight
        self.height = height
        self.first_name = first_name
        self.last_name = last_name
        self.catch_phrase = catch_phrase


user = Person(25, 80, 177, "Jon", "Snow", "You know nothing, Jon Snow")

print(user.catch_phrase)
print(user.weight)
print(f'You are {user.weight} kilos')
weight = int(input("How many kilos are you?: "))
height = float(input("What height are you in meters? "))
height_squared = height * height
pounds = weight * 2.2
poundsr = round(pounds,2)
print(f'You are {poundsr} pounds')
stone = pounds / 14
stoner = round(stone,2)
BMI = weight / height_squared
print(f'You are {stoner} stone')
BMIR = round(BMI,2)
print(f'Your BMI is {BMIR}')
