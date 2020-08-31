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
module: azure_rm_blobcontainer_info
version_added: '2.9'
short_description: Get BlobContainer info.
description:
  - Get info of BlobContainer.
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
  maxpagesize:
    description:
      - >-
        Optional. Specified maximum number of containers that can be included in
        the list.
    type: str
  filter:
    description:
      - >-
        Optional. When specified, only container names starting with the filter
        will be listed.
    type: str
  include:
    description:
      - >-
        Optional, used to include the properties for soft deleted blob
        containers.
    type: choice
  container_name:
    description:
      - >-
        The name of the blob container within the specified storage account.
        Blob container names must be between 3 and 63 characters in length and
        use numbers, lower-case letters and dash (-) only. Every dash (-)
        character must be immediately preceded and followed by a letter or
        number.
    type: str
  immutability_policy_name:
    description:
      - >-
        The name of the blob container immutabilityPolicy within the specified
        storage account. ImmutabilityPolicy Name must be 'default'
    type: constant
  if_match:
    description:
      - >-
        The entity state (ETag) version of the immutability policy to update. A
        value of "*" can be used to apply the operation only if the immutability
        policy already exists. If omitted, this operation will always be
        applied.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: ListContainers
      azure_rm_blobcontainer_info: 
        account_name: sto1590
        resource_group_name: res9290
        

    - name: ListDeletedContainers
      azure_rm_blobcontainer_info: 
        account_name: sto1590
        resource_group_name: res9290
        

    - name: GetContainers
      azure_rm_blobcontainer_info: 
        account_name: sto6217
        container_name: container1634
        resource_group_name: res9871
        

    - name: GetImmutabilityPolicy
      azure_rm_blobcontainer_info: 
        account_name: sto9177
        container_name: container3489
        resource_group_name: res5221
        

'''

RETURN = '''
blob_containers:
  description: >-
    A list of dict results where the key is the name of the BlobContainer and
    the values are the facts for that BlobContainer.
  returned: always
  type: complex
  contains:
    value:
      description:
        - List of blobs containers returned.
      returned: always
      type: list
      sample: null
      contains:
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
            - >-
              Default the container to use specified encryption scope for all
              writes.
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
              Specifies whether data in the container may be accessed publicly
              and the level of access.
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
          type: choice
          sample: null
        lease_state:
          description:
            - Lease state of the container.
          returned: always
          type: choice
          sample: null
        lease_duration:
          description:
            - >-
              Specifies whether the lease on a container is of infinite or fixed
              duration, only when the container is leased.
          returned: always
          type: choice
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
                      The ImmutabilityPolicy update type of a blob container,
                      possible values include: put, lock and extend.
                  returned: always
                  type: choice
                  sample: null
                immutability_period_since_creation_in_days:
                  description:
                    - >-
                      The immutability period for the blobs in the container
                      since the policy creation, in days.
                  returned: always
                  type: integer
                  sample: null
                timestamp:
                  description:
                    - >-
                      Returns the date and time the ImmutabilityPolicy was
                      updated.
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
                      Returns the Tenant ID that issued the token for the user
                      who updated the ImmutabilityPolicy.
                  returned: always
                  type: str
                  sample: null
                upn:
                  description:
                    - >-
                      Returns the User Principal Name of the user who updated
                      the ImmutabilityPolicy.
                  returned: always
                  type: str
                  sample: null
            immutability_period_since_creation_in_days:
              description:
                - >-
                  The immutability period for the blobs in the container since
                  the policy creation, in days.
              returned: always
              type: integer
              sample: null
            state:
              description:
                - >-
                  The ImmutabilityPolicy state of a blob container, possible
                  values include: Locked and Unlocked.
              returned: always
              type: choice
              sample: null
            allow_protected_append_writes:
              description:
                - >-
                  This property can only be changed for unlocked time-based
                  retention policies. When enabled, new blocks can be written to
                  an append blob while maintaining immutability protection and
                  compliance. Only new blocks can be added and any existing
                  blocks cannot be modified or deleted. This property cannot be
                  changed with ExtendImmutabilityPolicy API
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
                  The hasLegalHold public property is set to true by SRP if
                  there are at least one existing tag. The hasLegalHold public
                  property is set to false by SRP if all existing legal hold
                  tags are cleared out. There can be a maximum of 1000 blob
                  containers with hasLegalHold=true for a given account.
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
                      Returns the Tenant ID that issued the token for the user
                      who added the tag.
                  returned: always
                  type: str
                  sample: null
                upn:
                  description:
                    - >-
                      Returns the User Principal Name of the user who added the
                      tag.
                  returned: always
                  type: str
                  sample: null
        has_legal_hold:
          description:
            - >-
              The hasLegalHold public property is set to true by SRP if there
              are at least one existing tag. The hasLegalHold public property is
              set to false by SRP if all existing legal hold tags are cleared
              out. There can be a maximum of 1000 blob containers with
              hasLegalHold=true for a given account.
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
    next_link:
      description:
        - >-
          Request URL that can be used to query next page of containers.
          Returned when total number of requested containers exceed maximum page
          size.
      returned: always
      type: str
      sample: null
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
        - >-
          Default the container to use specified encryption scope for all
          writes.
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
          Specifies whether data in the container may be accessed publicly and
          the level of access.
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
      type: choice
      sample: null
    lease_state:
      description:
        - Lease state of the container.
      returned: always
      type: choice
      sample: null
    lease_duration:
      description:
        - >-
          Specifies whether the lease on a container is of infinite or fixed
          duration, only when the container is leased.
      returned: always
      type: choice
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
                  The ImmutabilityPolicy update type of a blob container,
                  possible values include: put, lock and extend.
              returned: always
              type: choice
              sample: null
            immutability_period_since_creation_in_days:
              description:
                - >-
                  The immutability period for the blobs in the container since
                  the policy creation, in days.
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
          type: choice
          sample: null
        allow_protected_append_writes:
          description:
            - >-
              This property can only be changed for unlocked time-based
              retention policies. When enabled, new blocks can be written to an
              append blob while maintaining immutability protection and
              compliance. Only new blocks can be added and any existing blocks
              cannot be modified or deleted. This property cannot be changed
              with ExtendImmutabilityPolicy API
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
              The hasLegalHold public property is set to true by SRP if there
              are at least one existing tag. The hasLegalHold public property is
              set to false by SRP if all existing legal hold tags are cleared
              out. There can be a maximum of 1000 blob containers with
              hasLegalHold=true for a given account.
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
                  Returns the Tenant ID that issued the token for the user who
                  added the tag.
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
          least one existing tag. The hasLegalHold public property is set to
          false by SRP if all existing legal hold tags are cleared out. There
          can be a maximum of 1000 blob containers with hasLegalHold=true for a
          given account.
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
      type: choice
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


