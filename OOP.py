# #Задача 14.1
# class Dog:
#     height = 20
#     weight = 15
#     name = "Sharik"
#     age = 2
#
#     def __init__(self, jump, run, bark):
#         self.jump = jump
#         self.run = run
#         self.bark = bark
#
# if __name__ == '__main__':
#     dog = Dog("jump", "run", "waf-waf")
#     print(dog.__dict__)
#     print(dog.height, dog.weight, dog.name, dog.age)

#Задача 14.2
class Dog:
    height = 20
    weight = 15
    name = "Sharik"
    age = 2

    def __init__(self, jump, run, bark, change_name):
        self.jump = jump
        self.run = run
        self.bark = bark
        self.change_name = change_name


    def dogs(self, down):
        self.down = down


if __name__ == '__main__':
    dog = "down"
    print(dog)


dog = Dog("jump", "run", "waf-waf", input())
dog.name = ""
del dog.name
print(dog.__dict__)
print(dog.height, dog.weight, dog.age)