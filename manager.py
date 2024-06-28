from func import UniLibManager, Library, Book, run_manager, pprint
import time
import os

pprint("""Hello This is a command line manager for Universities
      So You can manage your libraries easly""", 'green')
time.sleep(1)
pprint("""This manager rely on the path of you University folder and only one University folder it will work with
Folder arrangement should be something like shown""", 'green')
time.sleep(1)
pprint("""path-to-your-folder/name-of-university""", 'red',attrs=['bold'])
time.sleep(1)
pprint('''This will be enough you can add library, book, and stuff like this
Lets Begin''')


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

University = run_manager(path)

# while True:
