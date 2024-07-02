import pandas as pd
import numpy as np

class BookLover:
    num_books = 0
    book_list = pd.DataFrame({'book_name':[], 'book_rating':[]})
    def __init__(self, name, email, fav_genre):
        self.name = name
        self.email = email
        self.fav_genre = fav_genre
    def add_book(self, book_name, rating):
        if not self.has_read(book_name):
            new_book = pd.DataFrame({
                'book_name': [book_name], 
                'book_rating': [rating]
            })
            self.book_list = pd.concat([self.book_list, new_book], ignore_index=True)
            self.num_books += 1
        else:
            print(f"{book_name} is already in the book list")
    def has_read(self, book_name):
        return book_name in self.book_list['book_name'].values
    def num_books_read(self):
        return self.num_books
    def fav_books(self):
        return self.book_list[self.book_list['book_rating']>3]
if __name__ == '__main__':
    
    test_object = BookLover("James Hopper", "fyx6wf@virginia.edu", "scifi")
    test_object.add_book("War of the Worlds", 4)
    test_object.add_book("Dune", 5)
    test_object.add_book("Ender's Game", 5)
    test_object.add_book("The Hitchhiker's Guide to the Galaxy", 2)
    print("Books read:", test_object.num_books)
    print("Book list:\n", test_object.book_list)