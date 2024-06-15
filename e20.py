numbers = input("Enter numbers separated by spaces: ").split()
numbers = [int(num) for num in numbers]
print(f"The sum of the numbers is: {sum(numbers)}")
