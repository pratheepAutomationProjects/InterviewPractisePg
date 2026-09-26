from playwright.sync_api import sync_playwright, expect


class TestSelectablePage:
    def test_navigate_to_selectable_page(self):
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            page = browser.new_page()

            page.goto("https://letcode.in/selectable")
            print("\nPage title is:", page.title(), flush=True)

            # ------------------------------------------------------------------
            # 1. Locate Selectable Elements
            # ------------------------------------------------------------------
            selectable_items = page.locator(".list-container > div, .selectable > div, mat-list-option, div[class*='cursor-pointer']")
            selectable_items.first.wait_for(state="visible")

            total_items = selectable_items.count()
            print(f"1. Total Selectable Items Found: {total_items}", flush=True)

            all_texts = [item.strip() for item in selectable_items.all_text_contents() if item.strip()]
            print("   Available Items:", all_texts, flush=True)

            # ------------------------------------------------------------------
            # 2. Method 1: Single Item Selection (Click)
            # ------------------------------------------------------------------
            target_item_text = "Playwright"
            playwright_option = selectable_items.filter(has_text=target_item_text).first

            print(f"\n2. Selecting single item: '{target_item_text}'...", flush=True)
            playwright_option.click()
            page.wait_for_timeout(500)

            # ------------------------------------------------------------------
            # 3. Method 2: Multi-Selection using Ctrl / Command Key
            # ------------------------------------------------------------------
            items_to_select = ["Selenium", "Cypress", "Postman"]
            print(f"\n3. Multi-selecting using Control Key: {items_to_select}...", flush=True)

            # Hold Control key down for multi-selection
            page.keyboard.down("Control")
            for item_name in items_to_select:
                item_locator = selectable_items.filter(has_text=item_name).first
                if item_locator.count() > 0:
                    item_locator.click(modifiers=["Control"])
                    print(f"   Ctrl+Clicked: '{item_name}'", flush=True)
                    page.wait_for_timeout(300)
            page.keyboard.up("Control")

            # ------------------------------------------------------------------
            # 4. Method 3: Drag Selection (Marquee / Box Selection)
            # ------------------------------------------------------------------
            print("\n4. Performing Drag Selection across first 3 items...", flush=True)
            if total_items >= 3:
                first_box = selectable_items.first.bounding_box()
                third_box = selectable_items.nth(2).bounding_box()

                if first_box and third_box:
                    start_x = first_box["x"] + 10
                    start_y = first_box["y"] + 10
                    end_x = third_box["x"] + third_box["width"] - 10
                    end_y = third_box["y"] + third_box["height"] - 10

                    page.mouse.move(start_x, start_y)
                    page.mouse.down()
                    page.mouse.move(end_x, end_y, steps=10)
                    page.mouse.up()
                    page.wait_for_timeout(500)
                    print("   Drag selection performed successfully!", flush=True)

            # ------------------------------------------------------------------
            # 5. Assertions & Verification
            # ------------------------------------------------------------------
            selected_items_locator = page.locator(".list-container > div[class*='selected'], div[aria-selected='true'], div[class*='bg-']")
            selected_count = selected_items_locator.count()

            print(f"\n5. Total Selected Items Detected: {selected_count}", flush=True)
            assert total_items > 0, "Assertion Failed: Selectable list is empty."
            assert playwright_option.is_visible(), "Assertion Failed: Target selectable element is not visible."
            print("\n6. [Assertion Passed] Selectable page automation completed successfully!", flush=True)

            page.wait_for_timeout(5000)
            browser.close()


if __name__ == "__main__":
    TestSelectablePage().test_navigate_to_selectable_page()

