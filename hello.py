msg = "Hello World!"
print(msg)

type(4.5)

print(msg[0])
print(msg[-1])

print(msg[1:3])

print(f"Print this {msg}")

my_list = [[1, 2, 3], [4, 5, 6]]

print(my_list[0][1])

print(len(my_list[0]))

my_list1 = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
my_list1.append("j")

print(my_list1[1:3])
print(my_list1[1:len(my_list1):2])

my_tuple = (4, 4, 5, 6, 6, 7, 8, 9, 10)

print(my_tuple.count(6))
print(my_tuple.index(7))

a, b = 1, 2

print(f"{a}, {b}")

a, b = b, a

print(f"{a}, {b}")

my_dict = {"a": 1, "b": 2, "c": 3}

print(my_dict["a"])

my_dict["b"] = 22 

print(my_dict["b"])

favorite_season = "Summer"

if favorite_season == "Summer":
    print("That is my favorite season too!")

x = 15

if x > 9:
    print("Hello!")
else:
    print("Bye!")

print("End")

x = 5

if x < 9:
    print("Hello!")
elif x < 15:
    print("It's great to see you")
else:
    print("Bye!")

print("End")

for i in range(5):
    print(i)

for num in range(8):
	print("Hello" * num)
     
for_my_list = ["a", "b", "c", "d"]

for i in range(len(for_my_list)):
	print(for_my_list[i])
     
for i in range(2, 10):
	print(i)
     
for i in range(2, len(for_my_list)):
	print(for_my_list[i])
     
message = "Hello, World!"

for char in message:
	print(char)
      
my_list2 = [1, 2, 3, 4, 5]

for elem in my_list2:
	if elem % 2 == 0:
		print("Even:", elem)
		print("break")
		break
	else:
		print("Odd:", elem)

for elem in my_list2:
	if elem % 2 == 0:
		print("continue")
		continue
	print("Odd:", elem)
	
my_list11 = [1, 2, 3, 4]
my_list22 = [5, 6, 7, 8]

for elem1, elem2 in zip(my_list11, my_list22):
	print(elem1, elem2)
	
for i, elem in enumerate(my_list22):
	print(i, elem)
	
word = "Hello"

for elem11 in my_list11:
    if elem11 > 6:
        print("Found")
        break
else:
    print("Not Found")
	

x = 6

while x < 15:
	print(x)
	x += 1
	
x = 5

while x < 15:
	if x % 2 == 0:
		print("Even number found")
		break
	print(x)
	x += 2
else:
	print("All numbers were odd")

for i in range(3):
	for j in range(2):
		print(i, j)
		
def print_pattern():
    size = 4
    for i in range(size):
        print("*" * size)
		
print_pattern()

def get_rectangle_area(length, width):
    return length * width

area = get_rectangle_area(4, 5)

print(area)

def get_first_even(seq):
    for elem in seq:
        if elem % 2 == 0:
            return elem
    else:
        return None
	
value2 = get_first_even([3, 5, 7, 9])
print(value2)

# index = int(input("Enter the index: "))

# try:
#     my_list = [1, 2, 3, 4]
#     print(my_list[index])
# except:
#     print("Please enter a valid index.")

class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"woof-woof. I'm {self.name}")

    @property
    def name(self):
        print("Calling getter")
        return self._name

    @name.setter
    def name(self, new_name):
        print("Calling setter")
        self._name = new_name

    @name.deleter
    def name(self):
        print("Calling deleter")
        del self._name

my_dog = Dog("Nora", 10)

print(my_dog.name)

my_dog.age = 20
print(my_dog.age)

print(my_dog.bark())