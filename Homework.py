import tkinter as tk
from tkinter import ttk
from random import choice
from tkinter import messagebox
# import ttkbootstrap as ttk
import customtkinter as ct

# 1
# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
# p1 = Person('ali',20)
# print(f'name: {p1.name} ,age: {p1.age}')

# 2
# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
#     def greeting(self):
#         print(f'Hello {self.name}')
# p2 = Person('murtaza',20)
# p2.greeting()

# 3

# class car:
#     def __init__(self,make,model,year):
#         self.make = make
#         self.model = model
#         self.year = year
#     def details(self):
#         print(f'make in {self.make}\nmodel {self.model}\nyear of make {self.year}')
#
# c1 = car('Japan','x4',2000)
# c1.details()

# 4

# class circal:
#     def __init__(self,radius):
#         self.raduis = radius
#
#     def area(self):
#         a = self.raduis * self.raduis * 3.14
#         print(a)
# c = circal(3)
# c.area()

# 5

# class rectangle:
#     def __init__(self,width,hight):
#         self.width = width
#         self.hight = hight
#
#     def area(self):
#         a = self.width * self.hight
#         print(a)
# r = rectangle(2,3)
# r.area()

# 6

# class animal:
#     def speck(self):
#         print('')
# class dog(animal):
#     def speck(self):
#         print('bark bark bark')
# class cat(animal):
#     def speck(self):
#         print('mo mo mo')
# 7
#
# class shep:
#     def area(self):
#         return None
#
# class squre(shep):
#     def __init__(self,wedght,hight):
#         self.wedght = wedght
#         self.hight = hight
#     def area(self):
#         a = self.hight * self.wedght
#         return a
#
# class tringle(shep):
#     def __init__(self,bass,hight):
#         self.bass = bass
#         self.hight = hight
#     def area(self):
#         a = self.hight * self.bass * 0.5
#         return a


# 8
#
# class employee:
#     def __init__(self,name,salary):
#         self.name = name
#         self.salary = salary
# #
# class manager(employee):
#     def __init__(self,name,salary,department):
#         super().__init__(name,salary)
#         self.department = department

# 9

# class vehicle:
#     def drive(self):
#         print('')
#
# class bike(vehicle):
#     def drive(self):
#         print('ride start')
# class truck(vehicle):
#     def drive(self):
#         print('truck move start')

# 10

# class bird:
#     def fly(self):
#         print('')
#
# class eagle(bird):
#     def fly(self):
#         print('eagle can fly')
#
# class penguin(bird):
#     def fly(self):
#         print('penguin can not fly')

# 11

# class Account:
#     def __init__(self,blance):
#         self.__blance = blance
#
#     def deposit(self,other):
#         self.__blance += other
#         print(self.__blance)
#
#     def withdrow(self,other):
#         self.__blance -= other
#         print(self.__blance)



# 12

# class Book:
#     def __init__(self,title,author,page):
#         self.__title = title
#         self.__author = author
#         self.__page = page
#
#     def get_title(self):
#         print(self.__title)
#
#     def set_title(self,other):
#         self.__title = other
#         print(self.__title)
#
#     def get_author(self):
#         print(self.__author)
#
#     def set_author(self,other):
#         self.__author = other
#         print(self.__author)
#
#
#     def get_page(self):
#         print(self.__page)
#
#     def set_page(self,other):
#         self.__page = other
#         print(self.__page)
#
# book1 = Book('gool','murtaza',300)
# book1.get_title()
# book1.set_title('tife')



# 13

# class labtab:
#     def __init__(self,brand,model,price):
#         self.__brand = brand
#         self.__model = model
#         self.__price = price
#
#     def details(self):
#         print(f'computer brand {self.__brand}\ncomputer model {self.__model}\ncomputer price {self.__price}')
#
#     def disacount(self):
#
#         print('we disacount 50$ for you!!!')

# 14

# class bankacaunt:
#     def __init__(self,acount_number,balance):
#         self.__acount_number = acount_number
#         self.__balance = balance
#
#     def deposit(self,other):
#         self.__balance += other
#         print(self.__balance)
#
#     def withdraw(self,other):
#         self.__balance -= other
#         print(self.__balance)
#
#     def balance(self):
#         print(self.__balance)

# 15

# class student:
#     def __init__(self,name,grade,age):
#         self.__name = name
#         self.__grade = grade
#         self.__age = age
#
#     def details(self):
#         print(f'student name {self.__name}\n'
# #               f'student grade {self.__grade}\n'
# #               f'student age {self.__age}')

