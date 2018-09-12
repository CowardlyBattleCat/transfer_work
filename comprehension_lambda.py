lst = [2,5,-3, 4, 7, 9, -6]

sqrlist = [i**2 for i in lst if i%2 == 0]

print(sqrlist)


a = [(x, y) for x in range(1,5) for y in range(1,5)]
print(a)
#set comprehension
b = {(x, y) for x in range(1,5) for y in range(1,5)}
print(b)
#dictionary comprehension
c = {x: x**2 for x in range(-10, 11)}
print(c)

s = "we went to the store and helped people"

d = [r.lower() for r in s.split()]
print(d)

#map function
items = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, items))
print(squared)

number_list = range(-5, 5)
less_than_zero = list(filter(lambda x: x < 0, number_list))
print(less_than_zero)
