from playwright.sync_api import sync_playwright


class TestFramePage:
    def test_navigate_to_frame_page(self):
        with sync_playwright() as p:
            # Launch browser in headed mode for visual automation
            browser = p.chromium.launch(headless=False)
            context = browser.new_context()
            page = context.new_page()

            page.goto("https://letcode.in/frame")
            print("\nPage title is:", page.title(), flush=True)

            # ------------------------------------------------------------------
            # Condition 1: "Enter First Name & Last Name in Parent Frame"
            # Locator Strategy: Frame Locator (#firstFr or iframe[name='firstFr'])
            # ------------------------------------------------------------------
            parent_frame = page.frame_locator("#firstFr")

            # Fill First Name
            fname_input = parent_frame.locator("input[name='fname']")
            fname_input.fill("Pratheep")
            print("1. [Parent Frame Locator] Filled First Name: Pratheep", flush=True)
            assert fname_input.input_value() == "Pratheep", f"Expected 'Pratheep', got {fname_input.input_value()}"

            # Fill Last Name
            lname_input = parent_frame.locator("input[name='lname']")
            lname_input.fill("S")
            print("   [Parent Frame Locator] Filled Last Name: S", flush=True)
            assert lname_input.input_value() == "S", f"Expected 'S', got {lname_input.input_value()}"

            # Check heading text rendered inside parent frame
            header_locator = parent_frame.locator(".title, h1, p.has-text-info")
            if header_locator.count() > 0:
                print(f"   Parent frame message: '{header_locator.first.text_content().strip()}'", flush=True)

            # ------------------------------------------------------------------
            # Condition 2: "Enter Email in Child (Nested) Frame"
            # Locator Strategy: Chained Frame Locator (parent_frame.frame_locator("iframe[src='innerFrame']"))
            # ------------------------------------------------------------------
            child_frame = parent_frame.frame_locator("iframe[src*='inner'], iframe").first

            email_input = child_frame.locator("input[name='email']")
            email_input.fill("pratheep@example.com")
            print("2. [Nested Frame Locator] Filled Email in child frame: pratheep@example.com", flush=True)
            assert email_input.input_value() == "pratheep@example.com", f"Expected 'pratheep@example.com', got {email_input.input_value()}"

            # ------------------------------------------------------------------
            # Condition 3: "Interact back with Main Page DOM"
            # In Playwright, main page elements remain accessible directly via page.locator()
            # ------------------------------------------------------------------
            main_header = page.locator("h1.title, .hero-body .title").first
            if main_header.is_visible():
                print("3. [Main Page Locator] Switched context back. Main header:", main_header.text_content().strip(), flush=True)

            page.wait_for_timeout(3000)

            # Clean up
            context.close()
            browser.close()


if __name__ == "__main__":
    test_obj = TestFramePage()
    test_obj.test_navigate_to_frame_page()
