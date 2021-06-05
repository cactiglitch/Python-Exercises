cars = 100 #int
space_in_car = 4.0 #float
drivers = 30 #int
passengers = 90 #int
cars_not_driven = cars - drivers #int
cars_driven = drivers #int
carpool_capacity = cars_driven * space_in_car #float
average_passengers = passengers/cars_driven #float

print("There are", cars, " cars available. ")
print("There are only", drivers, " drivers available.")
print("There will be", cars_not_driven, " empty cars today." )
print("We can transport", carpool_capacity, " people today.")
print("We have", passengers, " to carpool today.")
print("We need to put about", average_passengers, " in each car.")

