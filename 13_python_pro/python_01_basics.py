# Variables
myAge, lucyAge = 34, 28
print(17 + 17)
y = "mi edad es"
if myAge == 34:
    print(f"Hey, {y} {myAge}")
# Printing on the same line
print("Soy Blackbird!", end=" ")
print(f"y mi edad: {myAge} años está en la misma linea gracias a end=' '")
print("I am", myAge, "years old And my friend Lucy is", lucyAge, "years old.")
# Changing the value of a variable
myAge = float(34.5)
print(f"Ahora tengo {myAge} años y es 2026. Por eso myAge cambió su valor")
print(type(myAge))  # Checking the type of the variable
x = y = z = "one value for three variables"
print(myAge, lucyAge)  # The best way to print multiple variables ","
print(myAge + lucyAge)
