# a=10
# b=a
# print(id(a))
# print(id(b))
# b=11
# a=b
# print(id(a))
# print(id(b))

a={"value":2}
b=a
print(id(a))
print(id(b))
c={"value":10}
b=c
a=b
print(id(a))
print(id(b))
print(id(b))
print(a,b,c)


