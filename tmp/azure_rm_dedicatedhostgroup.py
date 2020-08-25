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
module: azure_rm_dedicatedhostgroup
version_added: '2.9'
short_description: Manage Azure DedicatedHostGroup instance.
description:
  - 'Create, update and delete instance of Azure DedicatedHostGroup.'
options:
  resource_group_name:
    description:
      - The name of the resource group.
    type: str
  host_group_name:
    description:
      - The name of the dedicated host group.
    type: str
  location:
    description:
      - Resource location
    type: str
  zones:
    description:
      - >-
        Availability Zone to use for this host group. Only single zone is
        supported. The zone can be assigned only during creation. If not
        provided, the group supports all zones in the region. If provided,
        enforces each host in the group to be in the same zone.
    type: list
  platform_fault_domain_count:
    description:
      - Number of fault domains that the host group can span.
    type: integer
  support_automatic_placement:
    description:
      - >-
        Specifies whether virtual machines or virtual machine scale sets can be
        placed automatically on the dedicated host group. Automatic placement
        means resources are allocated on dedicated hosts, that are chosen by
        Azure, under the dedicated host group. The value is defaulted to 'true'
        when not provided. :code:`<br>`:code:`<br>`Minimum api-version:
        2020-06-01.
    type: bool
  expand:
    description:
      - >-
        The expand expression to apply on the operation. The response shows the
        list of instance view of the dedicated hosts under the dedicated host
        group.
    type: constant
  state:
    description:
      - Assert the state of the DedicatedHostGroup.
      - >-
        Use C(present) to create or update an DedicatedHostGroup and C(absent)
        to delete it.
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
    from azure.mgmt.compute import ComputeManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMDedicatedHostGroup(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str'
            ),
            host_group_name=dict(
                type='str'
            ),
            location=dict(
                type='str',
                disposition='/location'
            ),
            zones=dict(
                type='list',
                disposition='/zones'
            ),
            platform_fault_domain_count=dict(
                type='integer',
                disposition='/platform_fault_domain_count'
            ),
            support_automatic_placement=dict(
                type='bool',
                disposition='/support_automatic_placement'
            ),
            expand=dict(
                type='constant'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group_name = None
        self.host_group_name = None
        self.expand = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMDedicatedHostGroup, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(ComputeManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-06-01')

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
            response = self.mgmt_client.dedicated_host_groups.create_or_update(resource_group_name=self.resource_group_name,
                                                                               host_group_name=self.host_group_name,
                                                                               parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the DedicatedHostGroup instance.')
            self.fail('Error creating the DedicatedHostGroup instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.dedicated_host_groups.delete(resource_group_name=self.resource_group_name,
                                                                     host_group_name=self.host_group_name)
        except CloudError as e:
            self.log('Error attempting to delete the DedicatedHostGroup instance.')
            self.fail('Error deleting the DedicatedHostGroup instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        found = False
        try:
            response = self.mgmt_client.dedicated_host_groups.get(resource_group_name=self.resource_group_name,
                                                                  host_group_name=self.host_group_name,
                                                                  expand=self.expand)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMDedicatedHostGroup()


if __name__ == '__main__':
    main()
