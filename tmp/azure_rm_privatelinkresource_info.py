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
module: azure_rm_privatelinkresource_info
version_added: '2.9'
short_description: Get PrivateLinkResource info.
description:
  - Get info of PrivateLinkResource.
options:
  resource_group_name:
    description:
      - >-
        The name of the resource group within the user's subscription. The name
        is case insensitive.
    required: true
    type: str
  account_name:
    description:
      - >-
        The name of the storage account within the specified resource group.
        Storage account names must be between 3 and 24 characters in length and
        use numbers and lower-case letters only.
    required: true
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: StorageAccountListPrivateLinkResources
      azure_rm_privatelinkresource_info: 
        account_name: sto2527
        resource_group_name: res6977
        

'''

RETURN = '''
private_link_resources:
  description: >-
    A list of dict results where the key is the name of the PrivateLinkResource
    and the values are the facts for that PrivateLinkResource.
  returned: always
  type: complex
  contains:
    value:
      description:
        - Array of private link resources
      returned: always
      type: list
      sample: null
      contains:
        group_id:
          description:
            - The private link resource group id.
          returned: always
          type: str
          sample: null
        required_members:
          description:
            - The private link resource required member names.
          returned: always
          type: list
          sample: null
        required_zone_names:
          description:
            - The private link resource Private link DNS zone name.
          returned: always
          type: list
          sample: null

'''

import time
import json
from ansible.module_utils.azure_rm_common import AzureRMModuleBase
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.storage import StorageManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMPrivateLinkResourceInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            account_name=dict(
                type='str',
                required=True
            )
        )

        self.resource_group_name = None
        self.account_name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2019-06-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMPrivateLinkResourceInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(StorageManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2019-06-01')

        if (self.resource_group_name is not None and
            self.account_name is not None):
            self.results['private_link_resources'] = self.format_item(self.listbystorageaccount())
        return self.results

    def listbystorageaccount(self):
        response = None

        try:
            response = self.mgmt_client.private_link_resources.list_by_storage_account(resource_group_name=self.resource_group_name,
                                                                                       account_name=self.account_name)
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
    AzureRMPrivateLinkResourceInfo()


if __name__ == '__main__':
    main()
