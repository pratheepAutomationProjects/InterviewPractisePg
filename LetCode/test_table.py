from playwright.sync_api import sync_playwright, expect


class TestTablePage:
    def test_navigate_to_table_page(self):
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            page = browser.new_page()

            page.goto("https://letcode.in/table")
            print("\nPage title is:", page.title(), flush=True)

            # ------------------------------------------------------------------
            # 1. Sum Calculation & Verification (#shopping table)
            # ------------------------------------------------------------------
            shopping_table = page.locator("#shopping, table").first
            shopping_table.wait_for(state="visible")
            
            # Extract integer prices using list comprehension
            price_texts = shopping_table.locator("tbody tr td:nth-child(2)").all_text_contents()
            prices = [int(p.strip()) for p in price_texts if p.strip().isdigit()]

            calculated_total = sum(prices)
            print(f"1. Calculated Total: {calculated_total} (Prices: {prices})", flush=True)

            # Assert against footer total
            footer_total = shopping_table.locator("tfoot td:last-child").text_content().strip()
            if footer_total.isdigit():
                assert calculated_total == int(footer_total), f"Sum Mismatch! Expected {footer_total}, got {calculated_total}"
                print(f"   [Verified] Total matches footer total: {footer_total}", flush=True)

            # ------------------------------------------------------------------
            # 2. Row Target & Checkbox Interaction (Mark Present for 'Koushik')
            # ------------------------------------------------------------------
            target_name = "Raj"
            person_row = page.locator("#simpletable tr").filter(has_text=target_name).first

            if person_row.count() > 0:
                checkbox = person_row.locator("input[type='checkbox']")
                checkbox.check()
                expect(checkbox).to_be_checked()
                print(f"2. [Verified] Checkbox checked for '{target_name}'.", flush=True)


            # ------------------------------------------------------------------
            # 3. Industry-Standard Dynamic Sortable Table Verification
            # ------------------------------------------------------------------
            print("\n3. Testing Sortable Table (Dynamic Column Indexing)...", flush=True)

            sortable_table = page.locator("table.mat-sort, table").last
            target_column = "Dessert (100g)"

            # Step A: Dynamically determine column index by matching header text
            headers = [h.strip() for h in sortable_table.locator("th").all_text_contents()]
            if target_column in headers:
                col_index = headers.index(target_column) + 1  # 1-indexed for CSS nth-child
                header_locator = sortable_table.locator(f"th:nth-child({col_index})")

                # Step B: Verify Ascending Order
                header_locator.click()
                page.wait_for_timeout(500)

                column_cells_asc = sortable_table.locator(f"tbody tr td:nth-child({col_index})").all_text_contents()
                values_asc = [cell.strip() for cell in column_cells_asc]

                assert values_asc == sorted(values_asc), f"Ascending Sort Failed! Actual: {values_asc}"
                print(f"   [Verified] '{target_column}' Ascending Order:", values_asc, flush=True)

                # Step C: Verify Descending Order
                header_locator.click()
                page.wait_for_timeout(500)

                column_cells_desc = sortable_table.locator(f"tbody tr td:nth-child({col_index})").all_text_contents()
                values_desc = [cell.strip() for cell in column_cells_desc]

                assert values_desc == sorted(values_desc, reverse=True), f"Descending Sort Failed! Actual: {values_desc}"
                print(f"   [Verified] '{target_column}' Descending Order:", values_desc, flush=True)


            expect(shopping_table).to_be_visible()
            print("\n4. [Assertion Passed] Table automation test completed successfully!", flush=True)

            page.wait_for_timeout(3000)
            browser.close()


if __name__ == "__main__":
    TestTablePage().test_navigate_to_table_page()



