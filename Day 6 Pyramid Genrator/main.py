n = int(input("Enter the height of your pyramid: "))

# Print first peak top of the pyramid
spaces = n - 1
line = " " * spaces + "*"
print(line)


# Now print the rest of the pyramid
stars = 3
for i in range(1, n):
    spaces = n - i - 1
    line = " " * spaces + "*" * stars
    print(line)
    stars += 2
