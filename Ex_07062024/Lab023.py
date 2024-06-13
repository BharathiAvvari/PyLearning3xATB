# List - Shopping List
# milk, bread, butter, poha
# 1. Add item
# 2. Remove item
# 3. Update item
# 4. View item
# 5. Exit

shopping_list = ["milk", "bread", "butter", "poha"]
print(shopping_list)
print(len(shopping_list))
print(shopping_list[0])
print(shopping_list[-1])

shopping_list.append("eggs") #add one item to the list in the end
print(shopping_list)

shopping_list.insert(1, "jam")#add item in the middle
print(shopping_list)

shopping_list.extend(["sugar", "ghee"]) #add multiple items in the end
print(shopping_list)

shopping_list.remove("poha")#remove item from the list
print(shopping_list)

print(shopping_list.pop())#remove last item from the list
print(shopping_list)

print(shopping_list.index("eggs"))

shopping_list.reverse()
print(shopping_list)

shopping_list.sort()
print(shopping_list)

shopping_list[2] = "coke"
print(shopping_list)


my_list = [1, 2, 3, 4, True, 3.14, "Joy"]
print(type(my_list)) #<class 'list'>
print(my_list[0])
print(my_list[1])
