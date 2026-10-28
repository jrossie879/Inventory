def first_program():
    print("My name is jeremiah rossie")
    print("I am Learning programming")
    print("Python is my first programming language")

first_program()




name = "Jeremiah Rossie"
print(name)



age = 25
print(age)




name = "Jeremiah Rossie"
print("My name is " + name)




name = "Jeremiah Rossie"
age = 25
language = "I am Learning python"
print("My name is " + name)
print("I am " + age + "years old")
print(language)




price = 50
quantity = 4
print(price * quantity)




price = 100
quantity = 3
Discount = 20

total_price = (price * quantity)
subtotal = total_price - Discount
print(subtotal)



city = "Port Harcourt"
country = "Nigeria"
print("I live in " + city + ", " + country)




name = "Jeremiah Rossie"
age = 25
city = "Port Harcourt"
print("My name is " + name)
print("I am " + str(age) + " years old" )
print("I live in " + city)


name = input("type name: ")
city = input("type city: ")
print("Hello " + name)
print("I live in " + city)



city = input("type city: ")
print("I live in " + city)





name = "Jeremiah"
age = 25
price = 50.5
is_learning = True
print(name)
print(age)
print(price)
print(is_learning)




number = "50"
number = int(number)
print(number + 25)



price = "10.5"
price = float(price)
print(price + 5.5)


number = 100
number = str(number)
print("My number is " + number)



age = 20
if age >= 18:
    print("You are an adult")




age = 16
if age >= 18:
    print("Youre an adult")
else:
    print("Youre not adult")




age = 25
if age >= 18:
    print("You are an adult")
else:
    print("You are not an adult")




score = 65
if score >= 70:
    print("Excellent")
elif score >= 50:
    print("Pass")
else:
    print("Fail")


count = 2
while count <= 10:
    print(count)
    count = count + 2



for number in range(10, 0, -1):
    print(number)