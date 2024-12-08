import os
from abc import ABC, abstractmethod
class Storage(ABC):
    @abstractmethod
    def save(self):
        pass
    @abstractmethod
    def load(self):
        pass
    @abstractmethod
    def delete(self):
        pass
    @abstractmethod
    def isExists(self):
        pass
class MemoryStorage(Storage):
    def __init__(self):
        self.data = {}
    def save(self,key,value):
        self.data[key] = value
    def load(self,key):
        if self.isExists(key):
            return self.data[key]
        raise KeyError(f"Key '{key}' does not exist.")
    def delete(self,key):
        if self.isExists(key):
            del self.data[key]
    def isExists(self,key):
        return key in self.data.keys()
class FileStorage(Storage):
    def __init__(self, directory,filename):
        self.filepath = os.path.join(directory, filename)
    def save(self, content):
        with open(self.filepath, 'w') as file:
            file.write(content)
    def load(self):
        with open(self.filepath, 'r') as file:
            data = file.read()
        return data
    def delete(self):
        os.remove(self.filepath)
    def isExists(self):
        return os.path.exists(self.filepath)
def handle_file_operations(directory, filename, content, storage=Storage):
    storage.save(filepath, content)
    data = storage.load(filepath)
    print(f"Loaded {filename.split('.')[0]}: {data}")
    if storage.isExists(filepath):
        print(f"File '{filepath}' exists.")
    else:
        print(f"File '{filepath}' does not exist.")
    storage.delete(filepath)
    print(f"Data deleted for {filename}.")
    if not storage.isExists(filepath):
        print(f"Key '{filename.split('.')[0]}' successfully deleted.")
def main():
    directory = "data_storage"
    stoarge = MemoryStorage()
    handle_file_operations(directory, "username.txt", "JohnDoe", stoarge)
    handle_file_operations(directory, "email.txt", "john.doe@example.com", stoarge)
if __name__ == "__main__":
    main()