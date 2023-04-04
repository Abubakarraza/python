# Set Method 

# Joining set

# Sets in python more or less work in the same way as sets in mathematics. We can perform operation like union and intersection on the sets just like in mathematics

# union() and update()

# The union() and update methods prints a all items that are present in the sets.The union() method return a new set whereases update method add items into the existing set from another set

fruits ={"apple","banana","grapes"}

fruits2={"banana","strawberry","kiwi"}

fruits3=fruits.union(fruits2)

print('fruits:',fruits3)

print(fruits,fruits2)

# in union method result will be save in new variable it can't update old set (example above 👆)

fruits2.update(fruits)
print("fruits2:",fruits2)
# in update method result will be update the fruits2 (example above 👆)


# intersection() and intersection_update()

# Intersection : intersection give the result of common set value in two set

cities={"fsd","lhr","isb","karachi"}

cities2={"lhr","isb","gjr","multan"}

cities3 = cities.intersection(cities2)
# the result will save in new var
print("cities3:",cities3)

cities.intersection_update(cities2)
# it will update the cities
print("cities:",cities)



# Symmetric_difference() and symmetric_difference_update()

# The symmetric difference and symmetric difference_update() method print only items that are not similar to both the sets. The symmetric_difference method returns a new set whereas symmetric_difference_update into the existing set from another set.

country = {"pakistan","india","afghanistan","china"}
country2={"india","afghanistan"}

country3 = country.symmetric_difference(country2)

print("country3:",country3)

country.symmetric_difference_update(country2)
print("country:",country)


# difference() and difference_update()

# The difference() and difference_update() method prints only items that are only present in the original set and not in both the sets .The difference method returns a new set whereas difference_update() method return into the existing set from another set.

color={"red","green","blue","yellow","black"}

color2={"red","purple","yellow","brown"}

color3=color.difference(color2)

print('color3:',color3)

color.difference_update(color2)

print("color:",color)



# set Methods

# There are several in built method used for the manipulation of set. They are explained below

# isdisjoint():

# The isdisjoint() method checks if items of given set are present in another set. This method return false if items are  present , else it return True

num={1,3,4,5}
num2={1,3}
print("isDisjoint:",num.isdisjoint(num2))


# issuperset():

# The issuperset() method checks if all the items of a particular set are present in the original set. It returns True if all the items are present , else it return False

no={1,2,3,4,5,6,7,8}

no2={4,6,8,1}

print("isSuperset:",no.issuperset(no2))

# it return true because all items in no2 are present in no😊


# add()

# if you want to add a single item to the set use the add() method.

numb={1,3,4,5}
numb.add(8)
print("add number:",numb)


# update()

# if you want to add more than one item , simply create another set or any other iterable object(list,tuple,dictionary), and use the update() method to add it into the existing set

numb2={6,7,9}

numb.update(numb2)

print("number:",numb)


# remove()/discard()

# We can use remove() and discard() method to remove items from the set

numb.remove(9)

print("after Remove:",numb)

# The main difference between remove and discard is that, if we try to delete an item which is not present in set , then remove raises an error , whereas discard() does not raise any error