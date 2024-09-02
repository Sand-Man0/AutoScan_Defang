import re

# Read the content from the file
with open("./conf/local.yml", 'r') as file:
    content = file.read()

# Get the new contact address from user input
contactip = input("Please specify the contact IP address you want to use to access Caldera. Note that it if you want to access is web app it cannot be 0.0.0.0 ")
contacthttp = "http://"+contactip

# Define regex patterns with capturing groups
pattern1 = r"app\.frontend\.api_base_url:\s*(\S+)"
pattern2 = r"app\.contact\.http:\s*(\S+)"

# Search for matches in the content
match1 = re.search(pattern1, content)
match2 = re.search(pattern2, content)

# Replace
if match1:
    url1 = match1.group(1)  # Extract the first captured group from pattern1
    print(url1)
    content = content.replace(url1,contacthttp)
else:
    print("API Base URL pattern not found.")

if match2:
    url2 = match2.group(1)  # Extract the first captured group from pattern2
    content = content.replace(url2,contacthttp)

else:
    print("Contact HTTP pattern not found.")

print(content)
with open('./conf/local.yml', 'w') as file:
    file.write(content)