class AzureRMBlobContainerInfo(AzureRMModuleBase):
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
            maxpagesize=dict(
                type='str'
            ),
            filter=dict(
                type='str'
            ),
            include=dict(
                type='choice'
            ),
            container_name=dict(
                type='str'
            ),
            immutability_policy_name=dict(
                type='constant'
            ),
            if_match=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.account_name = None
        self.maxpagesize = None
        self.filter = None
        self.include = None
        self.container_name = None
        self.immutability_policy_name = None
        self.if_match = None

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
        super(AzureRMBlobContainerInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(StorageManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2019-06-01')

        if (self.resource_group_name is not None and
            self.account_name is not None and
            self.container_name is not None and
            self.immutability_policy_name is not None):
            self.results['blob_containers'] = self.format_item(self.getimmutabilitypolicy())
        elif (self.resource_group_name is not None and
              self.account_name is not None and
              self.container_name is not None):
            self.results['blob_containers'] = self.format_item(self.get())
        elif (self.resource_group_name is not None and
              self.account_name is not None):
            self.results['blob_containers'] = self.format_item(self.list())
        return self.results

    def getimmutabilitypolicy(self):
        response = None

        try:
            response = self.mgmt_client.blob_containers.get_immutability_policy(resource_group_name=self.resource_group_name,
                                                                                account_name=self.account_name,
                                                                                container_name=self.container_name,
                                                                                immutability_policy_name=self.immutability_policy_name,
                                                                                if_match=self.if_match)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def get(self):
        response = None

        try:
            response = self.mgmt_client.blob_containers.get(resource_group_name=self.resource_group_name,
                                                            account_name=self.account_name,
                                                            container_name=self.container_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.blob_containers.list(resource_group_name=self.resource_group_name,
                                                             account_name=self.account_name,
                                                             maxpagesize=self.maxpagesize,
                                                             filter=self.filter,
                                                             include=self.include)
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
    AzureRMBlobContainerInfo()


if __name__ == '__main__':
    main()
