#The array we are going to work with
S = [1,5,4,8,10,2,6,9,12,11,3,7]

inv = 0

def countsinv(array,inv):

 #If the length of the array is greater than two, we divide it in two
 if len(array)>2:

  mid = len(array)/2

  arrayL = array[0:mid]
  arrayR = array[mid:len(array)]

  #We recursively divide our problem
  L_arr,linv = countsinv(arrayL,inv)
  R_arr,rinv = countsinv(arrayR,inv)

  #We add up the two returned inversions
  inv = linv + rinv
 
  #Initializing counters
  i = 0
  j = 0

  #This is the array in which we are going to merge sort the two given arrays
  Sort_arr = []

  for k in range(0, len(R_arr)+len(L_arr)):

   #If we already completed adding the L_arr, or the R_arr, we add the opposite one
   if i == len(L_arr):
    Sort_arr.append(R_arr[j])
    j = j + 1
    continue

   if j == len(R_arr):
    Sort_arr.append(L_arr[i])
    i = i + 1
    continue

   if L_arr[i]<R_arr[j]:
    Sort_arr.append(L_arr[i])
    i = i + 1
    continue

   else:
    if L_arr[i]>2*R_arr[j]:
     inv = inv + len(L_arr)-(i) #If the position j of the array in the left is greater than the position i in the array on the right, that means that the rest of the numbers on the list will be greater too as the list is sorted
    Sort_arr.append(R_arr[j])
    j = j + 1

  #We return the sorted list and the number of inversions
  return Sort_arr,inv

 #If the length of the array is one, we just return it
 elif len(array)==1:
  return array,inv

 #Otherwise, if the length of the array is 2, we check if the array is sorted or not
 else:
  if array[0]<array[1]:
   return [array[0],array[1]],inv
  else:
   if(array[0]>2*array[1]):
    inv = inv + 1
   return [array[1],array[0]],inv


Sort_arr,n_inv = countsinv(S,inv)
print("Number of significant inversions: %i" %n_inv)