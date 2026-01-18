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

# Contactenating two arrays using the + operator
concat = [1, 2 , 3]
print(concat)

concat + [4, 5 ,6]
print(concat)

concat = concat + [4, 5, 6]
print(concat)

# Repeating Element in an array
repeat = ["Hacker"]
print(repeat)

repeat = repeat * 5
print(repeat)

# Slicing of an array
fruits = ["Apple", "Banana", "Guava", "Grapes", "Mango"]
print(fruits)

print(fruits[1 : 4])            # It will print from index 1 to 3 and not the 4th index ( it will only print from the starting upto the n-1 (where n is the last term))
print(fruits[  : 3])            # It will print from index 0 means from starting to 2
print(fruits[-4 : ])             # It will print from index -4 to the end of the string
print(fruits[-3 : -1])           # It will print from -3 to -2 

# Declaring and Defining multidimentional array
multd = [[1, 2], [3, 4], [5,6], [7,8]]
print(multd)
multd.append([9, 10])
print(multd)

print(multd[1])
print(multd[-1])
print(multd[2][0])
print(multd[4][-1])
print(multd[-1][-1])