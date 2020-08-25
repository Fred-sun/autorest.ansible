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


class AzureRMVirtualMachineScaleSetInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str'
            ),
            vm_scale_set_name=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.vm_scale_set_name = None

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
        super(AzureRMVirtualMachineScaleSetInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(ComputeManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if (self.resource_group_name is not None and
            self.vm_scale_set_name is not None):
            self.results['virtual_machine_scale_sets'] = self.format_item(self.getosupgradehistory())
        elif (self.resource_group_name is not None and
              self.vm_scale_set_name is not None):
            self.results['virtual_machine_scale_sets'] = self.format_item(self.getinstanceview())
        elif (self.resource_group_name is not None and
              self.vm_scale_set_name is not None):
            self.results['virtual_machine_scale_sets'] = self.format_item(self.listsku())
        elif (self.resource_group_name is not None and
              self.vm_scale_set_name is not None):
            self.results['virtual_machine_scale_sets'] = self.format_item(self.get())
        elif (self.resource_group_name is not None):
            self.results['virtual_machine_scale_sets'] = self.format_item(self.list())
        else:
            self.results['virtual_machine_scale_sets'] = self.format_item(self.listall())
        return self.results

    def getosupgradehistory(self):
        response = None

        try:
            response = self.mgmt_client.virtual_machine_scale_sets.get_os_upgrade_history(resource_group_name=self.resource_group_name,
                                                                                          vm_scale_set_name=self.vm_scale_set_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def getinstanceview(self):
        response = None

        try:
            response = self.mgmt_client.virtual_machine_scale_sets.get_instance_view(resource_group_name=self.resource_group_name,
                                                                                     vm_scale_set_name=self.vm_scale_set_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listsku(self):
        response = None

        try:
            response = self.mgmt_client.virtual_machine_scale_sets.list_sku(resource_group_name=self.resource_group_name,
                                                                            vm_scale_set_name=self.vm_scale_set_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def get(self):
        response = None

        try:
            response = self.mgmt_client.virtual_machine_scale_sets.get(resource_group_name=self.resource_group_name,
                                                                       vm_scale_set_name=self.vm_scale_set_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.virtual_machine_scale_sets.list(resource_group_name=self.resource_group_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listall(self):
        response = None

        try:
            response = self.mgmt_client.virtual_machine_scale_sets.list_all()
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
    AzureRMVirtualMachineScaleSetInfo()


if __name__ == '__main__':
    main()
