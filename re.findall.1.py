import re
x="my 2 favourite numbers are 19 and 42"
y =re.findall("[0-9]+",x)
print("y is ",y)
p=re.findall("[a-z 0-9]",x)
print("p is " ,p)
z =re.findall("[aeiou]",x)
print("z is" ,z)