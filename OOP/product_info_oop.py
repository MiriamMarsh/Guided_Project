import os
from abc import ABC, abstractmethod 

class FileManager(ABC):
    def __init__(self, product_id):
        self.file_path = f"products/{product_id}.txt"

class FileReader:
    def __init__(self, file_manager):
        self.file_path = file_manager.file_path  

    def get_product_info(self):
        try:
            file = open(self.file_path, "r")
            data = file.read()
            file.close()
            return data
        except FileNotFoundError:
            return None
        
class FileWriter:
    def __init__(self, file_manager):
        self.file_path = file_manager.file_path

    def save_product_info(self, data):
        try:
            file = open(self.file_path, "w")
            file.write(data)
            file.close()
        except IOError:
            pass

class FileDeleter:  
    def __init__(self, file_manager):
        self.file_path = file_manager.file_path

    def delete_product_info(self):
        try:
            os.remove(self.file_path)
        except FileNotFoundError:
            pass

# Example usage
def main():
    product_id = "P12345"
    filemanager = FileManager (product_id)

    product_info = FileReader(filemanager).get_product_info()
    print("Product information:", product_info)

    new_data = "This is some updated product information."
    filewriter = FileWriter(filemanager).save_product_info(new_data)

    filedeleter = FileDeleter(filemanager).delete_product_info()
    print("Product information deleted.")
main()


