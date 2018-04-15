#Supplies
s = [11,9,9,12,12,12,12,9,9,11]

#Rate per pound in company A
r = 1

#Fixed rate per week for company B
c = 10

#Initializing the best possible cost array
sch = [0]*(len(s)+1)
sch[0] = 0

#Schedule list
bestsch = [0]*(len(s)+1)
bestsch[0] = '0'

for i in range(0,len(s)):
 p = i+1
 if i<3:
  sch[p] = sch[p-1]+s[i]*r
  bestsch[p] = bestsch[p-1]+'A'
 else:
  if ((sch[p-1]+s[i]*r)-sch[p-4])>4*c:
   sch[p]=sch[p-4]+4*c
   bestsch[p] = bestsch[p-4]+'BBBB'
  else:
   sch[p]=sch[p-1]+r*s[i]
   bestsch[p] = bestsch[p-1]+'A'

print(sch)
print(bestsch[p])
