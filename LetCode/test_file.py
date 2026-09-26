from pathlib import Path
from playwright.sync_api import sync_playwright, expect


class TestFilePage:
    def test_file_upload_and_download(self):
        with sync_playwright() as p:
            # Launch Chromium in headed mode for visual automation as per workspace guidelines
            browser = p.chromium.launch(headless=False)
            context = browser.new_context(accept_downloads=True)
            page = context.new_page()

            try:
                page.goto("https://letcode.in/file")
                page.wait_for_load_state("domcontentloaded")
                print("\nPage title is:", page.title(), flush=True)

                # ==================================================================
                # Scenario 1: Upload a File
                # Locator Strategy: Built-in / CSS Input Selector (input[type='file'])
                # ==================================================================
                # Relative path relative to the test file directory
                test_file = Path(__file__).parent / "test_data" / "sample.xlsx"
                
                file_input = page.locator("input[type='file']")
                # Attach file directly using set_input_files
                file_input.set_input_files(str(test_file))
                print(f"1. [File Upload] Uploaded file: {test_file.name}", flush=True)

                # Optional verification if file label or name is updated on UI
                file_name_label = page.locator(".file-name")
                if file_name_label.count() > 0 and file_name_label.is_visible():
                    print(f"   Uploaded File Label on UI: {file_name_label.text_content().strip()}", flush=True)

                # ==================================================================
                # Scenario 2: Download Excel File
                # Locator Strategy: CSS ID Selector (#xls) or text locator
                # ==================================================================
                excel_btn = page.locator("#xls, a:has-text('Download Excel')").first
                if excel_btn.count() > 0:
                    with page.expect_download() as download_info:
                        excel_btn.click()
                    download_excel = download_info.value
                    suggested_excel_name = download_excel.suggested_filename
                    print(f"2. [File Download - Excel] Suggested filename: '{suggested_excel_name}'", flush=True)
                    assert ".xls" in suggested_excel_name.lower() or "sample" in suggested_excel_name.lower(), (
                        f"Expected Excel file, got {suggested_excel_name}"
                    )

                # ==================================================================
                # Scenario 3: Download PDF File
                # Locator Strategy: CSS ID Selector (#pdf) or text locator
                # ==================================================================
                pdf_btn = page.locator("#pdf, a:has-text('Download Pdf'), a:has-text('Download PDF')").first
                if pdf_btn.count() > 0:
                    with page.expect_download() as download_info:
                        pdf_btn.click()
                    download_pdf = download_info.value
                    suggested_pdf_name = download_pdf.suggested_filename
                    print(f"3. [File Download - PDF] Suggested filename: '{suggested_pdf_name}'", flush=True)
                    assert ".pdf" in suggested_pdf_name.lower() or "sample" in suggested_pdf_name.lower(), (
                        f"Expected PDF file, got {suggested_pdf_name}"
                    )

                # ==================================================================
                # Scenario 4: Download Text File
                # Locator Strategy: CSS ID Selector (#txt) or text locator
                # ==================================================================
                txt_btn = page.locator("#txt, a:has-text('Download Text')").first
                if txt_btn.count() > 0:
                    with page.expect_download() as download_info:
                        txt_btn.click()
                    download_txt = download_info.value
                    suggested_txt_name = download_txt.suggested_filename
                    print(f"4. [File Download - Text] Suggested filename: '{suggested_txt_name}'", flush=True)
                    assert ".txt" in suggested_txt_name.lower() or "sample" in suggested_txt_name.lower(), (
                        f"Expected Text file, got {suggested_txt_name}"
                    )

                page.wait_for_timeout(2000)

            finally:
                context.close()
                browser.close()


if __name__ == "__main__":
    test_obj = TestFilePage()
    test_obj.test_file_upload_and_download()
