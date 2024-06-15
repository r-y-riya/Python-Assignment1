user_input = input("Enter a string: ")
prefix = input("Enter a prefix: ")
suffix = input("Enter a suffix: ")

if user_input.startswith(prefix):
    print(f"The string starts with '{prefix}'")
else:
    print(f"The string does not start with '{prefix}'")

if user_input.endswith(suffix):
    print(f"The string ends with '{suffix}'")
else:
    print(f"The string does not end with '{suffix}'")
