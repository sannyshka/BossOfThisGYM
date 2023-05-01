import re

filename = input("Enter file name: ")
with open(filename, 'r') as file:
    text = file.read()

email_pattern = r'(\S)(\S*)@(\S*)(\S)'


def mask_email(match):
    return match.group(1) + '***@***' + match.group(4)


text_with_masked_emails = re.sub(email_pattern, mask_email, text)

print(text_with_masked_emails)
