#Here is the list of all the elements
n = {1:None,2:None,3:None,4:None}

#Possible tuples
m = [(1,2,'S'),(1,3,'D'),(1,4,'S'),(2,3,'D'),(2,4,'S'),(3,4,'S')]

for tuple in m:
 t0 = tuple[0]
 t1 = tuple[1]
 assign = tuple[2]

 print(n)

 #If both of them has a group assigned
 if n[t0] != None and n[t1] != None:
  if assign == 'S':
   if n[t0] == n[t1]:
    continue
   else:
    print('Inconsistency in tuple: ',tuple)
    break
  elif assign == 'D':  
   if n[t0] != n[t1]:
    continue
   else:
    print('Inconsistency in tuple: ',tuple)
    break

 #If one of them has a group assigned
 elif n[t0] != None or n[t1] != None:
  if n[t0] != None:
   if assign == 'S':
    n[t1] = n[t0]
    continue
   elif assign == 'D': 
    if n[t0] == 'A':
     n[t1] = 'B'
     continue
    else:
     n[t1] = 'A'
     continue
  elif n[t1] != None:
   if assign == 'S':
    n[t0] = n[t1]
    continue
   elif assign == 'D':
    if n[t0] == 'A':
     n[t1] = 'B'
     continue
    else:
     n[t1] = 'A'
     continue

 #If none of them have a group assigned
 elif n[t0] == n[t1] == None:
  if assign == 'S':
   n[t0] = 'A'
   n[t1] = 'A'
   continue
  else:
   n[t0] = 'A'
   n[t1] = 'B'
   continue
