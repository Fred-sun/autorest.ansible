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
module: azure_rm_virtualmachineextension_info
version_added: '2.9'
short_description: Get VirtualMachineExtension info.
description:
  - Get info of VirtualMachineExtension.
options:
  resource_group_name:
    description:
      - The name of the resource group.
    required: true
    type: str
  vm_name:
    description:
      - The name of the virtual machine containing the extension.
    required: true
    type: str
  vm_extension_name:
    description:
      - The name of the virtual machine extension.
    type: str
  expand:
    description:
      - The expand expression to apply on the operation.
    required: true
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''


import time
import json
from ansible.module_utils.azure_rm_common import AzureRMModuleBase
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.compute import ComputeManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMVirtualMachineExtensionInfo(AzureRMModuleBase):
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
            expand=dict(
                type='str',
                required=True
            )
        )

        self.resource_group_name = None
        self.vm_name = None
        self.vm_extension_name = None
        self.expand = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2020-06-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMVirtualMachineExtensionInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(ComputeManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-06-01')

        if (self.resource_group_name is not None and
            self.vm_name is not None and
            self.vm_extension_name is not None):
            self.results['virtual_machine_extensions'] = self.format_item(self.get())
        elif (self.resource_group_name is not None and
              self.vm_name is not None):
            self.results['virtual_machine_extensions'] = self.format_item(self.list())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.virtual_machine_extensions.get(resource_group_name=self.resource_group_name,
                                                                       vm_name=self.vm_name,
                                                                       vm_extension_name=self.vm_extension_name,
                                                                       expand=self.expand)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.virtual_machine_extensions.list(resource_group_name=self.resource_group_name,
                                                                        vm_name=self.vm_name,
                                                                        expand=self.expand)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def format_item(self, item):
        if hasattr(item, 'as_dict'):
            return [item.as_dict()]
        else:
            result = []
            items = list(item)
            for tmp in items:
               result.append(tmp.as_dict())
            return result


def main():
    AzureRMVirtualMachineExtensionInfo()


if __name__ == '__main__':
    main()
