echo "Installing IIS Server......"
Install-WindowsFeature -name Web-Server -IncludeManagementTools
echo "IIS Server Installed."