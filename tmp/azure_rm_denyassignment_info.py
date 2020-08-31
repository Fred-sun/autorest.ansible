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
module: azure_rm_denyassignment_info
version_added: '2.9'
short_description: Get DenyAssignment info.
description:
  - Get info of DenyAssignment.
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
      - The name of the resource to get deny assignments for.
    type: str
  filter:
    description:
      - >-
        The filter to apply on the operation. Use $filter=atScope() to return
        all deny assignments at or above the scope. Use
        $filter=denyAssignmentName eq '{name}' to search deny assignments by
        name at specified scope. Use $filter=principalId eq '{id}' to return all
        deny assignments at, above and below the scope for the specified
        principal. Use $filter=gdprExportPrincipalId eq '{id}' to return all
        deny assignments at, above and below the scope for the specified
        principal. This filter is different from the principalId filter as it
        returns not only those deny assignments that contain the specified
        principal is the Principals list but also those deny assignments that
        contain the specified principal is the ExcludePrincipals list.
        Additionally, when gdprExportPrincipalId filter is used, only the deny
        assignment name and description properties are returned.
    type: str
  scope:
    description:
      - The scope of the deny assignment.
      - The scope of the deny assignments.
    type: str
  deny_assignment_id:
    description:
      - The ID of the deny assignment to get.
      - >-
        The fully qualified deny assignment ID. For example, use the format,
        /subscriptions/{guid}/providers/Microsoft.Authorization/denyAssignments/{denyAssignmentId}
        for subscription level deny assignments, or
        /providers/Microsoft.Authorization/denyAssignments/{denyAssignmentId}
        for tenant level deny assignments.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: GetConfigurations
      azure_rm_denyassignment_info: 
        parent_resource_path: parentResourcePath
        resource_group_name: rgname
        resource_name: resourceName
        resource_provider_namespace: resourceProviderNamespace
        resource_type: resourceType
        

'''

RETURN = '''
deny_assignments:
  description: >-
    A list of dict results where the key is the name of the DenyAssignment and
    the values are the facts for that DenyAssignment.
  returned: always
  type: complex
  contains:
    value:
      description:
        - Deny assignment list.
      returned: always
      type: list
      sample: null
      contains:
        id:
          description:
            - The deny assignment ID.
          returned: always
          type: str
          sample: null
        name:
          description:
            - The deny assignment name.
          returned: always
          type: str
          sample: null
        type:
          description:
            - The deny assignment type.
          returned: always
          type: str
          sample: null
        deny_assignment_name:
          description:
            - The display name of the deny assignment.
          returned: always
          type: str
          sample: null
        description:
          description:
            - The description of the deny assignment.
          returned: always
          type: str
          sample: null
        permissions:
          description:
            - An array of permissions that are denied by the deny assignment.
          returned: always
          type: list
          sample: null
          contains:
            actions:
              description:
                - Actions to which the deny assignment does not grant access.
              returned: always
              type: list
              sample: null
            not_actions:
              description:
                - >-
                  Actions to exclude from that the deny assignment does not
                  grant access.
              returned: always
              type: list
              sample: null
            data_actions:
              description:
                - >-
                  Data actions to which the deny assignment does not grant
                  access.
              returned: always
              type: list
              sample: null
            not_data_actions:
              description:
                - >-
                  Data actions to exclude from that the deny assignment does not
                  grant access.
              returned: always
              type: list
              sample: null
        scope:
          description:
            - The deny assignment scope.
          returned: always
          type: str
          sample: null
        do_not_apply_to_child_scopes:
          description:
            - >-
              Determines if the deny assignment applies to child scopes. Default
              value is false.
          returned: always
          type: bool
          sample: null
        principals:
          description:
            - Array of principals to which the deny assignment applies.
          returned: always
          type: list
          sample: null
          contains:
            id:
              description:
                - >-
                  Object ID of the Azure AD principal (user, group, or service
                  principal) to which the deny assignment applies. An empty guid
                  '00000000-0000-0000-0000-000000000000' as principal id and
                  principal type as 'Everyone' represents all users, groups and
                  service principals.
              returned: always
              type: str
              sample: null
            type:
              description:
                - >-
                  Type of object represented by principal id (user, group, or
                  service principal). An empty guid
                  '00000000-0000-0000-0000-000000000000' as principal id and
                  principal type as 'Everyone' represents all users, groups and
                  service principals.
              returned: always
              type: str
              sample: null
        exclude_principals:
          description:
            - Array of principals to which the deny assignment does not apply.
          returned: always
          type: list
          sample: null
          contains:
            id:
              description:
                - >-
                  Object ID of the Azure AD principal (user, group, or service
                  principal) to which the deny assignment applies. An empty guid
                  '00000000-0000-0000-0000-000000000000' as principal id and
                  principal type as 'Everyone' represents all users, groups and
                  service principals.
              returned: always
              type: str
              sample: null
            type:
              description:
                - >-
                  Type of object represented by principal id (user, group, or
                  service principal). An empty guid
                  '00000000-0000-0000-0000-000000000000' as principal id and
                  principal type as 'Everyone' represents all users, groups and
                  service principals.
              returned: always
              type: str
              sample: null
        is_system_protected:
          description:
            - >-
              Specifies whether this deny assignment was created by Azure and
              cannot be edited or deleted.
          returned: always
          type: bool
          sample: null
    next_link:
      description:
        - The URL to use for getting the next set of results.
      returned: always
      type: str
      sample: null
    id:
      description:
        - The deny assignment ID.
      returned: always
      type: str
      sample: null
    name:
      description:
        - The deny assignment name.
      returned: always
      type: str
      sample: null
    type:
      description:
        - The deny assignment type.
      returned: always
      type: str
      sample: null
    deny_assignment_name:
      description:
        - The display name of the deny assignment.
      returned: always
      type: str
      sample: null
    description:
      description:
        - The description of the deny assignment.
      returned: always
      type: str
      sample: null
    permissions:
      description:
        - An array of permissions that are denied by the deny assignment.
      returned: always
      type: list
      sample: null
      contains:
        actions:
          description:
            - Actions to which the deny assignment does not grant access.
          returned: always
          type: list
          sample: null
        not_actions:
          description:
            - >-
              Actions to exclude from that the deny assignment does not grant
              access.
          returned: always
          type: list
          sample: null
        data_actions:
          description:
            - Data actions to which the deny assignment does not grant access.
          returned: always
          type: list
          sample: null
        not_data_actions:
          description:
            - >-
              Data actions to exclude from that the deny assignment does not
              grant access.
          returned: always
          type: list
          sample: null
    scope:
      description:
        - The deny assignment scope.
      returned: always
      type: str
      sample: null
    do_not_apply_to_child_scopes:
      description:
        - >-
          Determines if the deny assignment applies to child scopes. Default
          value is false.
      returned: always
      type: bool
      sample: null
    principals:
      description:
        - Array of principals to which the deny assignment applies.
      returned: always
      type: list
      sample: null
      contains:
        id:
          description:
            - >-
              Object ID of the Azure AD principal (user, group, or service
              principal) to which the deny assignment applies. An empty guid
              '00000000-0000-0000-0000-000000000000' as principal id and
              principal type as 'Everyone' represents all users, groups and
              service principals.
          returned: always
          type: str
          sample: null
        type:
          description:
            - >-
              Type of object represented by principal id (user, group, or
              service principal). An empty guid
              '00000000-0000-0000-0000-000000000000' as principal id and
              principal type as 'Everyone' represents all users, groups and
              service principals.
          returned: always
          type: str
          sample: null
    exclude_principals:
      description:
        - Array of principals to which the deny assignment does not apply.
      returned: always
      type: list
      sample: null
      contains:
        id:
          description:
            - >-
              Object ID of the Azure AD principal (user, group, or service
              principal) to which the deny assignment applies. An empty guid
              '00000000-0000-0000-0000-000000000000' as principal id and
              principal type as 'Everyone' represents all users, groups and
              service principals.
          returned: always
          type: str
          sample: null
        type:
          description:
            - >-
              Type of object represented by principal id (user, group, or
              service principal). An empty guid
              '00000000-0000-0000-0000-000000000000' as principal id and
              principal type as 'Everyone' represents all users, groups and
              service principals.
          returned: always
          type: str
          sample: null
    is_system_protected:
      description:
        - >-
          Specifies whether this deny assignment was created by Azure and cannot
          be edited or deleted.
      returned: always
      type: bool
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


