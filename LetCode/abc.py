from playwright.sync_api import sync_playwright


class TestInputPage:
    def test_navigate_to_test_page(self):
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            context = browser.new_context()
            page = context.new_page()

            page.goto("https://letcode.in/edit")
            print("Page title is:", page.title())
            page.get_by_placeholder("Enter first & last name").fill("Pratheep S")
            # Built-in Locators
            page.get_by_label("Append a text and press keyboard tab").fill("Pr")
            page.get_by_role("textbox", name="Append a text and press keyboard tab")
            page.get_by_placeholder("Enter")
            # CSS & ID Locators
            append_input = page.get_by_label("Append a text and press keyboard tab")
            current_text = append_input.input_value()
        
        # 2. Fill the field with the old text + the new text
            append_input.fill(current_text + " and feeling great")
            page.locator("#join").fill("Pr")
            page.locator("input[id='join']").fill("YY")
            page.locator("input[type='text'][id='join']").fill("PP")
            # XPATH
            page.locator("//input[@id='join']").fill("oo")
            page.locator("//input[contains(@class, 'ring-offset-background')]").nth(1).fill("I am good")
            page.wait_for_timeout(1000)

            # Close the context and browser
            context.close()
            browser.close()
            abc.close()