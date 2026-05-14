# EXECUTE OS COMMANDS

import subprocess
import json

# List of commands
commands = [
    "pwd",
    "ls",
    "df -h",
    "pwd",
    "invalid_command"
]

# Remove duplicate commands while preserving order
unique_commands = list(dict.fromkeys(commands))

# Store final output
result = []

# Execute commands
for command in unique_commands:

    try:
        process = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True
        )

        # Success
        if process.returncode == 0:
            command_result = {
                command: {
                    "output": process.stdout.strip(),
                    "error": "",
                    "status": "Success"
                }
            }

        # Failure
        else:
            command_result = {
                command: {
                    "output": "",
                    "error": process.stderr.strip(),
                    "status": "Failed"
                }
            }

    except Exception as e:
        command_result = {
            command: {
                "output": "",
                "error": str(e),
                "status": "Failed"
            }
        }

    result.append(command_result)

# Print final output
print(json.dumps(result, indent=4))