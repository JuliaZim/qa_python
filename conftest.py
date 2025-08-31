import pytest
from main import BooksCollector


@pytest.fixture
def collector():
    collector = BooksCollector()
    return collector


@pytest.fixture
def new_book(collector):
    collector.add_new_book("Гордость и предубеждение и зомби")
    return collector


@pytest.fixture
def new_books_with_genre(collector):
    collector.add_new_book("Гордость и предубеждение и зомби")
    collector.add_new_book("Что делать, если ваш кот хочет вас убить")
    collector.set_book_genre("Гордость и предубеждение и зомби", "Ужасы")
    collector.set_book_genre("Что делать, если ваш кот хочет вас убить", "Детективы")
    return collector
