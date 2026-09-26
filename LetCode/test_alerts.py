from playwright.sync_api import sync_playwright


class TestAlertPage:
    def test_navigate_to_alert_page(self):
        with sync_playwright() as p:
            # Launch browser in headed mode for visual automation
            browser = p.chromium.launch(headless=False)
            context = browser.new_context()
            page = context.new_page()

            page.goto("https://letcode.in/alert")
            print("\nPage title is:", page.title(), flush=True)

            # ------------------------------------------------------------------
            # Condition 1: "Accept the Alert"
            # Locator Strategy: CSS ID Selector (#accept)
            # ------------------------------------------------------------------
            def handle_simple_alert(dialog):
                print("1. [Dialog Handler] Simple Alert message:", dialog.message, flush=True)
                assert dialog.type == "alert", f"Expected 'alert', got {dialog.type}"
                dialog.accept()
            page.once("dialog", handle_simple_alert)
            page.locator("#accept").click()
            print("   Simple Alert handled successfully.", flush=True)

            # ------------------------------------------------------------------
            # Condition 2: "Dismiss the Alert & print the alert text"
            # Locator Strategy: CSS ID Selector (#confirm)
            # ------------------------------------------------------------------
            def handle_confirm_alert(dialog):
                print("2. [Dialog Handler] Confirm Alert message:", dialog.message, flush=True)
                assert dialog.type == "confirm", f"Expected 'confirm', got {dialog.type}"
                dialog.dismiss()

            page.once("dialog", handle_confirm_alert)
            page.locator("#confirm").click()
            print("   Confirm Alert dismissed successfully.", flush=True)

            # ------------------------------------------------------------------
            # Condition 3: "Type your name & accept"
            # Locator Strategy: CSS ID Selector (#prompt)
            # ------------------------------------------------------------------
            user_name = "Pratheep S"

            def handle_prompt_alert(dialog):
                print("3. [Dialog Handler] Prompt Alert message:", dialog.message, flush=True)
                assert dialog.type == "prompt", f"Expected 'prompt', got {dialog.type}"
                dialog.accept(user_name)

            page.once("dialog", handle_prompt_alert)
            
            page.locator("#prompt").click()

            # Verify the printed text on page under prompt section if applicable
            printed_name_locator = page.locator("#myName")
            if printed_name_locator.is_visible():
                printed_text = printed_name_locator.text_content()
                print(f"   Prompt response on page: '{printed_text}'", flush=True)

            print("   Prompt Alert handled successfully.", flush=True)

            # ------------------------------------------------------------------
            # Condition 4: "Sweet alert / Modern alert"
            # Locator Strategy: CSS ID Selector (#modern) & modal element locators
            # ------------------------------------------------------------------
            page.locator("#modern").click()

            # Wait for modern alert modal to appear
            modal_text_locator = page.locator(".modal-content p, .modal .card-content p").first
            modal_text_locator.wait_for(state="visible", timeout=5000)

            title_text = modal_text_locator.text_content()
            print("4. [CSS ID Selector] Modern Alert opened. Modal content:", title_text.strip(), flush=True)
            assert "Modern Alert" in title_text, f"Expected 'Modern Alert' in text, got '{title_text}'"

            # Close the modern alert modal by clicking close button
            close_btn = page.locator("button.modal-close, button[aria-label='close']").first
            close_btn.click()
            print("   Modern Alert modal closed successfully.", flush=True)

            page.wait_for_timeout(9000)

            # Clean up
            context.close()
            browser.close()


if __name__ == "__main__":
    test_obj = TestAlertPage()
    test_obj.test_navigate_to_alert_page()
