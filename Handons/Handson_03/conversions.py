def fFeetToMeter():
    x = int(input("Enter feet:"))
    sReturn = str(round(x*0.3048,2)) + " Meter/s" 
    return sReturn

def fMeterToFeet():
    x = int(input("\nEnter meter:"))
    sReturn = str(round(x/0.3048,2)) + " Feet"
    return sReturn

