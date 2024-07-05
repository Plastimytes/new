#algoritms??
def bubble_sort_books(book_titles):
    n=len(book_titles)
    for i in range(n):
        for j in range(0,n-i-1):
            if book_titles[j]>book_titles[j+1]:
                book_titles[j],book_titles[j+1]=book_titles[j+1],book_titles[j]
                return book_titles
            
book_titles=["python for dummies","Web design by Mr.Kato. M","1984","Passion of Christ"]
sorted_books=bubble_sort_books(book_titles)
print(sorted_books)

            
