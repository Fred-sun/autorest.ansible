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
module: azure_rm_diskencryptionset_info
version_added: '2.9'
short_description: Get DiskEncryptionSet info.
description:
  - Get info of DiskEncryptionSet.
options:
  resource_group_name:
    description:
      - The name of the resource group.
    type: str
  disk_encryption_set_name:
    description:
      - >-
        The name of the disk encryption set that is being created. The name
        can't be changed after the disk encryption set is created. Supported
        characters for the name are a-z, A-Z, 0-9 and _. The maximum name length
        is 80 characters.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: Get information about a disk encryption set.
      azure_rm_diskencryptionset_info: 
        disk_encryption_set_name: myDiskEncryptionSet
        resource_group_name: myResourceGroup
        

    - name: List all disk encryption sets in a resource group.
      azure_rm_diskencryptionset_info: 
        resource_group_name: myResourceGroup
        

    - name: List all disk encryption sets in a subscription.
      azure_rm_diskencryptionset_info: 
        {}
        

'''

RETURN = '''
disk_encryption_sets:
  description: >-
    A list of dict results where the key is the name of the DiskEncryptionSet
    and the values are the facts for that DiskEncryptionSet.
  returned: always
  type: complex
  contains:
    id:
      description:
        - Resource Id
      returned: always
      type: str
      sample: null
    name:
      description:
        - Resource name
      returned: always
      type: str
      sample: null
    type:
      description:
        - Resource type
      returned: always
      type: str
      sample: null
    location:
      description:
        - Resource location
      returned: always
      type: str
      sample: null
    tags:
      description:
        - Resource tags
      returned: always
      type: dictionary
      sample: null
    encryption_type:
      description:
        - The type of key used to encrypt the data of the disk.
      returned: always
      type: choice
      sample: null
    previous_keys:
      description:
        - >-
          A readonly collection of key vault keys previously used by this disk
          encryption set while a key rotation is in progress. It will be empty
          if there is no ongoing key rotation.
      returned: always
      type: list
      sample: null
      contains:
        key_url:
          description:
            - Url pointing to a key or secret in KeyVault
          returned: always
          type: str
          sample: null
        id:
          description:
            - Resource Id
          returned: always
          type: str
          sample: null
    provisioning_state:
      description:
        - The disk encryption set provisioning state.
      returned: always
      type: str
      sample: null
    key_url:
      description:
        - Url pointing to a key or secret in KeyVault
      returned: always
      type: str
      sample: null
    id_properties_active_key_source_vault_id:
      description:
        - Resource Id
      returned: always
      type: str
      sample: null
    type_identity_type:
      description:
        - >-
          The type of Managed Identity used by the DiskEncryptionSet. Only
          SystemAssigned is supported.
      returned: always
      type: choice
      sample: null
    principal_id:
      description:
        - >-
          The object id of the Managed Identity Resource. This will be sent to
          the RP from ARM via the x-ms-identity-principal-id header in the PUT
          request if the resource has a systemAssigned(implicit) identity
      returned: always
      type: str
      sample: null
    tenant_id:
      description:
        - >-
          The tenant id of the Managed Identity Resource. This will be sent to
          the RP from ARM via the x-ms-client-tenant-id header in the PUT
          request if the resource has a systemAssigned(implicit) identity
      returned: always
      type: str
      sample: null
    value:
      description:
        - A list of disk encryption sets.
      returned: always
      type: list
      sample: null
      contains:
        encryption_type:
          description:
            - The type of key used to encrypt the data of the disk.
          returned: always
          type: choice
          sample: null
        previous_keys:
          description:
            - >-
              A readonly collection of key vault keys previously used by this
              disk encryption set while a key rotation is in progress. It will
              be empty if there is no ongoing key rotation.
          returned: always
          type: list
          sample: null
          contains:
            key_url:
              description:
                - Url pointing to a key or secret in KeyVault
              returned: always
              type: str
              sample: null
            id:
              description:
                - Resource Id
              returned: always
              type: str
              sample: null
        provisioning_state:
          description:
            - The disk encryption set provisioning state.
          returned: always
          type: str
          sample: null
        key_url:
          description:
            - Url pointing to a key or secret in KeyVault
          returned: always
          type: str
          sample: null
        id_properties_active_key_source_vault_id:
          description:
            - Resource Id
          returned: always
          type: str
          sample: null
        type_identity_type:
          description:
            - >-
              The type of Managed Identity used by the DiskEncryptionSet. Only
              SystemAssigned is supported.
          returned: always
          type: choice
          sample: null
        principal_id:
          description:
            - >-
              The object id of the Managed Identity Resource. This will be sent
              to the RP from ARM via the x-ms-identity-principal-id header in
              the PUT request if the resource has a systemAssigned(implicit)
              identity
          returned: always
          type: str
          sample: null
        tenant_id:
          description:
            - >-
              The tenant id of the Managed Identity Resource. This will be sent
              to the RP from ARM via the x-ms-client-tenant-id header in the PUT
              request if the resource has a systemAssigned(implicit) identity
          returned: always
          type: str
          sample: null
    next_link:
      description:
        - >-
          The uri to fetch the next page of disk encryption sets. Call
          ListNext() with this to fetch the next page of disk encryption sets.
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
    from azure.mgmt.compute import ComputeManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMDiskEncryptionSetInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str'
            ),
            disk_encryption_set_name=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.disk_encryption_set_name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2020-05-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMDiskEncryptionSetInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(ComputeManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-05-01')

        if (self.resource_group_name is not None and
            self.disk_encryption_set_name is not None):
            self.results['disk_encryption_sets'] = self.format_item(self.get())
        elif (self.resource_group_name is not None):
            self.results['disk_encryption_sets'] = self.format_item(self.listbyresourcegroup())
        else:
            self.results['disk_encryption_sets'] = self.format_item(self.list())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.disk_encryption_sets.get(resource_group_name=self.resource_group_name,
                                                                 disk_encryption_set_name=self.disk_encryption_set_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbyresourcegroup(self):
        response = None

        try:
            response = self.mgmt_client.disk_encryption_sets.list_by_resource_group(resource_group_name=self.resource_group_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.disk_encryption_sets.list()
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
    AzureRMDiskEncryptionSetInfo()


if __name__ == '__main__':
    main()
