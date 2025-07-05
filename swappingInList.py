l = [1,2,3,4,5]
# l[0],l[4]=l[4],l[0]
# l[1],l[3]=l[3],l[1]
# print(l)

temp = l[0]
l[0]=l[4]
l[4]=temp

print(l)