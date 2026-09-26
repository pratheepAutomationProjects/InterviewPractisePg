---
name: playwright-test-generator
description: Generates robust, clean, and optimized Playwright Python automation test scripts for LetCode practice pages from an interview perspective, covering all scenarios with clear assertions.
---

# Playwright Test Generator Skill

Use this skill when tasked with creating a new automation test script for a LetCode practice page (e.g., input, buttons, dropdowns, alerts, frames, tables, windows, elements, draggable).

## Core Principles & Guidelines

1. **Clean & Optimized Code**:
   - Write concise, readable, and Pythonic code without redundant boilerplate.
   - Avoid hardcoded long sleeps when Playwright built-in waiters / auto-retries can be used.

2. **Interview Perspective & Best Practices**:
   - Demonstrate industry-standard locator strategies (Role, Placeholder, CSS, XPath).
   - Use meaningful assertions (`expect(...)` or explicit `assert` statements) that prove the test objective passed.
   - Include brief, insightful comments explaining *why* a particular method was chosen (e.g., handling popups, frames, dialogs, bounding box calculations).

3. **Comprehensive Scenario Coverage**:
   - Cover all practice objectives and test conditions defined on the target page.
   - Highlight alternative approaches when answering interview-style automation questions.

4. **File Placement & Execution**:
   - Save new tests inside the `LetCode/` directory following the naming pattern `test_<feature>.py`.
   - Always include an `if __name__ == "__main__":` block so scripts can be run directly via `python` or through `pytest`.
   - Pass `flush=True` to `print()` statements for real-time console feedback.

5. **Execute & Self-Correct**:
   - Always execute the generated test script to verify real-time execution.
   - If any errors, timeout issues, or locator mismatches occur during execution, immediately analyze the failure, correct the code, and re-verify until the test passes cleanly without errors.

## Template Structure

```python
from playwright.sync_api import sync_playwright, expect


class Test<Feature>Page:
    def test_navigate_to_<feature>_page(self):
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            page = browser.new_page()

            page.goto("https://letcode.in/<feature>")
            print("\nPage title is:", page.title(), flush=True)

            # Step 1: Scenario 1 - Description & Locator Strategy
            # ...

            # Step 2: Scenario 2 - Action & Explicit Assertion
            # ...

            page.wait_for_timeout(2000)
            browser.close()


if __name__ == "__main__":
    Test<Feature>Page().test_navigate_to_<feature>_page()
```
