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
module: azure_rm_denyassignment
version_added: '2.9'
short_description: Manage Azure DenyAssignment instance.
description:
  - 'Create, update and delete instance of Azure DenyAssignment.'
options:
  scope:
    description:
      - The scope of the deny assignment.
    required: true
    type: str
  deny_assignment_id:
    description:
      - The ID of the deny assignment to get.
    required: true
    type: str
  state:
    description:
      - Assert the state of the DenyAssignment.
      - >-
        Use C(present) to create or update an DenyAssignment and C(absent) to
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
'''

RETURN = '''
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
          Data actions to exclude from that the deny assignment does not grant
          access.
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
      Determines if the deny assignment applies to child scopes. Default value
      is false.
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
          '00000000-0000-0000-0000-000000000000' as principal id and principal
          type as 'Everyone' represents all users, groups and service
          principals.
      returned: always
      type: str
      sample: null
    type:
      description:
        - >-
          Type of object represented by principal id (user, group, or service
          principal). An empty guid '00000000-0000-0000-0000-000000000000' as
          principal id and principal type as 'Everyone' represents all users,
          groups and service principals.
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
          '00000000-0000-0000-0000-000000000000' as principal id and principal
          type as 'Everyone' represents all users, groups and service
          principals.
      returned: always
      type: str
      sample: null
    type:
      description:
        - >-
          Type of object represented by principal id (user, group, or service
          principal). An empty guid '00000000-0000-0000-0000-000000000000' as
          principal id and principal type as 'Everyone' represents all users,
          groups and service principals.
      returned: always
      type: str
      sample: null
is_system_protected:
  description:
    - >-
      Specifies whether this deny assignment was created by Azure and cannot be
      edited or deleted.
  returned: always
  type: bool
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


class AzureRMDenyAssignment(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            scope=dict(
                type='str',
                required=True
            ),
            deny_assignment_id=dict(
                type='str',
                required=True
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.scope = None
        self.deny_assignment_id = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMDenyAssignment, self).__init__(derived_arg_spec=self.module_arg_spec,
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
                                                    api_version='2018-07-01-preview')

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
            if self.to_do == Actions.Create:
                response = self.mgmt_client.deny_assignments.create()
            else:
                response = self.mgmt_client.deny_assignments.update()
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the DenyAssignment instance.')
            self.fail('Error creating the DenyAssignment instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.deny_assignments.delete()
        except CloudError as e:
            self.log('Error attempting to delete the DenyAssignment instance.')
            self.fail('Error deleting the DenyAssignment instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.deny_assignments.get(scope=self.scope,
                                                             deny_assignment_id=self.deny_assignment_id)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMDenyAssignment()


if __name__ == '__main__':
    main()
