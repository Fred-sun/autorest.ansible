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
module: azure_rm_blobcontainer
version_added: '2.9'
short_description: Manage Azure BlobContainer instance.
description:
  - 'Create, update and delete instance of Azure BlobContainer.'
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
  container_name:
    description:
      - >-
        The name of the blob container within the specified storage account.
        Blob container names must be between 3 and 63 characters in length and
        use numbers, lower-case letters and dash (-) only. Every dash (-)
        character must be immediately preceded and followed by a letter or
        number.
    required: true
    type: str
  default_encryption_scope:
    description:
      - Default the container to use specified encryption scope for all writes.
    type: str
  deny_encryption_scope_override:
    description:
      - Block override of encryption scope from the container default.
    type: bool
  public_access:
    description:
      - >-
        Specifies whether data in the container may be accessed publicly and the
        level of access.
    type: sealed-choice
  metadata:
    description:
      - A name-value pair to associate with the container as metadata.
    type: dictionary
  state:
    description:
      - Assert the state of the BlobContainer.
      - >-
        Use C(present) to create or update an BlobContainer and C(absent) to
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
    - name: PutContainerWithDefaultEncryptionScope
      azure_rm_blobcontainer: 
        account_name: sto328
        container_name: container6185
        resource_group_name: res3376
        

    - name: PutContainers
      azure_rm_blobcontainer: 
        account_name: sto328
        container_name: container6185
        resource_group_name: res3376
        

    - name: UpdateContainers
      azure_rm_blobcontainer: 
        account_name: sto328
        container_name: container6185
        resource_group_name: res3376
        

    - name: DeleteContainers
      azure_rm_blobcontainer: 
        account_name: sto4506
        container_name: container9689
        resource_group_name: res4079
        

'''

RETURN = '''
etag:
  description:
    - Resource Etag.
  returned: always
  type: str
  sample: null
version:
  description:
    - The version of the deleted blob container.
  returned: always
  type: str
  sample: null
deleted:
  description:
    - Indicates whether the blob container was deleted.
  returned: always
  type: bool
  sample: null
deleted_time:
  description:
    - Blob container deletion time.
  returned: always
  type: str
  sample: null
remaining_retention_days:
  description:
    - Remaining retention days for soft deleted blob container.
  returned: always
  type: integer
  sample: null
default_encryption_scope:
  description:
    - Default the container to use specified encryption scope for all writes.
  returned: always
  type: str
  sample: null
deny_encryption_scope_override:
  description:
    - Block override of encryption scope from the container default.
  returned: always
  type: bool
  sample: null
public_access:
  description:
    - >-
      Specifies whether data in the container may be accessed publicly and the
      level of access.
  returned: always
  type: sealed-choice
  sample: null
last_modified_time:
  description:
    - Returns the date and time the container was last modified.
  returned: always
  type: str
  sample: null
lease_status:
  description:
    - The lease status of the container.
  returned: always
  type: str
  sample: null
lease_state:
  description:
    - Lease state of the container.
  returned: always
  type: str
  sample: null
lease_duration:
  description:
    - >-
      Specifies whether the lease on a container is of infinite or fixed
      duration, only when the container is leased.
  returned: always
  type: str
  sample: null
metadata:
  description:
    - A name-value pair to associate with the container as metadata.
  returned: always
  type: dictionary
  sample: null
immutability_policy:
  description:
    - The ImmutabilityPolicy property of the container.
  returned: always
  type: dict
  sample: null
  contains:
    etag:
      description:
        - ImmutabilityPolicy Etag.
      returned: always
      type: str
      sample: null
    update_history:
      description:
        - The ImmutabilityPolicy update history of the blob container.
      returned: always
      type: list
      sample: null
      contains:
        update:
          description:
            - >-
              The ImmutabilityPolicy update type of a blob container, possible
              values include: put, lock and extend.
          returned: always
          type: str
          sample: null
        immutability_period_since_creation_in_days:
          description:
            - >-
              The immutability period for the blobs in the container since the
              policy creation, in days.
          returned: always
          type: integer
          sample: null
        timestamp:
          description:
            - Returns the date and time the ImmutabilityPolicy was updated.
          returned: always
          type: str
          sample: null
        object_identifier:
          description:
            - >-
              Returns the Object ID of the user who updated the
              ImmutabilityPolicy.
          returned: always
          type: str
          sample: null
        tenant_id:
          description:
            - >-
              Returns the Tenant ID that issued the token for the user who
              updated the ImmutabilityPolicy.
          returned: always
          type: str
          sample: null
        upn:
          description:
            - >-
              Returns the User Principal Name of the user who updated the
              ImmutabilityPolicy.
          returned: always
          type: str
          sample: null
    immutability_period_since_creation_in_days:
      description:
        - >-
          The immutability period for the blobs in the container since the
          policy creation, in days.
      returned: always
      type: integer
      sample: null
    state:
      description:
        - >-
          The ImmutabilityPolicy state of a blob container, possible values
          include: Locked and Unlocked.
      returned: always
      type: str
      sample: null
    allow_protected_append_writes:
      description:
        - >-
          This property can only be changed for unlocked time-based retention
          policies. When enabled, new blocks can be written to an append blob
          while maintaining immutability protection and compliance. Only new
          blocks can be added and any existing blocks cannot be modified or
          deleted. This property cannot be changed with ExtendImmutabilityPolicy
          API
      returned: always
      type: bool
      sample: null
