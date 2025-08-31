# qa_python
Добавление юнит тестов к функционалу BooksCollector
# Добавление книги
test_add_new_book_add_two_books

# 1. Проверка, что жанр из списка genre устанавливается
test_set_book_genre_set_genre_exist_in_list_genre

# 2. Проверка, что функция get_books_with_specific_genre возвращает коллекцию с заданным жанром
test_get_books_with_specific_genre_if_genre_exist_in_collector

# 3. Проверка, что метод get_book_genre возвращает жанр книги
test_get_books_genre

# 4. Проверка, что функция get_books_for_children возвращает книги доступные для детей
test_get_books_for_children_if_book_genre_for_children
    
# 5. Проверка, что функция get_books_for_children не возвращает книги недоступные для детей
test_get_books_for_children_if_book_genre_not_for_children
    
# 6. Проверка добавления книги в избранное
test_add_book_in_favorites
    
# 7. Проверка удаления книги из избранного
test_delete_book_from_favorites
    
# 8. Проверка, что функция get_list_of_favorites_books возвращает избранные книги
test_get_list_of_favorites_books
    
# 9. Если жанра нет в спике, то он не устанавливается
test_set_book_genre_set_genre_not_exist_in_list_genre
