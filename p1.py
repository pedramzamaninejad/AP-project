class UniLibManager:
    ...


class Library:
    def __init__(self, path: str) -> None:
        self.path = path
        self.name = self.path.split('/')[-1]
        self.books: list[dict] = []

    def read_book_from_csv(self) -> None:
        import pandas as pd
        import os

        os.chdir(f'{self.path}')
        for i in os.listdir():
            book = pd.read_csv(self.path + "/" + i, header=0, delimiter=' ')

        self.books += [
            Book(book.loc[i]['name'],
                 book.loc[i]['year_published'],
                 book.loc[i]['writers'],
                 book.loc[i]['keyword']) for i in range(len(book))
        ]

    def __len__(self) -> int:
        return len(self.books)


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

    def update(self, name=None, published_year=None, writers=None, keyword=None):
        if name is not None:
            self.name = name
        if published_year is not None:
            self.published_year = published_year
        if writers is not None:
            self.writers = writers
        if keyword is not None:
            self.key_word = keyword
