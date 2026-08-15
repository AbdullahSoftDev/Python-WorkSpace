# Write to file
with open('example.txt', 'w') as f:
    f.write("Hello, World!\n")
    f.write("Second line")

# Read file
with open('example.txt', 'r') as f:
    content = f.read()
    print(content)

# Read line by line
with open('example.txt', 'r') as f:
    for line in f:
        print(line.strip())

# Append to file
with open('example.txt', 'a') as f:
    f.write("\nAppended line")

# Read and write binary
with open('image.jpg', 'rb') as f:
    data = f.read()
with open('copy.jpg', 'wb') as f:
    f.write(data)

# File operations
import os
os.rename('example.txt', 'new.txt')
os.remove('new.txt')
os.mkdir('new_folder')
os.rmdir('new_folder')