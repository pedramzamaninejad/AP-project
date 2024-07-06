import os
import shutil
from typing import Tuple
import pandas as pd
import atexit


class UniLibManager:

    def __init__(self, path: str) -> None:
        self.path = path
        self.name = self.path.split('/')[-1]
        self.libraries: list[Library] = self.__read_libraries_from_dir()
        atexit.register(self.__save_library_items)

    def __read_libraries_from_dir(self) -> list:
        libraries = []

        os.chdir(self.path)
        for i in os.listdir():
            if not i.startswith('.') and not i == '__pycache__':
                libraries.append(Library(os.path.join(self.path, i)))

        return libraries

    def add_library(self, name: str) -> Tuple[str, int]:
        os.chdir(self.path)
        try:
            os.mkdir(name)
            self.libraries.append(Library(os.path.join(self.path, name)))
            data = {
                'name': [],
                'publish_year': [], 
                'writers': [], 
                'keyword': []
            }  
            df = pd.DataFrame(data)
            df.to_csv(os.path.join(name, "books.csv"), sep='\t', encoding='utf-8', index=False)
            return f"library {name} has been added successfully", 201
        
        except FileExistsError:
            return f"Library {name} already existed", 404
        
        except Exception as e:
            return f"An error occurred: {e}", 500
        
    def remove_library(self, name: str) -> str:
        os.chdir(self.path)
        try: 
            shutil.rmtree(name)
            self.libraries.remove(self.libraries.index(name))
            return f"Library {name} has been removed successfully.", 201
        
        except FileNotFoundError:
            return f"Library {name} does not exist.", 404
        
        except Exception as e:
            return f"An error occurred: {e}", 500
        
    def name_libraries(self):
    #     library_name = []

    #     for library in self.libraries:
    #         library_name.append(library.name)
        
    #     return library_name
        return self.libraries

    def update_library(self, current_name: str, new_name: str) -> str:
        os.chdir(self.path)

        try:
            os.rename(current_name, new_name)
            return f"Library {current_name} has been changed to {new_name}", 201
        
        except FileNotFoundError:
            return f"Library {current_name} does not exists", 404
        
        except Exception as e:
            return f"An error occurred: {e}", 500
        
    # def __del__(self):
    #     print(self.libraries)
    #     for library in self.libraries:
    #         del library
    def __save_library_items(self):
        for library in self.libraries:
            del library


class Library(object):

    def __init__(self, path: str) -> None:
        self.path = path
        self.name = self.path.split('/')[-1]
        self.books: list[Book] = self.__read_book_from_csv()
        atexit.register(self.__save_books_to_csv)

    def __read_book_from_csv(self) -> list:

        books = []

        os.chdir(self.path)
        for i in os.listdir():
            book = pd.read_csv(os.path.join(self.path, i), header=0, delimiter='\t')
        
            books += [
                Book(book.iloc[i]['name'],
                    book.iloc[i]['publish_year'],
                    book.iloc[i]['writers'],
                    book.iloc[i]['keyword']) for i in range(len(book))
            ]
 
        return books

    def add_book(self, name: str, year_published: str, writers: str, keyword: str) -> tuple[str, int]:
        if name not in self.books:
            self.books.append(Book(name, year_published, writers, keyword))
            return "Book has been added successfuly", 201
        elif name in self.books:
            locate = self.books.index(name)
            obj = self.books[locate]
            if obj.published_year == year_published:
                return f"A book named with this name and publish year already exist", 403

    def remove_book(self, name, year_published) -> tuple[str, int]:
        for i, obj in enumerate(self.books):
            if obj.published_year == year_published and obj.name == name:
                self.books.remove(i)
                return f"Book [{name}] Was removed", 201

        return f"Book [{name}] published in [{year_published}] was not found", 404

    def book_info(self, name, publish_year='') -> Tuple[str | dict, int]:
        if publish_year != '':
            print("Not Empty")
            for i in self.books:
                if i.name == name and i.published_year == int(publish_year):
                    return i.info(), 201
            
            return f'probebly book [{name}] in [{publish_year}] was not found', 404
        else:
            for i in self.books:
                if name == i.name:
                    return i.info(), 201
            return "Book not found", 404
    
    def book_edit(self, name, publish_year, new_name='', new_publish_year='', new_writers='', new_keyword=''):
        for i, obj in enumerate(self.books):
            if obj.published_year == publish_year and obj.name == name:
                obj.update(new_name, new_publish_year, new_writers, new_keyword), 201
                return f"Changes has been made", 201
        return f'Book [{name}] Not found', 404
        
    def __save_books_to_csv(self):
        import pandas as pd # To desolve the a problem

        data = {
            'name': [],
            'publish_year': [], 
            'writers': [], 
            'keyword': []
        } 
        for book in self.books:

            data['name'].append(book.name)
            data['publish_year'].append(book.published_year)
            data['writers'].append(book.writers)
            data['keyword'].append(book.key_word)
        df = pd.DataFrame(data)
        df.to_csv(os.path.join(self.path, "books.csv"), sep='\t', encoding='utf-8', index=False)
    
    def __len__(self) -> int:
        return len(self.books)

    def __repr__(self) -> str:
        return str(self.name)

    def __del__(self):
        print(f'Library: {self.name} has been deleted succesfully')


class Book:
    def __init__(self, name: str, publish_year: str, writers: str | list[str], key_word: str):
        self.name = name
        self.published_year = publish_year
        self.writers = writers
        self.key_word = key_word

    def info(self):
        return {'name': self.name,
                'year_published': self.published_year,
                'writers': self.writers,
                'keyword': self.key_word}

    def update(self, name='', published_year='', writers='', keyword=''):
        if name != '':
            self.name = name
        if published_year != '':
            self.published_year = published_year
        if writers != '':
            self.writers = writers
        if keyword != '':
            self.key_word = keyword

    def __repr__(self) -> str:
        return self.name