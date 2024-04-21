import os

def list_directory_contents(path):
  
  try:
    for root, directories, files in os.walk(path):
      print(f"Directory: {root}")
      for directory in directories:
        print(f"- Subdirectory: {directory}")
      for file in files:
        print(f"- File: {file}")
  except FileNotFoundError:
    print(f"Error: Directory not found: {path}")
  except PermissionError:
    print(f"Error: Access denied for directory: {path}")

def report_file_sizes(directory):
  """Reports the size of all files in a directory."""
  try:
    for root, _, files in os.walk(directory):
      for file in files:
        file_path = os.path.join(root, file)
        file_size = os.path.getsize(file_path)
        print(f"File: {file} - Size: {file_size} bytes")
  except FileNotFoundError:
    print(f"Error: Directory not found: {directory}")
  except PermissionError:
    print(f"Error: Access denied for directory: {path}")

if __name__ == "__main__":
  while True:
    print("\nMenu:")
    print("1. List Directory Contents")
    print("2. Report File Sizes")
    print("3. Exit")

    choice = input("Enter your choice (1-3): ")

    if choice == '1':
      path = input("Enter the directory path: ")
      list_directory_contents(path)
    elif choice == '2':
      path = input("Enter the directory path: ")
      report_file_sizes(path)
    elif choice == '3':
      print("Exiting...")
      break
    else:
      print("Invalid choice. Please try again.")
