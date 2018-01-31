men = ['V','W','X','Y','Z']
women = ['A','B','C','D','E']

#Men's preferences
vpref = ['B','A','D','E','C']
wpref = ['D','B','A','C','E']
xpref = ['B','E','C','D','A']
ypref = ['A','D','C','B','E']
zpref = ['B','D','A','E','C']

#Woman's preferences
apref = ['Z','V','W','Y','X']
bpref = ['X','W','Y','V','Z']
cpref = ['W','X','Y','Z','V']
dpref = ['V','Z','Y','X','W']
epref = ['Y','W','Z','X','V']

#We will use two dictionaries to check man and woman availability
manav = dict(zip(men,[1]*len(men)))
print(manav)
#womanav = []

###Do not forget to implement the efficient algo###

#Implementation of the propose and reject algorithm

for man in men:
 print(man)

###Changing the man order of proposal###

#In this case the order of man proposing goes from Z to V instead

###Another different implementation###

#What if women were proposing to men instead?

