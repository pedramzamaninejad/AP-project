import random
from p1 import Book, Library, UniLibManager
from termcolor import colored

def roll_dice() -> int:
    result = random.randint(1,6)
    print('It happend')
    return result


def pprint(message: str, *args, **kwargs) -> None:
    print(colored(message, *args, **kwargs))


def run_manager(path: str) -> UniLibManager:
    u1 = UniLibManager(path)
    pprint(f'Manager is running for\n{u1.name:-^20}', 'green')
    return u1

def get_libraires(university: UniLibManager, library_name:str) -> Library | None:
    try:
        lib: Library = university.libraries(university.libraries.index(library_name))
        return lib
    except ValueError:
        pprint(f'Library [{library_name}] you wanted does not exist in the university\nYou can make this library later', 'red')
        return None

def get_stage() -> str:
    li = [
        'create library', 'update library', 'retrive library', 'remove library',
        'create book', 'update book', 'retrive book', 'remove book',
        ]
    pprint(f'''With This command line you can use these command:''', 'green', attrs=['bold'])
    for index, options in enumerate(li):
        pprint(f'To {options:^5} use code {index:^5}')
    pprint('Now decide Waht you want to do', 'blue', attrs=['bold'])
    stage = input(':')

    return stage
