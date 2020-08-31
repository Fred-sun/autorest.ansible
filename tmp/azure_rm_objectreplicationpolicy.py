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
module: azure_rm_objectreplicationpolicy
version_added: '2.9'
short_description: Manage Azure ObjectReplicationPolicy instance.
description:
  - 'Create, update and delete instance of Azure ObjectReplicationPolicy.'
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
    required: true
    type: str
  source_account:
    description:
      - Required. Source account name.
    type: str
  destination_account:
    description:
      - Required. Destination account name.
    type: str
  rules:
    description:
      - The storage account object replication rules.
    type: list
    suboptions:
      rule_id:
        description:
          - >-
            Rule Id is auto-generated for each new rule on destination account.
            It is required for put policy on source account.
        type: str
      source_container:
        description:
          - Required. Source container name.
        required: true
        type: str
      destination_container:
        description:
          - Required. Destination container name.
        required: true
        type: str
      filters:
        description:
          - Optional. An object that defines the filter set.
        type: dict
        suboptions:
          prefix_match:
            description:
              - >-
                Optional. Filters the results to replicate only blobs whose
                names begin with the specified prefix.
            type: list
          min_creation_time:
            description:
              - >-
                Blobs created after the time will be replicated to the
                destination. It must be in datetime format
                'yyyy-MM-ddTHH:mm:ssZ'. Example: 2020-02-19T16:05:00Z
            type: str
  state:
    description:
      - Assert the state of the ObjectReplicationPolicy.
      - >-
        Use C(present) to create or update an ObjectReplicationPolicy and
        C(absent) to delete it.
    default: present
    choices:
      - absent
      - present
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: StorageAccountCreateObjectReplicationPolicyOnDestination
      azure_rm_objectreplicationpolicy: 
        account_name: dst112
        object_replication_policy_id: default
        resource_group_name: res7687
        properties:
          destination_account: dst112
          rules:
            - destination_container: dcont139
              filters:
                prefix_match:
                  - blobA
                  - blobB
              source_container: scont139
          source_account: src1122
        

    - name: StorageAccountCreateObjectReplicationPolicyOnSource
      azure_rm_objectreplicationpolicy: 
        account_name: src1122
        object_replication_policy_id: 2a20bb73-5717-4635-985a-5d4cf777438f
        resource_group_name: res7687
        properties:
          destination_account: dst112
          rules:
            - destination_container: dcont139
              filters:
                min_creation_time: '2020-02-19T16:05:00Z'
                prefix_match:
                  - blobA
                  - blobB
              rule_id: d5d18a48-8801-4554-aeaa-74faf65f5ef9
              source_container: scont139
          source_account: src1122
        

    - name: StorageAccountUpdateObjectReplicationPolicyOnDestination
      azure_rm_objectreplicationpolicy: 
        account_name: dst112
        object_replication_policy_id: 2a20bb73-5717-4635-985a-5d4cf777438f
        resource_group_name: res7687
        properties:
          destination_account: dst112
          rules:
            - destination_container: dcont139
              filters:
                prefix_match:
                  - blobA
                  - blobB
              rule_id: d5d18a48-8801-4554-aeaa-74faf65f5ef9
              source_container: scont139
            - destination_container: dcont179
              source_container: scont179
          source_account: src1122
        

    - name: StorageAccountUpdateObjectReplicationPolicyOnSource
      azure_rm_objectreplicationpolicy: 
        account_name: src1122
        object_replication_policy_id: 2a20bb73-5717-4635-985a-5d4cf777438f
        resource_group_name: res7687
        properties:
          destination_account: dst112
          rules:
            - destination_container: dcont139
              filters:
                prefix_match:
                  - blobA
                  - blobB
              rule_id: d5d18a48-8801-4554-aeaa-74faf65f5ef9
              source_container: scont139
            - destination_container: dcont179
              rule_id: cfbb4bc2-8b60-429f-b05a-d1e0942b33b2
              source_container: scont179
          source_account: src1122
        

    - name: StorageAccountDeleteObjectReplicationPolicies
      azure_rm_objectreplicationpolicy: 
        account_name: sto2527
        object_replication_policy_id: '{objectReplicationPolicy-Id}'
        resource_group_name: res6977
        