# 16
#
# class library:
#     list_books = []
#     def __init__(self,name,books):
#         self.name = name
#         self.books = books
#         library.list_books.append(self.books)
#
#     def add_book(self,other):
#         library.list_books.append(other)
#
#     def remove_book(self,other):
#         library.list_books.remove(other)
#
#
# 17
#
# class school:
#     student_list = []
#     def __init__(self,name,students):
#         self.name = name
#         self.student = students
#         school.student_list.append(students)
#
#     def add_student(self,other):
#         school.student_list.append(other)
#
#     def remove_student(self,other):
#         school.student_list.remove(other)
#
# s = school('habibua','murtaza')
# s.add_student('ali')
# print(school.student_list)
# s.remove_student('murtaza')
# print(school.student_list)
#
#
# 18
#
# class team:
#     team_list = []
#     def __init__(self,name,members):
#         self.name = name
#         self.members = members
#         team.team_list.append(members)
#
#     def add_members(self,other):
#         team.team_list.append(other)
#
#     def remove_members(self,other):
#         team.team_list.remove(other)
#
# 19
#
# class company:
#     company_list = []
#     def __init__(self,name,employee):
#         self.name = name
#         self.employee = employee
#         company.company_list.append(employee)
#
#     def add_employee(self,other):
#         company.company_list.append(other)
#
#     def remove_employee(self,other):
#         company.company_list.remove(other)
#
# 20
#
# class zoo:
#     animal_list = []
#     def __init__(self,name,animal):
#         self.name = name
#         self.animal = animal
#         zoo.animal_list.append(animal)
#
#     def add_animal(self,other):
#         zoo.animal_list.append(other)
#
#     def remove_animal(self,other):
#         zoo.animal_list.remove(other)


# 21

# class log:
#     def __init__(self,add_file):
#         self.add_file = add_file
#     def write_error(self,error):
#         with open(self.add_file,'a') as f:
#             f.write(error)



# 22

# class report:
#     def __init__(self,file_name):
#         self.file_name = file_name
#
#     def gem_report(self):
#         try:
#             with open(self.file_name,'r') as f:
#                 return f.read()
#         except FileNotFoundError:
#             print('FileNotFound')

# 23
# 24
# 25


# 26
#
# class ticket:
#     def __init__(self,movies_name,seat_num,price):
#         self.movies_name = movies_name
#         self.seat_num = seat_num
#         self.price = price
#
#     def details(self):
#         print(f'movies name {self.movies_name}\n'
#               f'seat number {self.seat_num}\n'
#               f'price {self.price}')
#
#     def discount(self):
#         print('we discount for you 20$')
#         self.price -= 20
#
# 27
#
# class shoppingcar:
#     iteams = []
#     def __init__(self,name,price):
#         self.name = name
#         self.price = price
#
#
#     def disply(self):
#         print(shoppingcar.iteams)
#
#     def add_iteams(self,other):
#         shoppingcar.iteams.append(other)
#
#     def remove_iteams(self,other):
#         shoppingcar.iteams.remove(other)
#
# s = shoppingcar('aa',200)
# s.add_iteams('bb')
# s.add_iteams('aa')
# s.disply()
# s.remove_iteams('bb')
# s.disply()


