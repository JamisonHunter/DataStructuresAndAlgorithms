"""
The following code represents a simple database search using linear search.
"""

def linear_search(list, target):
    """
    Returns the index position of the target if found, otherwise none is returned.
    """
    for i in range(0, len(list)):
        if list[i] == target:
            print(f"Index: {i}")
            return i
    print("Index not found.")
    return None
        
def main():
    search = input(str("Enter a first name to search: "))
    db = ["Jane", "Thomas", "Bill", "David", "Emily", "Susan", "Rachel", "Alice"]
    linear_search(db, search)

main()