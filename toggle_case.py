x="AvaNI"
s=""
i=0
while i<len(x):
    print(x[i])
    if x[i].islower():
        s+=x[i].upper()
    else:
        s+=x[i].lower()
    i+=1
print(s)