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
module: azure_rm_dedicatedhost_info
version_added: '2.9'
short_description: Get DedicatedHost info.
description:
  - Get info of DedicatedHost.
options:
  resource_group_name:
    description:
      - The name of the resource group.
    required: true
    type: str
  host_group_name:
    description:
      - The name of the dedicated host group.
    required: true
    type: str
  host_name:
    description:
      - The name of the dedicated host.
    type: str
  expand:
    description:
      - The expand expression to apply on the operation.
    type: constant
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


class AzureRMDedicatedHostInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            host_group_name=dict(
                type='str',
                required=True
            ),
            host_name=dict(
                type='str'
            ),
            expand=dict(
                type='constant'
            )
        )

        self.resource_group_name = None
        self.host_group_name = None
        self.host_name = None
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
        super(AzureRMDedicatedHostInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(ComputeManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-06-01')

        if (self.resource_group_name is not None and
            self.host_group_name is not None and
            self.host_name is not None):
            self.results['dedicated_hosts'] = self.format_item(self.get())
        elif (self.resource_group_name is not None and
              self.host_group_name is not None):
            self.results['dedicated_hosts'] = self.format_item(self.listbyhostgroup())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.dedicated_hosts.get(resource_group_name=self.resource_group_name,
                                                            host_group_name=self.host_group_name,
                                                            host_name=self.host_name,
                                                            expand=self.expand)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbyhostgroup(self):
        response = None

        try:
            response = self.mgmt_client.dedicated_hosts.list_by_host_group(resource_group_name=self.resource_group_name,
                                                                           host_group_name=self.host_group_name)
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
    AzureRMDedicatedHostInfo()


if __name__ == '__main__':
    main()