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
module: azure_rm_loganalytic
version_added: '2.9'
short_description: Manage Azure LogAnalytic instance.
description:
  - 'Create, update and delete instance of Azure LogAnalytic.'
options:
  location:
    description:
      - The location upon which virtual-machine-sizes is queried.
    required: true
    type: str
  blob_container_sas_uri:
    description:
      - >-
        SAS Uri of the logging blob container to which LogAnalytics Api writes
        output logs to.
    required: true
    type: str
  from_time:
    description:
      - From time of the query
    required: true
    type: str
  to_time:
    description:
      - To time of the query
    required: true
    type: str
  group_by_throttle_policy:
    description:
      - Group query result by Throttle Policy applied.
    required: true
    type: bool
  group_by_operation_name:
    description:
      - Group query result by Operation Name.
    required: true
    type: bool
  group_by_resource_name:
    description:
      - Group query result by Resource Name.
    required: true
    type: bool
  interval_length:
    description:
      - Interval value in minutes used to create LogAnalytics call rate logs.
    type: sealed-choice
  state:
    description:
      - Assert the state of the LogAnalytic.
      - >-
        Use C(present) to create or update an LogAnalytic and C(absent) to
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


class AzureRMLogAnalytic(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            location=dict(
                type='str',
                required=True
            ),
            blob_container_sas_uri=dict(
                type='str',
                disposition='/blob_container_sas_uri',
                required=True
            ),
            from_time=dict(
                type='str',
                disposition='/from_time',
                required=True
            ),
            to_time=dict(
                type='str',
                disposition='/to_time',
                required=True
            ),
            group_by_throttle_policy=dict(
                type='bool',
                disposition='/group_by_throttle_policy',
                required=True
            ),
            group_by_operation_name=dict(
                type='bool',
                disposition='/group_by_operation_name',
                required=True
            ),
            group_by_resource_name=dict(
                type='bool',
                disposition='/group_by_resource_name',
                required=True
            ),
            interval_length=dict(
                type='sealed-choice',
                disposition='/interval_length'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.location = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMLogAnalytic, self).__init__(derived_arg_spec=self.module_arg_spec,
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
            response = self.mgmt_client.log_analytics.create_or_update()
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the LogAnalytic instance.')
            self.fail('Error creating the LogAnalytic instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.log_analytics.delete()
        except CloudError as e:
            self.log('Error attempting to delete the LogAnalytic instance.')
            self.fail('Error deleting the LogAnalytic instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        found = False
        try:
            response = self.mgmt_client.log_analytics.get()
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMLogAnalytic()


if __name__ == '__main__':
    main()
