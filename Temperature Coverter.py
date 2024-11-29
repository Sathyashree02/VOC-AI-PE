#Defining function "convert_temperature" 
#We are receiving both temperature and its unit together
def convert_temperature(temp, unit):
    # We are converting the case for eradicating case related issues
    units=unit.upper()
    
    # To convert Fahrenheit to Celsius  
    if units == 'F':
        result = (temp - 32) * 5/9
        
    # To convert Celsius to Fahrenheit
    elif units == 'C':
        result = (temp * 9/5) + 32
        
    # If the input unit is wrong
    else:
        raise ValueError("Wrong Unit is Given. Please use 'F' if the temperature is in Fahrenheit or 'C' if the temperature is in Celsius.")

    # Output rounded off to two decimals
    return round(result,2)