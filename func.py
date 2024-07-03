import random
from typing import Tuple
from p1 import Library, UniLibManager
from termcolor import colored

def roll_dice() -> int:
    result = random.randint(1,6)
    return result


def sort_data_ludo(data: list(Tuple[int, int])) -> list(Tuple[int, int]): # type: ignore
    def change(li):
        return li[::-1]
    start_1 = 0, 8
    sort = []
    sort.append(start_1)
    j_nsort = []
    for i, j in data[3:]:
        if j >= start_1[1] and i > start_1[0]:
            if i != 6:
                sort.append((i, j))
            else:
                j_nsort.append((i,j))
                if j == 12:
                    row_sort = change(j_nsort)
                    sort.extend(row_sort)
    for i in sort:
        data.remove(i)

    sort.append((10, 7))
    data.reverse()
    data[-1], data[-2] = data[-2], data[-1]
    data[10], data[11], data[12], data[13], data[14] = data[14], data[13], data[12], data[11], data[10]
    sort.extend(data)
    return sort

def pprint(message: str, *args, **kwargs) -> None:
    print(colored(message, *args, **kwargs))


def run_manager(path: str) -> UniLibManager:
    u1 = UniLibManager(path)
    pprint(f'Manager is running for\n{u1.name:-^20}', 'green')
    return u1

def get_libraires(university: UniLibManager, library_name:str) -> Library | None:
    try:
        for i in university.libraries:
            if i.name == library_name:
                lib: Library = i
                return lib
    except ValueError:
        pprint(f'Library [{library_name}] you wanted does not exist in the university\nYou can make this library later', 'red')
        quit()

def get_stage() -> str:
    li = [
        'create library', 'update library', 'retrive library', 'remove library',
        'create book', 'update book', 'retrive book', 'remove book', 'quit'
        ]
    pprint(f'''With This command line you can use these command:''', 'green', attrs=['bold'])
    for index, options in enumerate(li):
        pprint(f'To {options:-^5} use code {index:-^5}')
    pprint('Now decide Waht you want to do', 'blue', attrs=['bold'])
    stage = input(':')

    return stage
