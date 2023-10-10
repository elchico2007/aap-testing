#!/usr/bin/python

# Copyright: (c) 2023, Luis Valle <luvalle@redhat.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.module_utils.basic import AnsibleModule
from pexpect import pxssh
import time

def run_module():
    # define available arguments/parameters a user can pass to the module
    module_args = dict(
        opengear_host=dict(type='str', required=True),
        opengear_user=dict(type='str', required=True),
        opengear_password=dict(type='str', required=True, no_log=True),
        port=dict(type='int', required=True),
        commands=dict(type='list', required=True)
    )

    result = dict(
        changed=False
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False
    )

    try:
        client = pxssh.pxssh(options={"StrictHostKeyChecking": "no"})
        client.login(module.params['opengear_host'], module.params['opengear_user'], module.params['opengear_password'])

        client.sendline("pmshell.sh")
        client.PROMPT = r'Connect to port> '
        client.sendline(f"{module.params['port']}" + "\n")
        time.sleep(3)
        client.PROMPT = r'\w+#'
        client.sendline("terminal length 0\n")
        client.sendline("configure terminal")
        client.PROMPT = r'\w+(config)#'
        for command in module.params['commands']:
            if 'crypto' in command:
                client.sendline(command)
                client.PROMPT = r'\w+(config)#'
                time.sleep(5)
            else:
                client.sendline(command)
                client.PROMPT = r'\w+(config)#'
                time.sleep(1)
        time.sleep(3)
        client.sendline("exit")
        client.PROMPT = r'\w+#'
        client.sendline("exit")
        client.close()

        result['changed'] = True

    except pxssh.ExceptionPxssh as e:
        module.fail_json(msg=e)

    module.exit_json(**result)


def main():
    run_module()

if __name__ == '__main__':
    main()
