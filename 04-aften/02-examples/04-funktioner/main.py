# En simpel funktion
def simple_function():
    print("Dette er en simpel funktion")


# En funktion med en parameter
def function_with_parameter(name):
    print(f"Hej {name}")


# En funktion der returnerer en værdi
def add_two_numbers(num1, num2):
    return num1 + num2


# Hvordan vi kalder på funktionerne
simple_function()
function_with_parameter("Mikkel")

result = add_two_numbers(5, 3)
print(result)
