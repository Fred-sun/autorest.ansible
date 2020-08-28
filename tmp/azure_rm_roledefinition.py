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
module: azure_rm_roledefinition
version_added: '2.9'
short_description: Manage Azure RoleDefinition instance.
description:
  - 'Create, update and delete instance of Azure RoleDefinition.'
options:
  scope:
    description:
      - The scope of the role definition.
    required: true
    type: str
  role_definition_id:
    description:
      - The ID of the role definition to delete.
      - The ID of the role definition.
    required: true
    type: str
  role_name:
    description:
      - The role name.
    type: str
  description:
    description:
      - The role definition description.
    type: str
  role_type:
    description:
      - The role type.
    type: str
  permissions:
    description:
      - Role definition permissions.
    type: list
    suboptions:
      actions:
        description:
          - Allowed actions.
        type: list
      not_actions:
        description:
          - Denied actions.
        type: list
      data_actions:
        description:
          - Allowed Data actions.
        type: list
      not_data_actions:
        description:
          - Denied Data actions.
        type: list
  assignable_scopes:
    description:
      - Role definition assignable scopes.
    type: list
  state:
    description:
      - Assert the state of the RoleDefinition.
      - >-
        Use C(present) to create or update an RoleDefinition and C(absent) to
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

EXAMPLES = '''
    - name: GetConfigurations
      azure_rm_roledefinition: 
        role_definition_id: roleDefinitionId
        scope: scope
        

'''

RETURN = '''
id:
  description:
    - The role definition ID.
  returned: always
  type: str
  sample: null
name:
  description:
    - The role definition name.
  returned: always
  type: str
  sample: null
type:
  description:
    - The role definition type.
  returned: always
  type: str
  sample: null
role_name:
  description:
    - The role name.
  returned: always
  type: str
  sample: null
description:
  description:
    - The role definition description.
  returned: always
  type: str
  sample: null
role_type:
  description:
    - The role type.
  returned: always
  type: str
  sample: null
permissions:
  description:
    - Role definition permissions.
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
assignable_scopes:
  description:
    - Role definition assignable scopes.
  returned: always
  type: list
  sample: null

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


class AzureRMRoleDefinition(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            scope=dict(
                type='str',
                required=True
            ),
            role_definition_id=dict(
                type='str',
                required=True
            ),
            role_name=dict(
                type='str',
                disposition='/role_name'
            ),
            description=dict(
                type='str',
                disposition='/description'
            ),
            role_type=dict(
                type='str',
                disposition='/role_type'
            ),
            permissions=dict(
                type='list',
                disposition='/permissions',
                elements='dict',
                options=dict(
                    actions=dict(
                        type='list',
                        disposition='actions',
                        elements='str'
                    ),
                    not_actions=dict(
                        type='list',
                        disposition='not_actions',
                        elements='str'
                    ),
                    data_actions=dict(
                        type='list',
                        disposition='data_actions',
                        elements='str'
                    ),
                    not_data_actions=dict(
                        type='list',
                        disposition='not_data_actions',
                        elements='str'
                    )
                )
            ),
            assignable_scopes=dict(
                type='list',
                disposition='/assignable_scopes',
                elements='str'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.scope = None
        self.role_definition_id = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMRoleDefinition, self).__init__(derived_arg_spec=self.module_arg_spec,
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
                                                    api_version='2018-01-01-preview')

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
            response = self.mgmt_client.role_definitions.create_or_update(scope=self.scope,
                                                                          role_definition_id=self.role_definition_id,
                                                                          role_definition=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the RoleDefinition instance.')
            self.fail('Error creating the RoleDefinition instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.role_definitions.delete(scope=self.scope,
                                                                role_definition_id=self.role_definition_id)
        except CloudError as e:
            self.log('Error attempting to delete the RoleDefinition instance.')
            self.fail('Error deleting the RoleDefinition instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.role_definitions.get(scope=self.scope,
                                                             role_definition_id=self.role_definition_id)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMRoleDefinition()


if __name__ == '__main__':
    main()
