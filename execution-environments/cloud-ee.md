# v1.3
# Execution Environment
```
version: 1
build_arg_defaults:
  EE_BASE_IMAGE: 'quay.io/ansible/ansible-runner:latest'
dependencies:
  galaxy: galaxy/requirements.yml
  python: python/requirements.txt
  system: system/bindep.txt
```
# Galaxy
```
---
collections:
  - name: community.general
  - name: amazon.aws
  - name: azure.azcollection
  - name: community.vmware
```
# Python
```
botocore>=1.21.0
boto3>=1.18.0
awscli
pycrypto
pyVmomi>=6.7
git+https://github.com/vmware/vsphere-automation-sdk-python.git ; python_version >= '2.7'  # Python 2.6 is not supported
```
# System
```
python38-devel [platform:rpm compile]
gcc [platform:rpm compile]
```