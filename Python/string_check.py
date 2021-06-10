s=input()
flag=0
for x in range(0, len(s), 2):
    if s[x].isupper():
        flag=flag+1
        break
for x in range(1, len(s), 2):
    if s[x].islower():
        flag=flag+1
        break

if(flag==0):
    print("Yes")
else:
    print("No")
