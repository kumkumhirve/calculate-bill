'''Q10: Write a program for generating electricity Bill.
Bill Accept last month unit and current month unit from user, then
calculate and print bill amount according to following condition
For units
0-100 charges 2 rs/unit
101-200 charges 3rs/unit
201-300 4rs/unit
&gt;300 charges 5rs/unit'''

last = int(input("enter the last month unit:"))
current = int(input("enter the last month unit:"))

units = current - last

if units <=100:
    print("bill amount",units*2)

elif units>=101 and units<=200:
    print("bill amount",units*3)

elif units>=201 and units<=300:
    print("bill amount",units*4)

else:
    print("bill amount ",units*5)