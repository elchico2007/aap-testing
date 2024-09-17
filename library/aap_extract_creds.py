# aap_extract_creds.py
# Note: This script is used to extract credentials from the AWX database and decrypt them.
#  Needs to be ran once you access the awc shell via the command "tower-manage shell_plus"
# Import necessary modules
from awx.main.models import Credential
from awx.main.utils import decrypt_field

# Retrieve all credentials from the database
credentials = Credential.objects.all()

# Iterate through each credential
for cred in credentials:
    print(f"\nCredential Name: {cred.name}")
    
    # Iterate through each field in the credential's inputs
    for field, value in cred.inputs.items():
        # Check if the field value is an encrypted string
        if isinstance(value, str) and value.startswith('$encrypted$'):
            # Decrypt the field value
            decrypted_value = decrypt_field(cred, field)
            print(f"{field}: {decrypted_value}")
        
        # Check for specific sensitive fields that might be encrypted
        #  depending on the keys, you have, you will need to add them to the list in order to decrypt them
        elif field in ['token', 'password', 'become_password', 'ssh_key_data', 
                       'api_key', 'slack_token', 'panos_password', 
                       'servicenow_password', 'mssql_password']:
            # If the field is encrypted, decrypt it
            if isinstance(value, str) and value.startswith('$encrypted$'):
                decrypted_value = decrypt_field(cred, field)
                print(f"{field}: {decrypted_value}")
            # If the field is not encrypted, print it as-is
            else:
                print(f"{field}: {value}")

# Note: This script will output sensitive information.
# Use with caution and only in secure environments.