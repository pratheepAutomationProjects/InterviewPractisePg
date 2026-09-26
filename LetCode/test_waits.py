from playwright.sync_api import sync_playwright, expect


class TestWaitsPage:
    def test_navigate_to_waits_page(self):
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            page = browser.new_page()

            page.goto("https://letcode.in/waits")
            print("\nPage title is:", page.title(), flush=True)

            # 1. Register Dialog Listener before Triggering Action
            page.once("dialog", lambda dialog: (
                print(f"\n[Dialog Intercepted] Type: '{dialog.type}', Msg: '{dialog.message}'", flush=True),
                dialog.accept()
            ))
            page.wait_for_timeout(3000)
            browser.close()


if __name__ == "__main__":
    TestWaitsPage().test_navigate_to_waits_page()

