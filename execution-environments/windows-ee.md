# v1.2
# Execution Environment
```
version: 1
build_arg_defaults:
  EE_BASE_IMAGE: 'quay.io/ansible/ansible-runner:latest'
dependencies:
  galaxy: galaxy/requirements.yml
  system: system/bindep.txt
```
# Galaxy
```
collections:
  - name: ansible.windows
  - name: community.windows
  - name: chocolatey.chocolatey
```
# System
```
python38-devel [platform:rpm compile]
```