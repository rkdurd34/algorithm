class Node:
    
    width = 0
    height = 0
    color = 'black'
    def get_area(self):
        return  (self.width * self.height,self.color)
    def set_area(self, data1, data2,data3):
        self.width = data1
        self.height = data2
        self.color = data3

    
square = Node()
square.set_area(5,5,'red')
print(square.get_area())
# class Quadrangle:
#     def __init__(self, width, height, color):
#         self.width = width
#         self.height = height
#         self.color = color
#     # def __del__(self):
#     #     print("Quadrangle object is deleted")
# kang = Quadrangle(1,2,"black")

class admin:
    def __init__(self, kor, eng, math, name):
        self.kor = kor
        self.eng = eng
        self.math = math
        self.name = name
    def average(self):
        return ((self.kor + self.eng+self.math)/3)
student_1 = admin(10,10,30,"경욱")
print(student_1.name)
print(student_1.average())
class Person :
    def __init__(self,name):
        self.name = name
class Student(Person):
    def study(self):
        print(self.name)
class Employee(Person):
    def work(self):
        print(self.name)
studnet1 = Student('kang')
employee1 = Employee ('kang_1')
employee1.work()

class Car :
    def __init__(self,name):
        self.name = name
    def get_info(self):
        print(self.name)
class ElecCar(Car):
    def get_info(self):
        print(self.name, "fuel : electorinic")
class GasoCar(Car):
    def get_info(self):
        print(self.name, "fuel :Gaoline")
elec = ElecCar('dave')
gaso = GasoCar("david")
car_1 = Car("hooah")
elec.get_info()
gaso.get_info()
car_1.get_info()
print("\n다음\n")
class Person:
    def work(self):
        print('work hard')
        print('부모꺼에서 가져옴')
class Student(Person):
    def work(self):
        Person.work(self)
        print('study hard')
    def parttime(self):
        super().work()
        
    def general(self):
        self.work()
student_1 = Student()
student_1.work()
student_1.parttime()
student_1.general()
print('\n추상클래스 상속하기\n')
from abc import *
class Character(metaclass=ABCMeta):
    def __init__(self,hp):
        self.hp = hp
    def get_hp(self):
        return self.hp

    @abstractmethod
    def attack(self):
        pass
    @abstractmethod
    def move(self):
        pass
class Elf(Character):
    def attack(self):
        print('practice the black art')
    def move(self):
        print('fly')
class Human(Character):
    def attack(self):
        print('plunge a knife')
    def move(self):
        print('run')
# elf1 = Elf()
# human1 = Human()
# elf1.attack()
# 추상 클래스는 객체를 만들 수 없다!!!d
elf_1 = Elf(10)
print(elf_1.get_hp())

class Car(metaclass=ABCMeta):
    

    def info(self):
        return print(self.name)
    @abstractmethod
    def fuel(self):
        pass
class Electronic(Car):
    def __init__(self,name):
        self.name = name

    def info(self):
        return print(self.name)
    def fuel(self):
        return print("Fuel연료")

car_1 = Electronic("ford")
car_1.info()
car_1.fuel()

class Figure:
    count=0
    def __init__(self,width,height):
        self.width = width
        self.height = height
        Figure.count +=1
    def __del__(self):
        Figure.count-= 1
    def calc_area(self):
        return self.width * self.height
    @staticmethod
    def print_count():
        print(Figure.count)
    @classmethod
    def print_count_from_class_method(cls):
        print(cls.count)
    # @staticmethod
    # def print_width():
    #     print(self.width)
    # 정적 메서드에서는 객체 attribute에는 접근 불가!!!!!!!!!!!!!!!
    # 오로지 클래스 attribute만 접근 가능 ex) figure.count
a = Figure(1,2)
print(Figure.count)
a.print_count()
print("이 위에는 정적 메서드에서 클래스 attribute figure.count에 접근하는방법")
a.print_count_from_class_method()
print("이 위에는 클래스 메서드에서 클래스 attribute figure.count에 접근하는방법")
b = Figure(2,3)
print(Figure.count)
c = Figure(3,4)
print(Figure.count)
del a
print(Figure.count)

class A(object):
    count=0
    def __init__(self,cnt):
        A.count+=1
        self.cnt = cnt
    def print_cnt(self):
        print(self.cnt)

    @classmethod
    def print_count(cls):
        print(cls.count)
print('심화문제 시작')
a1 = A(1)
a2 = A(2)
a3 = A(44)

a1.print_cnt()
a2.print_cnt()
a3.print_cnt()
A.print_count()


class SalesWorker:
    def __init__(self,name):
        self.name = name
    def work(self):
        print(self.name,'sells something')
class DevWorker:
    def __init__(self,name):
        self.name =name
    def work(self):
        print(self.name, "develops something")
worker1 = SalesWorker('Dave')
worker2 = SalesWorker('David')
worker3 = SalesWorker('Andy')
worker4 = DevWorker('Aiden')
worker5 = DevWorker('Tina')
worker6 = DevWorker('Anthony')

workers = [worker1, worker2, worker3, worker4, worker5, worker6]
for i in workers:
    i.work()


class Character(metaclass=ABCMeta):
    def __init__(self,name):
        self.name = name
    @abstractmethod
    def attack(self):
        pass
class Elf(Character):

    def attack(self):
        print("맘법으로 공격합니다")

class Fighter(Character):
    def attack(self):
        print("주먹으로 공격합니다")
fighter_1 = Fighter("figher_1")
elf_1 = Elf("elf_1")
fighter_1.attack()
elf_1.attack()

class Figure_3:
    def __init__(self,width,height):
        self.width = width
        self.height = height
class Quadrangle:
    def __init__(self,width,height):
        self.width = width
        self.height= height
    def __add__(self,second):
        return Quadrangle(self.width + second.width,self.height +second.height)
    def __getitem__(self,index):
        if index == 0:
            return self.width
        elif index ==1:
            return self.height
    def __str__(self):
        return f'width ;{self.width}, height{self.height}'

rectangle1 = Quadrangle(2,3)
figure1 = Figure_3(3,4)
rectangle2 = rectangle1 + figure1
print(rectangle2.width,rectangle2.height)

rectangle_3 = Quadrangle(6,4)
figure_2 = Figure_3(10,3)
rectangle_4 =rectangle_3 + figure_2 
# 위에 계산 할 때 앞뒤가바뀌면 안됨

print(rectangle_4.width, rectangle_4.height)
print(str(rectangle_4))
print(rectangle_4[0], "__getitem__매서드 사용하는거 .... 와..")