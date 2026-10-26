def read_from_file():
    filename = input("Enter the name of the file: ")
    try:
        file = open(filename, "r")     
        text = file.read()              
        file.close()
    except FileNotFoundError:
        print("Error: the file", filename, "does not exist.")
        return None

    numbers = []
    for item in text.split():
        numbers.append(int(item))
    return numbers



print()
print("=== Numbers from a file ===")
numbers = read_from_file()
if numbers is not None:        
    print("The numbers from the file are:", numbers)