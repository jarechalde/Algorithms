#Low stress jobs
l = [10,1,80,10,10,35]

#High Stress jobs
h = [5,50,160,300,1,40]

length = len(l)

#Initializing the revenue to 0
rev = [0]*length

#Adding 0 to the array
l.append(0)
h.append(0)

#Rest and skip variable
rest = 0
skip = 0

#Initializing some values
rev[0] = 0
rev[1] = max(l[0],h[0])

for i in range(1,length):
 
 #If we chose to rest, we skip this iteration
 if rest == 1:
  if h[i+1]>h[i]+l[i+1]:
   print('HEREE')
   rev[i] = rev[i-1]+h[i+1]+l[i-1]
   rest = 0
   skip = 1
   continue
  else:
   print('AQUI')
   rev[i] = rev[i-1]+h[i]
   rest = 0
  continue

 print(i)
 print(l[i],l[i+1])
 if h[i+1]>(l[i]+l[i+1]):
  print('Resting and choosing the high stress job')
  rest = 1
 #Else we choose the low stress job
 else:
  print("Choosing the low stress job")
  rev[i] = rev[i-1]+l[i]
  
print(rev)
