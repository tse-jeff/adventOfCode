

def sum_of_two_digit_numbers(text):
    lines = text.strip().split("\n")
    numbers = []
    for line in lines:
        for char in line:
            if char.isdigit():
                first_digit = int(char)
                break
        for char in reversed(line):
            if char.isdigit():
                last_digit = int(char)
                break
        numbers.append(first_digit * 10 + last_digit)

    sum_of_numbers = sum(numbers)

    return sum_of_numbers


# Read input from a text file
file_path = input("Enter the path to your file: ")
with open(file_path, "r") as file:
    text = file.read()

result = sum_of_two_digit_numbers(text)
print(result)
