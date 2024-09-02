import re
import subprocess
def yes_no_prompt(prompt):
    while True:
        response = input(prompt + " (y/n): ").strip().lower()
        if response in ('y', 'yes'):
            return True
        elif response in ('n', 'no'):
            return False
        else:
            print("Please enter 'y' for yes or 'n' for no.")


if yes_no_prompt("Do you want to get the dockerfile from github? "):
    import os
    os.remove("Dockerfile")
    
    command = [
        "sudo", "wget", "https://raw.githubusercontent.com/Blipblopblopblop/caldera/master/Dockerfile"
    ]
    
    # Run the command
    try:
        result = subprocess.run(command, check=True, text=True, capture_output=True)
        print("Command output:", result.stdout)
    except subprocess.CalledProcessError as e:
        print("An error occurred:", e.stderr)

if yes_no_prompt(" do you want to change the host contact address?" ):
        
    # Read the content from the file
    with open("./conf/local.yml", 'r') as file:
        content = file.read()
    
    # Get the new contact address from user input
    contactip = input("Please specify the contact IP address you want to use to access Caldera. Note that it if you want to access is web app it cannot be 0.0.0.0 ")
    contacthttp = "http://"+contactip+":8888"
    
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
    
    if yes_no_prompt(" do you want to write changes? " ):

        with open('./conf/local.yml', 'w') as file:
            file.write(content)
    
    
if yes_no_prompt(" do you want to start the docker build? " ):
    print("please wait patiently this will take a while ")
    # Define the Docker command
    command = [
        "sudo", "docker", "build", ".",
        "--build-arg", "WIN_BUILD=true",
        "-t", "caldera:latest"
    ]
    
    # Run the Docker command
    try:
        result = subprocess.run(command, check=True, text=True, capture_output=True)
        print("Command output:", result.stdout)
    except subprocess.CalledProcessError as e:
        print("An error occurred:", e.stderr)
