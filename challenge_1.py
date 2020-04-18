# CHALLENGE PROBLEMS
# YOU MAY NOT USE ANY ADDITIONAL LIBRARIES OR PACKAGES TO COMPLETE THIS CHALLENGE

# Divvy is Chicago's bike share system, which consists of almost 600 stations scattered
# around the city with blue bikes available for anyone to rent. Users begin a ride by removing
# a bike from a dock, and then they can end their ride by returning the bike to a dock at any Divvy 
# station in the city. You are going to use real data from Divvy collected at 1:30pm on 4/7/2020 
# to analyze supply and demand for bikes in the system. 

# import data

import json
divvy_stations = json.loads(open('divvy_stations.txt').read())

# PROBLEM 1
# find average number of empty docks (num_docks_available) and 
# available bikes (num_bikes_available) at all stations in the system

total_num_docks = 0
for item in divvy_stations:  
     a = item['num_docks_available'] # extract from the dict
     total_num_docks = a + total_num_docks
     avg_num_docks = total_num_docks/len(divvy_stations)
print(avg_num_docks)

total_ava_num_bikes = 0
for item in divvy_stations:  
     b = item['num_bikes_available'] # extract from the dict
     total_ava_num_bikes = b + total_ava_num_bikes
     avg_num_bikes = total_ava_num_bikes/len(divvy_stations)
print(avg_num_bikes)

# PROBLEM 2
# find ratio of bikes that are currently rented to total bikes in the system (ignore ebikes)

ratio_rented_total = total_num_docks / (total_ava_num_bikes + total_num_docks) 
# bike available  plus rented ones

print(ratio_rented_total)

# PROBLEM 3 
# Add a new variable for each divvy station's entry, "percent_bikes_remaining", that shows 
# the percentage of bikes available at each individual station (again ignore ebikes). 
# This variable should be formatted as a percentage rounded to 2 decimal places, e.g. 66.67%
for item in divvy_stations:
    a = 100 * item['num_bikes_available'] / (item['num_docks_available']+
                                                             item['num_bikes_available'])
    # calculate the raio of availablity
    b = round(a, 2) # round to 2 digits
    c = ('{}%'.format(b)) # modify the string 
    item['percent_bikes_remaining'] = c # add one item into each dict

