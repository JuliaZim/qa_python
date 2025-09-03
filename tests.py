from main import BooksCollector
import pytest


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book("Гордость и предубеждение и зомби")
        collector.add_new_book("Что делать, если ваш кот хочет вас убить")

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.books_genre) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    # 1. Проверка, что жанр из списка genre устанавливается
    @pytest.mark.parametrize(
        "genre", ["Фантастика", "Ужасы", "Детективы", "Мультфильмы", "Комедии"]
    )
    def test_set_book_genre_set_genre_exist_in_list_genre(self, new_book, genre):
        new_book.set_book_genre("Гордость и предубеждение и зомби", genre)
        assert new_book.books_genre["Гордость и предубеждение и зомби"] == genre

    # 2. Проверка, что функция get_books_with_specific_genre возвращает коллекцию с заданным жанром
    def test_get_books_with_specific_genre_if_genre_exist_in_collector(
        self, new_books_with_genre
    ):
        collector_by_genre = new_books_with_genre.get_books_with_specific_genre("Ужасы")
        assert (
            len(collector_by_genre) == 1
            and collector_by_genre[0] == "Гордость и предубеждение и зомби"
        )

    # 3. Проверка, что метод get_book_genre возвращает жанр книги
    @pytest.mark.parametrize(
        "genre", ["Фантастика", "Ужасы", "Детективы", "Мультфильмы", "Комедии"]
    )
    def test_get_books_genre(self, genre, new_book):
        # Добавляем жанр
        new_book.set_book_genre("Гордость и предубеждение и зомби", genre)
        assert new_book.get_books_genre() == {
            "Гордость и предубеждение и зомби": genre,
        }

    # 4. Проверка, что функция get_books_for_children возвращает книги доступные для детей
    @pytest.mark.parametrize("genre", ["Фантастика", "Мультфильмы", "Комедии"])
    def test_get_books_for_children_if_book_genre_for_children(self, genre):
        collector = BooksCollector()
        collector.add_new_book("Простоквашино")
        collector.set_book_genre("Простоквашино", genre)
        collector_for_children = collector.get_books_for_children()
        assert (
            len(collector_for_children) == 1
            and collector_for_children[0] == "Простоквашино"
        )

    # 5. Проверка, что функция get_books_for_children не возвращает книги недоступные для детей
    @pytest.mark.parametrize("genre", ["Детективы", "Ужасы"])
    def test_get_books_for_children_if_book_genre_not_for_children(
        self, genre, new_book
    ):
        new_book.set_book_genre("Гордость и предубеждение и зомби", genre)
        collector_for_children = new_book.get_books_for_children()
        assert len(collector_for_children) == 0

    # 6. Проверка добавления книги в избранное
    def test_add_book_in_favorites(self, new_books_with_genre):
        new_books_with_genre.add_book_in_favorites("Гордость и предубеждение и зомби")
        assert (
            len(new_books_with_genre.favorites) == 1
            and "Гордость и предубеждение и зомби" in new_books_with_genre.favorites
        )

    # 7. Проверка удаления книги из избранного
    def test_delete_book_from_favorites(self, new_books_with_genre):
        new_books_with_genre.add_book_in_favorites("Гордость и предубеждение и зомби")
        new_books_with_genre.delete_book_from_favorites(
            "Гордость и предубеждение и зомби"
        )
        assert (
            len(new_books_with_genre.favorites) == 0
            and "Гордость и предубеждение и зомби" not in new_books_with_genre.favorites
        )

    # 8. Проверка, что функция get_list_of_favorites_books возвращает избранные книги
    def test_get_list_of_favorites_books(self, new_books_with_genre):
        new_books_with_genre.add_book_in_favorites("Гордость и предубеждение и зомби")
        assert (
            len(new_books_with_genre.get_list_of_favorites_books()) == 1
            and "Гордость и предубеждение и зомби"
            in new_books_with_genre.get_list_of_favorites_books()
        )

    # 9. Если жанра нет в спике, то он не устанавливается
    def test_set_book_genre_set_genre_not_exist_in_list_genre(self, new_book):
        new_book.set_book_genre("Гордость и предубеждение и зомби", "Триллер")
        assert len(new_book.books_genre["Гордость и предубеждение и зомби"]) == 0
