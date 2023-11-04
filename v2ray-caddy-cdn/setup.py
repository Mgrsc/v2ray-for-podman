#!/usr/bin/env python3
from pathlib import Path
import json
import uuid

# Get the domain name from the user
domain = input("Please enter the domain name you want to use: ")

# Only proceed if a domain is provided
if domain:
    # Read the content of the Caddyfile
    caddyfile_path = Path("caddy/Caddyfile")
    with caddyfile_path.open() as file:
        caddyfile_content = file.read()

    # Replace "<your domain name>" with the user's input domain
    modified_caddyfile_content = caddyfile_content.replace("<your domain name>", domain)

    # Write the modified content back to the Caddyfile
    with caddyfile_path.open(mode="w") as file:
        file.write(modified_caddyfile_content)

    print("Caddyfile has been successfully modified!")
else:
    print("No domain was provided, Caddyfile remains unchanged.")


# Get the path of the configuration file
path = Path(__file__).parent.joinpath('v2ray/config/config.json')
# Open the configuration file
file = open(str(path), 'r', encoding='utf-8')
# Load the configuration
config = json.load(file)

# Generate a new UPSTREAM UUID
upstreamUUID = str(uuid.uuid4())

# Update the UPSTREAM UUID in the configuration file
config['inbounds'][0]['settings']['clients'][0]['id'] = upstreamUUID

# Save the updated configuration file
content = json.dumps(config, indent=2)
open(str(path), 'w', encoding='utf-8').write(content)

# Print the result
print('Upstream UUID:')
print(upstreamUUID)
print('\nDone!')

