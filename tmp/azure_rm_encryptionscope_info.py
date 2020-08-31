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
module: azure_rm_encryptionscope_info
version_added: '2.9'
short_description: Get EncryptionScope info.
description:
  - Get info of EncryptionScope.
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
  encryption_scope_name:
    description:
      - >-
        The name of the encryption scope within the specified storage account.
        Encryption scope names must be between 3 and 63 characters in length and
        use numbers, lower-case letters and dash (-) only. Every dash (-)
        character must be immediately preceded and followed by a letter or
        number.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: StorageAccountGetEncryptionScope
      azure_rm_encryptionscope_info: 
        account_name: '{storage-account-name}'
        encryption_scope_name: '{encryption-scope-name}'
        resource_group_name: resource-group-name
        

    - name: StorageAccountEncryptionScopeList
      azure_rm_encryptionscope_info: 
        account_name: '{storage-account-name}'
        resource_group_name: resource-group-name
        

'''

RETURN = '''
encryption_scopes:
  description: >-
    A list of dict results where the key is the name of the EncryptionScope and
    the values are the facts for that EncryptionScope.
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
    source:
      description:
        - >-
          The provider for the encryption scope. Possible values
          (case-insensitive):  Microsoft.Storage, Microsoft.KeyVault.
      returned: always
      type: str
      sample: null
    state:
      description:
        - >-
          The state of the encryption scope. Possible values
          (case-insensitive):  Enabled, Disabled.
      returned: always
      type: str
      sample: null
    creation_time:
      description:
        - Gets the creation date and time of the encryption scope in UTC.
      returned: always
      type: str
      sample: null
    last_modified_time:
      description:
        - >-
          Gets the last modification date and time of the encryption scope in
          UTC.
      returned: always
      type: str
      sample: null
    key_uri:
      description:
        - >-
          The object identifier for a key vault key object. When applied, the
          encryption scope will use the key referenced by the identifier to
          enable customer-managed key support on this encryption scope.
      returned: always
      type: str
      sample: null
    value:
      description:
        - List of encryption scopes requested.
      returned: always
      type: list
      sample: null
      contains:
        source:
          description:
            - >-
              The provider for the encryption scope. Possible values
              (case-insensitive):  Microsoft.Storage, Microsoft.KeyVault.
          returned: always
          type: str
          sample: null
        state:
          description:
            - >-
              The state of the encryption scope. Possible values
              (case-insensitive):  Enabled, Disabled.
          returned: always
          type: str
          sample: null
        creation_time:
          description:
            - Gets the creation date and time of the encryption scope in UTC.
          returned: always
          type: str
          sample: null
        last_modified_time:
          description:
            - >-
              Gets the last modification date and time of the encryption scope
              in UTC.
          returned: always
          type: str
          sample: null
        key_uri:
          description:
            - >-
              The object identifier for a key vault key object. When applied,
              the encryption scope will use the key referenced by the identifier
              to enable customer-managed key support on this encryption scope.
          returned: always
          type: str
          sample: null
    next_link:
      description:
        - >-
          Request URL that can be used to query next page of encryption scopes.
          Returned when total number of requested encryption scopes exceeds the
          maximum page size.
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


class AzureRMEncryptionScopeInfo(AzureRMModuleBase):
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
            encryption_scope_name=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.account_name = None
        self.encryption_scope_name = None

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
        super(AzureRMEncryptionScopeInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(StorageManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2019-06-01')

        if (self.resource_group_name is not None and
            self.account_name is not None and
            self.encryption_scope_name is not None):
            self.results['encryption_scopes'] = self.format_item(self.get())
        elif (self.resource_group_name is not None and
              self.account_name is not None):
            self.results['encryption_scopes'] = self.format_item(self.list())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.encryption_scopes.get(resource_group_name=self.resource_group_name,
                                                              account_name=self.account_name,
                                                              encryption_scope_name=self.encryption_scope_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.encryption_scopes.list(resource_group_name=self.resource_group_name,
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
    AzureRMEncryptionScopeInfo()


if __name__ == '__main__':
    main()
