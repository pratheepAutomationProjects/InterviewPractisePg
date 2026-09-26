from playwright.sync_api import sync_playwright


class TestWindowPage:
    def test_navigate_to_window_page(self):
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            context = browser.new_context()
            page = context.new_page()

            page.goto("https://letcode.in/windows")
            print("\nMain Page Title:", page.title(), flush=True)

            # ------------------------------------------------------------------
            # Approach 1: Single Window/Tab using page.expect_popup()
            # ------------------------------------------------------------------
            with page.expect_popup() as popup_info:
                page.locator("#home").click()

            new_tab = popup_info.value
            new_tab.wait_for_load_state()
            print("1. [Single Tab] Title:", new_tab.title(), flush=True)
            print("   [Single Tab] URL:", new_tab.url, flush=True)
            new_tab.close()

            # ------------------------------------------------------------------
            # Approach 2: Multiple Windows using context.pages
            # ------------------------------------------------------------------
            page.locator("#multi").click()
            page.wait_for_timeout(3000)

            print(f"\n2. [Multiple Tabs] Open count: {len(context.pages)}", flush=True)
            for idx, p_item in enumerate(context.pages):
                print(f"   Tab #{idx + 1}: {p_item.title()}", flush=True)

            # ------------------------------------------------------------------
            # Approach 3: Closing all child windows (except main page)
            # ------------------------------------------------------------------
            for p_item in context.pages:
                if p_item != page:
                    p_item.close()

            assert len(context.pages) == 1, "Only main window should remain."
            print("3. [Clean Up] Closed all child tabs. Main window active.", flush=True)

            page.wait_for_timeout(2000)
            context.close()
            browser.close()


if __name__ == "__main__":
    test_obj = TestWindowPage()
    test_obj.test_navigate_to_window_page()
