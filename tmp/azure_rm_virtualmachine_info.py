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
            self.results['virtualmachines'] = [self.format_item(self.instanceview())]
        elif (self.resource_group_name is not None and
              self.vm_name is not None):
            self.results['virtualmachines'] = [self.format_item(self.listavailablesize())]
        elif (self.resource_group_name is not None and
              self.vm_name is not None and
              self.expand is not None):
            self.results['virtualmachines'] = [self.format_item(self.get())]
        elif (self.resource_group_name is not None):
            self.results['virtualmachines'] = [self.format_item(self.list())]
        elif (self.location is not None):
            self.results['virtualmachines'] = [self.format_item(self.listbylocation())]
        elif (self.status_only is not None):
            self.results['virtualmachines'] = [self.format_item(self.listall())]
        return self.results

    def instanceview(self):
        response = None

        try:
            response = self.mgmt_client.virtualmachines.instance_view(resource_group_name=self.resource_group_name,
                                                                      vm_name=self.vm_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def listavailablesize(self):
        response = None

        try:
            response = self.mgmt_client.virtualmachines.list_available_size(resource_group_name=self.resource_group_name,
                                                                            vm_name=self.vm_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def get(self):
        response = None

        try:
            response = self.mgmt_client.virtualmachines.get(resource_group_name=self.resource_group_name,
                                                            vm_name=self.vm_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def list(self):
        response = None

        try:
            response = self.mgmt_client.virtualmachines.list(resource_group_name=self.resource_group_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def listbylocation(self):
        response = None

        try:
            response = self.mgmt_client.virtualmachines.list_by_location(location=self.location)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def listall(self):
        response = None

        try:
            response = self.mgmt_client.virtualmachines.list_all()
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def format_item(self, item):
        return item


def main():
    AzureRMVirtualMachineInfo()


if __name__ == '__main__':
    main()
