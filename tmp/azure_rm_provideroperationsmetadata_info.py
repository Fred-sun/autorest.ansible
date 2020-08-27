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
module: azure_rm_provideroperationsmetadata_info
version_added: '2.9'
short_description: Get ProviderOperationsMetadata info.
description:
  - Get info of ProviderOperationsMetadata.
options:
  resource_provider_namespace:
    description:
      - The namespace of the resource provider.
    type: str
  expand:
    description:
      - Specifies whether to expand the values.
    required: true
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: GetConfigurations
      azure_rm_provideroperationsmetadata_info: 
        resource_provider_namespace: resourceProviderNamespace
        

'''

RETURN = '''
provider_operations_metadata:
  description: >-
    A list of dict results where the key is the name of the
    ProviderOperationsMetadata and the values are the facts for that
    ProviderOperationsMetadata.
  returned: always
  type: complex
  contains:
    id:
      description:
        - The provider id.
      returned: always
      type: str
      sample: null
    name:
      description:
        - The provider name.
      returned: always
      type: str
      sample: null
    type:
      description:
        - The provider type.
      returned: always
      type: str
      sample: null
    display_name:
      description:
        - The provider display name.
      returned: always
      type: str
      sample: null
    resource_types:
      description:
        - The provider resource types
      returned: always
      type: list
      sample: null
      contains:
        name:
          description:
            - The resource type name.
          returned: always
          type: str
          sample: null
        display_name:
          description:
            - The resource type display name.
          returned: always
          type: str
          sample: null
        operations:
          description:
            - The resource type operations.
          returned: always
          type: list
          sample: null
          contains:
            name:
              description:
                - The operation name.
              returned: always
              type: str
              sample: null
            display_name:
              description:
                - The operation display name.
              returned: always
              type: str
              sample: null
            description:
              description:
                - The operation description.
              returned: always
              type: str
              sample: null
            origin:
              description:
                - The operation origin.
              returned: always
              type: str
              sample: null
            properties:
              description:
                - The operation properties.
              returned: always
              type: any
              sample: null
            is_data_action:
              description:
                - The dataAction flag to specify the operation type.
              returned: always
              type: bool
              sample: null
    operations:
      description:
        - The provider operations.
      returned: always
      type: list
      sample: null
      contains:
        name:
          description:
            - The operation name.
          returned: always
          type: str
          sample: null
        display_name:
          description:
            - The operation display name.
          returned: always
          type: str
          sample: null
        description:
          description:
            - The operation description.
          returned: always
          type: str
          sample: null
        origin:
          description:
            - The operation origin.
          returned: always
          type: str
          sample: null
        properties:
          description:
            - The operation properties.
          returned: always
          type: any
          sample: null
        is_data_action:
          description:
            - The dataAction flag to specify the operation type.
          returned: always
          type: bool
          sample: null
    value:
      description:
        - The list of providers.
      returned: always
      type: list
      sample: null
      contains:
        id:
          description:
            - The provider id.
          returned: always
          type: str
          sample: null
        name:
          description:
            - The provider name.
          returned: always
          type: str
          sample: null
        type:
          description:
            - The provider type.
          returned: always
          type: str
          sample: null
        display_name:
          description:
            - The provider display name.
          returned: always
          type: str
          sample: null
        resource_types:
          description:
            - The provider resource types
          returned: always
          type: list
          sample: null
          contains:
            name:
              description:
                - The resource type name.
              returned: always
              type: str
              sample: null
            display_name:
              description:
                - The resource type display name.
              returned: always
              type: str
              sample: null
            operations:
              description:
                - The resource type operations.
              returned: always
              type: list
              sample: null
              contains:
                name:
                  description:
                    - The operation name.
                  returned: always
                  type: str
                  sample: null
                display_name:
                  description:
                    - The operation display name.
                  returned: always
                  type: str
                  sample: null
                description:
                  description:
                    - The operation description.
                  returned: always
                  type: str
                  sample: null
                origin:
                  description:
                    - The operation origin.
                  returned: always
                  type: str
                  sample: null
                properties:
                  description:
                    - The operation properties.
                  returned: always
                  type: any
                  sample: null
                is_data_action:
                  description:
                    - The dataAction flag to specify the operation type.
                  returned: always
                  type: bool
                  sample: null
        operations:
          description:
            - The provider operations.
          returned: always
          type: list
          sample: null
          contains:
            name:
              description:
                - The operation name.
              returned: always
              type: str
              sample: null
            display_name:
              description:
                - The operation display name.
              returned: always
              type: str
              sample: null
            description:
              description:
                - The operation description.
              returned: always
              type: str
              sample: null
            origin:
              description:
                - The operation origin.
              returned: always
              type: str
              sample: null
            properties:
              description:
                - The operation properties.
              returned: always
              type: any
              sample: null
            is_data_action:
              description:
                - The dataAction flag to specify the operation type.
              returned: always
              type: bool
              sample: null
    next_link:
      description:
        - The URL to use for getting the next set of results.
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
    from azure.mgmt.authorization import AuthorizationManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMProviderOperationsMetadataInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_provider_namespace=dict(
                type='str'
            ),
            expand=dict(
                type='str',
                required=True
            )
        )

        self.resource_provider_namespace = None
        self.expand = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2018-01-01-preview'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMProviderOperationsMetadataInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(AuthorizationManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2018-01-01-preview')

        if (self.resource_provider_namespace is not None):
            self.results['provider_operations_metadata'] = self.format_item(self.get())
        else:
            self.results['provider_operations_metadata'] = self.format_item(self.list())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.provider_operations_metadata.get(resource_provider_namespace=self.resource_provider_namespace,
                                                                         expand=self.expand)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.provider_operations_metadata.list(expand=self.expand)
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
    AzureRMProviderOperationsMetadataInfo()


if __name__ == '__main__':
    main()