legal_hold:
  description:
    - The LegalHold property of the container.
  returned: always
  type: dict
  sample: null
  contains:
    has_legal_hold:
      description:
        - >-
          The hasLegalHold public property is set to true by SRP if there are at
          least one existing tag. The hasLegalHold public property is set to
          false by SRP if all existing legal hold tags are cleared out. There
          can be a maximum of 1000 blob containers with hasLegalHold=true for a
          given account.
      returned: always
      type: bool
      sample: null
    tags:
      description:
        - The list of LegalHold tags of a blob container.
      returned: always
      type: list
      sample: null
      contains:
        tag:
          description:
            - The tag value.
          returned: always
          type: str
          sample: null
        timestamp:
          description:
            - Returns the date and time the tag was added.
          returned: always
          type: str
          sample: null
        object_identifier:
          description:
            - Returns the Object ID of the user who added the tag.
          returned: always
          type: str
          sample: null
        tenant_id:
          description:
            - >-
              Returns the Tenant ID that issued the token for the user who added
              the tag.
          returned: always
          type: str
          sample: null
        upn:
          description:
            - Returns the User Principal Name of the user who added the tag.
          returned: always
          type: str
          sample: null
has_legal_hold:
  description:
    - >-
      The hasLegalHold public property is set to true by SRP if there are at
      least one existing tag. The hasLegalHold public property is set to false
      by SRP if all existing legal hold tags are cleared out. There can be a
      maximum of 1000 blob containers with hasLegalHold=true for a given
      account.
  returned: always
  type: bool
  sample: null
has_immutability_policy:
  description:
    - >-
      The hasImmutabilityPolicy public property is set to true by SRP if
      ImmutabilityPolicy has been created for this container. The
      hasImmutabilityPolicy public property is set to false by SRP if
      ImmutabilityPolicy has not been created for this container.
  returned: always
  type: bool
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


class AzureRMBlobContainer(AzureRMModuleBaseExt):
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
            container_name=dict(
                type='str',
                required=True
            ),
            default_encryption_scope=dict(
                type='str',
                disposition='/default_encryption_scope'
            ),
            deny_encryption_scope_override=dict(
                type='bool',
                disposition='/deny_encryption_scope_override'
            ),
            public_access=dict(
                type='sealed-choice',
                disposition='/public_access'
            ),
            metadata=dict(
                type='dictionary',
                disposition='/metadata'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group_name = None
        self.account_name = None
        self.container_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMBlobContainer, self).__init__(derived_arg_spec=self.module_arg_spec,
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
            if self.to_do == Actions.Create:
                response = self.mgmt_client.blob_containers.create(resource_group_name=self.resource_group_name,
                                                                   account_name=self.account_name,
                                                                   container_name=self.container_name,
                                                                   blob_container=self.body)
            else:
                response = self.mgmt_client.blob_containers.update(resource_group_name=self.resource_group_name,
                                                                   account_name=self.account_name,
                                                                   container_name=self.container_name,
                                                                   blob_container=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the BlobContainer instance.')
            self.fail('Error creating the BlobContainer instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.blob_containers.delete(resource_group_name=self.resource_group_name,
                                                               account_name=self.account_name,
                                                               container_name=self.container_name)
        except CloudError as e:
            self.log('Error attempting to delete the BlobContainer instance.')
            self.fail('Error deleting the BlobContainer instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.blob_containers.get(resource_group_name=self.resource_group_name,
                                                            account_name=self.account_name,
                                                            container_name=self.container_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMBlobContainer()


if __name__ == '__main__':
    main()
