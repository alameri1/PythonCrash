import sys

x=sys.argv[1]
y=sys.argv[2]
def hail_friend(name):
    print(f'Hail, {name}')
def add_numbers(ar1, ar2):
    sum = int(ar1)+int(ar2)
    print(sum)
    return sum
add_numbers(x, y)
