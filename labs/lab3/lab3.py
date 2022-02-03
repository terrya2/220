"""
Autumn Terry
lab3.py
Determined averages by different calculations and use of loops.
I certify that this assignment is entirely my own work.
"""

def traffic():
    roads = eval(input("How many roads were surveyed?: "))
    total_vehicles = 0
    for road in range(roads):
        sum = 0
        print("How many days was road", road + 1,"surveyed?: " )
        days = eval(input(""))
        for traffic in range(days):
            print("\tHow many cars traveled on day", traffic + 1, "?: " )
            total_cars = eval(input(""))
            sum = sum + total_cars
            total_vehicles = total_vehicles + total_cars
        avg = sum / days
        print(road + 1, "average vehicles per day: ", avg)
    avg_vehicles = total_vehicles / roads
    print("Total number of vehicles traveled on all roads: ", total_vehicles)
    print("Average number of vehicles per road: ", avg_vehicles)



