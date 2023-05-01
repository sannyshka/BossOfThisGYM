import re

filename = input("Enter file name: ")
with open(filename, 'r') as file:
    text = file.read()

email_pattern = r'(\S)(\S*)@(\S*)(\S)'

text_with_masked_emails = re.sub(email_pattern, '*@*', text)

print(text_with_masked_emails)
