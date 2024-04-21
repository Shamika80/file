import os

def list_directory_contents(path):
    
    try:
        if not os.path.isdir(path):
            raise OSError(f"Invalid path: '{path}' is not a directory.")

        print(f"Contents of directory: {path}")
        for entry in os.listdir(path):
            full_path = os.path.join(path, entry)  
           
            if os.path.isdir(full_path):
               
                list_directory_contents(full_path)
            else:
                print(f"[File] {entry}")

    except OSError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    while True:
        path = input("Enter directory path: ")
        try:
            list_directory_contents(path)
            break  
        except OSError:
            pass  