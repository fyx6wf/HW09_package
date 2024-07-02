import pandas as pd
import numpy as np
import unittest
from booklover import BookLover

class BookLoverTestSuite(unittest.TestCase):
    def test_1_add_book(self):
        test1 = BookLover("James Hopper", "fyx6wf@virginia.edu", "scifi")
        test1.add_book("The Martian", 4)
        self.assertTrue("The Martian" in test1.book_list['book_name'].values) 
    def test_2_add_book(self):
        test2 = BookLover("James Hopper", "fyx6wf@virginia.edu", "scifi")
        test2.add_book("Ready Player One", 2)
        test2.add_book("Ready Player One", 3)
        count = test2.book_list[test2.book_list['book_name'] == 'Ready Player One'].shape[0]
        self.assertEqual(count, 1) #Output: Ready Player One is already in the book list
    def test_3_has_read(self):
        test3 = BookLover("James Hopper", "fyx6wf@virginia.edu", "scifi")
        test3.add_book("Snowpiercer", 5)
        self.assertTrue(test3.has_read("Snowpiercer"))
    def test_4_has_read(self):
        test4 = BookLover("James Hopper", "fyx6wf@virginia.edu", "scifi")
        self.assertFalse(test4.has_read("Snow Crash"))
    def test_5_num_books_read(self):
        test5 = BookLover("James Hopper", "fyx6wf@virginia.edu", "scifi")
        test5.add_book("Foundation", 5)
        test5.add_book("Hyperion", 3)
        test5.add_book("Blindness", 4)
        self.assertEqual(test5.num_books_read(), 3)
    def test_6_fav_books(self):
        test6 = BookLover("James Hopper", "fyx6wf@virginia.edu", "scifi")
        test6.add_book("Children of Time", 1)
        test6.add_book("The Forever War", 3)
        test6.add_book("All Systems Red", 2) 
        my_fav_books = test6.fav_books()
        self.assertTrue(all(my_fav_books['book_rating']>3))
if __name__ == "__main__":    
    unittest.main(verbosity = 3)
    
            
    
        