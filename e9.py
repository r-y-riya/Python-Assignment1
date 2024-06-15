main_str = input("Enter the main string: ")
sub_str = input("Enter the substring: ")
if sub_str in main_str:
    print(f"'{sub_str}' is present in '{main_str}'.")
else:
    print(f"'{sub_str}' is not present in '{main_str}'.")
