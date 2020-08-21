#!/usr/bin/python
#
# Copyright (c) 2019 Zim Kalinowski, (@zikalino)
#
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type


ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}



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


class AzureRMVirtualMachineScaleSetVMExtensionInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=true
            ),
            vm_scale_set_name=dict(
                type='str',
                required=true
            ),
            instance_id=dict(
                type='str',
                required=true
            ),
            vm_extension_name=dict(
                type='str'
            ),
            expand=dict(
                type='str',
                required=true
            )
        )

        self.resource_group_name = None
        self.vm_scale_set_name = None
        self.instance_id = None
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
        super(AzureRMVirtualMachineScaleSetVMExtensionInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(ComputeManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-06-01')

        if (self.resource_group_name is not None and
            self.vm_scale_set_name is not None and
            self.instance_id is not None and
            self.vm_extension_name is not None and
            self.expand is not None):
            self.results['virtualmachinescalesetvmextensions'] = [self.format_item(self.get())]
        elif (self.resource_group_name is not None and
              self.vm_scale_set_name is not None and
              self.instance_id is not None and
              self.expand is not None):
            self.results['virtualmachinescalesetvmextensions'] = [self.format_item(self.list())]
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.virtualmachinescalesetvmextensions.get(resource_group_name=self.resource_group_name,
                                                                               vm_scale_set_name=self.vm_scale_set_name,
                                                                               instance_id=self.instance_id,
                                                                               vm_extension_name=self.vm_extension_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def list(self):
        response = None

        try:
            response = self.mgmt_client.virtualmachinescalesetvmextensions.list(resource_group_name=self.resource_group_name,
                                                                                vm_scale_set_name=self.vm_scale_set_name,
                                                                                instance_id=self.instance_id)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def format_item(self, item):
        return item


def main():
    AzureRMVirtualMachineScaleSetVMExtensionInfo()


if __name__ == '__main__':
    main()
