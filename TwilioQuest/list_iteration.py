from sys import argv
for person in range(len(argv)-1) :
    print(f'{person+1}. {argv[person+1]}')
