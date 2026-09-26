from playwright.sync_api import sync_playwright


class TestInputPage:
    def test_navigate_to_test_page(self):
        with sync_playwright() as p:
            # Launch browser in headed mode for visual automation
            browser = p.chromium.launch(headless=False)
            context = browser.new_context()
            page = context.new_page()

            page.goto("https://letcode.in/edit")
            print("\nPage title is:", page.title())

            # ------------------------------------------------------------------
            # Condition 1: "Enter your full Name"
            # Locator Strategy: Built-in Locator (get_by_placeholder)
            # ------------------------------------------------------------------
            full_name_box = page.get_by_placeholder("Enter first & last name")
            full_name_box.fill("Pratheep S")
            print("1. [Built-in Locator] Filled full name:", full_name_box.input_value())

            # ------------------------------------------------------------------
            # Condition 2: "Append a text and press keyboard tab"
            # Locator Strategy: CSS ID Selector (#join)
            # ------------------------------------------------------------------
            append_box = page.locator("#join")
            append_box.focus()
            append_box.press_sequentially(" at coding")
            append_box.press("Tab")
            print("2. [CSS ID Selector] Appended text:", append_box.input_value())

            # ------------------------------------------------------------------
            # Condition 3: "What is inside the text box"
            # Locator Strategy: XPath Selector (//input[@id='getMe'])
            # ------------------------------------------------------------------
            get_text_box = page.locator("//input[@id='getMe']")
            inside_text = get_text_box.input_value()
            print("3. [XPath Selector] Text inside box:", inside_text)

            # ------------------------------------------------------------------
            # Condition 4: "Clear the text"
            # Locator Strategy: CSS Attribute Selector (input[id='clearMe'])
            # ------------------------------------------------------------------
            clear_box = page.locator("input[id='clearMe']")
            clear_box.clear()
            print("4. [CSS Attribute Selector] Text after clearing:", repr(clear_box.input_value()))

            # ------------------------------------------------------------------
            # Condition 5: "Confirm edit field is disabled"
            # Locator Strategy: Playwright Built-in ID Selector (id=noEdit)
            # ------------------------------------------------------------------
            disabled_box = page.locator("id=noEdit")
            is_disabled = disabled_box.is_disabled()
            print("5. [Playwright ID Selector] Confirm edit field is disabled:", is_disabled)
            assert is_disabled, "Expected field 'noEdit' to be disabled"

            # ------------------------------------------------------------------
            # Condition 6: "Confirm text is readonly"
            # Locator Strategy: XPath Attribute Selector (//input[@readonly])
            # ------------------------------------------------------------------
            readonly_box = page.locator("//input[@readonly]")
            is_readonly = readonly_box.get_attribute("readonly") is not None
            readonly_text = readonly_box.input_value()
            print(f"6. [XPath Attribute Selector] Confirm text is readonly: {is_readonly} (Value: '{readonly_text}')")
            assert is_readonly, "Expected field 'dontwrite' to be readonly"

            page.wait_for_timeout(3000)

            # Clean up
            context.close()
            browser.close()


if __name__ == "__main__":
    test_obj = TestInputPage()
    test_obj.test_navigate_to_test_page()

