file1 = ["🙉 ", "🙉 ", "🙉 "]
file2 = ["🙉 ", "🙉 ", "🙉 "]
file3 = ["🙉 ", "🙉 ", "🙉 "]

map1 = [file1, file2, file3]
name = input("Enter position (like a1, b2, etc): ")


position = name[0].lower()
abc = ["a", "b", "c"]

name_index = abc.index(position)
number = int(name[1]) - 1
map1[number][name_index] = "🙈 "
print(f"{file1}\n{file2}\n{file3}")