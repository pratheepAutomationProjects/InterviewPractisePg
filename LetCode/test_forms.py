from playwright.sync_api import sync_playwright, expect


class TestFormsPage:
    def test_navigate_to_forms_page(self):
        with sync_playwright() as p:
            # Launch Chromium in headed mode for visual automation as per workspace rules
            browser = p.chromium.launch(headless=False)
            context = browser.new_context()
            page = context.new_page()

            try:
                page.goto("https://letcode.in/forms")
                print("\nPage title is:", page.title(), flush=True)
                assert "Forms" in page.title(), f"Unexpected page title: {page.title()}"

                # ------------------------------------------------------------------
                # Condition 1: Fill First Name
                # Locator Strategy: CSS ID Selector (#firstname)
                # ------------------------------------------------------------------
                first_name_input = page.locator("#firstname")
                first_name_input.fill("Antigravity")
                filled_first_name = first_name_input.input_value()
                print("1. [CSS ID Selector] Filled First Name:", filled_first_name, flush=True)
                assert filled_first_name == "Antigravity", f"Expected 'Antigravity', got '{filled_first_name}'"

                # ------------------------------------------------------------------
                # Condition 2: Fill Last Name
                # Locator Strategy: CSS ID Selector (#lasttname - note LetCode element ID spelling)
                # ------------------------------------------------------------------
                last_name_input = page.locator("#lasttname")
                last_name_input.fill("Automation")
                filled_last_name = last_name_input.input_value()
                print("2. [CSS ID Selector] Filled Last Name:", filled_last_name, flush=True)
                assert filled_last_name == "Automation", f"Expected 'Automation', got '{filled_last_name}'"

                # ------------------------------------------------------------------
                # Condition 3: Fill Email
                # Locator Strategy: CSS ID Selector (#email)
                # Note: Clear pre-filled placeholder text 'hello@' before entering target email
                # ------------------------------------------------------------------
                email_input = page.locator("#email")
                email_input.clear()
                email_input.fill("antigravity.test@example.com")
                filled_email = email_input.input_value()
                print("3. [CSS ID Selector] Filled Email:", filled_email, flush=True)
                assert filled_email == "antigravity.test@example.com", f"Expected 'antigravity.test@example.com', got '{filled_email}'"

                # ------------------------------------------------------------------
                # Condition 4: Select Country Code
                # Locator Strategy: CSS Selector (select:nth-of-type(1))
                # ------------------------------------------------------------------
                country_code_dropdown = page.locator("select").nth(0)
                selected_code = country_code_dropdown.select_option(label="India (+91)")
                print("4. [CSS Selector] Selected Country Code ('India (+91)'):", selected_code, flush=True)
                assert country_code_dropdown.input_value() == "91", f"Expected '91', got '{country_code_dropdown.input_value()}'"

                # ------------------------------------------------------------------
                # Condition 5: Fill Phone Number
                # Locator Strategy: CSS ID Selector (#Phno)
                # ------------------------------------------------------------------
                phone_input = page.locator("#Phno")
                phone_input.fill("9876543210")
                filled_phone = phone_input.input_value()
                print("5. [CSS ID Selector] Filled Phone Number:", filled_phone, flush=True)
                assert filled_phone == "9876543210", f"Expected '9876543210', got '{filled_phone}'"

                # ------------------------------------------------------------------
                # Condition 6: Fill Address Line 1
                # Locator Strategy: CSS ID Selector (#Addl1)
                # ------------------------------------------------------------------
                address1_input = page.locator("#Addl1")
                address1_input.fill("123 Tech Park Avenue")
                filled_addr1 = address1_input.input_value()
                print("6. [CSS ID Selector] Filled Address Line 1:", filled_addr1, flush=True)
                assert filled_addr1 == "123 Tech Park Avenue", f"Expected '123 Tech Park Avenue', got '{filled_addr1}'"

                # ------------------------------------------------------------------
                # Condition 7: Fill Address Line 2
                # Locator Strategy: CSS ID Selector (#Addl2)
                # ------------------------------------------------------------------
                address2_input = page.locator("#Addl2")
                address2_input.fill("Suite 400")
                filled_addr2 = address2_input.input_value()
                print("7. [CSS ID Selector] Filled Address Line 2:", filled_addr2, flush=True)
                assert filled_addr2 == "Suite 400", f"Expected 'Suite 400', got '{filled_addr2}'"

                # ------------------------------------------------------------------
                # Condition 8: Fill State
                # Locator Strategy: CSS ID Selector (#state)
                # ------------------------------------------------------------------
                state_input = page.locator("#state")
                state_input.fill("Tamil Nadu")
                filled_state = state_input.input_value()
                print("8. [CSS ID Selector] Filled State:", filled_state, flush=True)
                assert filled_state == "Tamil Nadu", f"Expected 'Tamil Nadu', got '{filled_state}'"

                # ------------------------------------------------------------------
                # Condition 9: Fill Postal Code
                # Locator Strategy: CSS ID Selector (#postalcode)
                # ------------------------------------------------------------------
                postal_input = page.locator("#postalcode")
                postal_input.fill("600001")
                filled_postal = postal_input.input_value()
                print("9. [CSS ID Selector] Filled Postal Code:", filled_postal, flush=True)
                assert filled_postal == "600001", f"Expected '600001', got '{filled_postal}'"

                # ------------------------------------------------------------------
                # Condition 10: Select Country
                # Locator Strategy: CSS Selector (select:nth-of-type(2))
                # ------------------------------------------------------------------
                country_dropdown = page.locator("select").nth(1)
                selected_country = country_dropdown.select_option(label="India")
                print("10. [CSS Selector] Selected Country ('India'):", selected_country, flush=True)
                assert country_dropdown.input_value() == "India", f"Expected 'India', got '{country_dropdown.input_value()}'"

                # ------------------------------------------------------------------
                # Condition 11: Set Date of Birth
                # Locator Strategy: XPath Selector (//input[@id='Date'])
                # ------------------------------------------------------------------
                dob_input = page.locator("//input[@id='Date']")
                dob_input.fill("1995-05-15")
                filled_dob = dob_input.input_value()
                print("11. [XPath Selector] Set Date of Birth:", filled_dob, flush=True)
                assert filled_dob == "1995-05-15", f"Expected '1995-05-15', got '{filled_dob}'"

                # ------------------------------------------------------------------
                # Condition 12: Select Gender Radio Button
                # Locator Strategy: CSS ID Selector (#male)
                # ------------------------------------------------------------------
                male_radio = page.locator("#male")
                female_radio = page.locator("#female")
                male_radio.check()
                print("12. [CSS ID Selector] Male Radio checked status:", male_radio.is_checked(), flush=True)
                assert male_radio.is_checked(), "Expected Male radio button to be checked"
                assert not female_radio.is_checked(), "Expected Female radio button to be unchecked"

                # ------------------------------------------------------------------
                # Condition 13: Check Agree Terms Checkbox
                # Locator Strategy: CSS Attribute Selector (input[type='checkbox'])
                # ------------------------------------------------------------------
                terms_checkbox = page.locator("input[type='checkbox']")
                terms_checkbox.check()
                print("13. [CSS Attribute Selector] Agree Terms checked status:", terms_checkbox.is_checked(), flush=True)
                assert terms_checkbox.is_checked(), "Expected terms checkbox to be checked"

                # ------------------------------------------------------------------
                # Condition 14: Submit Form
                # Locator Strategy: CSS Attribute Selector (input[type='submit'])
                # ------------------------------------------------------------------
                submit_button = page.locator("input[type='submit']")
                expect(submit_button).to_be_visible()
                submit_button.click()
                print("14. [CSS Attribute Selector] Form submitted successfully.", flush=True)

                page.wait_for_timeout(3000)

            finally:
                context.close()
                browser.close()


if __name__ == "__main__":
    test_obj = TestFormsPage()
    test_obj.test_navigate_to_forms_page()
