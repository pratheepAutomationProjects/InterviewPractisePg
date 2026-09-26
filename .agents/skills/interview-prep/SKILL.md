---
name: interview-prep
description: Prepares QA Automation interview questions, answers, locator strategy explanations, and comparative analyses (e.g. Selenium vs Playwright dialog handling).
---

# QA Automation Interview Prep Skill

Use this skill when explaining test automation concepts, preparing for QA technical interviews, or breaking down how specific web elements are automated.

## Key Technical Topics
1. **Dialog & Alert Handling**:
   - Difference between browser modal dialogs (alert, confirm, prompt) and DOM modal popups (SweetAlert, Bootstrap modal).
   - How Playwright auto-dismisses unhandled dialogs vs Selenium throwing `UnhandledAlertException`.
2. **Locator Strategies**:
   - CSS vs XPath performance and readability.
   - Playwright auto-waiting locators vs explicit waits in Selenium (`WebDriverWait`).
3. **Multi-Tab & Frame Automation**:
   - Handling `<iframe>` using `page.frame_locator()`.
   - Handling multi-window popups with `context.expect_page()`.
