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
module: azure_rm_privateendpointconnection_info
version_added: '2.9'
short_description: Get PrivateEndpointConnection info.
description:
  - Get info of PrivateEndpointConnection.
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
  private_endpoint_connection_name:
    description:
      - >-
        The name of the private endpoint connection associated with the Azure
        resource
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: StorageAccountListPrivateEndpointConnections
      azure_rm_privateendpointconnection_info: 
        account_name: sto2527
        resource_group_name: res6977
        

    - name: StorageAccountGetPrivateEndpointConnection
      azure_rm_privateendpointconnection_info: 
        account_name: sto2527
        private_endpoint_connection_name: '{privateEndpointConnectionName}'
        resource_group_name: res6977
        

'''

RETURN = '''
private_endpoint_connections:
  description: >-
    A list of dict results where the key is the name of the
    PrivateEndpointConnection and the values are the facts for that
    PrivateEndpointConnection.
  returned: always
  type: complex
  contains:
    value:
      description:
        - Array of private endpoint connections
      returned: always
      type: list
      sample: null
      contains:
        private_endpoint:
          description:
            - The resource of private end point.
          returned: always
          type: dict
          sample: null
          contains:
            id:
              description:
                - The ARM identifier for Private Endpoint
              returned: always
              type: str
              sample: null
        private_link_service_connection_state:
          description:
            - >-
              A collection of information about the state of the connection
              between service consumer and provider.
          returned: always
          type: dict
          sample: null
          contains:
            status:
              description:
                - >-
                  Indicates whether the connection has been
                  Approved/Rejected/Removed by the owner of the service.
              returned: always
              type: choice
              sample: null
            description:
              description:
                - The reason for approval/rejection of the connection.
              returned: always
              type: str
              sample: null
            action_required:
              description:
                - >-
                  A message indicating if changes on the service provider
                  require any updates on the consumer.
              returned: always
              type: str
              sample: null
        provisioning_state:
          description:
            - >-
              The provisioning state of the private endpoint connection
              resource.
          returned: always
          type: choice
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
    private_endpoint:
      description:
        - The resource of private end point.
      returned: always
      type: dict
      sample: null
      contains:
        id:
          description:
            - The ARM identifier for Private Endpoint
          returned: always
          type: str
          sample: null
    private_link_service_connection_state:
      description:
        - >-
          A collection of information about the state of the connection between
          service consumer and provider.
      returned: always
      type: dict
      sample: null
      contains:
        status:
          description:
            - >-
              Indicates whether the connection has been
              Approved/Rejected/Removed by the owner of the service.
          returned: always
          type: choice
          sample: null
        description:
          description:
            - The reason for approval/rejection of the connection.
          returned: always
          type: str
          sample: null
        action_required:
          description:
            - >-
              A message indicating if changes on the service provider require
              any updates on the consumer.
          returned: always
          type: str
          sample: null
    provisioning_state:
      description:
        - The provisioning state of the private endpoint connection resource.
      returned: always
      type: choice
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


class AzureRMPrivateEndpointConnectionInfo(AzureRMModuleBase):
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
            private_endpoint_connection_name=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.account_name = None
        self.private_endpoint_connection_name = None

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
        super(AzureRMPrivateEndpointConnectionInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(StorageManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2019-06-01')

        if (self.resource_group_name is not None and
            self.account_name is not None and
            self.private_endpoint_connection_name is not None):
            self.results['private_endpoint_connections'] = self.format_item(self.get())
        elif (self.resource_group_name is not None and
              self.account_name is not None):
            self.results['private_endpoint_connections'] = self.format_item(self.list())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.private_endpoint_connections.get(resource_group_name=self.resource_group_name,
                                                                         account_name=self.account_name,
                                                                         private_endpoint_connection_name=self.private_endpoint_connection_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.private_endpoint_connections.list(resource_group_name=self.resource_group_name,
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
    AzureRMPrivateEndpointConnectionInfo()


if __name__ == '__main__':
    main()
