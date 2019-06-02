factorlist = []
for x in range(1,1000): 
    if x % 3 == 0: 
        factorlist.append(x)
    elif x % 5 == 0: 
        factorlist.append(x)
print (factorlist)
output = sum(factorlist)
print (output)