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
module: azure_rm_availabilityset_info
version_added: '2.9'
short_description: Get AvailabilitySet info.
description:
  - Get info of AvailabilitySet.
options:
  resource_group_name:
    description:
      - The name of the resource group.
    type: str
  availability_set_name:
    description:
      - The name of the availability set.
    type: str
  expand:
    description:
      - >-
        The expand expression to apply to the operation. Allowed values are
        'instanceView'.
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


class AzureRMAvailabilitySetInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str'
            ),
            availability_set_name=dict(
                type='str'
            ),
            expand=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.availability_set_name = None
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
        super(AzureRMAvailabilitySetInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(ComputeManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-06-01')

        if (self.resource_group_name is not None and
            self.availability_set_name is not None):
            self.results['availability_sets'] = self.format_item(self.get())
        elif (self.resource_group_name is not None and
              self.availability_set_name is not None):
            self.results['availability_sets'] = self.format_item(self.listavailablesize())
        elif (self.resource_group_name is not None):
            self.results['availability_sets'] = self.format_item(self.list())
        else:
            self.results['availability_sets'] = self.format_item(self.listbysubscription())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.availability_sets.get(resource_group_name=self.resource_group_name,
                                                              availability_set_name=self.availability_set_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listavailablesize(self):
        response = None

        try:
            response = self.mgmt_client.availability_sets.list_available_size(resource_group_name=self.resource_group_name,
                                                                              availability_set_name=self.availability_set_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.availability_sets.list(resource_group_name=self.resource_group_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbysubscription(self):
        response = None

        try:
            response = self.mgmt_client.availability_sets.list_by_subscription(expand=self.expand)
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
    AzureRMAvailabilitySetInfo()


if __name__ == '__main__':
    main()