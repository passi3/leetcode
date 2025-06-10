import pandas as pd

def find_books_with_no_available_copies(library_books: pd.DataFrame, borrowing_records: pd.DataFrame) -> pd.DataFrame:
    borrowing_records = borrowing_records[borrowing_records['return_date'].isnull()].groupby('book_id').size().reset_index(name='current_borrowers')
    library_books = library_books.merge(borrowing_records, on='book_id', how='left')
    return library_books[library_books['total_copies']==library_books['current_borrowers']].drop(columns=['total_copies']).sort_values(['current_borrowers', 'title'], ascending=[0, 1])