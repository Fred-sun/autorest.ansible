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
module: azure_rm_fileshare_info
version_added: '2.9'
short_description: Get FileShare info.
description:
  - Get info of FileShare.
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
        Optional. Specified maximum number of shares that can be included in the
        list.
    type: str
  filter:
    description:
      - >-
        Optional. When specified, only share names starting with the filter will
        be listed.
    type: str
  expand:
    description:
      - 'Optional, used to expand the properties within share''s properties.'
    required: true
    type: constant
  share_name:
    description:
      - >-
        The name of the file share within the specified storage account. File
        share names must be between 3 and 63 characters in length and use
        numbers, lower-case letters and dash (-) only. Every dash (-) character
        must be immediately preceded and followed by a letter or number.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: ListDeletedShares
      azure_rm_fileshare_info: 
        account_name: sto1590
        resource_group_name: res9290
        

    - name: ListShares
      azure_rm_fileshare_info: 
        account_name: sto1590
        resource_group_name: res9290
        

    - name: GetShareStats
      azure_rm_fileshare_info: 
        account_name: sto6217
        resource_group_name: res9871
        share_name: share1634
        

    - name: GetShares
      azure_rm_fileshare_info: 
        account_name: sto6217
        resource_group_name: res9871
        share_name: share1634
        

'''

RETURN = '''
file_shares:
  description: >-
    A list of dict results where the key is the name of the FileShare and the
    values are the facts for that FileShare.
  returned: always
  type: complex
  contains:
    value:
      description:
        - List of file shares returned.
      returned: always
      type: list
      sample: null
      contains:
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
              The maximum size of the share, in gigabytes. Must be greater than
              0, and less than or equal to 5TB (5120). For Large File Shares,
              the maximum size is 102400.
          returned: always
          type: integer
          sample: null
        enabled_protocols:
          description:
            - >-
              The authentication protocol that is used for the file share. Can
              only be specified when creating a share.
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
              TransactionOptimized (default), Hot, and Cool. FileStorage account
              can choose Premium.
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
              The approximate size of the data stored on the share. Note that
              this value may not include all recently created or recently
              resized files.
          returned: always
          type: integer
          sample: null
    next_link:
      description:
        - >-
          Request URL that can be used to query next page of shares. Returned
          when total number of requested shares exceed maximum page size.
      returned: always
      type: str
      sample: null
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
          The maximum size of the share, in gigabytes. Must be greater than 0,
          and less than or equal to 5TB (5120). For Large File Shares, the
          maximum size is 102400.
      returned: always
      type: integer
      sample: null
    enabled_protocols:
      description:
        - >-
          The authentication protocol that is used for the file share. Can only
          be specified when creating a share.
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
          The approximate size of the data stored on the share. Note that this
          value may not include all recently created or recently resized files.
      returned: always
      type: integer
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


class AzureRMFileShareInfo(AzureRMModuleBase):
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
            expand=dict(
                type='constant',
                required=True
            ),
            share_name=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.account_name = None
        self.maxpagesize = None
        self.filter = None
        self.expand = None
        self.share_name = None

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
        super(AzureRMFileShareInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(StorageManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2019-06-01')

        if (self.resource_group_name is not None and
            self.account_name is not None and
            self.share_name is not None):
            self.results['file_shares'] = self.format_item(self.get())
        elif (self.resource_group_name is not None and
              self.account_name is not None):
            self.results['file_shares'] = self.format_item(self.list())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.file_shares.get(resource_group_name=self.resource_group_name,
                                                        account_name=self.account_name,
                                                        share_name=self.share_name,
                                                        expand=self.expand)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.file_shares.list(resource_group_name=self.resource_group_name,
                                                         account_name=self.account_name,
                                                         maxpagesize=self.maxpagesize,
                                                         filter=self.filter,
                                                         expand=self.expand)
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
    AzureRMFileShareInfo()


if __name__ == '__main__':
    main()
