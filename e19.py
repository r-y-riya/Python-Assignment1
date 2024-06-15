import string

user_input = input("Enter a string: ")
cleaned_str = user_input.translate(str.maketrans('', '', string.punctuation))
print(f"The string without punctuation is: {cleaned_str}")
