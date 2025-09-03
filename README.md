#converting chains to other functions.
print("Welcome to using the NYC Subway distance converter!")
print(" ")
chains = float( input ("please enter distance in chains"))

#making all the converstions.

feet = chains * 66
meters = feet * 0.3048
miles = feet / 5280
kilometers = meters / 1000
time = (miles / 3.1) * 60

#editing to make it round to certain decmial places to make it easier to read.

feet = round(feet,2)
meters = round(meters, 2)
miles = round(miles, 3)
kilometers = round(kilometers, 3)
time = round(time, 1)
print ("distance:", chains, "chains")
print ("meters:", meters)
print ("feet:", feet)
print ("miles:", miles)
print ("kilometers:", kilometers)
print ("minutes:", time)
print ("thank you for using the converter. Goodbye!")
