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
module: azure_rm_managementpolicy
version_added: '2.9'
short_description: Manage Azure ManagementPolicy instance.
description:
  - 'Create, update and delete instance of Azure ManagementPolicy.'
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
  rules:
    description:
      - >-
        The Storage Account ManagementPolicies Rules. See more details in:
        https://docs.microsoft.com/en-us/azure/storage/common/storage-lifecycle-managment-concepts.
    type: list
    suboptions:
      enabled:
        description:
          - Rule is enabled if set to true.
        type: bool
      name:
        description:
          - >-
            A rule name can contain any combination of alpha numeric characters.
            Rule name is case-sensitive. It must be unique within a policy.
        required: true
        type: str
      type:
        description:
          - The valid value is Lifecycle
        required: true
        type: str
        choices:
          - Lifecycle
      definition:
        description:
          - An object that defines the Lifecycle rule.
        required: true
        type: dict
        suboptions:
          actions:
            description:
              - An object that defines the action set.
            required: true
            type: dict
            suboptions:
              base_blob:
                description:
                  - The management policy action for base blob
                type: dict
                suboptions:
                  tier_to_cool:
                    description:
                      - >-
                        The function to tier blobs to cool storage. Support
                        blobs currently at Hot tier
                    type: dict
                    suboptions:
                      days_after_modification_greater_than:
                        description:
                          - >-
                            Value indicating the age in days after last
                            modification
                        required: true
                        type: number
                  tier_to_archive:
                    description:
                      - >-
                        The function to tier blobs to archive storage. Support
                        blobs currently at Hot or Cool tier
                    type: dict
                    suboptions:
                      days_after_modification_greater_than:
                        description:
                          - >-
                            Value indicating the age in days after last
                            modification
                        required: true
                        type: number
                  delete:
                    description:
                      - The function to delete the blob
                    type: dict
                    suboptions:
                      days_after_modification_greater_than:
                        description:
                          - >-
                            Value indicating the age in days after last
                            modification
                        required: true
                        type: number
              snapshot:
                description:
                  - The management policy action for snapshot
                type: dict
                suboptions:
                  delete:
                    description:
                      - The function to delete the blob snapshot
                    type: dict
                    suboptions:
                      days_after_creation_greater_than:
                        description:
                          - Value indicating the age in days after creation
                        required: true
                        type: number
          filters:
            description:
              - An object that defines the filter set.
            type: dict
            suboptions:
              prefix_match:
                description:
                  - An array of strings for prefixes to be match.
                type: list
              blob_types:
                description:
                  - >-
                    An array of predefined enum values. Only blockBlob is
                    supported.
                required: true
                type: list
              blob_index_match:
                description:
                  - >-
                    An array of blob index tag based filters, there can be at
                    most 10 tag filters
                type: list
                suboptions:
                  name:
                    description:
                      - >-
                        This is the filter tag name, it can have 1 - 128
                        characters
                    required: true
                    type: str
                  op:
                    description:
                      - >-
                        This is the comparison operator which is used for object
                        comparison and filtering. Only == (equality operator) is
                        currently supported
                    required: true
                    type: str
                  value:
                    description:
                      - >-
                        This is the filter tag value field used for tag based
                        filtering, it can have 0 - 256 characters
                    required: true
                    type: str
  state:
    description:
      - Assert the state of the ManagementPolicy.
      - >-
        Use C(present) to create or update an ManagementPolicy and C(absent) to
        delete it.
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
    - name: StorageAccountSetManagementPolicies
      azure_rm_managementpolicy: 
        account_name: sto9699
        management_policy_name: default
        resource_group_name: res7687
        properties:
          policy:
            rules:
              - name: olcmtest1
                type: Lifecycle
                definition:
                  actions:
                    base_blob:
                      delete:
                        days_after_modification_greater_than: 1000
                      tier_to_archive:
                        days_after_modification_greater_than: 90
                      tier_to_cool:
                        days_after_modification_greater_than: 30
                    snapshot:
                      delete:
                        days_after_creation_greater_than: 30
                  filters:
                    blob_types:
                      - blockBlob
                    prefix_match:
                      - olcmtestcontainer1
                enabled: true
              - name: olcmtest2
                type: Lifecycle
                definition:
                  actions:
                    base_blob:
                      delete:
                        days_after_modification_greater_than: 1000
                      tier_to_archive:
                        days_after_modification_greater_than: 90
                      tier_to_cool:
                        days_after_modification_greater_than: 30
                  filters:
                    blob_index_match:
                      - name: tag1
                        op: '=='
                        value: val1
                      - name: tag2
                        op: '=='
                        value: val2
                    blob_types:
                      - blockBlob
                    prefix_match:
                      - olcmtestcontainer2
                enabled: true
        

    - name: StorageAccountDeleteManagementPolicies
      azure_rm_managementpolicy: 
        account_name: sto2527
        management_policy_name: default
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
          A rule name can contain any combination of alpha numeric characters.
          Rule name is case-sensitive. It must be unique within a policy.
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
                      The function to tier blobs to cool storage. Support blobs
                      currently at Hot tier
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
                  An array of blob index tag based filters, there can be at most
                  10 tag filters
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
                      This is the comparison operator which is used for object
                      comparison and filtering. Only == (equality operator) is
                      currently supported
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


