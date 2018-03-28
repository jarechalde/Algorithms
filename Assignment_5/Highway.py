
x = [1,10,13,14,20,23,28,30,36,40]
r = [10,3,4,20,10,7,6,3,10,20]

n = len(x)

#Initialize M
M = [0]*(n+1)

#Initializing M[0] and M[1]
M[0] = 0
M[1] = r[0]

for j in range (2,n+1):
 print('j = %i' %j)
 print('Distance to the previous point: %i' %(x[j-1]-x[j-2]))
 if x[j-1]-x[j-2]>=5:
  M[j] = M[j-1]+r[j-1]
  print('M[%i] = %i' %(j,M[j]))
  print('\n')
 else:
  #Look for the eastmost valid
  print('Looking for the eastmost valid value')
  for i in range(j-1,-1,-1):
   print('%i-%i>=5?' %(x[j-1],x[i-1]))
   if x[j-1]-x[i-1]>=5:
    print('YES')
    print('M[%i]+%i>M[%i]?' %(i,r[j-1],j-1))
    if M[i]+r[j-1]>M[j-1]:
     print('YES')
     print('M[%i] = M[%i] + %i' %(j,i,r[j-1]))
     M[j] = M[i]+r[j-1]
     print('M[%i] = %i' %(j,M[j]))
     print('\n')
    else:
     print('NO')
     print('M[%i] = M[%i]' %(j,j-1))
     M[j] = M[j-1]
     print('M[%i] = %i' %(j,M[j]))
     print('\n')
    break
   else:
    print('NO')

print('MAXIMUM REVENUE: %i' %M[n])
