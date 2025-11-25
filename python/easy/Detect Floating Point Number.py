T = int(input())
num= 0

while num < T:
    num+=1
    N = input().strip()
    try:
        float(N)      
    except ValueError:
        print(False)
        continue      

    if N.endswith('.'):
        print(False)
        continue

    if N.count('.') != 1:
        print(False)
        continue
        
    print(True)
