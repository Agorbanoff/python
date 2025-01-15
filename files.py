import os
import shutil
import random

def create_directory():
    path = input("Enter a full path or name for the new folder: ")
    try:
        os.makedirs(path, exist_ok=True)
        print(f"The folder '{path}' has been created successfully.")
    except Exception as e:
        print(f"Error creating folder: {e}")

def delete_directory():
    path = input("Enter the full path of the folder to delete: ")
    if os.path.isdir(path):
        confirm = input(f"Are you sure you want to delete the folder '{path}'? (y/n): ")
        if confirm.lower() in ("y", "yes"):
            try:
                shutil.rmtree(path)
                print(f"The folder '{path}' has been deleted successfully.")
            except Exception as e:
                print(f"Error deleting the folder: {e}")
        else:
            print("Operation canceled.")
    else:
        print("The specified folder does not exist.")

def create_directory_in_folder():
    parent_path = input("Enter the path of the parent folder: ")
    if os.path.isdir(parent_path):
        new_dir_name = input("Enter the name of the new folder: ")
        full_path = os.path.join(parent_path, new_dir_name)
        try:
            os.makedirs(full_path, exist_ok=True)
            print(f"The folder '{full_path}' has been created successfully.")
        except Exception as e:
            print(f"Error creating the folder: {e}")
    else:
        print("The parent folder does not exist.")

def delete_files():
    path = input("Enter the path to the file or the directory containing files: ")
    if os.path.isfile(path):
        # Single file deletion
        confirm = input(f"Are you sure you want to delete the file '{path}'? (y/n): ")
        if confirm.lower() in ("y", "yes"):
            try:
                os.remove(path)
                print(f"The file '{path}' has been deleted successfully.")
            except Exception as e:
                print(f"Error deleting the file: {e}")
        else:
            print("Operation canceled.")
    elif os.path.isdir(path):
        # Directory with files
        files = os.listdir(path)
        if not files:
            print("The folder is empty.")
            return
        print("List of files in the directory:")
        for i, f in enumerate(files):
            print(f"{i}: {f}")
        indices = input("Enter the indices of the files to delete, separated by commas, or '*' to delete all: ")
        if indices.strip() == "*":
            confirm = input("Are you sure you want to delete all files in this folder? (y/n): ")
            if confirm.lower() in ("y", "yes"):
                for f in files:
                    file_path = os.path.join(path, f)
                    if os.path.isfile(file_path):
                        os.remove(file_path)
                print("All files have been deleted successfully.")
        else:
            try:
                idx_list = [int(x.strip()) for x in indices.split(",")]
                for idx in idx_list:
                    if 0 <= idx < len(files):
                        file_path = os.path.join(path, files[idx])
                        if os.path.isfile(file_path):
                            os.remove(file_path)
                            print(f"The file '{files[idx]}' has been deleted successfully.")
                    else:
                        print(f"Invalid index: {idx}")
            except Exception as e:
                print(f"Error: {e}")
    else:
        print("The specified path does not exist.")

def create_random_files_in_folder():
    path = input("Enter the folder path in which to create files: ")
    if os.path.isdir(path):
        min_count = input("Enter the minimum number of files: ")
        max_count = input("Enter the maximum number of files: ")
        try:
            min_count = int(min_count)
            max_count = int(max_count)
            if min_count > max_count:
                print("The minimum number cannot be greater than the maximum.")
                return
            number_of_files = random.randint(min_count, max_count)
            for i in range(number_of_files):
                file_name = f"random_file_{i}.txt"
                file_path = os.path.join(path, file_name)
                with open(file_path, "w") as f:
                    f.write("This is a random file.\n")
            print(f"{number_of_files} files have been created in '{path}'.")
        except ValueError:
            print("Please enter valid numbers for the minimum and maximum file count.")
    else:
        print("The specified folder does not exist.")

def main():
    while True:
        print("\nMENU:")
        print("1: Create a folder")
        print("2: Delete a folder")
        print("3: Create a folder inside another folder")
        print("4: Delete file(s)")
        print("5: Create a random number of files in a chosen folder")
        print("6: Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            create_directory()
        elif choice == "2":
            delete_directory()
        elif choice == "3":
            create_directory_in_folder()
        elif choice == "4":
            delete_files()
        elif choice == "5":
            create_random_files_in_folder()
        elif choice == "6":
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()