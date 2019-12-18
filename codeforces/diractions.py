xy=input().split()
s=input().lower()
x=int(xy[0])
y=int(xy[1])
for letter in s:
    if letter=='u':
        y+=1
    elif letter == 'd':
        y+=1
    elif letter == 'l':
        x-=1
    elif letter == 'r':
        x+=1
print(f'{x} {y}')
