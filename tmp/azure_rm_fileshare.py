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
module: azure_rm_fileshare
version_added: '2.9'
short_description: Manage Azure FileShare instance.
description:
  - 'Create, update and delete instance of Azure FileShare.'
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
  share_name:
    description:
      - >-
        The name of the file share within the specified storage account. File
        share names must be between 3 and 63 characters in length and use
        numbers, lower-case letters and dash (-) only. Every dash (-) character
        must be immediately preceded and followed by a letter or number.
    required: true
    type: str
  metadata:
    description:
      - A name-value pair to associate with the share as metadata.
    type: dictionary
  share_quota:
    description:
      - >-
        The maximum size of the share, in gigabytes. Must be greater than 0, and
        less than or equal to 5TB (5120). For Large File Shares, the maximum
        size is 102400.
    type: integer
  enabled_protocols:
    description:
      - >-
        The authentication protocol that is used for the file share. Can only be
        specified when creating a share.
    type: str
    choices:
      - SMB
      - NFS
  root_squash:
    description:
      - The property is for NFS share only. The default is NoRootSquash.
    type: str
    choices:
      - NoRootSquash
      - RootSquash
      - AllSquash
  access_tier:
    description:
      - >-
        Access tier for specific share. GpV2 account can choose between
        TransactionOptimized (default), Hot, and Cool. FileStorage account can
        choose Premium.
    type: str
    choices:
      - TransactionOptimized
      - Hot
      - Cool
      - Premium
  expand:
    description:
      - 'Optional, used to expand the properties within share''s properties.'
    type: constant
  state:
    description:
      - Assert the state of the FileShare.
      - >-
        Use C(present) to create or update an FileShare and C(absent) to delete
        it.
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
    - name: Create NFS Shares
      azure_rm_fileshare: 
        account_name: sto666
        resource_group_name: res346
        share_name: share1235
        

    - name: PutShares
      azure_rm_fileshare: 
        account_name: sto328
        resource_group_name: res3376
        share_name: share6185
        

    - name: PutShares with Access Tier
      azure_rm_fileshare: 
        account_name: sto666
        resource_group_name: res346
        share_name: share1235
        

    - name: UpdateShares
      azure_rm_fileshare: 
        account_name: sto328
        resource_group_name: res3376
        share_name: share6185
        

    - name: DeleteShares
      azure_rm_fileshare: 
        account_name: sto4506
        resource_group_name: res4079
        share_name: share9689
        

'''

RETURN = '''
etag:
  description:
    - Resource Etag.
  returned: always
  type: str
  sample: null
last_modified_time:
  description:
    - Returns the date and time the share was last modified.
  returned: always
  type: str
  sample: null
metadata:
  description:
    - A name-value pair to associate with the share as metadata.
  returned: always
  type: dictionary
  sample: null
share_quota:
  description:
    - >-
      The maximum size of the share, in gigabytes. Must be greater than 0, and
      less than or equal to 5TB (5120). For Large File Shares, the maximum size
      is 102400.
  returned: always
  type: integer
  sample: null
enabled_protocols:
  description:
    - >-
      The authentication protocol that is used for the file share. Can only be
      specified when creating a share.
  returned: always
  type: str
  sample: null
root_squash:
  description:
    - The property is for NFS share only. The default is NoRootSquash.
  returned: always
  type: str
  sample: null
version:
  description:
    - The version of the share.
  returned: always
  type: str
  sample: null
deleted:
  description:
    - Indicates whether the share was deleted.
  returned: always
  type: bool
  sample: null
deleted_time:
  description:
    - The deleted time if the share was deleted.
  returned: always
  type: str
  sample: null
remaining_retention_days:
  description:
    - Remaining retention days for share that was soft deleted.
  returned: always
  type: integer
  sample: null
access_tier:
  description:
    - >-
      Access tier for specific share. GpV2 account can choose between
      TransactionOptimized (default), Hot, and Cool. FileStorage account can
      choose Premium.
  returned: always
  type: str
  sample: null
access_tier_change_time:
  description:
    - Indicates the last modification time for share access tier.
  returned: always
  type: str
  sample: null
access_tier_status:
  description:
    - Indicates if there is a pending transition for access tier.
  returned: always
  type: str
  sample: null
share_usage_bytes:
  description:
    - >-
      The approximate size of the data stored on the share. Note that this value
      may not include all recently created or recently resized files.
  returned: always
  type: integer
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


class AzureRMFileShare(AzureRMModuleBaseExt):
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
            share_name=dict(
                type='str',
                required=True
            ),
            metadata=dict(
                type='dictionary',
                disposition='/metadata'
            ),
            share_quota=dict(
                type='integer',
                disposition='/share_quota'
            ),
            enabled_protocols=dict(
                type='str',
                disposition='/enabled_protocols',
                choices=['SMB',
                         'NFS']
            ),
            root_squash=dict(
                type='str',
                disposition='/root_squash',
                choices=['NoRootSquash',
                         'RootSquash',
                         'AllSquash']
            ),
            access_tier=dict(
                type='str',
                disposition='/access_tier',
                choices=['TransactionOptimized',
                         'Hot',
                         'Cool',
                         'Premium']
            ),
            expand=dict(
                type='constant'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group_name = None
        self.account_name = None
        self.share_name = None
        self.expand = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMFileShare, self).__init__(derived_arg_spec=self.module_arg_spec,
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
                response = self.mgmt_client.file_shares.create(resource_group_name=self.resource_group_name,
                                                               account_name=self.account_name,
                                                               share_name=self.share_name,
                                                               file_share=self.body)
            else:
                response = self.mgmt_client.file_shares.update(resource_group_name=self.resource_group_name,
                                                               account_name=self.account_name,
                                                               share_name=self.share_name,
                                                               file_share=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the FileShare instance.')
            self.fail('Error creating the FileShare instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.file_shares.delete(resource_group_name=self.resource_group_name,
                                                           account_name=self.account_name,
                                                           share_name=self.share_name)
        except CloudError as e:
            self.log('Error attempting to delete the FileShare instance.')
            self.fail('Error deleting the FileShare instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.file_shares.get(resource_group_name=self.resource_group_name,
                                                        account_name=self.account_name,
                                                        share_name=self.share_name,
                                                        expand=self.expand)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMFileShare()


if __name__ == '__main__':
    main()
