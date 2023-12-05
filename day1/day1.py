def sum_of_two_digit_numbers(text):
    words = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
             "six": 6, "seven": 7, "eight": 8, "nine": 9}

    sum_of_numbers = 0

    lines = text.strip().split("\n")
    for line in lines:
        first_digit = None
        second_digit = None

        for i in range(len(line)):
            if (first_digit):
                break

            if line[i].isdigit():
                first_digit = int(line[i])
                break
            elif i <= len(line) - 3:
                word = line[i:i + 3]
                # print("first word", word)
                if word in words:
                    first_digit = words[word]
                    break
                j = i + 3
                while j < len(line) and line[j].isalpha() and len(word) <= 5:
                    word += line[j]
                    # print("first word", word)
                    if word in words:
                        first_digit = words[word]
                        break
                    j += 1

        for i in range(len(line) - 1, -1, -1):
            if (second_digit):
                break
            if line[i].isdigit():
                second_digit = int(line[i])
                break
            elif i >= 2:
                word = line[i - 2:i + 1]
                # print("second word", word)
                if word in words:
                    second_digit = words[word]
                    break
                j = i - 3
                while j >= 0 and line[j].isalpha() and len(word) <= 5:
                    word = line[j] + word
                    # print("second word", word)
                    if word in words:
                        second_digit = words[word]
                        break
                    j -= 1

        num = first_digit * 10 + second_digit
        # print(line, num)
        # print()

        sum_of_numbers += num
    return sum_of_numbers


# Read input from a text file
file_path = input("Enter the path to your file: ")
with open(file_path, "r") as file:
    text = file.read()

result = sum_of_two_digit_numbers(text)
print(result)
