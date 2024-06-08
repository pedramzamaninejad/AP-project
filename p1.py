class UniLibManager:
    ...


class Library:
    def __init__(self, path: str) -> None:
        self.path = path
        self.name = self.path.split('/')[-1]
        self.books: list[Book] = []

    def read_book_from_csv(self) -> None:
        import pandas as pd
        import os

        os.chdir(f'{self.path}')
        for i in os.listdir():
            book = pd.read_csv(self.path + "/" + i, header=0, delimiter=',')

        self.books += [
            Book(book.loc[i]['name'],
                 book.loc[i]['publish_year'],
                 book.loc[i]['writers'],
                 book.loc[i]['keyword']) for i in range(len(book))
        ]

    def add_book(self, name: str, year_published: str, writers: str, keyword: str) -> str:
        self.books.append(Book(name, year_published, writers, keyword))

        return "Book has been added successfuly"

    def remove_book(self, name, year_published) -> str:
        for i in self.books:
            if i.name == name and year_published == i.publish_year:
                self.books.remove(i)
                return "Book has been removed successfully"
        return "Book not found"

    def book_info(self, name) -> dict | str:
        for i in self.books:
            if i.name == name:
                return i.info()
        return "Book not found"

    def __len__(self) -> int:
        return len(self.books)

    def __del__(self):
        import pandas as pd

        data = {'name': [], 'publish_year': [], 'writers': [], 'keyword': []}
        for book in self.books:
            book_info = book.info()
            data['name'].append(book_info['name'])
            data['publish_year'].append(book_info['year_published'])
            data['writers'].append(book_info['writers'])
            data['keyword'].append(book_info['keyword'])

        df = pd.DataFrame(data)

        df.to_csv(self.path + "/" + "books.csv", sep=',', encoding='utf-8')


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
