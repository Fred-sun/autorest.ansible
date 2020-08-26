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
module: azure_rm_diskencryptionset
version_added: '2.9'
short_description: Manage Azure DiskEncryptionSet instance.
description:
  - 'Create, update and delete instance of Azure DiskEncryptionSet.'
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
  location:
    description:
      - Resource location
    type: str
  encryption_type:
    description:
      - The type of key used to encrypt the data of the disk.
    type: choice
  key_url:
    description:
      - Url pointing to a key or secret in KeyVault
    type: str
  id:
    description:
      - Resource Id
    type: str
  type:
    description:
      - >-
        The type of Managed Identity used by the DiskEncryptionSet. Only
        SystemAssigned is supported.
    type: choice
  active_key:
    description:
      - >-
        Key Vault Key Url and vault id of KeK, KeK is optional and when provided
        is used to unwrap the encryptionKey
    type: dict
    suboptions:
      key_url:
        description:
          - Url pointing to a key or secret in KeyVault
        required: true
        type: str
      id:
        description:
          - Resource Id
        type: str
  state:
    description:
      - Assert the state of the DiskEncryptionSet.
      - >-
        Use C(present) to create or update an DiskEncryptionSet and C(absent) to
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


import time
import json
import re
from ansible.module_utils.azure_rm_common_ext import AzureRMModuleBaseExt
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.compute import ComputeManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMDiskEncryptionSet(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str'
            ),
            disk_encryption_set_name=dict(
                type='str'
            ),
            location=dict(
                type='str',
                disposition='/location'
            ),
            encryption_type=dict(
                type='choice',
                disposition='/encryption_type'
            ),
            key_url=dict(
                type='str',
                disposition='/key_url'
            ),
            id=dict(
                type='str',
                disposition='/id'
            ),
            type=dict(
                type='choice',
                disposition='/type'
            ),
            active_key=dict(
                type='dict',
                disposition='/active_key',
                options=dict(
                    key_url=dict(
                        type='str',
                        disposition='key_url',
                        required=True
                    ),
                    id=dict(
                        type='str',
                        disposition='id'
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
        self.disk_encryption_set_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMDiskEncryptionSet, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(ComputeManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-05-01')

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
            if self.to_do == Actions.Create:
                response = self.mgmt_client.disk_encryption_sets.create(resource_group_name=self.resource_group_name,
                                                                        disk_encryption_set_name=self.disk_encryption_set_name,
                                                                        disk_encryption_set=self.body)
            else:
                response = self.mgmt_client.disk_encryption_sets.update(resource_group_name=self.resource_group_name,
                                                                        disk_encryption_set_name=self.disk_encryption_set_name,
                                                                        disk_encryption_set=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the DiskEncryptionSet instance.')
            self.fail('Error creating the DiskEncryptionSet instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.disk_encryption_sets.delete(resource_group_name=self.resource_group_name,
                                                                    disk_encryption_set_name=self.disk_encryption_set_name)
        except CloudError as e:
            self.log('Error attempting to delete the DiskEncryptionSet instance.')
            self.fail('Error deleting the DiskEncryptionSet instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        found = False
        try:
            response = self.mgmt_client.disk_encryption_sets.get(resource_group_name=self.resource_group_name,
                                                                 disk_encryption_set_name=self.disk_encryption_set_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMDiskEncryptionSet()


if __name__ == '__main__':
    main()
