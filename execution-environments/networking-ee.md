# v1.7
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
collections:
  - name: cisco.ios
  - name: junipernetworks.junos
  - name: arista.eos
  - name: arubanetworks.aoscx
  - name: community.network
  - name: paloaltonetworks.panos
  - name: elchico2007.chatgpt
```
# Python
```
junos-eznc
xmltodict
paramiko
requests
pyaoscx>=2.3.1
openai
```
# System
```
python38-devel [platform:rpm compile]
```