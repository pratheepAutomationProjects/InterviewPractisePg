from playwright.sync_api import sync_playwright, expect


class TestElementsPage:
    def test_navigate_to_elements_page(self):
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            page = browser.new_page()

            page.goto("https://letcode.in/elements")
            print("\nPage title is:", page.title(), flush=True)

            # 1. Type and Enter Git username
            username_input = page.locator("input[name='username']")
            username_input.fill("ortoniKC")
            username_input.press("Enter")

            # 2. Assert avatar image is displayed
            avatar = page.locator("img[alt='User avatar']")
            expect(avatar).to_be_visible()
            print("1 & 2. Searched user & verified avatar image:", avatar.get_attribute("src"), flush=True)

            # 3. Print user name & other profile information
            profile_info = page.locator("//div[contains(@class,'flex-1')] //h2").first.inner_text().strip()
            print(f"\n3. User Profile Info:\n{profile_info}", flush=True)


            page.wait_for_timeout(2000)
            browser.close()


if __name__ == "__main__":
    TestElementsPage().test_navigate_to_elements_page()
