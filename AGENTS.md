# LetCode Automation Workspace Guidelines

These guidelines define standard coding conventions, locator strategies, and execution practices for Playwright Python automation tests in this workspace.

## Coding Conventions
1. **Framework & Language**: Use `playwright.sync_api` (`sync_playwright`) with Python.
2. **Class Structure**: Structure tests using OOP class design (e.g. `Test<Feature>Page`).
3. **Execution**: Include a `if __name__ == "__main__":` block to allow running each test file directly or via `pytest`.
4. **Browser Launch**: Always launch Chromium in headed mode (`headless=False`) for visual automation unless headless is explicitly requested.

## Locator Strategy Priorities
1. **Built-in Locators**: `page.get_by_role()`, `page.get_by_placeholder()`, `page.get_by_text()`.
2. **CSS Selectors**: `#id_name`, `input[title='...']`, `button[id='...']`.
3. **XPath Selectors**: Use explicit XPath `//button[@id='color']` when checking CSS properties or attribute selectors.

## Dialog & Alert Handling
- Handle standard browser dialogs using `page.once("dialog", handler)`.
- Explicitly log dialog messages with `print(..., flush=True)`.
- Distinguish between standard dialogs (alert, confirm, prompt) and custom HTML modal dialogs (Sweet Alert / Modern Alert).
