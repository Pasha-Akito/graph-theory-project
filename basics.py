# Python Basics
print("Hello world")

a = 1
b = 1.0
s = "hello from 'a' string"
t = '"hello" from a different string'

print(a, b, s, t)

print(type(s))

print(s[0:2]) #prints he. substring(0,2)

print(s[3:10:1]) #for(int i = 3; i < 10; i++) return i;

x = [1, 2, 3, "Hello", 1.0]
print(x) # [1, 2, 3, 'Hello']
#print(x[0])
#print(x[2])
#print(x[-1])

for i in x[::2]:
    print(i)
    print(i + i)


#for i in range(10):
#    print(i)

d = {"no_wheels": 4, "make": "Skoda"}
print(d["no_wheels"])
print(d["make"])

d["model"] = "Superb"

print(d["model"])

r = [1,2,3,4]
print(r)

s = [i * i for i in r]
print(s)
