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
module: azure_rm_queueservice_info
version_added: '2.9'
short_description: Get QueueService info.
description:
  - Get info of QueueService.
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
  queue_service_name:
    description:
      - >-
        The name of the Queue Service within the specified storage account.
        Queue Service Name must be 'default'
    type: constant
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: QueueServicesList
      azure_rm_queueservice_info: 
        account_name: sto1590
        resource_group_name: res9290
        

    - name: QueueServicesGet
      azure_rm_queueservice_info: 
        account_name: sto8607
        resource_group_name: res4410
        

'''

RETURN = '''
queue_services:
  description: >-
    A list of dict results where the key is the name of the QueueService and the
    values are the facts for that QueueService.
  returned: always
  type: complex
  contains:
    value:
      description:
        - List of queue services returned.
      returned: always
      type: list
      sample: null
      contains:
        queue_service_properties:
          description:
            - The properties of a storage account’s Queue service.
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
    queue_service_properties:
      description:
        - The properties of a storage account’s Queue service.
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


class AzureRMQueueServiceInfo(AzureRMModuleBase):
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
            queue_service_name=dict(
                type='constant'
            )
        )

        self.resource_group_name = None
        self.account_name = None
        self.queue_service_name = None

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
        super(AzureRMQueueServiceInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(StorageManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2019-06-01')

        if (self.resource_group_name is not None and
            self.account_name is not None and
            self.queue_service_name is not None):
            self.results['queue_services'] = self.format_item(self.getserviceproperty())
        elif (self.resource_group_name is not None and
              self.account_name is not None):
            self.results['queue_services'] = self.format_item(self.list())
        return self.results

    def getserviceproperty(self):
        response = None

        try:
            response = self.mgmt_client.queue_services.get_service_property(resource_group_name=self.resource_group_name,
                                                                            account_name=self.account_name,
                                                                            queue_service_name=self.queue_service_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.queue_services.list(resource_group_name=self.resource_group_name,
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
    AzureRMQueueServiceInfo()


if __name__ == '__main__':
    main()
