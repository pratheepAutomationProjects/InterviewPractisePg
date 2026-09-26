from playwright.sync_api import sync_playwright


class TestDropdownPage:
    def test_navigate_to_dropdown_page(self):
        with sync_playwright() as p:
            # Launch browser in headed mode for visual automation
            browser = p.chromium.launch(headless=False)
            context = browser.new_context()
            page = context.new_page()

            page.goto("https://letcode.in/dropdowns")
            print("\nPage title is:", page.title(), flush=True)

            # ------------------------------------------------------------------
            # Condition 1: "Select the apple using visible text"
            # Locator Strategy: CSS ID Selector (#fruits)
            # ------------------------------------------------------------------
            fruit_dropdown = page.locator("#fruits")
            selected_fruit = fruit_dropdown.select_option(label="Apple")
            print("1. [CSS ID Selector] Selected fruit by visible text ('Apple'):", selected_fruit, flush=True)
            assert selected_fruit == ["0"], f"Expected ['0'], got {selected_fruit}"

            # ------------------------------------------------------------------
            # Condition 2: "Select your super hero's" (Multi-select dropdown)
            # Locator Strategy: CSS ID Selector (#superheros)
            # ------------------------------------------------------------------
            hero_dropdown = page.locator("#superheros")
            # Multi-select allows selecting multiple options by value or label
            selected_heroes = hero_dropdown.select_option(label=["Aquaman", "Batman"])
            print("2. [CSS ID Selector] Selected super heroes:", selected_heroes, flush=True)
            assert "aq" in selected_heroes and "bt" in selected_heroes, f"Expected ['aq', 'bt'], got {selected_heroes}"

            # ------------------------------------------------------------------
            # Condition 3: "Select the last programming language and print all the options"
            # Locator Strategy: CSS ID Selector (#lang) & child option locators
            # ------------------------------------------------------------------
            lang_dropdown = page.locator("#lang")
            all_lang_options = lang_dropdown.locator("option").all_text_contents()
            last_language = all_lang_options[-1]
            selected_lang = lang_dropdown.select_option(label=last_language)
            print("3. [CSS ID Selector] Selected last programming language:", selected_lang, flush=True)
            print("   All available programming language options:", all_lang_options, flush=True)
            assert selected_lang == ["sharp"], f"Expected ['sharp'], got {selected_lang}"

            # ------------------------------------------------------------------
            # Condition 4: "Select India using value & print the selected value"
            # Locator Strategy: CSS ID Selector (#country)
            # ------------------------------------------------------------------
            country_dropdown = page.locator("#country")
            selected_country = country_dropdown.select_option(value="India")
            selected_value = country_dropdown.input_value()
            print("4. [CSS ID Selector] Selected country by value ('India'):", selected_country, flush=True)
            print("   Selected dropdown value:", selected_value, flush=True)
            assert selected_value == "India", f"Expected 'India', got {selected_value}"

            page.wait_for_timeout(9000)

            # Clean up
            context.close()
            browser.close()


if __name__ == "__main__":
    test_obj = TestDropdownPage()
    test_obj.test_navigate_to_dropdown_page()
