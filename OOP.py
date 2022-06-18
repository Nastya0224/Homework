# #Задача 14.1
# class Dog:
#
#     def __init__(self, height, weight, name, age):
#         self.height = height
#         self.weight = weight
#         self.name = name
#         self.age = age
#
#     def jump(self, height):
#         print(height)
#
#     def run(self, speed):
#         print(speed)
#
#     def bark(self, voice):
#         print(voice)
#
# dog = Dog(20, 15, "Sharik", 2)
# print(dog.__dict__)
# if __name__ == '__main__':
#     jump = 10
#     run = 30
#     bark = "Waf-Waf"
#
# print(jump, run, bark)


#Задача 14.2
class Dog:

    def __init__(self, height, weight, name, age):
        self.height = height
        self.weight = weight
        self.name = name
        self.age = age

    def jump(self, height):
        print(height)

    def run(self, speed):
        print(speed)

    def bark(self, voice):
        print(voice)

    def dogs(self, down):
        print(down)

    def change_name(self, name1):
        dog.name = name1

dog = Dog(20, 15, "Sharik", 2)
print(dog.__dict__)
print(dog.name)

if __name__ == '__main__':
   dog.change_name(input())

print(dog.name)