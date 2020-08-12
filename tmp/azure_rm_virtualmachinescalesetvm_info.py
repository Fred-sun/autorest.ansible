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
from ansible.module_utils.azure_rm_common_rest import GenericRestClient
from copy import deepcopy
from msrestazure.azure_exceptions import CloudError


class AzureRMVirtualMachineScaleSetVMInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='',
                required=true
            ),
            vm_scale_set_name=dict(
                type='',
                required=true
            ),
            instance_id=dict(
                type='',
                required=true
            ),
            expand=dict(
                type=''
            ),
            apiversion=dict(
                type='',
                required=true
            ),
            subscription_id=dict(
                type='',
                required=true
            ),
            virtual_machine_scale_set_name=dict(
                type='',
                required=true
            ),
            filter=dict(
                type=''
            ),
            select=dict(
                type=''
            ),
            expand=dict(
                type=''
            )
        )


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

        self.mgmt_client = self.get_mgmt_svc_client(GenericRestClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if (self.resource_group is not None and
            self.vm_scale_set_name is not None and
            self.instance_id is not None and
            self.apiversion is not None and
            self.subscription_id is not None):
            self.results['null'] = self.format_item(self.getinstanceview())
        elif (self.resource_group is not None and
              self.vm_scale_set_name is not None and
              self.instance_id is not None and
              self.expand is not None and
              self.apiversion is not None and
              self.subscription_id is not None):
            self.results['null'] = self.format_item(self.get())
        elif (self.resource_group is not None and
              self.virtual_machine_scale_set_name is not None and
              self.filter is not None and
              self.select is not None and
              self.expand is not None and
              self.apiversion is not None and
              self.subscription_id is not None):
            self.results['null'] = self.format_item(self.list())
        return self.results

    def getinstanceview(self):
        response = None
        results = {}
        # prepare url
        self.url = ('/subscriptions' +
                    '/{subscriptionId}' +
                    '/resourceGroups' +
                    '/{resourceGroupName}' +
                    '/providers' +
                    '/Microsoft.Compute' +
                    '/virtualMachineScaleSets' +
                    '/{vmScaleSetName}' +
                    '/virtualmachines' +
                    '/{instanceId}' +
                    '/instanceView')

        try:
            response = self.mgmt_client.query(self.url,
                                              'GET',
                                              self.query_parameters,
                                              self.header_parameters,
                                              None,
                                              self.status_code,
                                              600,
                                              30)
            results['temp_item'] = json.loads(response.text)
            # self.log('Response : {0}'.format(response))
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return results

    def get(self):
        response = None
        results = {}
        # prepare url
        self.url = ('/subscriptions' +
                    '/{subscriptionId}' +
                    '/resourceGroups' +
                    '/{resourceGroupName}' +
                    '/providers' +
                    '/Microsoft.Compute' +
                    '/virtualMachineScaleSets' +
                    '/{vmScaleSetName}' +
                    '/virtualmachines' +
                    '/{instanceId}')

        try:
            response = self.mgmt_client.query(self.url,
                                              'GET',
                                              self.query_parameters,
                                              self.header_parameters,
                                              None,
                                              self.status_code,
                                              600,
                                              30)
            results['temp_item'] = json.loads(response.text)
            # self.log('Response : {0}'.format(response))
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return results

    def list(self):
        response = None
        results = {}
        # prepare url
        self.url = ('/subscriptions' +
                    '/{subscriptionId}' +
                    '/resourceGroups' +
                    '/{resourceGroupName}' +
                    '/providers' +
                    '/Microsoft.Compute' +
                    '/virtualMachineScaleSets' +
                    '/{virtualMachineScaleSetName}' +
                    '/virtualMachines')

        try:
            response = self.mgmt_client.query(self.url,
                                              'GET',
                                              self.query_parameters,
                                              self.header_parameters,
                                              None,
                                              self.status_code,
                                              600,
                                              30)
            results['temp_item'] = json.loads(response.text)
            # self.log('Response : {0}'.format(response))
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return results

    def format_item(item):
        return item


def main():
    AzureRMVirtualMachineScaleSetVMInfo()


if __name__ == '__main__':
    main()
