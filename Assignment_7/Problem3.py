D1 = [0,4,5,6,7,8,20,22,34,56]
D2 = [3,5,45,60,65,66,70,78,79,90]

n = len(D1)

c1 = 0
c2 = 0

valn = 0
valn1 = 0

for i in range(0,n+1):
 print(i)
 print(c1,c2)
 valn = valn1
 if D1[c1]<D2[c2]:
  valn1 = D1[c1]
  c1 = c1 + 1
 else:
  valn1 = D2[c2]
  c2 = c2 + 1

print(valn,valn1)
median = (valn+valn1)/2.
print('The median value is: %f' %median)
