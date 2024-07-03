from func import run_manager, pprint, get_libraires, get_stage
import time
import os

pprint("""Hello This is a command line manager for Universities
So You can manage your libraries easly\n""", 'green')
time.sleep(1)
pprint("""This manager rely on the path of you University folder and only one University folder it will work with
Folder arrangement should be something like shown\n""", 'green')
time.sleep(1)
pprint("""path-to-your-folder/name-of-university\n""", 'red',attrs=['bold'])
time.sleep(1)
pprint('''This will be enough you can add library, book, and stuff like this
Lets Begin\n''')

time
path = input("Please Enter The path of your university: ")

while True:
    try:
        os.chdir(path)
        break
    except FileNotFoundError:
        pprint('The path given was not found', 'red', attrs=['bold'])
        pprint('Do you want to create The folder in the given address? (y, n)', 'green', attrs=['underline'])
        check = input(':')
        if check != 'y' or check != 'n':
            continue
        elif check == 'y':
            pprint('OK', 'green')
            os.mkdir(path)
            break
        elif check == 'n':
            pprint('Then goodbye', 'gray')
            pprint('Pedram Zamaninejad', 'blue', atter=['bold', 'underline'])
            quit()

university = run_manager(path)

while True:
    stage = get_stage()
    if 1 <= int(stage) <= 7:
        pprint('To do these stuff you need to chose The library', 'red', attrs=['bold'])
        pprint(f'{university.libraries}', 'blue')
        time.sleep(1)
        pprint('Chose the library\n(mind the spelling): ')
        lib_name = input()
        
        library = get_libraires(university, lib_name)
        pprint(f"now you are using {library.name:-^20}")
        time.sleep(0.8)
        match stage:
            case '1':
                pprint(f"What do you want to set the new name:", 'yellow', attrs=['underline'])
                new_name = input()
                current_name = library.name
                print(university.update_library(current_name=current_name, new_name=new_name)[0])
            
            case '2':
                pprint(f'Here are The Libraries {university.name_libraries()}')

            case '3':
                pprint("Which Library do you want to delete: ", 'yellow', attrs=['underline'])
                lib_name = input()
                pprint(university.remove_library(lib_name)[0])

            case '4':
                pprint('What Book do you want to add: ', 'yellow')
                name = input('What is the name of the Book: ')
                year_published = input("What is the year the book was writen: ")
                writers = input("Who did writer name: ")
                keyword = input('What is the keyword of this book: ')

                message, code = library.add_book(name, year_published, writers, keyword)
                if code != 201:
                    pprint(message, 'red', attrs=['bold'])
                else: 
                    pprint(message, 'green', attrs=['bold'])

            case '5':
                pprint('What is the Book you want to update: ', 'yellow')
                current_name = input("Which book do you want to change: (name) ")
                current_year = input(f"What year was the book {current_name} published: ")
                new_name = input(f"Do you want to change the name of this book ?\n(leave blank and enter if not): ")
                new_year = input(f"DO you want to change the year this book was publushed ?\n(leave blank and enter if not): ")
                new_writer = input(f"Do you want to change the writers of this book ?\n(leave blank and enter if not): ")
                new_keyword = input(f"Do you want to change the keyword of this book ?\n(leave blank and enter if not): ")
                message, code = library.book_edit(current_name, current_year, new_name, new_year, new_writer, new_keyword)
                if code != 201:
                    pprint(message, 'red', attrs=['bold'])
                else:
                    pprint(message, 'green', attrs=['underline'])

            case '6':
                pprint("Which book do you want to see information ?", 'yellow')
                name = input("Name of the book is : ")
                year = input("Year published of the book\n(Optional leave blank if you dont need it) :")
                message, code = library.book_info(name, year)
                if code != 201:
                    pprint(message, 'red', attrs=['bold'])
                else:
                    pprint(message, 'green', attrs=['underline'])

            case '7':
                pprint('Which book do you want to delete', 'yellow')
                name = input("Name: ")
                year = input("Year: ")
                message, code = library.remove_book(name, year)
                if code != 201:
                    pprint(message, 'red', attrs=['bold'])
                else:
                    pprint(message, 'green', attrs=['underline'])
    else:
        match stage:
            case '0':
                pprint('What is the name of the library you want to add ', 'yellow')
                name = input(': ')
                message, code = university.add_library(name)
                if code != 201:
                    pprint(message, 'red', attrs=['bold'])
                else:
                    pprint(message, 'green', attrs=['underline'])
            case '8':
                pprint("Good buy", 'blue')
                pprint("Best Wishes from :", 'green')
                pprint("Foad rezaii", 'red')
                pprint("Pedram zamaninejad", 'red')
                quit()
     