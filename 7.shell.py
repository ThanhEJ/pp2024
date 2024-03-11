import subprocess
while True:
    user_input = input("$ ")
    command_args = user_input.split()
    if command_args[0].lower() == 'exit':
        break
    try:
        result = subprocess.run(command_args, capture_output=True, text=True, check=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.stderr}")
print("Exiting the terminal.")