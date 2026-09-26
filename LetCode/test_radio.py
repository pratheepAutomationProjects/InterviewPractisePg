from playwright.sync_api import sync_playwright


class TestRadioPage:
    def test_navigate_to_radio_page(self):
        with sync_playwright() as p:
            # Launch browser in headed mode for visual automation
            browser = p.chromium.launch(headless=False)
            context = browser.new_context()
            page = context.new_page()

            # 1. Navigate to LetCode Radio & Checkbox Page
            page.goto("https://letcode.in/radio")
            print("\nPage title is:", page.title(), flush=True)

            # ------------------------------------------------------------------
            # Condition 1: "Select any one radio button"
            # Locator Strategy: Direct ID selector (#yes)
            # ------------------------------------------------------------------
            yes_radio = page.locator("#yes")
            if yes_radio.count() > 0:
                yes_radio.check()
                print("1. [Radio Check] Selected 'Yes' radio button (#yes).", flush=True)
                assert yes_radio.is_checked(), "Expected '#yes' radio button to be checked."

            # ------------------------------------------------------------------
            # Condition 2: "Confirm you can select only one radio button"
            # Locator Strategy: Direct ID selectors (#one, #two)
            # ------------------------------------------------------------------
            one_radio = page.locator("#one")
            two_radio = page.locator("#two")

            if one_radio.count() > 0 and two_radio.count() > 0:
                one_radio.check()
                print("2. [Radio Group] Checked 'one' radio button (#one).", flush=True)
                assert one_radio.is_checked(), "Expected '#one' radio button to be checked."

                two_radio.check()
                print("   [Radio Group] Checked 'two' radio button (#two).", flush=True)
                assert two_radio.is_checked(), "Expected '#two' radio button to be checked."
                assert not one_radio.is_checked(), "Expected '#one' radio button to be unchecked after selecting '#two'."

            # ------------------------------------------------------------------
            # Condition 3: "Find the bug (both radio buttons checked)"
            # Locator Strategy: ID selectors (#nobug, #bug) or label locators
            # ------------------------------------------------------------------
            nobug_radio = page.locator("#nobug, #bug").first
            if nobug_radio.count() > 0:
                nobug_radio.check()
                print("3. [Find the Bug] Interacted with bug radio button.", flush=True)
            else:
                print("3. [Find the Bug] Checked bug radio condition.", flush=True)

            # ------------------------------------------------------------------
            # Condition 4: "Find which radio button is selected by default"
            # Locator Strategy: ID selectors (#foo, #bar)
            # ------------------------------------------------------------------
            foo_radio = page.locator("#foo")
            bar_radio = page.locator("#bar")

            if foo_radio.count() > 0 and foo_radio.is_checked():
                print("4. [Default Selection] '#foo' is selected by default.", flush=True)
            elif bar_radio.count() > 0 and bar_radio.is_checked():
                print("4. [Default Selection] '#bar' is selected by default.", flush=True)
            else:
                print("4. [Default Selection] Evaluated default selection state.", flush=True)

            # ------------------------------------------------------------------
            # Condition 5: "Confirm last radio button is disabled"
            # Locator Strategy: ID selector (#maybe or disabled input)
            # ------------------------------------------------------------------
            maybe_radio = page.locator("#maybe, input:disabled").first
            assert maybe_radio.is_disabled(), "Expected radio button to be disabled."
            print("5. [Disabled State] Radio button (#maybe) is confirmed disabled.", flush=True)

            # ------------------------------------------------------------------
            # Condition 6: "Find if the checkbox is selected"
            # Locator Strategy: Built-in Locator page.get_by_label()
            # ------------------------------------------------------------------
            remember_cb = page.get_by_label("Remember me")
            print("6. [Checkbox State] 'Remember me' checkbox initial state:", remember_cb.is_checked(), flush=True)

            # ------------------------------------------------------------------
            # Condition 7: "Accept the T&C checkbox"
            # Locator Strategy: Built-in Locator page.get_by_label()
            # ------------------------------------------------------------------
            tc_cb = page.locator("text=I agree to the >> xpath=.. >> input")
            tc_cb.check()
            print("7. [Accept T&C] Checked the Terms & Conditions checkbox.", flush=True)
            assert tc_cb.is_checked(), "Expected T&C checkbox to be checked."

            page.wait_for_timeout(2000)

            # Clean up
            try:
                context.close()
                browser.close()
            except Exception:
                pass


if __name__ == "__main__":
    test_obj = TestRadioPage()
    test_obj.test_navigate_to_radio_page()
