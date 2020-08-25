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
module: azure_rm_roleassignment_info
version_added: '2.9'
short_description: Get RoleAssignment info.
description:
  - Get info of RoleAssignment.
options:
  resource_group_name:
    description:
      - The name of the resource group.
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
      - The name of the resource to get role assignments for.
    type: str
  filter:
    description:
      - >-
        The filter to apply on the operation. Use $filter=atScope() to return
        all role assignments at or above the scope. Use $filter=principalId eq
        {id} to return all role assignments at, above or below the scope for the
        specified principal.
    type: str
  scope:
    description:
      - The scope of the role assignment.
    type: str
  role_assignment_name:
    description:
      - The name of the role assignment to get.
    type: str
  role_id:
    description:
      - The ID of the role assignment to get.
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


class AzureRMRoleAssignmentInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str'
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
            ),
            filter=dict(
                type='str'
            ),
            scope=dict(
                type='str'
            ),
            role_assignment_name=dict(
                type='str'
            ),
            role_id=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.resource_provider_namespace = None
        self.parent_resource_path = None
        self.resource_type = None
        self.resource_name = None
        self.filter = None
        self.scope = None
        self.role_assignment_name = None
        self.role_id = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2020-04-01-preview'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMRoleAssignmentInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(AuthorizationManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-04-01-preview')

        if (self.resource_group_name is not None and
            self.resource_provider_namespace is not None and
            self.parent_resource_path is not None and
            self.resource_type is not None and
            self.resource_name is not None):
            self.results['role_assignments'] = self.format_item(self.listforresource())
        elif (self.scope is not None and
              self.role_assignment_name is not None):
            self.results['role_assignments'] = self.format_item(self.get())
        elif (self.resource_group_name is not None):
            self.results['role_assignments'] = self.format_item(self.listforresourcegroup())
        elif (self.scope is not None):
            self.results['role_assignments'] = self.format_item(self.listforscope())
        elif (self.role_id is not None):
            self.results['role_assignments'] = self.format_item(self.getbyid())
        else:
            self.results['role_assignments'] = self.format_item(self.list())
        return self.results

    def listforresource(self):
        response = None

        try:
            response = self.mgmt_client.role_assignments.list_for_resource(resource_group_name=self.resource_group_name,
                                                                           resource_provider_namespace=self.resource_provider_namespace,
                                                                           parent_resource_path=self.parent_resource_path,
                                                                           resource_type=self.resource_type,
                                                                           resource_name=self.resource_name,
                                                                           filter=self.filter)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def get(self):
        response = None

        try:
            response = self.mgmt_client.role_assignments.get(scope=self.scope,
                                                             role_assignment_name=self.role_assignment_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listforresourcegroup(self):
        response = None

        try:
            response = self.mgmt_client.role_assignments.list_for_resource_group(resource_group_name=self.resource_group_name,
                                                                                 filter=self.filter)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listforscope(self):
        response = None

        try:
            response = self.mgmt_client.role_assignments.list_for_scope(scope=self.scope,
                                                                        filter=self.filter)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def getbyid(self):
        response = None

        try:
            response = self.mgmt_client.role_assignments.get_by_id(role_id=self.role_id)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.role_assignments.list(filter=self.filter)
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
    AzureRMRoleAssignmentInfo()


if __name__ == '__main__':
    main()
