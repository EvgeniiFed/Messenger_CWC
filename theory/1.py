
b = 10
a = [1, 'qwe', True, None, b, [0, 1, 2, 3]]
print(a)
print(type(a))

print(a[0])
print(a[-1][3])
print(a[2:4])

print(sorted([5, 24, 5464, 4894]))

d = {
    'key': 'value',
    'name': 'John',
    'a': a
}
print(d)
print(d['name'])
print(d['a'][-1])