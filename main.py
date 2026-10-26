# Lab 2 - Reading data from the keyboard and from a file


def read_sequence():
    text = input("Enter numbers separated by spaces: ")
    numbers = []
    for item in text.split():     
        numbers.append(int(item))  
    return numbers


def read_array():
    rows = int(input("Number of rows: "))
    cols = int(input("Number of columns: "))

    array = []
    for i in range(rows):
        row = []
        for j in range(cols):
            value = int(input("Element [" + str(i) + "][" + str(j) + "]: "))
            row.append(value)
        array.append(row)
    return array


def display_array(array):
    for row in array:
        for value in row:
            print(value, end="\t")   
        print()                     


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


print("=== Sequence of numbers ===")
sequence = read_sequence()
print("The sequence is:", sequence)

print()
print("=== Array of numbers ===")
array = read_array()
print("The array is:")
display_array(array)

print()
print("=== Numbers from a file ===")
numbers = read_from_file()
if numbers is not None:         
    print("The numbers from the file are:", numbers)
