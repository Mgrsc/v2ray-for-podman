#!/usr/bin/env python3
from pathlib import Path
import json
import uuid

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

