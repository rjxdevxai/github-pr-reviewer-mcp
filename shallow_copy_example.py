"""
Shallow Copy Example
====================

A shallow copy creates a new object but does NOT recursively copy nested objects.
Instead, it copies references to the nested objects. This means changes to nested
objects will affect both the original and the copied version.

Use shallow copy when:
- You want a new top-level object
- Nested objects are immutable (strings, numbers, tuples)
- You intentionally want shared references to nested objects
"""

import copy

print("=" * 60)
print("SHALLOW COPY EXAMPLE")
print("=" * 60)

# Example 1: List with nested lists
print("\n1. List with nested lists:")
original_list = [1, 2, [3, 4, 5]]
shallow_copied_list = copy.copy(original_list)

print(f"Original: {original_list}")
print(f"Shallow copy: {shallow_copied_list}")
print(f"Are they the same object? {original_list is shallow_copied_list}")
print(f"Are nested lists the same object? {original_list[2] is shallow_copied_list[2]}")

# Modifying the nested list affects both!
shallow_copied_list[2][0] = 999
print(f"\nAfter modifying nested list in copy:")
print(f"Original: {original_list}")
print(f"Shallow copy: {shallow_copied_list}")

# Example 2: Dictionary with nested dictionary
print("\n\n2. Dictionary with nested dictionary:")
original_dict = {
    "name": "John",
    "hobbies": ["reading", "gaming"],
    "info": {"age": 30, "city": "NYC"}
}
shallow_copied_dict = copy.copy(original_dict)

print(f"Original: {original_dict}")
print(f"Shallow copy: {shallow_copied_dict}")

# Modifying nested mutable objects
shallow_copied_dict["hobbies"].append("sports")
shallow_copied_dict["info"]["age"] = 31

print(f"\nAfter modifying nested objects:")
print(f"Original: {original_dict}")
print(f"Shallow copy: {shallow_copied_dict}")

# Example 3: Using list slicing (also creates shallow copy)
print("\n\n3. List slicing (also a shallow copy):")
original = [[1, 2], [3, 4]]
sliced = original[:]  # Creates a shallow copy

print(f"Original: {original}")
print(f"Sliced: {sliced}")
sliced[0][0] = 999
print(f"After modification in sliced:")
print(f"Original: {original}")

print("\n" + "=" * 60)
