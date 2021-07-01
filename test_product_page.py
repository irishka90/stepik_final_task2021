from pages.product_page import PageObject


def test_guest_can_add_product_to_basket(browser):
    login_link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = PageObject(browser, login_link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.success_add_to_basket()
    page.book_price()

