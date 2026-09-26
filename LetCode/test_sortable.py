from playwright.sync_api import sync_playwright, expect


class TestSortablePage:
    def test_navigate_to_sortable_page(self):
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            page = browser.new_page()

            page.goto("https://letcode.in/sortable")
            print("\nPage title is:", page.title(), flush=True)

            # ------------------------------------------------------------------
            # 1. Locate Sortable Items
            # ------------------------------------------------------------------
            sortable_items = page.locator(".cdk-drag, div[draggable='true'], #sample-box1, .example-box, div.box")
            sortable_items.first.wait_for(state="visible")

            initial_order = [item.strip() for item in sortable_items.all_text_contents() if item.strip()]
            print(f"1. Initial Order ({len(initial_order)} items):", initial_order, flush=True)

            # ------------------------------------------------------------------
            # 2. Perform Ascending Order Reordering (A to Z)
            # ------------------------------------------------------------------
            target_ascending = sorted(initial_order)
            print("2. Target Ascending Order:", target_ascending, flush=True)

            for target_index, text in enumerate(target_ascending):
                item_to_drag = sortable_items.filter(has_text=text).first
                target_slot = sortable_items.nth(target_index)

                print(f"   Moving '{text}' -> Slot {target_index}", flush=True)
                item_to_drag.drag_to(target_slot)
                page.wait_for_timeout(500)

            # ------------------------------------------------------------------
            # 3. Assert list is sorted in Ascending Order
            # ------------------------------------------------------------------
            final_order = [item.strip() for item in sortable_items.all_text_contents() if item.strip()]
            print("3. Final Order After Sorting:", final_order, flush=True)

            assert final_order == target_ascending, f"Assertion Failed: Expected {target_ascending}, but got {final_order}"
            print("4. [Assertion Passed] Sortable list successfully sorted in ascending order!", flush=True)

            page.wait_for_timeout(7000)
            browser.close()


if __name__ == "__main__":
    TestSortablePage().test_navigate_to_sortable_page()

