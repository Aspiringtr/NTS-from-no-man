a = tuple(map(int,input("Enter elements for the Tuple separated by commas:").split(',')))
tuple_length = len(a)
print(f"Length of the Tuple: {tuple_length}")
sorting=tuple(sorted(a))
print("Sorted list",sorting)
print(f"Maximum element in the Tuple: {sorting[-1]}")
print(f"Minimum element in the Tuple: {sorting[0]}")