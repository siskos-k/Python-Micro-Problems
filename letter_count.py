#get the input string from the user
input_string = input("Please enter your text: ")

#create a dictionary to count the occurrence of each letter
letter_count = {}

#convert the input string to lowercase for case-insensitive counting
input_string = input_string.lower()

#iterate over each letter in the input string and count its occurrence
for letter in input_string:
    #check if the letter is an alphabetical character
    if letter.isalpha():
        if letter not in letter_count:
            letter_count[letter] = 0
        letter_count[letter] += 1

#get the total number of letters in the input string
total_letters = sum(letter_count.values())

#find the most common letter and its count
most_common_letter = ''
max_count = 0
for letter, count in letter_count.items():
    if count > max_count:
        most_common_letter = letter
        max_count = count

#calculate the percentage of the most common letter
percentage = (max_count / total_letters) * 100

#print the result
print(f"The most common letter is '{most_common_letter}': {percentage:.2f}%")
