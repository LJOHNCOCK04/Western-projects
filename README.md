#program: converting chains to other functions.
# name: Leemon Johncock
print("Welcome to using the NYC Subway distance converter!")
print()#using to create spaces
chains = float( input ("please enter distance in chains ")) #changing to a float so can be multiplied with decimals
print()#using to create spaces
#all constants. I know this is a bit pointless to make a constant for everything.
AWS = 3.1 #AWS is Average walk speed for a human.
one_hour_in_minutes = 60
mile_in_feet = 5280
feet_in_a_chain = 66
meter_in_feet = .3048
meters_in_a_kilometer = 1000
#making all the converstions. doing this from given converstions
feet = chains * feet_in_a_chain                                 # turning chains to feet
meters = feet * meter_in_feet                                   # getting meters from feet and .3048
miles = feet / mile_in_feet                                     # getting the miles from the feet being divided by 5280
kilometers = meters / meters_in_a_kilometer                     # fiding kilometers from meters divied by 1000
time = (miles / AWS) * one_hour_in_minutes                      # getting the time from miles divied by the AWS of a human

#editing to make it round to certain decmial places to make it easier to read and required in the rubric.

feet = round(feet,3)                                             # rounding to 3 decial place for all besides time. Time walking is rounded to one decimal place.
meters = round(meters, 3)
miles = round(miles, 3)
kilometers = round(kilometers, 3)
time = round(time, 1)
#final print to show converstions for user.
print ("distance:", chains, "chains")
print ("meters:", meters)
print ("feet:", feet)
print ("miles:", miles)
print ("kilometers:", kilometers)
print ("minutes:", time)
print() #using to create spaces
print ("thank you for using the converter. Goodbye!")

