import pytest
from selenium import webdriver

class TestMainPage():
    # номер 1  y
    @pytest.mark.xfail
    @pytest.mark.smoke
    def test_guest_can_login(self, browser):
        print('Выполено - 1')
        assert True

    # номер 2 -
    @pytest.mark.regression
    def test_guest_can_add_book_from_catalog_to_basket(self, browser):
        print('Выполено - 2')
        assert True
        print('Выполено - 2')

class TestBasket():
    # номер 3 y
    @pytest.mark.skip(reason="not implemented yet")
    @pytest.mark.smoke
    def test_guest_can_go_to_payment_page(self, browser):
        print('Выполено - 3')
        assert True

    # номер 4  y
    @pytest.mark.smoke
    def test_guest_can_see_total_price(self, browser):
        print('Выполено - 4')
        assert True

@pytest.fixture
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()

@pytest.mark.skip
class TestBookPage():
    # номер 5 y
    @pytest.mark.smoke
    def test_guest_can_add_book_to_basket(self, browser):
        assert True
        print('Выполено - 5')

    # номер 6
    @pytest.mark.regression
    def test_guest_can_see_book_price(self, browser):
        assert True
        print('Выполено - 6')

# номер 7 -
@pytest.mark.beta_users
@pytest.mark.smoke
def test_guest_can_open_gadget_catalogue(browser):
    assert True
    print('Выполено - 7')