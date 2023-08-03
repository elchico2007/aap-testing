#!/usr/bin/python

# Copyright: (c) 2018, Terry Jones <terry.jones@example.org>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.module_utils.basic import AnsibleModule
import paramiko
import time

def run_module():
    # define available arguments/parameters a user can pass to the module
    module_args = dict(
        opengear_host=dict(type='str', required=True),
        opengear_user=dict(type='str', required=True),
        opengear_password=dict(type='str', required=True, no_log=True),
        port=dict(type='int', required=True),
        network_user=dict(type='str', required=True),
        network_password=dict(type='str', required=True, no_log=True),
        commands=dict(type='list', required=True)
    )

    result = dict(
        changed=False
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False
    )
    # # use whatever logic you need to determine whether or not this module
    # # made any modifications to your target
    # if module.params['new']:
    #     result['changed'] = True


    client = paramiko.client.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(module.params['opengear_host'], username=module.params['opengear_user'], password=module.params['opengear_password'])
    
    # Open a shell
    shell = client.invoke_shell()

    # Send the command to start the interactive Bash script
    shell.send("./opengear.sh" + "\n")

    # Wait for a bit to allow the script to start
    time.sleep(2)
  
    # Interact with the script by sending additional commands
    while True:
        user_input = "show version"
        if user_input.lower() == "exit":
            break
        shell.send(user_input + "\n")
        while shell.recv_ready():
            output = shell.recv(1024).decode("utf-8")
            shell.send(user_input + "\n")
            module.exit_json(msg=output)

    #_stdin, _stdout,_stderr = client.exec_command("./opengear.sh")

    #module.exit_json(msg=_stdout.read())

    # result['output'] = _stdout.read().decode()
    # result['output_lines'] = result['output'].split('\n')

    # result['output_err'] = _stderr.read().decode()
    # if result['output_err'] != "":
    #     module.fail_json(msg='Something went wrong', **result)
    
    client.close()

    module.exit_json(**result)


def main():
    run_module()

if __name__ == '__main__':
    main()