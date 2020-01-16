import utils
import sorts

#################################################
###        Load in short bookshelf order      ###
#################################################

bookshelf = utils.load_books('books_small.csv')
bookshelf_v1 = bookshelf.copy()
bookshelf_v2 = bookshelf.copy()
print("\n##### Bookshelf Load Complete #####\n")


#################################################
###  Order by title ascending - Bubble Sort   ###
#################################################
def by_title_ascending(book_a, book_b):
    return book_a.get('title_lower') > book_b.get('title_lower')

sort_1 = sorts.bubble_sort(bookshelf, by_title_ascending)
for val in sort_1:
    print(val)
print("\n ##### Bookshelf Sort by Title Complete #####\n")


#################################################
### Order by author ascending  - Bubble Sort  ###
#################################################
def by_author_ascending(book_a, book_b):
    return book_a.get('author_lower') > book_b.get('author_lower')

sort_2 = sorts.bubble_sort(bookshelf_v1, by_author_ascending)
for val in sort_2:
    print(val)
print("\n ##### Bookshelf Sort by Author Complete #####\n")


#################################################
###   Order by author ascending - Quick Sort  ###
#################################################
sorts.quicksort(bookshelf_v2, 0, len(bookshelf_v2) - 1, by_author_ascending)
for val in bookshelf_v2:
    print(val)
print("\n ##### Bookshelf Sort by Author Complete #####\n")



#################################################
###        Load in long bookshelf order       ###
#################################################
long_bookshelf = utils.load_books('books_large.csv')

def by_total_length(book_a, book_b):
    return (len(book_a.get('title'))+len(book_a.get('author'))) > (len(book_b.get('title'))+len(book_b.get('author')))

################################################
##       Order by length - Bubble Sort       ###
################################################

sort_3 = sorts.bubble_sort(long_bookshelf, by_total_length)

#################################################
###        Order by length - Quick Sort       ###
#################################################

sorts.quicksort(long_bookshelf, 0, len(long_bookshelf)-1, by_total_length)