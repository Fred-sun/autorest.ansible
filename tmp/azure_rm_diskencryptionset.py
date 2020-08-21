#!/usr/bin/python
#
# Copyright (c) 2019 Zim Kalinowski, (@zikalino)
#
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type


ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}



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


class AzureRMDiskEncryptionSet(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str'
            ),
            disk_encryption_set_name=dict(
                type='str'
            ),
            location=dict(
                type='str',
                disposition='null'
            ),
            encryption_type=dict(
                type='choice',
                disposition='null'
            ),
            key_url=dict(
                type='str',
                disposition='null'
            ),
            id=dict(
                type='str',
                disposition='null'
            ),
            type=dict(
                type='choice',
                disposition='null'
            ),
            active_key=dict(
                type='dict',
                disposition='null',
                options=dict(
                    key_url=dict(
                        type='str',
                        disposition='null',
                        required=true
                    ),
                    id=dict(
                        type='str',
                        disposition='null'
                    )
                )
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group_name = None
        self.disk_encryption_set_name = None
        self.location = None
        self.tags = None
        self.encryption_type = None
        self.key_url = None
        self.id = None
        self.type = None
        self.active_key = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMDiskEncryptionSet, self).__init__(derived_arg_spec=self.module_arg_spec,
                                                       supports_check_mode=True,
                                                       supports_tags=True)

    def exec_module(self, **kwargs):
        for key in list(self.module_arg_spec.keys()):
            setattr(self, key, kwargs[key])


        old_response = None
        response = None

        self.mgmt_client = self.get_mgmt_svc_client(GenericRestClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

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
            response = self.mgmt_client.diskencryptionsets.create_or_update(resource_group_name=self.resource_group_name,
                                                                            disk_encryption_set_name=self.disk_encryption_set_name,
                                                                            location=self.location)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the DiskEncryptionSet instance.')
            self.fail('Error creating the DiskEncryptionSet instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.diskencryptionsets.delete(resource_group_name=self.resource_group_name,
                                                                  disk_encryption_set_name=self.disk_encryption_set_name)
        except CloudError as e:
            self.log('Error attempting to delete the DiskEncryptionSet instance.')
            self.fail('Error deleting the DiskEncryptionSet instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        found = False
        try:
            response = self.mgmt_client.diskencryptionsets.get(resource_group_name=self.resource_group_name,
                                                               disk_encryption_set_name=self.disk_encryption_set_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMDiskEncryptionSet()


if __name__ == '__main__':
    main()