'''

RETURN = '''
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
          Rule Id is auto-generated for each new rule on destination account. It
          is required for put policy on source account.
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
              Optional. Filters the results to replicate only blobs whose names
              begin with the specified prefix.
          returned: always
          type: list
          sample: null
        min_creation_time:
          description:
            - >-
              Blobs created after the time will be replicated to the
              destination. It must be in datetime format 'yyyy-MM-ddTHH:mm:ssZ'.
              Example: 2020-02-19T16:05:00Z
          returned: always
          type: str
          sample: null

'''

import time
import json
import re
from ansible.module_utils.azure_rm_common_ext import AzureRMModuleBaseExt
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.storage import StorageManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMObjectReplicationPolicy(AzureRMModuleBaseExt):
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
                type='str',
                required=True
            ),
            source_account=dict(
                type='str',
                disposition='/source_account'
            ),
            destination_account=dict(
                type='str',
                disposition='/destination_account'
            ),
            rules=dict(
                type='list',
                disposition='/rules',
                elements='dict',
                options=dict(
                    rule_id=dict(
                        type='str',
                        disposition='rule_id'
                    ),
                    source_container=dict(
                        type='str',
                        disposition='source_container',
                        required=True
                    ),
                    destination_container=dict(
                        type='str',
                        disposition='destination_container',
                        required=True
                    ),
                    filters=dict(
                        type='dict',
                        disposition='filters',
                        options=dict(
                            prefix_match=dict(
                                type='list',
                                disposition='prefix_match',
                                elements='str'
                            ),
                            min_creation_time=dict(
                                type='str',
                                disposition='min_creation_time'
                            )
                        )
                    )
                )
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group_name = None
        self.account_name = None
        self.object_replication_policy_id = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMObjectReplicationPolicy, self).__init__(derived_arg_spec=self.module_arg_spec,
                                                             supports_check_mode=True,
                                                             supports_tags=True)

    def exec_module(self, **kwargs):
        for key in list(self.module_arg_spec.keys()):
            if hasattr(self, key):
                setattr(self, key, kwargs[key])
            elif kwargs[key] is not None:
                self.body[key] = kwargs[key]

        self.inflate_parameters(self.module_arg_spec, self.body, 0)

        old_response = None
        response = None

        self.mgmt_client = self.get_mgmt_svc_client(StorageManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2019-06-01')

        old_response = self.get_resource()

        if not old_response:
            if self.state == 'present':
                self.to_do = Actions.Create
        else:
            if self.state == 'absent':
                self.to_do = Actions.Delete
            else:
                modifiers = {}
                self.create_compare_modifiers(self.module_arg_spec, '', modifiers)
                self.results['modifiers'] = modifiers
                self.results['compare'] = []
                if not self.default_compare(modifiers, self.body, old_response, '', self.results):
                    self.to_do = Actions.Update

        if (self.to_do == Actions.Create) or (self.to_do == Actions.Update):
            self.results['changed'] = True
            if self.check_mode:
                return self.results
            response = self.create_update_resource()
        elif self.to_do == Actions.Delete:
            self.results['changed'] = True
            if self.check_mode:
                return self.results
            self.delete_resource()
        else:
            self.results['changed'] = False
            response = old_response

        return self.results

    def create_update_resource(self):
        try:
            response = self.mgmt_client.object_replication_policies.create_or_update(resource_group_name=self.resource_group_name,
                                                                                     account_name=self.account_name,
                                                                                     object_replication_policy_id=self.object_replication_policy_id,
                                                                                     properties=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the ObjectReplicationPolicy instance.')
            self.fail('Error creating the ObjectReplicationPolicy instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.object_replication_policies.delete(resource_group_name=self.resource_group_name,
                                                                           account_name=self.account_name,
                                                                           object_replication_policy_id=self.object_replication_policy_id)
        except CloudError as e:
            self.log('Error attempting to delete the ObjectReplicationPolicy instance.')
            self.fail('Error deleting the ObjectReplicationPolicy instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.object_replication_policies.get(resource_group_name=self.resource_group_name,
                                                                        account_name=self.account_name,
                                                                        object_replication_policy_id=self.object_replication_policy_id)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMObjectReplicationPolicy()


if __name__ == '__main__':
    main()
