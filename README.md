
# Google Colab Notebook: Convert Markdown to Google Doc

This script converts markdown text into a formatted Google Doc using the Google Docs API.

## Features

- **Google Cloud Integration**: Leverages the Google Docs API for seamless document creation and formatting.
- **Markdown Parsing**: Automatically applies appropriate styles (headings, checkboxes, text) based on Markdown input.
- **Dynamic Formatting**: Supports headings (`#`, `##`, `###`), checkboxes (`- [ ]`, `- [x]`), and plain text formatting.

---

## Prerequisites

1. **Python Environment**: Ensure you have Python installed along with the required libraries:

   ```bash
   pip install google-api-python-client google-auth google-auth-oauthlib
   ```

2. **Google Cloud Project**:

   - Log in to your [Google Cloud Console](https://console.cloud.google.com/).
   - Enable the **Google Docs API** under the "APIs & Services" section.

3. **Authorization**:

   - Authenticate with your Google Cloud account using `auth.authenticate_user()` (designed for Google Colab environments).

---

## Setup and Usage

### 1. Clone or Download the Script

Save the Python script to your local environment or Google Colab.

### 2. Authenticate

In Google Colab, the script will prompt you to authenticate:

```python
from google.colab import auth
from googleapiclient.discovery import build

auth.authenticate_user()
service = build('docs', 'v1')
```

### 3. Customize Markdown Input

Edit the `markdown_notes` variable in the script to include your desired content:

```python
markdown_notes = """# Meeting Notes
- [ ] Task 1
- [x] Task 2
"""
```

### 4. Run the Script

Execute the script to:

- Create a new Google Doc.
- Format the content according to the Markdown structure.

---

## Script Overview

### `authenticate()`

Handles user authentication and initializes the Google Docs service.

### `create_google_doc(service, title)`

Creates a new Google Doc with the specified title.

### `format_doc(service, doc_id, markdown)`

Parses the provided Markdown content and formats the document:

- **Headings**: Supports levels 1, 2, and 3.
- **Checkboxes**: Converts Markdown checkboxes into visual symbols.
- **Plain Text**: Adds unformatted text where applicable.

### `main()`

Combines all functionalities to:

1. Authenticate the user.
2. Create a new document.
3. Format the document with Markdown input.

---

## Example Output

### Input Markdown:

```markdown
# Team Meeting
## Agenda
- [ ] Discuss project updates
- [x] Review budget
```

### Google Doc Output:

#### Team Meeting

**Agenda**

- ☐ Discuss project updates
- ☑ Review budget

---

## Notes

- This script is optimized for Google Colab but can be adapted for other environments.
- Ensure API quotas and permissions are configured in your Google Cloud project.

---

For additional details, refer to the [Google Docs API documentation](https://developers.google.com/docs/api).


## Troubleshooting
- Update the script to handle API index updates dynamically.

