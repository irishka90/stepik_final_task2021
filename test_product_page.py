import pytest

from pages.product_page import PageObject


@pytest.mark.xfail(reason="won't be fixed")
@pytest.mark.parametrize('link', ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])
def test_guest_can_add_product_to_basket(browser, link):
    login_link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{link}"
    page = PageObject(browser, login_link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.success_add_to_basket()
    page.book_price()
