# AI Usage Documentation

## Tools Used
- **Lovable** → for brainstorming creative design ideas and exploring different UI inspirations.
- **Claude** → for deeply understanding the assignment requirements, clarifying ambiguous instructions, and breaking down complex tasks step by step.
- **DesignArena** → for professional UI suggestions, layout comparisons, and feedback on improving the visual appeal of the app.
- **Copilot (Microsoft)** → for generating Django code, debugging errors, refining the dark theme UI, and guiding me through Git/GitHub setup.

---

## Prompts Given
Here are examples of the detailed prompts I used:

- To **Copilot**:
  - “Create a Django app for packaging box calculation with automatic dimension detection using OpenCV.”
  - “Make the UI professional with a dark theme and sidebar navigation.”
  - “Fix the image upload issue so the uploaded product image displays correctly.”
  - “Generate a README.md and AI_USAGE.md file for submission.”

- To **Claude**:
  - “Explain the assignment submission format step by step.”
  - “Help me understand how to structure AI usage documentation.”
  - “Clarify how to write test cases and test outputs for Django projects.”

- To **Lovable**:
  - “Suggest creative design ideas for a packaging calculator dashboard.”
  - “Give me inspiration for sidebar layouts and modern UI themes.”

- To **DesignArena**:
  - “Provide UI suggestions for a dark‑themed dashboard.”
  - “Compare different sidebar styles and recommend the most professional look.”

---

## Accepted Outputs
- Final Django code (models, views, templates).
- Dark theme CSS with sidebar navigation and hover effects.
- README.md, AI_USAGE.md, TEST_CASES.md, and TEST_OUTPUT.md files.
- Step‑by‑step submission guide for GitHub and project packaging.

---

## Rejected Outputs
- Early UI drafts without sidebar or dark theme.
- Simple unstyled templates that didn’t meet professional standards.
- Incomplete Git instructions (like using `push` instead of `git push`).

---

## Mistakes Found
- Missing `MEDIA_URL` and `MEDIA_ROOT` setup (images not showing).
- `NoReverseMatch` error for undefined routes (`dashboard` not found).
- Git command confusion (`push` vs `git push`).
- OpenCV failing to detect contours on certain images.

---

## Verification Steps
- Tested image upload and confirmed product image displays correctly.
- Verified box dimension calculation and cost estimation logic.
- Confirmed dark theme rendering with sidebar navigation.
- Checked GitHub repository push and file visibility.
- Ran Django test cases to validate functionality.
