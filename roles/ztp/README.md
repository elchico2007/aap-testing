# Arista ZTP Role for Ansible

## Overview

This Ansible role automates the Zero Touch Provisioning (ZTP) process for Arista devices. It takes in specific variables to generate a basic configuration file and a `dhcpd.conf` file. The generated Arista configuration is then sent to an HTTP server for provisioning.

## Requirements

- Ansible 2.9 or higher
- A running HTTP server to host the generated Arista configuration files

## Role Variables

The role requires the following variables to be defined:

- `src_mac`: The source MAC address for the device.
- `management_address`: The management IP address in CIDR format.
- `enable_hash`: The hashed enable password for the device.
- `default_gateway`: The default gateway for the management interface.
- `admin_hash`: The hashed admin password for the device.

Example variable definitions:

```yaml
src_mac: "0c:3b:67:a3:00:00"
management_address: "192.168.0.181/24"
enable_hash: "$6$pF/D1M8wdTyZqKwZ$sqXsnI5EefvN1MWItNlk/h8vnTbZiVGao6z1cCLnZmc/xOzJe8sQilXKOeweBW6k1YQCn8rDuNz7X3NrOmzHM0"
default_gateway: "192.68.0.1"
admin_hash: "$6$MmZzZH4tyXjXEC2v$/neUCrtnss5xAPDXFzAkmpJuaPyk1w/wlzCLB26qX1xA5Rd93XTyy/UnkfWM3TX5bmJ30SwKIYQJSMfRaEGJE/"
```

## Usage

Include the role in your playbook and pass the required variables:

```yaml
---
- name: Arista ZTP
  hosts: all
  become: true
  gather_facts: false
  roles:
    - role: roles/ztp
      src_mac: "{{ src_mac }}"
      management_address: "{{ management_address }}"
      enable_hash: "{{ enable_hash }}"
      default_gateway: "{{ default_gateway }}"
      admin_hash: "{{ admin_hash }}"
```

## Example Playbook

Here is an example playbook that demonstrates how to use the Arista ZTP role:

```yaml
---
- name: Arista ZTP
  hosts: all
  become: true
  gather_facts: false
  roles:
    - role: roles/ztp
      src_mac: "{{ src_mac }}"
      management_address: "{{ management_address }}"
      enable_hash: "{{ enable_hash }}"
      default_gateway: "{{ default_gateway }}"
      admin_hash: "{{ admin_hash }}"
```

## Files Generated

This role generates the following files:

- A basic Arista configuration file based on the provided variables.
- A `dhcpd.conf` file configured for the DHCP server.

## Sending Configuration to HTTP Server

The generated Arista configuration file will be sent to a specified HTTP server for device provisioning. Ensure that your HTTP server is properly configured to serve these files.

## License

This role is licensed under the MIT License. See the LICENSE file for details.