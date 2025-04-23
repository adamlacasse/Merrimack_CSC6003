fruits = "apple", "banana"
a, b = fruits
fruits[0] = "orange"  # This will raise a TypeError
print(a)
print(b)
