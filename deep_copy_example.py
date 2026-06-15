"""
Deep Copy Example
=================

A deep copy creates a new object AND recursively copies all nested objects.
This means the copied object is completely independent from the original.
Changes to nested objects in the copy will NOT affect the original.

Use deep copy when:
- You need complete independence between original and copy
- You're working with deeply nested structures
- You want to avoid unintended side effects from shared references
"""

import copy

print("=" * 60)
print("DEEP COPY EXAMPLE")
print("=" * 60)

# Example 1: List with nested lists
print("\n1. List with nested lists:")
original_list = [1, 2, [3, 4, 5]]

###
deep_copied_list = copy.copy(original_list)

print(f"Original: {original_list}")
print(f"Deep copy: {deep_copied_list}")
print(f"Are they the same object? {original_list is deep_copied_list}")
print(f"Are nested lists the same object? {original_list[2] is deep_copied_list[2]}")

# Modifying the nested list does NOT affect the original
deep_copied_list[2][0] = 999
print(f"\nAfter modifying nested list in copy:")
print(f"Original: {original_list}")
print(f"Deep copy: {deep_copied_list}")

# Example 2: Dictionary with nested dictionary
print("\n\n2. Dictionary with nested dictionary:")
original_dict = {
    "name": "John",
    "hobbies": ["reading", "gaming"],
    "info": {"age": 30, "city": "NYC"}
}
deep_copied_dict = copy.deepcopy(original_dict)

print(f"Original: {original_dict}")
print(f"Deep copy: {deep_copied_dict}")

# Modifying nested objects
deep_copied_dict["hobbies"].append("sports")
deep_copied_dict["info"]["age"] = 31

print(f"\nAfter modifying nested objects:")
print(f"Original: {original_dict}")
print(f"Deep copy: {deep_copied_dict}")

# Example 3: Complex nested structure
print("\n\n3. Complex nested structure:")
company = {
    "name": "TechCorp",
    "employees": [
        {"id": 1, "name": "Alice", "skills": ["Python", "JS"]},
        {"id": 2, "name": "Bob", "skills": ["Java", "C++"]}
    ],
    "departments": {
        "backend": ["Alice"],
        "frontend": ["Bob"]
    }
}

deep_copied_company = copy.deepcopy(company)

# Make changes to the deep copy
deep_copied_company["employees"][0]["name"] = "Alicia"
deep_copied_company["employees"][0]["skills"].append("Go")
deep_copied_company["departments"]["backend"].append("Charlie")

print(f"Original company employees: {company['employees']}")
print(f"Deep copy company employees: {deep_copied_company['employees']}")
print(f"\nOriginal departments: {company['departments']}")
print(f"Deep copy departments: {deep_copied_company['departments']}")

print("\n" + "=" * 60)
print("KEY DIFFERENCES SUMMARY")
print("=" * 60)
print("Shallow Copy: Copies top-level object, shares references to nested objects")
print("Deep Copy:    Copies everything recursively, completely independent objects")
print("=" * 60)
