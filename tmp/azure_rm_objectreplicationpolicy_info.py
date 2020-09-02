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
module: azure_rm_objectreplicationpolicy_info
version_added: '2.9'
short_description: Get ObjectReplicationPolicy info.
description:
  - Get info of ObjectReplicationPolicy.
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
  object_replication_policy_id:
    description:
      - >-
        The ID of object replication policy or 'default' if the policy ID is
        unknown.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: StorageAccountListObjectReplicationPolicies
      azure_rm_objectreplicationpolicy_info: 
        account_name: sto2527
        resource_group_name: res6977
        

    - name: StorageAccountGetObjectReplicationPolicies
      azure_rm_objectreplicationpolicy_info: 
        account_name: sto2527
        object_replication_policy_id: '{objectReplicationPolicy-Id}'
        resource_group_name: res6977
        

'''

RETURN = '''
object_replication_policies:
  description: >-
    A list of dict results where the key is the name of the
    ObjectReplicationPolicy and the values are the facts for that
    ObjectReplicationPolicy.
  returned: always
  type: complex
  contains:
    value:
      description:
        - The replication policy between two storage accounts.
      returned: always
      type: list
      sample: null
      contains:
        policy_id:
          description:
            - A unique id for object replication policy.
          returned: always
          type: str
          sample: null
        enabled_time:
          description:
            - Indicates when the policy is enabled on the source account.
          returned: always
          type: str
          sample: null
        source_account:
          description:
            - Required. Source account name.
          returned: always
          type: str
          sample: null
        destination_account:
          description:
            - Required. Destination account name.
          returned: always
          type: str
          sample: null
        rules:
          description:
            - The storage account object replication rules.
          returned: always
          type: list
          sample: null
          contains:
            rule_id:
              description:
                - >-
                  Rule Id is auto-generated for each new rule on destination
                  account. It is required for put policy on source account.
              returned: always
              type: str
              sample: null
            source_container:
              description:
                - Required. Source container name.
              returned: always
              type: str
              sample: null
            destination_container:
              description:
                - Required. Destination container name.
              returned: always
              type: str
              sample: null
            filters:
              description:
                - Optional. An object that defines the filter set.
              returned: always
              type: dict
              sample: null
              contains:
                prefix_match:
                  description:
                    - >-
                      Optional. Filters the results to replicate only blobs
                      whose names begin with the specified prefix.
                  returned: always
                  type: list
                  sample: null
                min_creation_time:
                  description:
                    - >-
                      Blobs created after the time will be replicated to the
                      destination. It must be in datetime format
                      'yyyy-MM-ddTHH:mm:ssZ'. Example: 2020-02-19T16:05:00Z
                  returned: always
                  type: str
                  sample: null
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
    policy_id:
      description:
        - A unique id for object replication policy.
      returned: always
      type: str
      sample: null
    enabled_time:
      description:
        - Indicates when the policy is enabled on the source account.
      returned: always
      type: str
      sample: null
    source_account:
      description:
        - Required. Source account name.
      returned: always
      type: str
      sample: null
    destination_account:
      description:
        - Required. Destination account name.
      returned: always
      type: str
      sample: null
    rules:
      description:
        - The storage account object replication rules.
      returned: always
      type: list
      sample: null
      contains:
        rule_id:
          description:
            - >-
              Rule Id is auto-generated for each new rule on destination
              account. It is required for put policy on source account.
          returned: always
          type: str
          sample: null
        source_container:
          description:
            - Required. Source container name.
          returned: always
          type: str
          sample: null
        destination_container:
          description:
            - Required. Destination container name.
          returned: always
          type: str
          sample: null
        filters:
          description:
            - Optional. An object that defines the filter set.
          returned: always
          type: dict
          sample: null
          contains:
            prefix_match:
              description:
                - >-
                  Optional. Filters the results to replicate only blobs whose
                  names begin with the specified prefix.
              returned: always
              type: list
              sample: null
            min_creation_time:
              description:
                - >-
                  Blobs created after the time will be replicated to the
                  destination. It must be in datetime format
                  'yyyy-MM-ddTHH:mm:ssZ'. Example: 2020-02-19T16:05:00Z
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


class AzureRMObjectReplicationPolicyInfo(AzureRMModuleBase):
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
            object_replication_policy_id=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.account_name = None
        self.object_replication_policy_id = None

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
        super(AzureRMObjectReplicationPolicyInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(StorageManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2019-06-01')

        if (self.resource_group_name is not None and
            self.account_name is not None and
            self.object_replication_policy_id is not None):
            self.results['object_replication_policies'] = self.format_item(self.get())
        elif (self.resource_group_name is not None and
              self.account_name is not None):
            self.results['object_replication_policies'] = self.format_item(self.list())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.object_replication_policies.get(resource_group_name=self.resource_group_name,
                                                                        account_name=self.account_name,
                                                                        object_replication_policy_id=self.object_replication_policy_id)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.object_replication_policies.list(resource_group_name=self.resource_group_name,
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
    AzureRMObjectReplicationPolicyInfo()


if __name__ == '__main__':
    main()
