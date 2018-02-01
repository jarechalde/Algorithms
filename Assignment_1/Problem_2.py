men = ['V','W','X','Y','Z']
women = ['A','B','C','D','E']

#Men's preferences
vpref = ['B','A','D','E','C']
wpref = ['D','B','A','C','E']
xpref = ['B','E','C','D','A']
ypref = ['A','D','C','B','E']
zpref = ['B','D','A','E','C']

#Create a dictionary to store men's preferences
menpref = {'V':vpref,'W':wpref,'X':xpref,'Y':ypref,'Z':zpref}

#Woman's preferences and inverses
#V=0.W=1.X=2.Y=3.Z=4
apref = ['Z','V','W','Y','X']
apref = [4,0,1,3,2]

bpref = ['X','W','Y','V','Z']
bpref = [2,1,3,0,4]

cpref = ['W','X','Y','Z','V']
cpref = [1,2,3,4,0]

dpref = ['V','Z','Y','X','W']
dpref = [0,4,3,2,1]

epref = ['Y','W','Z','X','V']
epref = [3,1,4,2,0]

ainv = [None]*len(apref)
binv = [None]*len(bpref)
cinv = [None]*len(cpref)
dinv = [None]*len(dpref)
einv = [None]*len(epref)

for i in range(0,len(apref)):
 ainv[apref[i]] = i
 binv[bpref[i]] = i
 cinv[cpref[i]] = i
 dinv[dpref[i]] = i
 einv[epref[i]] = i

print(ainv,binv,cinv,dinv,einv)


#Create a dictionary to store women's preferences
womenpref = {'A':ainv, 'B':binv, 'C':cinv, 'D':dinv, 'E':einv}

#We will use two dictionaries to check man and woman availability
manav = dict(zip(men,[1]*len(men)))
womanav = dict(zip(women,[1]*len(women)))

#Engage dictionary, we will use woman as a key to help check the womans preference
eng = {'A':None,'B':None,'C':None,'D':None,'E':None}

#Implementation of the propose and reject algorithm

def engagement(men):

 menav = len(men)

 menindex = ['V','W','X','Y','Z']

 while menav>0:
  for man in men:
   print('Engaging man: %s' %man)
   while manav.get(man) == 1:
    #We propose to one woman
    for i in range(0,len(menpref.get(man))):
     #Now we start proposing to every woman on the list
     pref = menpref.get(man)
     #The current woman we are proposing to
     woman = pref[i]
     #If the woman is not engaged, they get automatically engaged
     if womanav.get(woman)==1:
      print('%s engaged to %s\n' %(man,woman))
      #Engage that man and woman
      eng[woman] = man
      #Set that man's and woman's availability to 0
      manav[man] = 0
      womanav[woman] = 0
     
      menav = menav - 1
     
      #Break the for loop and go to the next man
      break
     #If the woman is already engaged we will have to check the womans preference list
     else:
      currentengman = eng.get(woman)
      print('%s already engaged to: %s' %(woman,currentengman))
      #His position in the list
      #men.index(..) gives us the man number to use in the inverse
      posnew = womenpref.get(woman)[menindex.index(man)]
      poseng = womenpref.get(woman)[menindex.index(currentengman)]

      print(womenpref.get(woman))
      print('Index Eng: %i'%menindex.index(currentengman))
      print('New: %i Eng: %i' %(posnew,poseng))

      #If this man is higher in the list of pref. than the other man we dump the current one and 
      #engage her with this one
      if posnew<poseng:
       print('Updating Engagement')
       print('%s engaged to %s\n' %(man,woman))

       #Engage that man and woman
       eng[woman] = man

       #We set this mans availability to 0 and the old engaged man to 1
       manav[man] = 0
       manav[currentengman] = 1

       #Append the man to the end of the list so we have to iterate over him again
       men.append(currentengman)
    
       break
 
       #Engage them
       eng[woman] = man

      #If this man is lower in the list that the man the woman is already engaged with,
      #this man will try to engage to the next woman on the list
      else:
       continue

 #We print the final results
 print(eng)

#Calling the function
engagement(men)

###Changing the man order of proposal###

#In this case the order of man proposing goes from Z to V instead
men2 = ['Z','Y','X','W','V']

#We reset the engage dictionary
eng = {'A':None,'B':None,'C':None,'D':None,'E':None}

#Reset the availability dictionary
manav = dict(zip(men2,[1]*len(men2)))
womanav = dict(zip(women,[1]*len(women)))

#Update the inverse

#Reversing the inverses
#ainv = ainv[::-1]
#binv = binv[::-1]
#cinv = cinv[::-1]
#dinv = dinv[::-1]
#einv = einv[::-1]
#womenpref = {'A':ainv, 'B':binv, 'C':cinv, 'D':dinv, 'E':einv}

engagement(men2)

###Another different implementation###

#What if women were proposing to men instead?

