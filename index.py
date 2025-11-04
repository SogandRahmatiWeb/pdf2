x = 5
print(type(x)) 


# تنظیم نوع داده
x = "Hello World"
#display x:
print(x)
 #display the data type of x:
print(type(x))

x = ["apple", "banana", "cherry"]
 #display x:
print(x)
 #display the data type of x:
print(type(x))

x = 20
 #display x:
print(x)
 #display the data type of x:
print(type(x))

x = frozenset({"apple", "banana", "cherry"})
 #display x:
print(x)
 #display the data type of x:
print(type(x))

#   تنظیم نوع داده خاص

x = str("Hello World")
 #display x:
print(x)
 #display the data type of x:
print(type(x)) 

x = list(("apple", "banana", "cherry"))
 #display x:
print(x)
 #display the data type of x:
print(type(x))

x = int(20)
 #display x:
print(x)
 #display the data type of x:
print(type(x))

x = bool(5)
 #display x:
print(x)
 #display the data type of x:
print(type(x))

# قالب بندی رشته 
age = 36
 #This will produce an error:
txt = "My name is John, I am " + age
print(txt) 

age = 36
txt = f"My name is John, I am {age}"
print(txt)

#  بولین های پایتون
a = 200
b = 33
if b > a:print("b is greater than a")
else:print("b is not greater than a")