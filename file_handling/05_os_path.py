import os
import shutil

# Current directory
print(os.getcwd())

# List files
print(os.listdir('.'))

# Create directory
os.mkdir('temp')

# Remove directory
os.rmdir('temp')

# Check if exists
print(os.path.exists('data.csv'))
print(os.path.isfile('data.csv'))
print(os.path.isdir('folder'))

# Path operations
print(os.path.basename('/path/to/file.txt'))
print(os.path.dirname('/path/to/file.txt'))
print(os.path.join('/path', 'to', 'file.txt'))
print(os.path.splitext('file.txt'))

# Copy file
shutil.copy('data.csv', 'backup.csv')

# Move file
shutil.move('data.csv', 'data_backup.csv')