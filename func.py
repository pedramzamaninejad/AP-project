import random
from p1 import Book, Library, UniLibManager
from termcolor import colored

def roll_dice():
    result = random.randint(1,6)
    print('It happend')
    return result


def pprint(message, *args, **kwargs):
    print(colored(message, *args, **kwargs))


def run_manager(path):
    u1 = UniLibManager(path)
    pprint(f'Manager is running for\n{u1.name:-^20}', 'green')
    return u1
