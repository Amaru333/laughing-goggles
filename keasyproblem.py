a=int(input())
b=list(map(int,input().split()))
c=b.count(1)
if c>=1:
    print("HARD")
else:
    print("EASY")
