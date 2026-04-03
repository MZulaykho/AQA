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


if __name__ == "__main__":
    task_05()
