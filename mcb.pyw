#! python3
# mcb.pyw clipboard storing multiple elements (dictionary-like)
# py.exe mcb.pyw save <keyword> save clipboard to keyword
# py.exe mcb.pyw list - load all keywords to clipboard
# py.exe mcb.pyw <keyword> copy keyword's value to clipboard
import pyperclip
import shelve
import sys

# create binary storage object
mcbShelf  = shelve.open('mcb')
# save functionality, if there are three arguments
if len(sys.argv) == 3: 
    # and second arg is 'save'
    if sys.argv[1].lower() == 'save':
        # save clipboard int binary storage under third argument keyword
        mcbShelf[sys.argv[2]] = pyperclip.paste()
        # delete entry under third argument keyword if user confirms
    elif sys.argv[1].lower() == 'delete':
        print(f'Would you like to delete <{sys.argv[2]}> entry from mcb storage?')
        confirmation = input()
        if confirmation.lower() in ['y', 'yes']:
            del mcbShelf[sys.argv[2]]
# if two arguments
elif len(sys.argv) == 2:
    # if second argument == list copy list of binary objects keys into clipboard 
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
        # clear storage if passed delete as second arguent and confirmed
    elif sys.argv[1].lower() == 'delete':
        print('Would you like to delete all entries from mcb storage?')
        confirmation = input()
        if confirmation.lower() in ['y', 'yes']:
            print('OK')
            mcbShelf.clear()
    # else if argument is a key in binary object, copy assigned value to clipboard
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])
# close storage
mcbShelf.close()