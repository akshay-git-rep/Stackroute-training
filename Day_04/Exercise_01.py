def convert_units(value, fromUnit, toUnit):
    result = 0.0
    if toUnit in ("cm","inch","m","km","l","ml","oz","g","kg","lb","F","C"):
 
        match fromUnit:
            case "cm":
                if toUnit == "m":
                    result = value/100
                elif  toUnit == "km":
                    result = value/100000  
                elif  toUnit == "inch":
                    result = value*0.394
                else:
                    return "Invalid conversion unit"
               
            case "m":
                if toUnit == "cm":
                    result = value*100
                elif  toUnit == "km":
                    result = value/1000  
                elif  toUnit == "inch":
                    result = value*39.370
                else:
                    return "Invalid conversion unit"
             
            case "km":
                if toUnit == "m":
                    result = value*1000
                elif  toUnit == "cm":
                    result = value*100000  
                elif  toUnit == "inch":
                    result = value*39.37
                else:
                    return "Invalid conversion unit"
               
            case "inch":
                if toUnit == "cm":
                    result = value*2.54
                elif  toUnit == "m":
                    result = value*0.0254  
                elif  toUnit == "km":
                    result = value*0.000254
                else:
                    return "Invalid conversion unit"
                 
            case "l":
                if toUnit == "ml":
                    result = value*1000
                elif toUnit == "oz":
                    result = value*33.814  
                else:
                    return "Invalid conversion unit"
               
            case "ml":
                if toUnit == "l":
                    result = value/1000
                elif toUnit == "oz":
                    result = value/29.574  
                else:
                    return "Invalid conversion unit"
               
            case "oz":
                if toUnit == "ml":
                    result = value*29.574
                elif toUnit == "l":
                    result = value*0.0296
                else:
                    return "Invalid conversion unit"
               
            case "g":
                if toUnit == "kg":
                    result = value/1000
                elif toUnit == "lb":
                    result = value*0.0022
                else:
                    return "Invalid conversion unit"  
               
            case "kg":
                if toUnit == "g":
                    result = value*1000
                elif toUnit == "lb":
                    result = value*2.205
                else:
                    return "Invalid conversion unit"    
               
            case "lb":
                if toUnit == "g":
                    result = value*453.6
                elif toUnit == "kg":
                    result = value*0.454  
                else:
                    return "Invalid conversion unit"    
               
            case "C":
                if toUnit == "F":
                    result = ((9/5)*value)+32
                else:
                    return "Invalid conversion unit"
               
            case "F":
                if toUnit == "C":
                    result = ((5/9)*(value-32))
                else:
                    return "Invalid conversion unit"
                               
        return f"The value of {value} {fromUnit} in {toUnit} is = {round(result)} {toUnit}"
    else:
        return "Invalid Conversion Unit"
 
   
value = float(input("Enter a value to be converted :\n"))
fromUnit = input(f"Enter the units for {value} :\n")
 
if fromUnit in ("cm","inch","m","km","l","ml","oz","g","kg","lb","F","C"):
    toUnit = input(f"Enter units for {value} {fromUnit} to convert into :\n")
    print(convert_units(value, fromUnit, toUnit))
else:
    print("Invalid unit entered")