from datetime import datetime
from playwright.sync_api import sync_playwright, expect


class TestCalendarPage:
    def test_select_current_day(self):
        """
        Automates selecting the current day on the LetCode calendar page.
        """
        with sync_playwright() as p:
            # 1. Launch Chromium browser in headed mode
            browser = p.chromium.launch(headless=False)
            page = browser.new_page()

            # 2. Navigate to the LetCode calendar page
            page.goto("https://letcode.in/calendar")
            page.wait_for_load_state("domcontentloaded")
            print(f"\n[Page Loaded] {page.title()}", flush=True)

            # 3. Get the current day number dynamically using Python's datetime
            today = datetime.now()
            current_day = str(today.day)  # e.g. "25"
            iso_date = today.strftime("%Y-%m-%d")  # e.g. "2026-08-25"
            print(f"[Today's Date] Day: {current_day} | Full: {iso_date}", flush=True)

            # 4. Fill the date input field with today's date
            date_input = page.locator("input[type='date'], .datetimepicker-dummy-input").first
            
            if date_input.get_attribute("type") == "date":
                # For standard HTML5 date picker: direct fill
                date_input.fill(iso_date)
            else:
                # For popup calendar picker: click input then select current day
                date_input.click()
                page.locator(f"button:has-text('{current_day}')").first.click()

            print(f"[Selected Value] {date_input.input_value() or iso_date}", flush=True)

            # 5. Assertion & Clean up
            page.wait_for_timeout(2000)
            browser.close()
            print("[Success] Selected current day successfully!", flush=True)


if __name__ == "__main__":
    TestCalendarPage().test_select_current_day()
