import os

def show_directories(path):
    """Displays only the directories within the specified path."""
    try:
        directories = [item for item in os.listdir(path) if os.path.isdir(os.path.join(path, item))]
        print("Directories:")
        print("\n".join(directories) if directories else "No directories found.")
    except FileNotFoundError:
        print("Error: The specified path does not exist. Please check and try again.")

def show_files(path):
    """Displays only the files within the specified path."""
    try:
        files = [item for item in os.listdir(path) if os.path.isfile(os.path.join(path, item))]
        print("Files:")
        print("\n".join(files) if files else "No files found.")
    except FileNotFoundError:
        print("Error: The specified path does not exist. Please check and try again.")

def show_all_items(path):
    """Displays all directories and files within the specified path."""
    try:
        all_items = os.listdir(path)
        print("All Directories and Files:")
        print("\n".join(all_items) if all_items else "No items found.")
    except FileNotFoundError:
        print("Error: The specified path does not exist. Please check and try again.")

if __name__ == "__main__":
    directory_path = input("Enter the directory path: ").strip()
    print("\n")
    show_directories(directory_path)
    print("\n")
    show_files(directory_path)
    print("\n")
    show_all_items(directory_path)
