my_string = input("Enter your string: \n")

my_string = my_string.lower().replace(" ", "")

frequency = {}

for char in my_string:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1

max_char = None
max_count = 0

for char, count in frequency.items():
    if count > max_count:
        max_count = count
        max_char = char

print("The most common symbol in this string is:", max_char)
