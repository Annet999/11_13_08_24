# library_manager/utils/data_validation.py
def validate_book_data(data):
    if not all(key in data for key in ['title', 'author', 'genre']):
        return False
    if not all(isinstance(data[key], str) and data[key] for key in ['title', 'author', 'genre']):
        return False
    return True