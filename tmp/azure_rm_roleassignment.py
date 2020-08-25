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
module: azure_rm_roleassignment
version_added: '2.9'
short_description: Manage Azure RoleAssignment instance.
description:
  - 'Create, update and delete instance of Azure RoleAssignment.'
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
      - The scope of the role assignment to delete.
    type: str
  role_assignment_name:
    description:
      - The name of the role assignment to delete.
    type: str
  role_definition_id:
    description:
      - The role definition ID used in the role assignment.
    type: str
  principal_id:
    description:
      - >-
        The principal ID assigned to the role. This maps to the ID inside the
        Active Directory. It can point to a user, service principal, or security
        group.
    type: str
  principal_type:
    description:
      - The principal type of the assigned principal ID.
    type: choice
  can_delegate:
    description:
      - The delegation flag used for creating a role assignment
    type: bool
  description:
    description:
      - Description of role assignment
    type: str
  condition:
    description:
      - The conditions on the role assignment
    type: str
  condition_version:
    description:
      - Version of the condition
    type: str
  role_id:
    description:
      - The ID of the role assignment to delete.
    type: str
  state:
    description:
      - Assert the state of the RoleAssignment.
      - >-
        Use C(present) to create or update an RoleAssignment and C(absent) to
        delete it.
    default: present
    choices:
      - absent
      - present
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''


import time
import json
import re
from ansible.module_utils.azure_rm_common_ext import AzureRMModuleBaseExt
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.authorization import AuthorizationManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMRoleAssignment(AzureRMModuleBaseExt):
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
            role_definition_id=dict(
                type='str',
                disposition='/role_definition_id'
            ),
            principal_id=dict(
                type='str',
                disposition='/principal_id'
            ),
            principal_type=dict(
                type='choice',
                disposition='/principal_type'
            ),
            can_delegate=dict(
                type='bool',
                disposition='/can_delegate'
            ),
            description=dict(
                type='str',
                disposition='/description'
            ),
            condition=dict(
                type='str',
                disposition='/condition'
            ),
            condition_version=dict(
                type='str',
                disposition='/condition_version'
            ),
            role_id=dict(
                type='str'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
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
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMRoleAssignment, self).__init__(derived_arg_spec=self.module_arg_spec,
                                                    supports_check_mode=True,
                                                    supports_tags=True)

    def exec_module(self, **kwargs):
        for key in list(self.module_arg_spec.keys()):
            if hasattr(self, key):
                setattr(self, key, kwargs[key])
            elif kwargs[key] is not None:
                self.body[key] = kwargs[key]

        self.inflate_parameters(self.module_arg_spec, self.body, 0)

        old_response = None
        response = None

        self.mgmt_client = self.get_mgmt_svc_client(AuthorizationManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-04-01-preview')

        old_response = self.get_resource()

        if not old_response:
            if self.state == 'present':
                self.to_do = Actions.Create
        else:
            if self.state == 'absent':
                self.to_do = Actions.Delete
            else:
                modifiers = {}
                self.create_compare_modifiers(self.module_arg_spec, '', modifiers)
                self.results['modifiers'] = modifiers
                self.results['compare'] = []
                if not self.default_compare(modifiers, self.body, old_response, '', self.results):
                    self.to_do = Actions.Update

        if (self.to_do == Actions.Create) or (self.to_do == Actions.Update):
            self.results['changed'] = True
            if self.check_mode:
                return self.results
            response = self.create_update_resource()
        elif self.to_do == Actions.Delete:
            self.results['changed'] = True
            if self.check_mode:
                return self.results
            self.delete_resource()
        else:
            self.results['changed'] = False
            response = old_response

        return self.results

    def create_update_resource(self):
        try:
            response = self.mgmt_client.role_assignments.create_or_update()
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the RoleAssignment instance.')
            self.fail('Error creating the RoleAssignment instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.role_assignments.delete(scope=self.scope,
                                                                role_assignment_name=self.role_assignment_name)
        except CloudError as e:
            self.log('Error attempting to delete the RoleAssignment instance.')
            self.fail('Error deleting the RoleAssignment instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        found = False
        try:
            response = self.mgmt_client.role_assignments.get(scope=self.scope,
                                                             role_assignment_name=self.role_assignment_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMRoleAssignment()


if __name__ == '__main__':
    main()
