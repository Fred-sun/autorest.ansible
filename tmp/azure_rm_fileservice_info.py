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
module: azure_rm_fileservice_info
version_added: '2.9'
short_description: Get FileService info.
description:
  - Get info of FileService.
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
  file_services_name:
    description:
      - >-
        The name of the file Service within the specified storage account. File
        Service Name must be "default"
    type: constant
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: ListFileServices
      azure_rm_fileservice_info: 
        account_name: sto1590
        resource_group_name: res9290
        

    - name: GetFileServices
      azure_rm_fileservice_info: 
        file_services_name: default
        account_name: sto8607
        resource_group_name: res4410
        

'''

RETURN = '''
file_services:
  description: >-
    A list of dict results where the key is the name of the FileService and the
    values are the facts for that FileService.
  returned: always
  type: complex
  contains:
    value:
      description:
        - List of file services returned.
      returned: always
      type: list
      sample: null
      contains:
        file_service_properties:
          description:
            - The properties of File services in storage account.
          returned: always
          type: dict
          sample: null
          contains:
            cors:
              description:
                - >-
                  Specifies CORS rules for the File service. You can include up
                  to five CorsRule elements in the request. If no CorsRule
                  elements are included in the request body, all CORS rules will
                  be deleted, and CORS will be disabled for the File service.
              returned: always
              type: dict
              sample: null
              contains:
                cors_rules:
                  description:
                    - >-
                      The List of CORS rules. You can include up to five
                      CorsRule elements in the request.
                  returned: always
                  type: list
                  sample: null
                  contains:
                    allowed_origins:
                      description:
                        - >-
                          Required if CorsRule element is present. A list of
                          origin domains that will be allowed via CORS, or "*"
                          to allow all domains
                      returned: always
                      type: list
                      sample: null
                    allowed_methods:
                      description:
                        - >-
                          Required if CorsRule element is present. A list of
                          HTTP methods that are allowed to be executed by the
                          origin.
                      returned: always
                      type: list
                      sample: null
                    max_age_in_seconds:
                      description:
                        - >-
                          Required if CorsRule element is present. The number of
                          seconds that the client/browser should cache a
                          preflight response.
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
                          Required if CorsRule element is present. A list of
                          headers allowed to be part of the cross-origin
                          request.
                      returned: always
                      type: list
                      sample: null
            share_delete_retention_policy:
              description:
                - The file service properties for share soft delete.
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
    file_service_properties:
      description:
        - The properties of File services in storage account.
      returned: always
      type: dict
      sample: null
      contains:
        cors:
          description:
            - >-
              Specifies CORS rules for the File service. You can include up to
              five CorsRule elements in the request. If no CorsRule elements are
              included in the request body, all CORS rules will be deleted, and
              CORS will be disabled for the File service.
          returned: always
          type: dict
          sample: null
          contains:
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
        share_delete_retention_policy:
          description:
            - The file service properties for share soft delete.
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


class AzureRMFileServiceInfo(AzureRMModuleBase):
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
            file_services_name=dict(
                type='constant'
            )
        )

        self.resource_group_name = None
        self.account_name = None
        self.file_services_name = None

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
        super(AzureRMFileServiceInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(StorageManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2019-06-01')

        if (self.resource_group_name is not None and
            self.account_name is not None and
            self.file_services_name is not None):
            self.results['file_services'] = self.format_item(self.getserviceproperties())
        elif (self.resource_group_name is not None and
              self.account_name is not None):
            self.results['file_services'] = self.format_item(self.list())
        return self.results

    def getserviceproperties(self):
        response = None

        try:
            response = self.mgmt_client.file_services.get_service_properties(resource_group_name=self.resource_group_name,
                                                                             account_name=self.account_name,
                                                                             file_services_name=self.file_services_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.file_services.list(resource_group_name=self.resource_group_name,
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
    AzureRMFileServiceInfo()


if __name__ == '__main__':
    main()
