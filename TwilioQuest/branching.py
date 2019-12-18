from sys import argv
x= float(argv[1])
y=float(argv[2])
sum =x+y
if 0>=sum:
    print('You have chosen the path of destitution.')
elif sum in range(1,101,1) :
    print('You have chosen the path of plenty.')
elif sum>100:
    print('You have chosen the path of excess.')
