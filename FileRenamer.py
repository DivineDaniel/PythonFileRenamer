# https://pynative.com/python-rename-file/
import os

# Displays a menu listing all the items in the folder
def display_menu(folder_path):
    
    divider()
    print("File Menu:")
    divider()

    # Lists everything in the specified folder
    items = os.listdir(folder_path)
    for i, item in enumerate(items, start=1):
        print(f"{i}. {item}")

# Renaming a file in the folder
def rename_file(folder_path, old_name, new_name):
    
    # Current name of the file
    old_path = os.path.join(folder_path, old_name)
    # New name of the file
    new_path = os.path.join(folder_path, new_name)
    
    existing_files = [f.lower() for f in os.listdir(folder_path)]
    if new_name.lower() in existing_files:
        # Checking if a file with the new name already exists in the folder
        print("That file name already exists!")
    elif old_name.lower() == new_name.lower():
        # Checking if the new name is the same as the old name (ignoring capitalization)
        print("New name is the same as the old name. No changes made.")
    else:
        os.rename(old_path, new_path)
        print("Name change was successful!")

# My love, the divider method
def divider():
    print("---------------")

# Main function pog
def main():
    
    # Folder path where the file is located - Replace with other folder paths if you want to rename files elsewhere
    # Might not work for every file cuz permissions - Will have to find a fix for that someday
    folder_path = r"C:\Users\danie\Downloads\Overpromised - Overwatch Documentary"
    
    while True:
        
        display_menu(folder_path)
    
        try:
            
            divider()
            
            # Get the users choice
            choice = int(input("Enter the number of the item you want to rename: "))
            items = os.listdir(folder_path)
            selected_item = items[choice - 1]
            
            # Get the new name of the item via user input
            new_name = input(f"Enter the new name for '{selected_item}': ")
            
            # Renaming the file
            rename_file(folder_path, selected_item, new_name)

            divider()

            choice = input("Do you want to rename another file? (yes/no): ").lower()

            if choice != "yes":
                print("Goodbye!")
                divider()
                break

        except (ValueError, IndexError):
            print("Invalid choice. Please enter a valid number.")
        except OSError as e:
            print(f"An error has occurred: {e}")

if __name__ == "__main__":
    main()
