class Folder:
    def __init__(self, name):
        self.name = name
        self.files = []
        self.subfolders = []

    def add_file(self, file_name):
        self.files.append(file_name)

    def add_subfolder(self, subfolder):
        self.subfolders.append(subfolder)

    def select_folder(self, folder_name):
        for subfolder in self.subfolders:
            if subfolder == folder_name:
                return subfolder
        return None

    def __count_files(self):
        total_files = len(self.files)
        for subfolder in self.subfolders:
            total_files += subfolder.__count_files()
        return total_files

    def __eq__(self, other):
        return self.name == other

    def __len__(self):
        return self.__count_files()

    def __str__(self):
        result = f"Folder: {self.name}\n"
        result += "  Files:\n" + "\n".join(f"    {file}" for file in self.files) + "\n"
        result += "  Subfolders:\n"
        for subfolder in self.subfolders:
            result += "    " + str(subfolder).replace("\n", "\n    ") + "\n"
        return result

def main():
    root_folder = None

    while True:
        if root_folder is None:
            root_name = input("Enter the name of the root folder: ")
            root_folder = Folder(root_name)
        else:
            print("\nMain Menu:")
            print("1. Add a file")
            print("2. Add a subfolder")
            print("3. Select a folder")
            print("4. Print folder contents")
            print("5. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                file_name = input("Enter the file name: ")
                root_folder.add_file(file_name)
            elif choice == "2":
                subfolder_name = input("Enter the subfolder name: ")
                subfolder = Folder(subfolder_name)
                root_folder.add_subfolder(subfolder)
            elif choice == "3":
                folder_name = input("Enter the folder name to select: ")
                selected_folder = root_folder.select_folder(folder_name)
                root_folder = selected_folder
            elif choice == "4":
                print(root_folder)
            elif choice == "5":
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
