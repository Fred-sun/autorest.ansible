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
module: azure_rm_availabilityset
version_added: '2.9'
short_description: Manage Azure AvailabilitySet instance.
description:
  - 'Create, update and delete instance of Azure AvailabilitySet.'
options:
  resource_group_name:
    description:
      - The name of the resource group.
    type: str
  availability_set_name:
    description:
      - The name of the availability set.
    type: str
  location:
    description:
      - Resource location
    type: str
  sku:
    description:
      - >-
        Sku of the availability set, only name is required to be set. See
        AvailabilitySetSkuTypes for possible set of values. Use 'Aligned' for
        virtual machines with managed disks and 'Classic' for virtual machines
        with unmanaged disks. Default value is 'Classic'.
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
  platform_update_domain_count:
    description:
      - Update Domain count.
    type: integer
  platform_fault_domain_count:
    description:
      - Fault Domain count.
    type: integer
  virtual_machines:
    description:
      - A list of references to all virtual machines in the availability set.
    type: list
  proximity_placement_group:
    description:
      - >-
        Specifies information about the proximity placement group that the
        availability set should be assigned to. :code:`<br>`:code:`<br>`Minimum
        api-version: 2018-04-01.
    type: dict
    suboptions:
      id:
        description:
          - Resource Id
        type: str
  expand:
    description:
      - >-
        The expand expression to apply to the operation. Allowed values are
        'instanceView'.
    type: str
  state:
    description:
      - Assert the state of the AvailabilitySet.
      - >-
        Use C(present) to create or update an AvailabilitySet and C(absent) to
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


class AzureRMAvailabilitySet(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str'
            ),
            availability_set_name=dict(
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
            platform_update_domain_count=dict(
                type='integer',
                disposition='/platform_update_domain_count'
            ),
            platform_fault_domain_count=dict(
                type='integer',
                disposition='/platform_fault_domain_count'
            ),
            virtual_machines=dict(
                type='list',
                disposition='/virtual_machines'
            ),
            proximity_placement_group=dict(
                type='dict',
                disposition='/proximity_placement_group',
                options=dict(
                    id=dict(
                        type='str',
                        disposition='id'
                    )
                )
            ),
            expand=dict(
                type='str'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group_name = None
        self.availability_set_name = None
        self.expand = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMAvailabilitySet, self).__init__(derived_arg_spec=self.module_arg_spec,
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
            if self.to_do == Actions.Create:
                response = self.mgmt_client.availability_sets.create(resource_group_name=self.resource_group_name,
                                                                     availability_set_name=self.availability_set_name,
                                                                     parameters=self.body)
            else:
                response = self.mgmt_client.availability_sets.update(resource_group_name=self.resource_group_name,
                                                                     availability_set_name=self.availability_set_name,
                                                                     parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the AvailabilitySet instance.')
            self.fail('Error creating the AvailabilitySet instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.availability_sets.delete(resource_group_name=self.resource_group_name,
                                                                 availability_set_name=self.availability_set_name)
        except CloudError as e:
            self.log('Error attempting to delete the AvailabilitySet instance.')
            self.fail('Error deleting the AvailabilitySet instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        found = False
        try:
            response = self.mgmt_client.availability_sets.get(resource_group_name=self.resource_group_name,
                                                              availability_set_name=self.availability_set_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMAvailabilitySet()


if __name__ == '__main__':
    main()
