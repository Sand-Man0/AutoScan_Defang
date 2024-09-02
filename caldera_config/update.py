
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
