
def check_list(a):
    for elem in a:
        if elem < 0:
            print('Bad', elem)
            return False
    return True


print(check_list([1, 3, 4, 6]))
print(check_list([1, 3, -4, 6]))