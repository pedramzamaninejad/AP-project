class UniLibManager:
    ...

class Library:
    def __init__(self, path: str):
        self.path = path
        self.name = self.path.split('/')[-1]
        self.books: list[dict] = []

    def read_book_from_csv(self):
        import pandas as pd
        import os

        os.chdir(f'{self.path}')
        for i in os.listdir():
            book = pd.read_csv(self.path+"/"+i, header=0, delimiter=' ')

        self.books += [
                        {'name': book.loc[i]['name'],
                         'writers': book.loc[i]['writers'],
                         'year_published': book.loc[i]['year_published'],
                         'keyword': book.loc[i]['keyword'],
                         } for i in range(len(book))
        ]

class Book:
    def __init__(self, name: str, publish_year: str, writers: str | list[str], key_word: str):
        self.name = name
        self.published_year = publish_year
        self.writers = writers
        self.key_word = key_word
