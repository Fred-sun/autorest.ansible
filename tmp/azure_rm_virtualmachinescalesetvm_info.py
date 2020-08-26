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
module: azure_rm_virtualmachinescalesetvm_info
version_added: '2.9'
short_description: Get VirtualMachineScaleSetVM info.
description:
  - Get info of VirtualMachineScaleSetVM.
options:
  resource_group_name:
    description:
      - The name of the resource group.
    required: true
    type: str
  vm_scale_set_name:
    description:
      - The name of the VM scale set.
    type: str
  instance_id:
    description:
      - The instance ID of the virtual machine.
    type: str
  expand:
    description:
      - >-
        The expand expression to apply to the operation. Allowed values are
        'instanceView'.
    type: str
  virtual_machine_scale_set_name:
    description:
      - The name of the VM scale set.
    type: str
  filter:
    description:
      - >-
        The filter to apply to the operation. Allowed values are
        'startswith(instanceView/statuses/code, 'PowerState') eq true',
        'properties/latestModelApplied eq true', 'properties/latestModelApplied
        eq false'.
    type: str
  select:
    description:
      - >-
        The list parameters. Allowed values are 'instanceView',
        'instanceView/statuses'.
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


class AzureRMVirtualMachineScaleSetVMInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            vm_scale_set_name=dict(
                type='str'
            ),
            instance_id=dict(
                type='str'
            ),
            expand=dict(
                type='constant'
            ),
            virtual_machine_scale_set_name=dict(
                type='str'
            ),
            filter=dict(
                type='str'
            ),
            select=dict(
                type='str'
            ),
            expand=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.vm_scale_set_name = None
        self.instance_id = None
        self.expand = None
        self.virtual_machine_scale_set_name = None
        self.filter = None
        self.select = None
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
        super(AzureRMVirtualMachineScaleSetVMInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(ComputeManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-06-01')

        if (self.resource_group_name is not None and
            self.vm_scale_set_name is not None and
            self.instance_id is not None):
            self.results['virtual_machine_scale_set_vms'] = self.format_item(self.get())
        elif (self.resource_group_name is not None and
              self.vm_scale_set_name is not None and
              self.instance_id is not None):
            self.results['virtual_machine_scale_set_vms'] = self.format_item(self.getinstanceview())
        elif (self.resource_group_name is not None and
              self.virtual_machine_scale_set_name is not None):
            self.results['virtual_machine_scale_set_vms'] = self.format_item(self.list())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.virtual_machine_scale_set_vms.get(resource_group_name=self.resource_group_name,
                                                                          vm_scale_set_name=self.vm_scale_set_name,
                                                                          instance_id=self.instance_id,
                                                                          expand=self.expand)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def getinstanceview(self):
        response = None

        try:
            response = self.mgmt_client.virtual_machine_scale_set_vms.get_instance_view(resource_group_name=self.resource_group_name,
                                                                                        vm_scale_set_name=self.vm_scale_set_name,
                                                                                        instance_id=self.instance_id)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.virtual_machine_scale_set_vms.list(resource_group_name=self.resource_group_name,
                                                                           virtual_machine_scale_set_name=self.virtual_machine_scale_set_name,
                                                                           filter=self.filter,
                                                                           select=self.select,
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
    AzureRMVirtualMachineScaleSetVMInfo()


if __name__ == '__main__':
    main()