# 28
#
# class restaurant:
#     menu_list = []
#     def __init__(self,name,menu):
#         self.name = name
#         self.menu = menu
#         restaurant.menu_list.append(self.menu)
#     def add_menu(self,other):
#         restaurant.menu_list.append(other)
#
#     def remove_menu(self,other):
#         restaurant.menu_list.remove(other)
#
# 29
#
# class flight:
#     list_passengers = []
#     def __init__(self,flight_num,destination,passengers):
#         self.flight_num = flight_num
#         self.destination = destination
#         self.passengers = passengers
#         flight.list_passengers.append(self.passengers)
#
#     def remove_passengers(self,other):
#         flight.list_passengers.remove(other)
#
# f = flight(9,'harat','qasim')
# print(flight.list_passengers)
# #
# f.remove_passengers('qasim')
# print(flight.list_passengers)
# 36
# class counter:
#     def __init__(self,window):
#         self.window = window
#         self.title = window.title('App')
#         self.geo = window.geometry('300x200')
#         self.label = ttk.Label(window,text='')
#         self.label.pack()
#
#         self.num = 0
#         self.btn1 = ttk.Button(window,text='increment',command=self.increment)
#         self.btn1.pack(pady=7)
#         self.btn2 = ttk.Button(window, text='decrement',command=self.decrement)
#         self.btn2.pack(pady=7)
#
#     def increment(self):
#         self.num += 1
#         self.label.config(text=f'counter: {self.num}')
#
#
#     def decrement(self):
#         self.num -= 1
#         self.label.config(text=f'counter: {self.num}')
#
# if __name__ == '__main__':
#     window = tk.Tk()
#     app = counter(window)
#     window.mainloop()
#
#
# 37
#
# class todoapp:
#     def __init__(self,window):
#         self.window = window
#         self.title = window.title('To Do App')
#         self.geo = window.geometry('500x600')
#
#         self.list_box = tk.Listbox(window,height=20,width=50)
#         self.list_box.pack()
#
#         self.entry = ttk.Entry(window)
#         self.entry.pack()
#         self.btn = ttk.Button(window,text='add task',command=self.add_task)
#         self.btn.pack()
#         self.btn1 = ttk.Button(window, text='remove task',command=self.remove_task)
#         self.btn1.pack()
#
#     def add_task(self):
#         task = self.entry.get()
#         self.list_box.insert(tk.END,task)
#         self.entry.delete(0,tk.END)
#
#     def remove_task(self):
#         remove = self.list_box.curselection()
#         self.list_box.delete(remove)
#
#

# 38
#
# class calcator:
#     def __init__(self, window):
#         self.window = window
#         self.title = window.title('calculator')
#         self.geo = window.geometry('320x400')
#
#         self.even = ''
#
#         self.entry = ttk.Entry(window,font=50,width=26)
#         self.entry.grid(row=0, column=0, columnspan=4)
#
#         self.btn1 = ttk.Button(window, text='1', command=self.num1)
#         self.btn2 = ttk.Button(window, text='2', command=self.num2)
#         self.btn3 = ttk.Button(window, text='3', command=self.num3)
#         self.btn_sum = ttk.Button(window, text='+', command=self.num_sum)
#         self.btn4 = ttk.Button(window, text='4', command=self.num4)
#         self.btn5 = ttk.Button(window, text='5', command=self.num5)
#         self.btn6 = ttk.Button(window, text='6', command=self.num6)
#         self.btn_mainha = ttk.Button(window, text='-', command=self.nume_manha)
#         self.btn7 = ttk.Button(window, text='7', command=self.num7)
#         self.btn8 = ttk.Button(window, text='8', command=self.num8)
#         self.btn9 = ttk.Button(window, text='9', command=self.num9)
#         self.btn_zarb = ttk.Button(window, text='*', command=self.nume_zarb)
#         self.btnc = ttk.Button(window, text='C',command=self.delet_)
#         self.btn0 = ttk.Button(window, text='0', command=self.num0)
#         self.btne = ttk.Button(window, text='=', command=self.nume)
#         self.btn_taqsim = ttk.Button(window, text='/', command=self.nume_taqsim)
#
#         self.btn1.grid(row=1, column=0,padx=2,pady=2)
#         self.btn2.grid(row=1, column=1,padx=2,pady=2)
#         self.btn3.grid(row=1, column=2,padx=2,pady=2)
#         self.btn_sum.grid(row=1, column=3,padx=2,pady=2)
#         self.btn4.grid(row=2, column=0,padx=2,pady=2)
#         self.btn5.grid(row=2, column=1,padx=2,pady=2)
#         self.btn6.grid(row=2, column=2,padx=2,pady=2)
#         self.btn_mainha.grid(row=2, column=3,padx=2,pady=2)
#         self.btn7.grid(row=3, column=0,padx=2,pady=2)
#         self.btn8.grid(row=3, column=1,padx=2,pady=2)
#         self.btn9.grid(row=3, column=2,padx=2,pady=2)
#         self.btn_zarb.grid(row=3, column=3,padx=2,pady=2)
#         self.btnc.grid(row=4, column=0,padx=2,pady=2)
#         self.btn0.grid(row=4, column=1,padx=2,pady=2)
#         self.btne.grid(row=4, column=2,padx=2,pady=2)
#         self.btn_taqsim.grid(row=4, column=3,padx=2,pady=2)
#
#     def num1(self):
#         self.even += '1'
#         self.entry.delete(0, tk.END)
#         self.entry.insert(tk.END, self.even)
#
#     def num2(self):
#         self.even += '2'
#         self.entry.delete(0, tk.END)
#         self.entry.insert(tk.END, self.even)
#
#     def num3(self):
#         self.even += '3'
#         self.entry.delete(0, tk.END)
#         self.entry.insert(tk.END, self.even)
#
#     def num4(self):
#         self.even += '4'
#         self.entry.delete(0, tk.END)
#         self.entry.insert(tk.END, self.even)
#
#     def num5(self):
#         self.even += '5'
#         self.entry.delete(0, tk.END)
#         self.entry.insert(tk.END, self.even)
#
#     def num6(self):
#         self.even += '6'
#         self.entry.delete(0, tk.END)
#         self.entry.insert(tk.END, self.even)
#
#     def num7(self):
#         self.even += '7'
#         self.entry.delete(0, tk.END)
#         self.entry.insert(tk.END, self.even)
#
#     def num8(self):
#         self.even += '8'
#         self.entry.delete(0, tk.END)
#         self.entry.insert(tk.END, self.even)
#
#     def num9(self):
#         self.even += '9'
#         self.entry.delete(0, tk.END)
#         self.entry.insert(tk.END, self.even)
#
#     def num0(self):
#         self.even += '0'
#         self.entry.delete(0, tk.END)
#         self.entry.insert(tk.END, self.even)
#
#     def num_sum(self):
#         self.even += '+'
#         self.entry.delete(0, tk.END)
#         self.entry.insert(tk.END, self.even)
#
#     def nume_manha(self):
#         self.even += '-'
#         self.entry.delete(0, tk.END)
#         self.entry.insert(tk.END, self.even)
#
#     def nume_zarb(self):
#         self.even += '*'
#         self.entry.delete(0, tk.END)
#         self.entry.insert(tk.END, self.even)
#
#     def nume_taqsim(self):
#         self.even += '/'
#         self.entry.delete(0, tk.END)
#         self.entry.insert(tk.END, self.even)
#
#     def nume(self):
#         result = str(eval(self.even))
#         self.entry.delete(0, tk.END)
#         self.entry.insert(tk.END, result)
#         self.even = ''
#
#     def delet_(self):
#         self.entry.delete(0,tk.END)
#         self.even = ''
#
#
#
# if __name__ == '__main__':
#     window = tk.Tk()
#     app = calcator(window)
#     window.mainloop()

