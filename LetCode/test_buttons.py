from playwright.sync_api import sync_playwright


class TestButtonPage:
    def test_navigate_to_button_page(self):
        with sync_playwright() as p:
            # Launch browser in headed mode for visual automation
            browser = p.chromium.launch(headless=False)
            context = browser.new_context()
            page = context.new_page()

            page.goto("https://letcode.in/button")
            print("\nPage title is:", page.title(), flush=True)

            # ------------------------------------------------------------------
            # Condition 1: "Goto Home and come back here using driver commands"
            # Locator Strategy: Built-in Locator (get_by_role)
            # ------------------------------------------------------------------
            home_button = page.get_by_role("link", name="Goto Home")
            home_button.click()
            print("1. [Built-in Locator] Clicked 'Goto Home'. Current URL:", page.url, flush=True)
            page.go_back()
            print("   Returned back to button page. Current URL:", page.url, flush=True)

            # ------------------------------------------------------------------
            # Condition 2: "Get the X & Y co-ordinates"
            # Locator Strategy: CSS ID Selector (#position)
            # ------------------------------------------------------------------
            position_box = page.locator("#position").bounding_box()
            if position_box:
                print(f"2. [CSS ID Selector] Button Location -> X: {position_box['x']}, Y: {position_box['y']}", flush=True)

            # ------------------------------------------------------------------
            # Condition 3: "Find the color of the button"
            # Locator Strategy: XPath Selector (//button[@id='color'])
            # ------------------------------------------------------------------
            color_btn = page.locator("//button[@id='color']")
            btn_color = color_btn.evaluate("el => getComputedStyle(el).backgroundColor")
            print("3. [XPath Selector] Button Background Color:", btn_color, flush=True)

            # ------------------------------------------------------------------
            # Condition 4: "Find the height & width of the button"
            # Locator Strategy: CSS Attribute Selector (button[id='property'])
            # ------------------------------------------------------------------
            prop_box = page.locator("button[id='property']").bounding_box()
            if prop_box:
                print(f"4. [CSS Attribute Selector] Button Size -> Height: {prop_box['height']}px, Width: {prop_box['width']}px", flush=True)

            # ------------------------------------------------------------------
            # Condition 5: "Confirm button is disabled"
            # Locator Strategy: Playwright Attribute Selector (button[title='Disabled button'])
            # ------------------------------------------------------------------
            disabled_btn = page.locator("button[title='Disabled button']")
            is_disabled = disabled_btn.is_disabled()
            print("5. [Attribute Selector] Confirm button is disabled:", is_disabled, flush=True)
            assert is_disabled, "Expected button to be disabled"

            # ------------------------------------------------------------------
            # Condition 6: "Click and Hold Button"
            # Locator Strategy: XPath / Text Selector (page.locator("button", has_text="Button Hold!"))
            # ------------------------------------------------------------------
            hold_btn = page.locator("button", has_text="Button Hold!")
            hold_btn.hover()
            page.mouse.down()
            page.wait_for_timeout(1500)  # Hold for 1.5 seconds
            page.mouse.up()
            print("6. [Text Locator] Click and hold performed successfully.", flush=True)

            page.wait_for_timeout(3000)

            # Clean up
            context.close()
            browser.close()


if __name__ == "__main__":
    test_obj = TestButtonPage()
    test_obj.test_navigate_to_button_page()
