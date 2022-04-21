"""
Autumn Terry
lab13.py
Create programs using binary searches and functions.
I certify that this is entirely my own work, but I discussed it with: Margaret Kimery.
"""


def trade_alert(filename):
    file = open(filename, "r")
    data = file.readline()
    trade_vol = data.split()
    count = 0
    for trade in trade_vol:
        count = count + 1
        if int(trade) > 830:
            print("Warning: trading volume exceeds 830", "at", count, "seconds")
        elif int(trade) == 500:
            print("Alert: pay attention if the volume equals 500 at any second", "at", count, "seconds")
    file.close()