#
# 39
# class login:
#     def __init__(self,window):
#         self.window = window
#         self.title = window.title('login page')
#         self.geo = window.geometry('400x400')
#
#         self.entry1 = ttk.Entry(window)
#         self.entry2 = ttk.Entry(window)
#
#         self.label1 = ttk.Label(window,text='username:',font=('Areal',14))
#         self.label2 = ttk.Label(window,text='password:',font=('Areal',14))
#
#         self.btn = ttk.Button(window,text='login',command=self.login_func)
#         self.btn.place(x=160,y=130)
#
#
#         self.entry1.place(x=200,y=50)
#         self.entry2.place(x=200,y=80)
#
#         self.label1.place(x=100,y=45)
#         self.label2.place(x=100,y=75)
#
#     def login_func(self):
#
#         name = self.entry1.get()
#         pas = self.entry2.get()
#
#         if name == 'murtaza' and pas == '123':
#             messagebox.showinfo('error','login successful welcome murtaza')
#         elif name == '' or pas == '':
#             messagebox.showinfo('error','you should file all entry')
#         else:
#             messagebox.showinfo('error','not crcate')
# if __name__ == '__main__':
#     window = tk.Tk()
#     app = login(window)
#     window.mainloop()
#
#
# 40
# class weather:
#     def __init__(self,window):
#         self.window = window
#         self.title = window.title('weather app')
#         self.geo = window.geometry('400x400')
#
#         self.entry1 = ttk.Entry(window)
#         self.label1 = ttk.Label(window,text='Enter the place:',font=('Areal',12))
#
#         self.entry1.place(x=200,y=50)
#         self.label1.place(x=80,y=48)
#
#         self.btn = ttk.Button(window,text='search',command=self.weather_func)
#         self.btn.place(x=160,y=130)
#
#         self.label2 = ttk.Label(window,text='',font=('Areal',12))
#         self.label2.place(x=160,y=180)
#
#
#     def weather_func(self):
#         weather_lst = ['sun 25c', 'rani 14c', 'snow -5c', 'cloudy 0c']
#         self.label2.config(text=choice(weather_lst))


# class FillManage:
#     def file_read(self):
#         file = open('Home1.txt','wr')
#         print(file.read())
#
# f = FillManage()
# f.file_read()
