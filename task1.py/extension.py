import os

def list_directory_contents(path):
  """Lists all files and subdirectories in a given directory."""
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
    print(f"Error: Directory not found: {path}")
  except PermissionError:
    print(f"Error: Access denied for directory: {path}")

def count_file_extensions(directory):
  """Counts the number of files of each extension type in a directory (case-insensitive)."""
  extension_counts = {}
  try:
    for root, _, files in os.walk(directory):
      for file in files:
        extension = os.path.splitext(file)[1].lower()  # Get lowercase extension
        extension_counts[extension] = extension_counts.get(extension, 0) + 1
    for extension, count in extension_counts.items():
      print(f"{extension.upper()}: {count}")
  except FileNotFoundError:
    print(f"Error: Directory not found: {path}")
  except PermissionError:
    print(f"Error: Access denied for directory: {path}")

if __name__ == "__main__":
  while True:
    print("\nMenu:")
    print("1. List Directory Contents")
    print("2. Report File Sizes")
    print("3. Count File Extensions")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
      path = input("Enter the directory path: ")
      list_directory_contents(path)
    elif choice == '2':
      path = input("Enter the directory path: ")
      report_file_sizes(path)
    elif choice == '3':
      path = input("Enter the directory path: ")
      count_file_extensions(path)
    elif choice == '4':
      print("Exiting...")
      break
    else:
      print("Invalid choice. Please try again.")