#!/usr/bin/python
#
# Copyright (c) 2020 GuopengLin, (@t-glin)
#
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type


ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}


DOCUMENTATION = '''
---
module: azure_rm_virtualmachineextension
version_added: '2.9'
short_description: Manage Azure VirtualMachineExtension instance.
description:
  - 'Create, update and delete instance of Azure VirtualMachineExtension.'
options:
  resource_group_name:
    description:
      - The name of the resource group.
    required: true
    type: str
  vm_name:
    description:
      - >-
        The name of the virtual machine where the extension should be created or
        updated.
    required: true
    type: str
  vm_extension_name:
    description:
      - The name of the virtual machine extension.
    type: str
  location:
    description:
      - Resource location
    type: str
  force_update_tag:
    description:
      - >-
        How the extension handler should be forced to update even if the
        extension configuration has not changed.
    type: str
  publisher:
    description:
      - The name of the extension handler publisher.
    type: str
  type:
    description:
      - >-
        Specifies the type of the extension; an example is
        "CustomScriptExtension".
    type: str
  type_handler_version:
    description:
      - Specifies the version of the script handler.
    type: str
  auto_upgrade_minor_version:
    description:
      - >-
        Indicates whether the extension should use a newer minor version if one
        is available at deployment time. Once deployed, however, the extension
        will not upgrade minor versions unless redeployed, even with this
        property set to true.
    type: bool
  enable_automatic_upgrade:
    description:
      - >-
        Indicates whether the extension should be automatically upgraded by the
        platform if there is a newer version of the extension available.
    type: bool
  settings:
    description:
      - Json formatted public settings for the extension.
    type: any
  protected_settings:
    description:
      - >-
        The extension can contain either protectedSettings or
        protectedSettingsFromKeyVault or no protected settings at all.
    type: any
  name:
    description:
      - The virtual machine extension name.
    type: str
  virtual_machine_extension_instance_view_type:
    description:
      - >-
        Specifies the type of the extension; an example is
        "CustomScriptExtension".
    type: str
  virtual_machine_extension_instance_view_type_handler_version_type_handler_version:
    description:
      - Specifies the version of the script handler.
    type: str
  substatuses:
    description:
      - The resource status information.
    type: list
  statuses:
    description:
      - The resource status information.
    type: list
  expand:
    description:
      - The expand expression to apply on the operation.
    type: str
  state:
    description:
      - Assert the state of the VirtualMachineExtension.
      - >-
        Use C(present) to create or update an VirtualMachineExtension and
        C(absent) to delete it.
    default: present
    choices:
      - absent
      - present
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''


import time
import json
import re
from ansible.module_utils.azure_rm_common_ext import AzureRMModuleBaseExt
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.compute import ComputeManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMVirtualMachineExtension(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            vm_name=dict(
                type='str',
                required=True
            ),
            vm_extension_name=dict(
                type='str'
            ),
            location=dict(
                type='str',
                disposition='/location'
            ),
            force_update_tag=dict(
                type='str',
                disposition='/force_update_tag'
            ),
            publisher=dict(
                type='str',
                disposition='/publisher'
            ),
            type=dict(
                type='str',
                disposition='/type'
            ),
            type_handler_version=dict(
                type='str',
                disposition='/type_handler_version'
            ),
            auto_upgrade_minor_version=dict(
                type='bool',
                disposition='/auto_upgrade_minor_version'
            ),
            enable_automatic_upgrade=dict(
                type='bool',
                disposition='/enable_automatic_upgrade'
            ),
            settings=dict(
                type='any',
                disposition='/settings'
            ),
            protected_settings=dict(
                type='any',
                disposition='/protected_settings'
            ),
            name=dict(
                type='str',
                disposition='/name'
            ),
            virtual_machine_extension_instance_view_type=dict(
                type='str',
                disposition='/virtual_machine_extension_instance_view_type'
            ),
            virtual_machine_extension_instance_view_type_handler_version_type_handler_version=dict(
                type='str',
                disposition='/virtual_machine_extension_instance_view_type_handler_version_type_handler_version'
            ),
            substatuses=dict(
                type='list',
                disposition='/substatuses'
            ),
            statuses=dict(
                type='list',
                disposition='/statuses'
            ),
            expand=dict(
                type='str'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group_name = None
        self.vm_name = None
        self.vm_extension_name = None
        self.expand = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMVirtualMachineExtension, self).__init__(derived_arg_spec=self.module_arg_spec,
                                                             supports_check_mode=True,
                                                             supports_tags=True)

    def exec_module(self, **kwargs):
        for key in list(self.module_arg_spec.keys()):
            if hasattr(self, key):
                setattr(self, key, kwargs[key])
            elif kwargs[key] is not None:
                self.body[key] = kwargs[key]

        self.inflate_parameters(self.module_arg_spec, self.body, 0)

        old_response = None
        response = None

        self.mgmt_client = self.get_mgmt_svc_client(ComputeManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-06-01')

        old_response = self.get_resource()

        if not old_response:
            if self.state == 'present':
                self.to_do = Actions.Create
        else:
            if self.state == 'absent':
                self.to_do = Actions.Delete
            else:
                modifiers = {}
                self.create_compare_modifiers(self.module_arg_spec, '', modifiers)
                self.results['modifiers'] = modifiers
                self.results['compare'] = []
                if not self.default_compare(modifiers, self.body, old_response, '', self.results):
                    self.to_do = Actions.Update

        if (self.to_do == Actions.Create) or (self.to_do == Actions.Update):
            self.results['changed'] = True
            if self.check_mode:
                return self.results
            response = self.create_update_resource()
        elif self.to_do == Actions.Delete:
            self.results['changed'] = True
            if self.check_mode:
                return self.results
            self.delete_resource()
        else:
            self.results['changed'] = False
            response = old_response

        return self.results

    def create_update_resource(self):
        try:
            if self.to_do == Actions.Create:
                response = self.mgmt_client.virtual_machine_extensions.create(resource_group_name=self.resource_group_name,
                                                                              vm_name=self.vm_name,
                                                                              vm_extension_name=self.vm_extension_name,
                                                                              extension_parameters=self.body)
            else:
                response = self.mgmt_client.virtual_machine_extensions.update(resource_group_name=self.resource_group_name,
                                                                              vm_name=self.vm_name,
                                                                              vm_extension_name=self.vm_extension_name,
                                                                              extension_parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the VirtualMachineExtension instance.')
            self.fail('Error creating the VirtualMachineExtension instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.virtual_machine_extensions.delete(resource_group_name=self.resource_group_name,
                                                                          vm_name=self.vm_name,
                                                                          vm_extension_name=self.vm_extension_name)
        except CloudError as e:
            self.log('Error attempting to delete the VirtualMachineExtension instance.')
            self.fail('Error deleting the VirtualMachineExtension instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        found = False
        try:
            response = self.mgmt_client.virtual_machine_extensions.get(resource_group_name=self.resource_group_name,
                                                                       vm_name=self.vm_name,
                                                                       vm_extension_name=self.vm_extension_name,
                                                                       expand=self.expand)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMVirtualMachineExtension()


if __name__ == '__main__':
    main()
