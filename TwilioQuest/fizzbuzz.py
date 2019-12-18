import sys
for i in range(len(sys.argv)-1):
    if (int(sys.argv[i+1])%3==0) and (int(sys.argv[i+1])%5==0) :
        print('fizzbuzz')
        continue 
    elif int(sys.argv[i+1])%5==0 :
        print('buzz')
        continue
    elif int(sys.argv[i+1])%3==0 :
        print('fizz')
    else:
        print(sys.argv[i+1])
    
