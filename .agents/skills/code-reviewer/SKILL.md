---
name: code-reviewer
description: Audits Python Playwright automation code for robust locator strategies, proper handling of dialogs/frames/modals, non-flaky waits, assertion coverage, and PEP8 standards.
---

# Code Reviewer Skill

Use this skill to audit and review test automation code in this workspace.

## Audit Checklist
- [ ] **Locators**: Are locators unique, maintainable, and using proper priorities (ID > Role > Attribute > XPath)?
- [ ] **Synchronization**: Are non-deterministic `time.sleep` calls avoided in favor of Playwright built-in auto-waiting or `wait_for()`?
- [ ] **Assertions**: Does every interaction have explicit assertion checks validating post-conditions?
- [ ] **Dialog Handling**: Are dialog listeners (`page.once("dialog", ...)`) registered before triggering actions?
- [ ] **Clean Up**: Are browser contexts and browser instances closed properly in a `finally` block or context manager?
