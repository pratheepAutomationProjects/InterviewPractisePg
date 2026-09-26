from playwright.sync_api import sync_playwright, expect


class TestShadowDOMPage:
    def test_navigate_to_shadow_page(self):
        with sync_playwright() as p:
            # Launch Chromium in headed mode for visual automation as per workspace guidelines
            browser = p.chromium.launch(headless=False)
            context = browser.new_context()
            page = context.new_page()

            try:
                page.goto("https://letcode.in/shadow")
                page.wait_for_load_state("domcontentloaded")
                print("\nPage title is:", page.title(), flush=True)
                assert "Shadow" in page.title() or "LetCode" in page.title(), f"Unexpected title: {page.title()}"

                # ------------------------------------------------------------------
                # Condition 1: "Enter your First Name in Shadow DOM"
                # Locator Strategy: Built-in / CSS ID Selector (#fname)
                # Interview Insight: Playwright CSS selectors automatically pierce open
                # Shadow DOM roots without requiring JavaScript execution or special APIs.
                # ------------------------------------------------------------------
                fname_input = page.locator("#fname")
                fname_input.fill("Antigravity")
                filled_fname = fname_input.input_value()
                print("1. [Shadow DOM - CSS ID Selector] Filled First Name:", filled_fname, flush=True)
                assert filled_fname == "Antigravity", f"Expected 'Antigravity', got '{filled_fname}'"

                # ------------------------------------------------------------------
                # Condition 2: "Enter your Last Name in Shadow DOM"
                # Locator Strategy: CSS ID Selector (#lname)
                # ------------------------------------------------------------------
                lname_input = page.locator("#lname")
                # Alternatively press keys or direct fill
                lname_input.fill("Tester")
                filled_lname = lname_input.input_value()
                print("2. [Shadow DOM - CSS ID Selector] Filled Last Name:", filled_lname, flush=True)
                assert filled_lname == "Tester", f"Expected 'Tester', got '{filled_lname}'"

                # ------------------------------------------------------------------
                # Condition 3: "Enter your Email in Shadow DOM"
                # Locator Strategy: CSS ID Selector (#email) / Attribute Selector
                # ------------------------------------------------------------------
                email_input = page.locator("#email")
                if email_input.count() > 0:
                    email_input.fill("antigravity.shadow@example.com")
                    filled_email = email_input.input_value()
                    print("3. [Shadow DOM - CSS ID Selector] Filled Email:", filled_email, flush=True)
                    assert filled_email == "antigravity.shadow@example.com", (
                        f"Expected 'antigravity.shadow@example.com', got '{filled_email}'"
                    )

                page.wait_for_timeout(3000)

            finally:
                context.close()
                browser.close()


if __name__ == "__main__":
    test_obj = TestShadowDOMPage()
    test_obj.test_navigate_to_shadow_page()
