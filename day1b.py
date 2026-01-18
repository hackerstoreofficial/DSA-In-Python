#Defining and Printing index of array
arr = [10, 20, 30, 40, 50]
print(arr)
# Accessing Array Elements
print(arr[0])
print(arr[1])
print(arr[2])
print(arr[-1])      # Negative Indexing
print(arr[-2])      # Negative Indexing

brands = ["Apple", "BlackBerry", "Vivo", "Oppo", "Realme"]
print(brands)

# Finding the length of the array
num_brands = len(brands)
print(num_brands)

# Adding an element to an array using append()
brands.append("Mi")
print(brands)
brands.append("Samsung")
print(brands)

# Finding the index of "Samsung"
samsung_index = brands.index("Samsung")
print("Index of Samsung:", samsung_index)

# Removing an element from an array
del brands[0]
print(brands)

brands.remove("Samsung")
print(brands)

brands.pop(2)
print(brands)

# Removing everything except "Vivo"
brands = [brand for brand in brands if brand == "Vivo"]
print(brands)

# Modifying the elements of an array using indexing
fruits = ["Apple", "Banana", "Guava", "Grapes", "Mango"]
print(fruits)

fruits[3] = "Pineapple"
print(fruits)
fruits[-3] = "Berry"
print(fruits)