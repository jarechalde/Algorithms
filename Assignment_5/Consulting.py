#Low stress jobs
l = [10,1,80,10,10]

#High Stress jobs
h = [5,50,90,5,1]

length = len(l)

#Initializing the revenue to 0
rev = 0

#Adding 0 to the array
l.append(0)
h.append(0)

#Rest variable
rest = 0

for i in range(0,length):
 
 #If we chose to rest, we skip this iteration
 if rest == 1:
  if h[i+1]>h[i]+l[i+1]:
   rev = rev+h[i+1]+l[i-1]
   rest = 0
   continue
  else:
   rev = rev+h[i]
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
  rev = rev+l[i]
  
print(rev)
