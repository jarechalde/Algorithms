#We will first create a  list that contains the participants in the competition
#and their swimming time, biking time, and running time
contestants = [
(1,2,3), #Contestant #1
(2,3,10), #...
(4,5,3)  #Contestant #N
]

#Deadlines list
deadline = [0]*len(contestants)

#We calculate the total deadline for each one of the contestants
for i in range(0,len(contestants)):
 contestant = contestants[i]
 deadline[i] = sum(contestant)

#We print our results
print(deadline)

def quicksort(array):
 upperlist = []
 lowerlist = []
 pivotlist = []

 #If the length of the array is 1 it doesnt need sorting of any kind
 if len(array)<=1:
  return array
 
 #Else, we will separate the list into the upper elements and lower
 else:
  pivot = array[0]

  for i in range(0,len(array)):
   element = array[i]

   if element<pivot:
    lowerlist.append(element)
   elif element>pivot:
    upperlist.append(element)
   else:
    pivotlist.append(element)

  upperlist= quicksort(upperlist)
  lowerlist = quicksort(lowerlist)


 return lowerlist + pivotlist + upperlist

#We will return an array with the indexes in the order that they need to be accessed
schedule = quicksort(deadline)
print(schedule)
