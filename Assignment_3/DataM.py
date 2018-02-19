#These are the two sets that we want to compare
s1 = ['buy Yahoo','buy eBay','buy Yahoo','buy Oracle']
s2 = ['buy Amazon','buy Yahoo','buy eBay','buy Yahoo','buy Yahoo','buy Oracle']

def comp(s1,s2):

 #Getting the length of the two sets
 l1 = len(s1)
 l2 = len(s2)

 #We initialize the operators
 ipos = 0
 jpos = 0

 while(jpos<l2-1):
  el1 = s1[ipos]
  for j in range(jpos,l2):
   el2 = s2[j]

   #If the element is in that position of the list...
   if el1==el2:
    if(ipos==l1-1):
     ipos = ipos+1
     print("S1 is a subset of S2")
     return
    elif(ipos!=l1):
     ipos = ipos+1
     jpos = j
     break #We exit the for loop

   #If we cant find the element in that position of the list
   #We move to the next element
   elif(el1!=el2):
    jpos = j
    continue

 #If the loop above didn't return that S1 is a subset of S2
 # we print the opposite
 print('S1 is not a subset of S2')
 return

comp(s1,s2)
