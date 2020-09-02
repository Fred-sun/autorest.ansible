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
module: azure_rm_managementpolicy_info
version_added: '2.9'
short_description: Get ManagementPolicy info.
description:
  - Get info of ManagementPolicy.
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
  management_policy_name:
    description:
      - >-
        The name of the Storage Account Management Policy. It should always be
        'default'
    required: true
    type: str
    choices:
      - default
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: StorageAccountGetManagementPolicies
      azure_rm_managementpolicy_info: 
        account_name: sto2527
        management_policy_name: default
        resource_group_name: res6977
        

'''

RETURN = '''
management_policies:
  description: >-
    A list of dict results where the key is the name of the ManagementPolicy and
    the values are the facts for that ManagementPolicy.
  returned: always
  type: complex
  contains:
    id:
      description:
        - >-
          Fully qualified resource Id for the resource. Ex -
          /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
      returned: always
      type: str
      sample: null
    name:
      description:
        - The name of the resource
      returned: always
      type: str
      sample: null
    type:
      description:
        - >-
          The type of the resource. Ex- Microsoft.Compute/virtualMachines or
          Microsoft.Storage/storageAccounts.
      returned: always
      type: str
      sample: null
    last_modified_time:
      description:
        - Returns the date and time the ManagementPolicies was last modified.
      returned: always
      type: str
      sample: null
    rules:
      description:
        - >-
          The Storage Account ManagementPolicies Rules. See more details in:
          https://docs.microsoft.com/en-us/azure/storage/common/storage-lifecycle-managment-concepts.
      returned: always
      type: list
      sample: null
      contains:
        enabled:
          description:
            - Rule is enabled if set to true.
          returned: always
          type: bool
          sample: null
        name:
          description:
            - >-
              A rule name can contain any combination of alpha numeric
              characters. Rule name is case-sensitive. It must be unique within
              a policy.
          returned: always
          type: str
          sample: null
        type:
          description:
            - The valid value is Lifecycle
          returned: always
          type: str
          sample: null
        definition:
          description:
            - An object that defines the Lifecycle rule.
          returned: always
          type: dict
          sample: null
          contains:
            actions:
              description:
                - An object that defines the action set.
              returned: always
              type: dict
              sample: null
              contains:
                base_blob:
                  description:
                    - The management policy action for base blob
                  returned: always
                  type: dict
                  sample: null
                  contains:
                    tier_to_cool:
                      description:
                        - >-
                          The function to tier blobs to cool storage. Support
                          blobs currently at Hot tier
                      returned: always
                      type: dict
                      sample: null
                      contains:
                        days_after_modification_greater_than:
                          description:
                            - >-
                              Value indicating the age in days after last
                              modification
                          returned: always
                          type: number
                          sample: null
                    tier_to_archive:
                      description:
                        - >-
                          The function to tier blobs to archive storage. Support
                          blobs currently at Hot or Cool tier
                      returned: always
                      type: dict
                      sample: null
                      contains:
                        days_after_modification_greater_than:
                          description:
                            - >-
                              Value indicating the age in days after last
                              modification
                          returned: always
                          type: number
                          sample: null
                    delete:
                      description:
                        - The function to delete the blob
                      returned: always
                      type: dict
                      sample: null
                      contains:
                        days_after_modification_greater_than:
                          description:
                            - >-
                              Value indicating the age in days after last
                              modification
                          returned: always
                          type: number
                          sample: null
                snapshot:
                  description:
                    - The management policy action for snapshot
                  returned: always
                  type: dict
                  sample: null
                  contains:
                    delete:
                      description:
                        - The function to delete the blob snapshot
                      returned: always
                      type: dict
                      sample: null
                      contains:
                        days_after_creation_greater_than:
                          description:
                            - Value indicating the age in days after creation
                          returned: always
                          type: number
                          sample: null
            filters:
              description:
                - An object that defines the filter set.
              returned: always
              type: dict
              sample: null
              contains:
                prefix_match:
                  description:
                    - An array of strings for prefixes to be match.
                  returned: always
                  type: list
                  sample: null
                blob_types:
                  description:
                    - >-
                      An array of predefined enum values. Only blockBlob is
                      supported.
                  returned: always
                  type: list
                  sample: null
                blob_index_match:
                  description:
                    - >-
                      An array of blob index tag based filters, there can be at
                      most 10 tag filters
                  returned: always
                  type: list
                  sample: null
                  contains:
                    name:
                      description:
                        - >-
                          This is the filter tag name, it can have 1 - 128
                          characters
                      returned: always
                      type: str
                      sample: null
                    op:
                      description:
                        - >-
                          This is the comparison operator which is used for
                          object comparison and filtering. Only == (equality
                          operator) is currently supported
                      returned: always
                      type: str
                      sample: null
                    value:
                      description:
                        - >-
                          This is the filter tag value field used for tag based
                          filtering, it can have 0 - 256 characters
                      returned: always
                      type: str
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


class AzureRMManagementPolicyInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            account_name=dict(
                type='str',
                required=True
            ),
            management_policy_name=dict(
                type='str',
                choices=['default'],
                required=True
            )
        )

        self.resource_group_name = None
        self.account_name = None
        self.management_policy_name = None

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
        super(AzureRMManagementPolicyInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(StorageManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2019-06-01')

        if (self.resource_group_name is not None and
            self.account_name is not None and
            self.management_policy_name is not None):
            self.results['management_policies'] = self.format_item(self.get())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.management_policies.get(resource_group_name=self.resource_group_name,
                                                                account_name=self.account_name,
                                                                management_policy_name=self.management_policy_name)
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
    AzureRMManagementPolicyInfo()


if __name__ == '__main__':
    main()
