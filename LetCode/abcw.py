from playwright.sync_api import sync_playwright, expect


class TestAdvancedTablePage:
    def test_navigate_to_advanced_table_page(self):
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            page = browser.new_page()

            page.goto("https://letcode.in/advancedtable")
            print("\nPage title is:", page.title(), flush=True)

            tables = page.locator("#advancedtable")
            tables.wait_for(state="visible")
            search_table = page.get_by_placeholder("Search table...")
            search_table.fill("University")

            results = tables.locator("tbody tr").all()
            for index, value in enumerate(results):
                print(value.text_content().strip())
                assert "University".lower in value.text_content().strip()
            
            unsec = [cell.strip() for cell in tables.locator("ee").all_text_contents()]
            button:has_text('next')



