import time

link = " http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_add_to_basket_button(browser):
    browser.get(link)
    time.sleep(30)
    add_button = browser.find_element_by_class_name("btn.btn-lg.btn-primary.btn-add-to-basket")
    assert add_button , "button is not on the page"



