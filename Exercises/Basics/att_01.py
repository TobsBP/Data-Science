name = input("Write your full name: ")

print("Uppercase:", name.upper())
print("Lowercase:", name.lower())

only_name = name.replace(" ", "")

print("Number of characters:", len(only_name))

changed_name = name.replace("Pereira", "do Inatel")

print("Changed name:", changed_name)