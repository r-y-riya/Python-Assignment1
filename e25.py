with open("source.txt", "r") as src_file:
    content = src_file.read()

with open("destination.txt", "w") as dest_file:
    dest_file.write(content)
