#This converts temp from C to F
tempc = float(input("Temperature in C? ")) #asks user for temperature in C. Converts to int and the float.
tempf = tempc * 1.8 + 32.0 #mathematics, ya'll
print(str(tempf) + " F") #prints temp; converts float from line above to string to concat with "F"
