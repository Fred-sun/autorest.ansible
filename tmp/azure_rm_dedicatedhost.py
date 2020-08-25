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
module: azure_rm_dedicatedhost
version_added: '2.9'
short_description: Manage Azure DedicatedHost instance.
description:
  - 'Create, update and delete instance of Azure DedicatedHost.'
options:
  resource_group_name:
    description:
      - The name of the resource group.
    required: true
    type: str
  host_group_name:
    description:
      - The name of the dedicated host group.
    required: true
    type: str
  host_name:
    description:
      - The name of the dedicated host .
    type: str
  location:
    description:
      - Resource location
    type: str
  sku:
    description:
      - >-
        SKU of the dedicated host for Hardware Generation and VM family. Only
        name is required to be set. List Microsoft.Compute SKUs for a list of
        possible values.
    type: dict
    suboptions:
      name:
        description:
          - The sku name.
        type: str
      tier:
        description:
          - >-
            Specifies the tier of virtual machines in a scale set.:code:`<br
            />`:code:`<br />` Possible Values::code:`<br />`:code:`<br />`
            **Standard**\ :code:`<br />`:code:`<br />` **Basic**
        type: str
      capacity:
        description:
          - Specifies the number of virtual machines in the scale set.
        type: integer
  platform_fault_domain:
    description:
      - Fault domain of the dedicated host within a dedicated host group.
    type: integer
  auto_replace_on_failure:
    description:
      - >-
        Specifies whether the dedicated host should be replaced automatically in
        case of a failure. The value is defaulted to 'true' when not provided.
    type: bool
  license_type:
    description:
      - >-
        Specifies the software license type that will be applied to the VMs
        deployed on the dedicated host. :code:`<br>`:code:`<br>` Possible values
        are: :code:`<br>`:code:`<br>` **None** :code:`<br>`:code:`<br>`
        **Windows_Server_Hybrid** :code:`<br>`:code:`<br>`
        **Windows_Server_Perpetual** :code:`<br>`:code:`<br>` Default: **None**
    type: sealed-choice
  expand:
    description:
      - The expand expression to apply on the operation.
    type: constant
  state:
    description:
      - Assert the state of the DedicatedHost.
      - >-
        Use C(present) to create or update an DedicatedHost and C(absent) to
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
    from azure.mgmt.compute import ComputeManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMDedicatedHost(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            host_group_name=dict(
                type='str',
                required=True
            ),
            host_name=dict(
                type='str'
            ),
            location=dict(
                type='str',
                disposition='/location'
            ),
            sku=dict(
                type='dict',
                disposition='/sku',
                options=dict(
                    name=dict(
                        type='str',
                        disposition='name'
                    ),
                    tier=dict(
                        type='str',
                        disposition='tier'
                    ),
                    capacity=dict(
                        type='integer',
                        disposition='capacity'
                    )
                )
            ),
            platform_fault_domain=dict(
                type='integer',
                disposition='/platform_fault_domain'
            ),
            auto_replace_on_failure=dict(
                type='bool',
                disposition='/auto_replace_on_failure'
            ),
            license_type=dict(
                type='sealed-choice',
                disposition='/license_type'
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
        self.host_name = None
        self.expand = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMDedicatedHost, self).__init__(derived_arg_spec=self.module_arg_spec,
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
            response = self.mgmt_client.dedicated_hosts.create_or_update(resource_group_name=self.resource_group_name,
                                                                         host_group_name=self.host_group_name,
                                                                         host_name=self.host_name,
                                                                         parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the DedicatedHost instance.')
            self.fail('Error creating the DedicatedHost instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.dedicated_hosts.delete(resource_group_name=self.resource_group_name,
                                                               host_group_name=self.host_group_name,
                                                               host_name=self.host_name)
        except CloudError as e:
            self.log('Error attempting to delete the DedicatedHost instance.')
            self.fail('Error deleting the DedicatedHost instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        found = False
        try:
            response = self.mgmt_client.dedicated_hosts.get(resource_group_name=self.resource_group_name,
                                                            host_group_name=self.host_group_name,
                                                            host_name=self.host_name,
                                                            expand=self.expand)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMDedicatedHost()


if __name__ == '__main__':
    main()
