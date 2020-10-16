name = "John"
age = "35"

print("There was once a man named " + name + ", ")
print("he was " + age + " years old")

name = "Carl"
newAge = 25
isAdult = True
print(name + " is " + format(int(newAge)) + ".")

txt = "For only {price:.2f} dollars!"

print(txt.format(price = 49))