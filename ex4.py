# Define 100 cars
cars = 100
# Define the space in a car , and it is a floating point
space_in_a_car = 4.0
# Define the numbers of drivers
drivers = 30
# Define the numbers of passengers
passengers = 90
# the numbers of empty cars
cars_not_driven = cars - drivers
# the numbers of driving cars
cars_driven = drivers
# the capacity about working cars
carpool_capacity = cars_driven * space_in_a_car
# the average passenger numbers in each car
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."