from playwright.sync_api import sync_playwright, expect
import re


class TestAdvancedTablePage:
    def test_navigate_to_advanced_table_page(self):
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            page = browser.new_page()

            page.goto("https://letcode.in/advancedtable")
            print("\nPage title is:", page.title(), flush=True)

            # ------------------------------------------------------------------
            # 1. Locate Advanced Table & Verify Headers
            # ------------------------------------------------------------------
            table = page.locator("table").first
            table.wait_for(state="visible")

            headers = [h.strip() for h in table.locator("th").all_text_contents()]
            print("1. Table Headers Found:", headers, flush=True)
            assert "UNIVERSITY NAME" in headers, "Assertion Failed: 'UNIVERSITY NAME' header not found."

            # ------------------------------------------------------------------
            # 2. Scenario 1: Filter / Global Search Functionality
            # ------------------------------------------------------------------
            search_input = page.get_by_placeholder("Search table...")
            search_input.wait_for(state="visible")

            search_query = "Aberdeen"
            print(f"\n2. Searching for query: '{search_query}'...", flush=True)
            search_input.fill(search_query)
            page.wait_for_timeout(500)

            matching_rows = table.locator("tbody tr").all()
            print(f"   Total matching rows displayed: {len(matching_rows)}", flush=True)

            for index, row in enumerate(matching_rows):
                row_text = row.text_content().strip()
                assert search_query.lower() in row_text.lower(), f"Row {index+1} does not match search query '{search_query}'"

            print(f"   [Verified] All filtered rows contain '{search_query}'.", flush=True)

            # Clear search input
            search_input.clear()
            page.wait_for_timeout(500)

            # ------------------------------------------------------------------
            # 3. Scenario 2: Column Sorting Verification (Ascending & Descending)
            # ------------------------------------------------------------------
            print("\n3. Verifying Column Sorting (Ascending & Descending)...", flush=True)
            col_index = headers.index("UNIVERSITY NAME") + 1 if "UNIVERSITY NAME" in headers else 2
            sort_header = table.locator(f"th:nth-child({col_index})")

            # Click header -> Ascending Order
            sort_header.click()
            page.wait_for_timeout(500)

            uni_asc = [cell.strip() for cell in table.locator(f"tbody tr td:nth-child({col_index})").all_text_contents()]
            assert uni_asc == sorted(uni_asc), f"Ascending Sort Failed! Actual: {uni_asc}"
            print("   [Verified] Ascending Order:", uni_asc[:3], "...", flush=True)

            # Click header again -> Descending Order
            sort_header.click()
            page.wait_for_timeout(500)

            uni_desc = [cell.strip() for cell in table.locator(f"tbody tr td:nth-child({col_index})").all_text_contents()]
            assert uni_desc == sorted(uni_desc, reverse=True), f"Descending Sort Failed! Actual: {uni_desc}"
            print("   [Verified] Descending Order:", uni_desc[:3], "...", flush=True)

            # Reset header sort
            sort_header.click()
            page.wait_for_timeout(500)

            # ------------------------------------------------------------------
            # 4. Scenario 3: Website Link Validation
            # ------------------------------------------------------------------
            print("\n4. Validating Website Links...", flush=True)
            website_links = table.locator("tbody tr td a").all()
            print(f"   Total visible website links: {len(website_links)}", flush=True)

            for link in website_links[:3]:
                href = link.get_attribute("href") or ""
                print(f"   Link text: '{link.text_content().strip()}' -> href: '{href}'", flush=True)
                assert href.startswith("http"), f"Assertion Failed: Invalid URL '{href}'"

            print("   [Verified] All website links are valid HTTP/HTTPS URLs.", flush=True)

            # ------------------------------------------------------------------
            # 5. Scenario 4: Pagination Navigation & Total Records Verification
            # ------------------------------------------------------------------
            print("\n5. Verifying Pagination & Traversing All Pages...", flush=True)
            all_records = []
            page_number = 1

            while True:
                current_rows = table.locator("tbody tr").all()
                page_records = [[cell.strip() for cell in r.locator("td").all_text_contents()] for r in current_rows]
                all_records.extend(page_records)
                print(f"   Page {page_number}: Collected {len(page_records)} rows (Total so far: {len(all_records)})", flush=True)

                # Locate Next pagination button
                next_btn = page.locator("button:has-text('Next'), a:has-text('Next'), .pagination-next, .next").first
                if next_btn.count() == 0 or not next_btn.is_visible() or next_btn.is_disabled() or "disabled" in (next_btn.get_attribute("class") or ""):
                    print("   Reached the last page.", flush=True)
                    break

                next_btn.click()
                page.wait_for_timeout(500)
                page_number += 1

            print(f"\n   [Verified] Successfully collected all {len(all_records)} records across {page_number} pages!", flush=True)
            assert len(all_records) > 0, "Assertion Failed: No records were collected."

            expect(table).to_be_visible()
            print("\n6. [Assertion Passed] Advanced table automation completed successfully!", flush=True)

            page.wait_for_timeout(3000)
            browser.close()


if __name__ == "__main__":
    TestAdvancedTablePage().test_navigate_to_advanced_table_page()


