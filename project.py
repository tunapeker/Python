from library import *
print("""
Library program created by Tuna Peker.

Actions:

1. Adding books
2.Showing the books
3.Searching the books
4.Deleting books

Press q to leave the program.
""")
library = Library()

while True:
    inp = input("Enter the process:")
    if inp == "q":
        library.connection_stop()
        print("Exiting the program...")
        time.sleep(1)
        print("See you next time.")
        break
    elif inp == "1":
        isim = input("Name:")
        yazar = input(("Author:"))
        sayfa_sayisi = int(input("Page number:"))
        baski = int(input("Edition:"))
        new_book = Book(isim,yazar,sayfa_sayisi,baski)
        library.add_book(new_book)
    elif inp == "2":
        library.select_all_data()
    elif inp == "3":
        isim = input("Name of the book:")
        print("Searching...")
        time.sleep(1)
        library.select_data(isim)
    elif inp == "4":
        isim = input("Enter the name of the book you want to be deleted:")
        print("Deleting...")
        time.sleep(1)
        library.delete_book(isim)
    else:
        print("Invalid process!")