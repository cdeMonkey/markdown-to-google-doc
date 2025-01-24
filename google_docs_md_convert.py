from google.colab import auth
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow



def authenticate():
    # Authenticate the user with Google Colab's built-in method
    auth.authenticate_user()
    # Build the Google Docs service
    service = build('docs', 'v1')
    return service

def create_google_doc(service, title):
    doc = service.documents().create(body={"title": title}).execute()
    print(f"Document created: {doc.get('title')} (ID: {doc.get('documentId')})")
    return doc.get('documentId')

def format_doc(service, doc_id, markdown):
    requests = []
    current_index = 1  # Start at index 1 since 0 is reserved for the beginning of the document

    # Split markdown into sections
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):  # Heading 1
            requests.append({
                'insertText': {
                    'location': {'index': current_index},
                    'text': line[2:] + "\n"
                }
            })
            requests.append({
                'updateParagraphStyle': {
                    'range': {
                        'startIndex': current_index,
                        'endIndex': current_index + len(line[2:]) + 1,
                    },
                    'paragraphStyle': {'namedStyleType': 'HEADING_1'},
                    'fields': 'namedStyleType',
                }
            })
            current_index += len(line[2:]) + 1
        elif line.startswith("## "):  # Heading 2
            requests.append({
                'insertText': {
                    'location': {'index': current_index},
                    'text': line[3:] + "\n"
                }
            })
            requests.append({
                'updateParagraphStyle': {
                    'range': {
                        'startIndex': current_index,
                        'endIndex': current_index + len(line[3:]) + 1,
                    },
                    'paragraphStyle': {'namedStyleType': 'HEADING_2'},
                    'fields': 'namedStyleType',
                }
            })
            current_index += len(line[3:]) + 1
        elif line.startswith("### "):  # Heading 3
            requests.append({
                'insertText': {
                    'location': {'index': current_index},
                    'text': line[4:] + "\n"
                }
            })
            requests.append({
                'updateParagraphStyle': {
                    'range': {
                        'startIndex': current_index,
                        'endIndex': current_index + len(line[4:]) + 1,
                    },
                    'paragraphStyle': {'namedStyleType': 'HEADING_3'},
                    'fields': 'namedStyleType',
                }
            })
            current_index += len(line[4:]) + 1
        elif line.startswith("- [ ] "):  # Unchecked checkbox
            checkbox_text = "☐ " + line[6:] + "\n"
            requests.append({
                'insertText': {
                    'location': {'index': current_index},
                    'text': checkbox_text
                }
            })
            current_index += len(checkbox_text)
        elif line.startswith("- [x] "):  # Checked checkbox
            checkbox_text = "☑ " + line[6:] + "\n"
            requests.append({
                'insertText': {
                    'location': {'index': current_index},
                    'text': checkbox_text
                }
            })
            current_index += len(checkbox_text)
        else:  # Regular text
            requests.append({
                'insertText': {
                    'location': {'index': current_index},
                    'text': line + "\n"
                }
            })
            current_index += len(line) + 1

    # Execute the batch update
    try:
        service.documents().batchUpdate(
            documentId=doc_id,
            body={"requests": requests}
        ).execute()
        print("Document formatted successfully.")
    except HttpError as error:
        print(f"An error occurred: {error}")



# Main function, left notes as one big string, probably not write and should import the notes....
def main():
    markdown_notes = """# Product Team Sync - May 15, 2023

## Attendees
- Sarah Chen (Product Lead)
- Mike Johnson (Engineering)
- Anna Smith (Design)
- David Park (QA)

## Agenda

### 1. Sprint Review
* Completed Features
  * User authentication flow
  * Dashboard redesign
  * Performance optimization
    * Reduced load time by 40%
    * Implemented caching solution
* Pending Items
  * Mobile responsive fixes
  * Beta testing feedback integration

### 2. Current Challenges
* Resource constraints in QA team
* Third-party API integration delays
* User feedback on new UI
  * Navigation confusion
  * Color contrast issues

### 3. Next Sprint Planning
* Priority Features
  * Payment gateway integration
  * User profile enhancement
  * Analytics dashboard
* Technical Debt
  * Code refactoring
  * Documentation updates

## Action Items
- [ ] @sarah: Finalize Q3 roadmap by Friday
- [ ] @mike: Schedule technical review for payment integration
- [ ] @anna: Share updated design system documentation
- [ ] @david: Prepare QA resource allocation proposal

## Next Steps
* Schedule individual team reviews
* Update sprint board
* Share meeting summary with stakeholders

## Notes
* Next sync scheduled for May 22, 2023
* Platform demo for stakeholders on May 25
* Remember to update JIRA tickets

---
Meeting recorded by: Sarah Chen
Duration: 45 minutes
"""

    service = authenticate()
    doc_id = create_google_doc(service, "Product Team Sync Notes")
    format_doc(service, doc_id, markdown_notes)

if __name__ == "__main__":
    main()
