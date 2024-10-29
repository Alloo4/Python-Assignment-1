# Step 1: Create an empty list called my_list
my_list = []

# Step 2: Append the following elements to my_list: 10, 20, 30, 40
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# Printing the list after appending elements
print("After appending elements:", my_list)

# Step 3: Insert the value 15 at the second position in the list
my_list.insert(1, 15)  # Indexing starts at 0, so 1 is the second position

# Printing the list after insertion
print("After inserting 15 at the second position:", my_list)

# Step 4: Extend my_list with another list: [50, 60, 70]
my_list.extend([50, 60, 70])

# Printing the list after extending
print("After extending with [50, 60, 70]:", my_list)

# Step 5: Remove the last element from my_list
my_list.pop()  # This removes the last item in the list

# Printing the list after removing the last element
print("After removing the last element:", my_list)

# Step 6: Sort my_list in ascending order
my_list.sort()

# Printing the sorted list
print("After sorting in ascending order:", my_list)

# Step 7: Find and print the index of the value 30 in my_list
index_of_30 = my_list.index(30)
print("The index of the value 30 in my_list is:", index_of_30)
