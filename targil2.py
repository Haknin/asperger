import os
import sys

if not len(sys.argv) >= 2:
    print("Usage: python list_files.py <directory>")
    sys.exit(1)

dir_path = sys.argv[1]

if not os.path.exists(dir_path):
    print(f"Error: {dir_path} does not exist")
    sys.exit(1)

for root, dirs, files in os.walk(dir_path):
    for file in files:
        print(os.path.join(root, file))