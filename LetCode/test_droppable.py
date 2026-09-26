from playwright.sync_api import sync_playwright, expect


class TestDroppablePage:
    def test_navigate_to_droppable_page(self):
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            page = browser.new_page()

            page.goto("https://letcode.in/droppable")
            print("\nPage title is:", page.title(), flush=True)

            # ------------------------------------------------------------------
            # 1. Locate Source (Draggable element) and Target (#droppable)
            # ------------------------------------------------------------------
            source = page.locator("#draggable, div[draggable='true']").first
            target = page.locator("#droppable")

            print(f"1. Target Header: '{target.locator('h2').text_content().strip()}'", flush=True)
            print(f"   Items inside Target before drop: {target.locator('[draggable=\'true\']').count()}", flush=True)

            # ------------------------------------------------------------------
            # 2. Perform Drag and Drop Action
            # ------------------------------------------------------------------
            source.drag_to(target)

            # ------------------------------------------------------------------
            # 3. Assert Draggable element is now inside #droppable
            # ------------------------------------------------------------------
            dropped_item = target.locator("[draggable='true']")
            expect(dropped_item).to_be_visible()
            print(f"2. Items inside Target after drop: {dropped_item.count()}", flush=True)
            print("3. [Assertion Passed] Draggable item successfully moved inside Target container!", flush=True)

            page.wait_for_timeout(2000)
            browser.close()


if __name__ == "__main__":
    TestDroppablePage().test_navigate_to_droppable_page()
