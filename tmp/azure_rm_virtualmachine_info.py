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
module: azure_rm_virtualmachine_info
version_added: '2.9'
short_description: Get VirtualMachine info.
description:
  - Get info of VirtualMachine.
options:
  location:
    description:
      - >-
        The location for which virtual machines under the subscription are
        queried.
    type: str
  resource_group_name:
    description:
      - The name of the resource group.
    type: str
  vm_name:
    description:
      - The name of the virtual machine.
    type: str
  expand:
    description:
      - The expand expression to apply on the operation.
    type: constant
  status_only:
    description:
      - >-
        statusOnly=true enables fetching run time status of all Virtual Machines
        in the subscription.
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


class AzureRMVirtualMachineInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            location=dict(
                type='str'
            ),
            resource_group_name=dict(
                type='str'
            ),
            vm_name=dict(
                type='str'
            ),
            expand=dict(
                type='constant'
            ),
            status_only=dict(
                type='str'
            )
        )

        self.location = None
        self.resource_group_name = None
        self.vm_name = None
        self.expand = None
        self.status_only = None

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
        super(AzureRMVirtualMachineInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(ComputeManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-06-01')

        if (self.resource_group_name is not None and
            self.vm_name is not None):
            self.results['virtual_machines'] = self.format_item(self.get())
        elif (self.resource_group_name is not None and
              self.vm_name is not None):
            self.results['virtual_machines'] = self.format_item(self.instanceview())
        elif (self.resource_group_name is not None and
              self.vm_name is not None):
            self.results['virtual_machines'] = self.format_item(self.listavailablesize())
        elif (self.location is not None):
            self.results['virtual_machines'] = self.format_item(self.listbylocation())
        elif (self.resource_group_name is not None):
            self.results['virtual_machines'] = self.format_item(self.list())
        else:
            self.results['virtual_machines'] = self.format_item(self.listall())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.virtual_machines.get(resource_group_name=self.resource_group_name,
                                                             vm_name=self.vm_name,
                                                             expand=self.expand)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def instanceview(self):
        response = None

        try:
            response = self.mgmt_client.virtual_machines.instance_view(resource_group_name=self.resource_group_name,
                                                                       vm_name=self.vm_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listavailablesize(self):
        response = None

        try:
            response = self.mgmt_client.virtual_machines.list_available_size(resource_group_name=self.resource_group_name,
                                                                             vm_name=self.vm_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbylocation(self):
        response = None

        try:
            response = self.mgmt_client.virtual_machines.list_by_location(location=self.location)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.virtual_machines.list(resource_group_name=self.resource_group_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listall(self):
        response = None

        try:
            response = self.mgmt_client.virtual_machines.list_all(status_only=self.status_only)
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
    AzureRMVirtualMachineInfo()


if __name__ == '__main__':
    main()
