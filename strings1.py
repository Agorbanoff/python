sentences = "Not every key opens every door. Choosing the right one requires knowledge."
vowel = 0
consonant = 0

for i in sentences:
    if i == 'a' or i == 'A' or i == 'e' or i == 'E' or i == 'i' or i == 'I' or i == 'o' or i == 'O' or i == 'u' or i == 'U':
        vowel += 1
 
    elif i.isalpha():   
        consonant += 1

print(vowel, "is the number of your vowel letters")
print(consonant, "is the number of your consonant letters")

# Ensures that only alphabetic characters are counted as consonants (.isalha)