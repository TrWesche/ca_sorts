import csv
import os

# This code loads the current book
# shelf data from the csv file
def load_books(filename):
  bookshelf = []
  with open(os.path.join("C:\\","Local Repos","ca_sorts","a_sorted_tale",filename)) as file:
      shelf = csv.DictReader(file)
      for book in shelf:
          # add your code here
          print(book.get('title'))
          # author_lower = {'author_lower' : book.get('author').lower()}
          # title_lower = {'title_lower' : book.get('title').lower()}
          book_new = {'title' : book.get('title'), 'author' : book.get('author'), 'title_lower' : book.get('title').lower(), 'author_lower' : book.get('author').lower()}
          # book = book.append(title_lower)
          bookshelf.append(book_new)
          # print(book_new)
  return bookshelf

# print(ord("z"))
# print(ord("1"))
# print(ord("A")) 