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
module: azure_rm_roledefinition_info
version_added: '2.9'
short_description: Get RoleDefinition info.
description:
  - Get info of RoleDefinition.
options:
  scope:
    description:
      - The scope of the role definition.
    type: str
  role_definition_id:
    description:
      - The ID of the role definition.
    type: str
  filter:
    description:
      - >-
        The filter to apply on the operation. Use atScopeAndBelow filter to
        search below the given scope as well.
    type: str
  role_id:
    description:
      - >-
        The fully qualified role definition ID. Use the format,
        /subscriptions/{guid}/providers/Microsoft.Authorization/roleDefinitions/{roleDefinitionId}
        for subscription level role definitions, or
        /providers/Microsoft.Authorization/roleDefinitions/{roleDefinitionId}
        for tenant level role definitions.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

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


class AzureRMRoleDefinitionInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            scope=dict(
                type='str'
            ),
            role_definition_id=dict(
                type='str'
            ),
            filter=dict(
                type='str'
            ),
            role_id=dict(
                type='str'
            )
        )

        self.scope = None
        self.role_definition_id = None
        self.filter = None
        self.role_id = None

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
        super(AzureRMRoleDefinitionInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(AuthorizationManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2018-01-01-preview')

        if (self.scope is not None and
            self.role_definition_id is not None):
            self.results['role_definitions'] = self.format_item(self.get())
        elif (self.scope is not None):
            self.results['role_definitions'] = self.format_item(self.list())
        elif (self.role_id is not None):
            self.results['role_definitions'] = self.format_item(self.getbyid())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.role_definitions.get(scope=self.scope,
                                                             role_definition_id=self.role_definition_id)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.role_definitions.list(scope=self.scope,
                                                              filter=self.filter)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def getbyid(self):
        response = None

        try:
            response = self.mgmt_client.role_definitions.get_by_id(role_id=self.role_id)
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
    AzureRMRoleDefinitionInfo()


if __name__ == '__main__':
    main()
