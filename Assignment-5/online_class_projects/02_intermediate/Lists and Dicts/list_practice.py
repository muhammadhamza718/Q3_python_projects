def main():
    # Problem #1: List Practice
    
    # Create a list called `fruit_list` that contains the following fruits: 
    fruit_list = ['apple', 'banana', 'orange', 'grape', 'pineapple']
    
    # Print the length of the list.
    print("Length of fruit_list:", len(fruit_list))
    
    # Add 'mango' at the end of the list. 
    fruit_list.append('mango')
    
    # Print the updated list.
    print("Updated fruit_list:", fruit_list)

    # Problem #2: Index Game
    
    elements = [10, "hello", 3.14, "world", 42]
    
    def access_element(lst, index):
        try:
            return lst[index]
        except IndexError:
            return "Index out of range."
    
    def modify_element(lst, index, new_value):
        if 0 <= index < len(lst):
            lst[index] = new_value
            return lst
        return "Index out of range."
    
    def slice_list(lst, start, end):
        if 0 <= start <= len(lst) and 0 <= end <= len(lst):
            return lst[start:end]
        return "Invalid indices."
    
    while True:
        print("\nChoose an operation:")
        print("1. Access an element")
        print("2. Modify an element")
        print("3. Slice the list")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            index = int(input("Enter index: "))
            print("Element at index", index, ":", access_element(elements, index))
        elif choice == "2":
            index = int(input("Enter index: "))
            new_value = input("Enter new value: ")
            print("Updated list:", modify_element(elements, index, new_value))
        elif choice == "3":
            start = int(input("Enter start index: "))
            end = int(input("Enter end index: "))
            print("Sliced list:", slice_list(elements, start, end))
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