class AzureRMDenyAssignmentInfo(AzureRMModuleBase):
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
            deny_assignment_id=dict(
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
        self.deny_assignment_id = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2018-07-01-preview'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMDenyAssignmentInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(AuthorizationManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2018-07-01-preview')

        if (self.resource_group_name is not None and
            self.resource_provider_namespace is not None and
            self.parent_resource_path is not None and
            self.resource_type is not None and
            self.resource_name is not None):
            self.results['deny_assignments'] = self.format_item(self.listforresource())
        elif (self.scope is not None and
              self.deny_assignment_id is not None):
            self.results['deny_assignments'] = self.format_item(self.get())
        elif (self.resource_group_name is not None):
            self.results['deny_assignments'] = self.format_item(self.listforresourcegroup())
        elif (self.scope is not None):
            self.results['deny_assignments'] = self.format_item(self.listforscope())
        elif (self.deny_assignment_id is not None):
            self.results['deny_assignments'] = self.format_item(self.getbyid())
        else:
            self.results['deny_assignments'] = self.format_item(self.list())
        return self.results

    def listforresource(self):
        response = None

        try:
            response = self.mgmt_client.deny_assignments.list_for_resource(resource_group_name=self.resource_group_name,
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
            response = self.mgmt_client.deny_assignments.get(scope=self.scope,
                                                             deny_assignment_id=self.deny_assignment_id)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listforresourcegroup(self):
        response = None

        try:
            response = self.mgmt_client.deny_assignments.list_for_resource_group(resource_group_name=self.resource_group_name,
                                                                                 filter=self.filter)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listforscope(self):
        response = None

        try:
            response = self.mgmt_client.deny_assignments.list_for_scope(scope=self.scope,
                                                                        filter=self.filter)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def getbyid(self):
        response = None

        try:
            response = self.mgmt_client.deny_assignments.get_by_id(deny_assignment_id=self.deny_assignment_id)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.deny_assignments.list(filter=self.filter)
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
    AzureRMDenyAssignmentInfo()


if __name__ == '__main__':
    main()
