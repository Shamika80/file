import re

def extract_emails(filename):
  """Extracts all email addresses from a text file."""
  emails = []  
  email_regex = r"\b[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+\b"  
  try:
    with open(filename, 'r') as file:
      for line in file:
        matches = re.findall(email_regex, line)
        emails.extend(matches)  
  except FileNotFoundError:
    print(f"Error: File not found: {filename}")
  except PermissionError:
    print(f"Error: Access denied for file: {filename}")
  return emails

if __name__ == "__main__":
  filename = "contacts.txt"  
  all_emails = extract_emails(filename)
  if all_emails:
    print("All Email Addresses:")
    for email in all_emails:
      print(email)
  else:
    print("No email addresses found in the file.")