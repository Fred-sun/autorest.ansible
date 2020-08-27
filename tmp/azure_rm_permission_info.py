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
module: azure_rm_permission_info
version_added: '2.9'
short_description: Get Permission info.
description:
  - Get info of Permission.
options:
  resource_group_name:
    description:
      - The name of the resource group.
    required: true
    type: str
  resource_provider_namespace:
    description:
      - The namespace of the resource provider.
    type: str
  parent_resource_path:
    description:
      - The parent resource identity.
    type: str
  resource_type:
    description:
      - The resource type of the resource.
    type: str
  resource_name:
    description:
      - The name of the resource to get the permissions for.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: GetConfigurations
      azure_rm_permission_info: 
        resource_group_name: rgname
        

'''

RETURN = '''
permissions:
  description: >-
    A list of dict results where the key is the name of the Permission and the
    values are the facts for that Permission.
  returned: always
  type: complex
  contains:
    value:
      description:
        - An array of permissions.
      returned: always
      type: list
      sample: null
      contains:
        actions:
          description:
            - Allowed actions.
          returned: always
          type: list
          sample: null
        not_actions:
          description:
            - Denied actions.
          returned: always
          type: list
          sample: null
        data_actions:
          description:
            - Allowed Data actions.
          returned: always
          type: list
          sample: null
        not_data_actions:
          description:
            - Denied Data actions.
          returned: always
          type: list
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


class AzureRMPermissionInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            resource_provider_namespace=dict(
                type='str'
            ),
            parent_resource_path=dict(
                type='str'
            ),
            resource_type=dict(
                type='str'
            ),
            resource_name=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.resource_provider_namespace = None
        self.parent_resource_path = None
        self.resource_type = None
        self.resource_name = None

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
        super(AzureRMPermissionInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(AuthorizationManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2018-01-01-preview')

        if (self.resource_group_name is not None and
            self.resource_provider_namespace is not None and
            self.parent_resource_path is not None and
            self.resource_type is not None and
            self.resource_name is not None):
            self.results['permissions'] = self.format_item(self.listforresource())
        elif (self.resource_group_name is not None):
            self.results['permissions'] = self.format_item(self.listforresourcegroup())
        return self.results

    def listforresource(self):
        response = None

        try:
            response = self.mgmt_client.permissions.list_for_resource(resource_group_name=self.resource_group_name,
                                                                      resource_provider_namespace=self.resource_provider_namespace,
                                                                      parent_resource_path=self.parent_resource_path,
                                                                      resource_type=self.resource_type,
                                                                      resource_name=self.resource_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listforresourcegroup(self):
        response = None

        try:
            response = self.mgmt_client.permissions.list_for_resource_group(resource_group_name=self.resource_group_name)
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
    AzureRMPermissionInfo()


if __name__ == '__main__':
    main()