class AzureRMManagementPolicy(AzureRMModuleBaseExt):
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
            ),
            rules=dict(
                type='list',
                disposition='/rules',
                elements='dict',
                options=dict(
                    enabled=dict(
                        type='bool',
                        disposition='enabled'
                    ),
                    name=dict(
                        type='str',
                        disposition='name',
                        required=True
                    ),
                    type=dict(
                        type='str',
                        disposition='type',
                        choices=['Lifecycle'],
                        required=True
                    ),
                    definition=dict(
                        type='dict',
                        disposition='definition',
                        required=True,
                        options=dict(
                            actions=dict(
                                type='dict',
                                disposition='actions',
                                required=True,
                                options=dict(
                                    base_blob=dict(
                                        type='dict',
                                        disposition='base_blob',
                                        options=dict(
                                            tier_to_cool=dict(
                                                type='dict',
                                                disposition='tier_to_cool',
                                                options=dict(
                                                    days_after_modification_greater_than=dict(
                                                        type='number',
                                                        disposition='days_after_modification_greater_than',
                                                        required=True
                                                    )
                                                )
                                            ),
                                            tier_to_archive=dict(
                                                type='dict',
                                                disposition='tier_to_archive',
                                                options=dict(
                                                    days_after_modification_greater_than=dict(
                                                        type='number',
                                                        disposition='days_after_modification_greater_than',
                                                        required=True
                                                    )
                                                )
                                            ),
                                            delete=dict(
                                                type='dict',
                                                disposition='delete',
                                                options=dict(
                                                    days_after_modification_greater_than=dict(
                                                        type='number',
                                                        disposition='days_after_modification_greater_than',
                                                        required=True
                                                    )
                                                )
                                            )
                                        )
                                    ),
                                    snapshot=dict(
                                        type='dict',
                                        disposition='snapshot',
                                        options=dict(
                                            delete=dict(
                                                type='dict',
                                                disposition='delete',
                                                options=dict(
                                                    days_after_creation_greater_than=dict(
                                                        type='number',
                                                        disposition='days_after_creation_greater_than',
                                                        required=True
                                                    )
                                                )
                                            )
                                        )
                                    )
                                )
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
                                    blob_types=dict(
                                        type='list',
                                        disposition='blob_types',
                                        required=True,
                                        elements='str'
                                    ),
                                    blob_index_match=dict(
                                        type='list',
                                        disposition='blob_index_match',
                                        elements='dict',
                                        options=dict(
                                            name=dict(
                                                type='str',
                                                disposition='name',
                                                required=True
                                            ),
                                            op=dict(
                                                type='str',
                                                disposition='op',
                                                required=True
                                            ),
                                            value=dict(
                                                type='str',
                                                disposition='value',
                                                required=True
                                            )
                                        )
                                    )
                                )
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
        self.management_policy_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMManagementPolicy, self).__init__(derived_arg_spec=self.module_arg_spec,
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
            response = self.mgmt_client.management_policies.create_or_update(resource_group_name=self.resource_group_name,
                                                                             account_name=self.account_name,
                                                                             management_policy_name=self.management_policy_name,
                                                                             properties=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the ManagementPolicy instance.')
            self.fail('Error creating the ManagementPolicy instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.management_policies.delete(resource_group_name=self.resource_group_name,
                                                                   account_name=self.account_name,
                                                                   management_policy_name=self.management_policy_name)
        except CloudError as e:
            self.log('Error attempting to delete the ManagementPolicy instance.')
            self.fail('Error deleting the ManagementPolicy instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.management_policies.get(resource_group_name=self.resource_group_name,
                                                                account_name=self.account_name,
                                                                management_policy_name=self.management_policy_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMManagementPolicy()


if __name__ == '__main__':
    main()
