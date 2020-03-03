if 17126357862491 % 3 == 0:
    print(0)
elif 17126357862491 % 3 == 1:
    print(1)
else:
    print(2)

password = 'qqq'
default_password = '5645467456163'

result_password = password if len(password) > 0 else default_password

print(result_password)

i = 0
while i < 10:
    print(i)
    # i = i + 1
    i += 1
print('Finish while loop')
print('-' * 100)

a = [1, 'qwe', True, None, 10, [0, 1, 2, 3]]

for i in range(10):
    print(i * i)

squares = [i * i for i in range(10) if i % 2 == 0]
print(squares)