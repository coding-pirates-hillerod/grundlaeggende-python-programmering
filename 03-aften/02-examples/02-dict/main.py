me = {"name": "John", "age": 42}


# Hvordan man tilføjer ny key ogvalue
me.update({"city": "Hillerød"})


# Hvordan man looper igennem en dict
for key, value in me.items():
    print(f"{key}: {value}")
