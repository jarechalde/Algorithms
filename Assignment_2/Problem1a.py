#We have two jars that are not broken k1,k2
k1 = 'Ok'
k2 = 'Ok'

bd = 11 #Breaking distance
n = 16 #In this case we have n rungs, where n = 16
r0 = r = 0 #Starting rung
m = 4 #We divide our rungs in 4 equal parts


while(k1 == 'Ok'):
 r0 = r
 r = r0 + n/m
 print('Current rung: %i' %r)
 if(r>bd):
  k1 = 'RIP'
  print('k1 Broke\n')

#The safest rung before break point will be
r = r0

while(k2 == 'Ok'):
 r = r+1
 print('Current rung: %i' %r)
 if(r>bd):
   k2 ='RIP'
   print('k2 Broke\n')
   sr = r-1
   print('Safest rung distance: %i' %sr)



