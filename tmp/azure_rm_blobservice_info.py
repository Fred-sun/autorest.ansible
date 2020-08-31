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
module: azure_rm_blobservice_info
version_added: '2.9'
short_description: Get BlobService info.
description:
  - Get info of BlobService.
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
  blob_services_name:
    description:
      - >-
        The name of the blob Service within the specified storage account. Blob
        Service Name must be 'default'
    type: constant
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: ListBlobServices
      azure_rm_blobservice_info: 
        account_name: sto8607
        resource_group_name: res4410
        

    - name: GetBlobServices
      azure_rm_blobservice_info: 
        blob_services_name: default
        account_name: sto8607
        resource_group_name: res4410
        

'''

RETURN = '''
blob_services:
  description: >-
    A list of dict results where the key is the name of the BlobService and the
    values are the facts for that BlobService.
  returned: always
  type: complex
  contains:
    value:
      description:
        - List of blob services returned.
      returned: always
      type: list
      sample: null
      contains:
        blob_service_properties:
          description:
            - The properties of a storage account’s Blob service.
          returned: always
          type: dict
          sample: null
          contains:
            default_service_version:
              description:
                - >-
                  DefaultServiceVersion indicates the default version to use for
                  requests to the Blob service if an incoming request’s version
                  is not specified. Possible values include version 2008-10-27
                  and all more recent versions.
              returned: always
              type: str
              sample: null
            delete_retention_policy:
              description:
                - The blob service properties for blob soft delete.
              returned: always
              type: dict
              sample: null
              contains:
                enabled:
                  description:
                    - Indicates whether DeleteRetentionPolicy is enabled.
                  returned: always
                  type: bool
                  sample: null
                days:
                  description:
                    - >-
                      Indicates the number of days that the deleted item should
                      be retained. The minimum specified value can be 1 and the
                      maximum value can be 365.
                  returned: always
                  type: integer
                  sample: null
            is_versioning_enabled:
              description:
                - Versioning is enabled if set to true.
              returned: always
              type: bool
              sample: null
            automatic_snapshot_policy_enabled:
              description:
                - Deprecated in favor of isVersioningEnabled property.
              returned: always
              type: bool
              sample: null
            restore_policy:
              description:
                - The blob service properties for blob restore policy.
              returned: always
              type: dict
              sample: null
              contains:
                enabled:
                  description:
                    - Blob restore is enabled if set to true.
                  returned: always
                  type: bool
                  sample: null
                days:
                  description:
                    - >-
                      how long this blob can be restored. It should be great
                      than zero and less than DeleteRetentionPolicy.days.
                  returned: always
                  type: integer
                  sample: null
                last_enabled_time:
                  description:
                    - Deprecated in favor of minRestoreTime property.
                  returned: always
                  type: str
                  sample: null
                min_restore_time:
                  description:
                    - >-
                      Returns the minimum date and time that the restore can be
                      started.
                  returned: always
                  type: str
                  sample: null
            container_delete_retention_policy:
              description:
                - The blob service properties for container soft delete.
              returned: always
              type: dict
              sample: null
              contains:
                enabled:
                  description:
                    - Indicates whether DeleteRetentionPolicy is enabled.
                  returned: always
                  type: bool
                  sample: null
                days:
                  description:
                    - >-
                      Indicates the number of days that the deleted item should
                      be retained. The minimum specified value can be 1 and the
                      maximum value can be 365.
                  returned: always
                  type: integer
                  sample: null
            enabled:
              description:
                - >-
                  Indicates whether change feed event logging is enabled for the
                  Blob service.
              returned: always
              type: bool
              sample: null
            cors_rules:
              description:
                - >-
                  The List of CORS rules. You can include up to five CorsRule
                  elements in the request.
              returned: always
              type: list
              sample: null
              contains:
                allowed_origins:
                  description:
                    - >-
                      Required if CorsRule element is present. A list of origin
                      domains that will be allowed via CORS, or "*" to allow all
                      domains
                  returned: always
                  type: list
                  sample: null
                allowed_methods:
                  description:
                    - >-
                      Required if CorsRule element is present. A list of HTTP
                      methods that are allowed to be executed by the origin.
                  returned: always
                  type: list
                  sample: null
                max_age_in_seconds:
                  description:
                    - >-
                      Required if CorsRule element is present. The number of
                      seconds that the client/browser should cache a preflight
                      response.
                  returned: always
                  type: integer
                  sample: null
                exposed_headers:
                  description:
                    - >-
                      Required if CorsRule element is present. A list of
                      response headers to expose to CORS clients.
                  returned: always
                  type: list
                  sample: null
                allowed_headers:
                  description:
                    - >-
                      Required if CorsRule element is present. A list of headers
                      allowed to be part of the cross-origin request.
                  returned: always
                  type: list
                  sample: null
        sku:
          description:
            - Sku name and tier.
          returned: always
          type: dict
          sample: null
          contains:
            name:
              description:
                - >-
                  The SKU name. Required for account creation; optional for
                  update. Note that in older versions, SKU name was called
                  accountType.
              returned: always
              type: choice
              sample: null
            tier:
              description:
                - The SKU tier. This is based on the SKU name.
              returned: always
              type: sealed-choice
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
    blob_service_properties:
      description:
        - The properties of a storage account’s Blob service.
      returned: always
      type: dict
      sample: null
      contains:
        default_service_version:
          description:
            - >-
              DefaultServiceVersion indicates the default version to use for
              requests to the Blob service if an incoming request’s version is
              not specified. Possible values include version 2008-10-27 and all
              more recent versions.
          returned: always
          type: str
          sample: null
        delete_retention_policy:
          description:
            - The blob service properties for blob soft delete.
          returned: always
          type: dict
          sample: null
          contains:
            enabled:
              description:
                - Indicates whether DeleteRetentionPolicy is enabled.
              returned: always
              type: bool
              sample: null
            days:
              description:
                - >-
                  Indicates the number of days that the deleted item should be
                  retained. The minimum specified value can be 1 and the maximum
                  value can be 365.
              returned: always
              type: integer
              sample: null
        is_versioning_enabled:
          description:
            - Versioning is enabled if set to true.
          returned: always
          type: bool
          sample: null
        automatic_snapshot_policy_enabled:
          description:
            - Deprecated in favor of isVersioningEnabled property.
          returned: always
          type: bool
          sample: null
        restore_policy:
          description:
            - The blob service properties for blob restore policy.
          returned: always
          type: dict
          sample: null
          contains:
            enabled:
              description:
                - Blob restore is enabled if set to true.
              returned: always
              type: bool
              sample: null
            days:
              description:
                - >-
                  how long this blob can be restored. It should be great than
                  zero and less than DeleteRetentionPolicy.days.
              returned: always
              type: integer
              sample: null
            last_enabled_time:
              description:
                - Deprecated in favor of minRestoreTime property.
              returned: always
              type: str
              sample: null
            min_restore_time:
              description:
                - >-
                  Returns the minimum date and time that the restore can be
                  started.
              returned: always
              type: str
              sample: null
        container_delete_retention_policy:
          description:
            - The blob service properties for container soft delete.
          returned: always
          type: dict
          sample: null
          contains:
            enabled:
              description:
                - Indicates whether DeleteRetentionPolicy is enabled.
              returned: always
              type: bool
              sample: null
            days:
              description:
                - >-
                  Indicates the number of days that the deleted item should be
                  retained. The minimum specified value can be 1 and the maximum
                  value can be 365.
              returned: always
              type: integer
              sample: null
        enabled:
          description:
            - >-
              Indicates whether change feed event logging is enabled for the
              Blob service.
          returned: always
          type: bool
          sample: null
        cors_rules:
          description:
            - >-
              The List of CORS rules. You can include up to five CorsRule
              elements in the request.
          returned: always
          type: list
          sample: null
          contains:
            allowed_origins:
              description:
                - >-
                  Required if CorsRule element is present. A list of origin
                  domains that will be allowed via CORS, or "*" to allow all
                  domains
              returned: always
              type: list
              sample: null
            allowed_methods:
              description:
                - >-
                  Required if CorsRule element is present. A list of HTTP
                  methods that are allowed to be executed by the origin.
              returned: always
              type: list
              sample: null
            max_age_in_seconds:
              description:
                - >-
                  Required if CorsRule element is present. The number of seconds
                  that the client/browser should cache a preflight response.
              returned: always
              type: integer
              sample: null
            exposed_headers:
              description:
                - >-
                  Required if CorsRule element is present. A list of response
                  headers to expose to CORS clients.
              returned: always
              type: list
              sample: null
            allowed_headers:
              description:
                - >-
                  Required if CorsRule element is present. A list of headers
                  allowed to be part of the cross-origin request.
              returned: always
              type: list
              sample: null
    sku:
      description:
        - Sku name and tier.
      returned: always
      type: dict
      sample: null
      contains:
        name:
          description:
            - >-
              The SKU name. Required for account creation; optional for update.
              Note that in older versions, SKU name was called accountType.
          returned: always
          type: choice
          sample: null
        tier:
          description:
            - The SKU tier. This is based on the SKU name.
          returned: always
          type: sealed-choice
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


class AzureRMBlobServiceInfo(AzureRMModuleBase):
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
            blob_services_name=dict(
                type='constant'
            )
        )

        self.resource_group_name = None
        self.account_name = None
        self.blob_services_name = None

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
        super(AzureRMBlobServiceInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(StorageManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2019-06-01')

        if (self.resource_group_name is not None and
            self.account_name is not None and
            self.blob_services_name is not None):
            self.results['blob_services'] = self.format_item(self.getserviceproperty())
        elif (self.resource_group_name is not None and
              self.account_name is not None):
            self.results['blob_services'] = self.format_item(self.list())
        return self.results

    def getserviceproperty(self):
        response = None

        try:
            response = self.mgmt_client.blob_services.get_service_property(resource_group_name=self.resource_group_name,
                                                                           account_name=self.account_name,
                                                                           blob_services_name=self.blob_services_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.blob_services.list(resource_group_name=self.resource_group_name,
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
    AzureRMBlobServiceInfo()


if __name__ == '__main__':
    main()
