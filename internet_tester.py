from playwright.sync_api import sync_playwright


URL = "https://the-internet.herokuapp.com/"


def navigate_to_example(page, example_name:str):
    page.get_by_text(example_name).click()
    return page.url

def task_01():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(URL)
        # assert page.title() == "the-internet"
        assert "The Internet" in page.title(), "Слово не содержит зе интернет"

        text1 = page.locator("#content h2").inner_text()
        print(f"Сайт доступен. Заголовок: {text1}")

        browser.close()


def task_02():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=1000)
        page = browser.new_page()
        page.goto(URL)

        form_url = navigate_to_example(page, "Form Authentication")
        assert "/login" in page.url
        print(f"✅ Перешли в: Form Authentication | URL: {form_url}")

        browser.close()

def task_03():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=1000)
        page = browser.new_page()
        page.goto(URL)

        navigate_to_example(page, "Form Authentication")
        page.locator("#username").fill("tomsmith")
        page.locator("#password").fill("SuperSecretPassword!")
        page.get_by_text(" Login", exact=True).click()
        assert "/secure" in page.url
        print(f"✅ Успешный вход! URL:{page.url}")

        browser.close()


def task_04():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=1000)
        page = browser.new_page()
        page.goto(URL)

        navigate_to_example(page, "Form Authentication")
        page.locator("#username").fill("tomsmith")
        page.locator("#password").fill("SuperSecretPassword!")
        page.get_by_text(" Login", exact=True).click()

        page.get_by_text("Logout", exact=True).click()
        assert "/login" in page.url
        print(f"✅ Успешный выход! URL: {page.url}")

        browser.close()

def task_05():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=1000)
        page = browser.new_page()
        page.goto(URL)

        navigate_to_example(page, "Checkboxes")
        checkbox1 = page.locator("(//form[@id = 'checkboxes']/input)[1]")
        checkbox2 = page.locator("(//form[@id = 'checkboxes']/input)[2]")

        assert checkbox1.is_checked() == False
        assert checkbox2.is_checked() == True

        checkbox1.check()
        checkbox2.uncheck()

        assert checkbox1.is_checked() == True
        assert checkbox2.is_checked() == False

        print(f"✅ Checkbox 1: checked={checkbox1.is_checked()} \n"
              f" ✅ Checkbox 2: checked={checkbox2.is_checked()}")

        browser.close()


def task_06():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=1000)
        page = browser.new_page()
        page.goto(URL)

        navigate_to_example(page, "Dropdown")
        dropdownloc = page.locator("#dropdown")
        assert "Please select an option" in page.locator("#dropdown>option:first-child").inner_text()


        dropdownloc.select_option(label="Option 1")
        assert "Option 1" in page.locator("#dropdown>option:nth-child(2)").inner_text()

        dropdownloc.select_option(label="Option 2")
        assert "Option 2" in page.locator("#dropdown>option:nth-child(3)").inner_text()

        print("Выбрано: Option 2")

        browser.close()

def task_07():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=1000)
        page = browser.new_page()
        page.goto(URL)

        navigate_to_example(page, "Inputs")
        inputsloc = page.locator('[type="number"]')
        inputsloc.fill("123")

        assert "123" in inputsloc.input_value()

        inputsloc.clear()

        inputsloc.fill("456")

        assert "456" in inputsloc.input_value()

        print("✅ Введено: 456")





if __name__ == "__main__":
    task_07()