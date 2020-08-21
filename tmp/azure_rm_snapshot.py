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


class AzureRMSnapshot(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str'
            ),
            snapshot_name=dict(
                type='str'
            ),
            location=dict(
                type='str',
                disposition='null'
            ),
            os_type=dict(
                type='sealed-choice',
                disposition='null'
            ),
            hyper_vgeneration=dict(
                type='choice',
                disposition='null'
            ),
            creation_data=dict(
                type='dict',
                disposition='null',
                options=dict(
                    create_option=dict(
                        type='choice',
                        disposition='null',
                        required=true
                    ),
                    storage_account_id=dict(
                        type='str',
                        disposition='null'
                    ),
                    image_reference=dict(
                        type='dict',
                        disposition='null',
                        options=dict(
                            id=dict(
                                type='str',
                                disposition='null',
                                required=true
                            ),
                            lun=dict(
                                type='integer',
                                disposition='null'
                            )
                        )
                    ),
                    gallery_image_reference=dict(
                        type='dict',
                        disposition='null',
                        options=dict(
                            id=dict(
                                type='str',
                                disposition='null',
                                required=true
                            ),
                            lun=dict(
                                type='integer',
                                disposition='null'
                            )
                        )
                    ),
                    source_uri=dict(
                        type='str',
                        disposition='null'
                    ),
                    source_resource_id=dict(
                        type='str',
                        disposition='null'
                    ),
                    source_unique_id=dict(
                        type='str',
                        updatable=False,
                        disposition='null'
                    ),
                    upload_size_bytes=dict(
                        type='integer',
                        disposition='null'
                    )
                )
            ),
            disk_size_gb=dict(
                type='integer',
                disposition='null'
            ),
            encryption_settings_collection=dict(
                type='dict',
                disposition='null',
                options=dict(
                    enabled=dict(
                        type='bool',
                        disposition='null',
                        required=true
                    ),
                    encryption_settings=dict(
                        type='list',
                        disposition='null'
                    ),
                    encryption_settings_version=dict(
                        type='str',
                        disposition='null'
                    )
                )
            ),
            incremental=dict(
                type='bool',
                disposition='null'
            ),
            encryption=dict(
                type='dict',
                disposition='null',
                options=dict(
                    disk_encryption_set_id=dict(
                        type='str',
                        disposition='null'
                    ),
                    type=dict(
                        type='choice',
                        disposition='null'
                    )
                )
            ),
            network_access_policy=dict(
                type='choice',
                disposition='null'
            ),
            disk_access_id=dict(
                type='str',
                disposition='null'
            ),
            name=dict(
                type='choice',
                disposition='null'
            ),
            access=dict(
                type='choice',
                disposition='null'
            ),
            duration_in_seconds=dict(
                type='integer',
                disposition='null'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group_name = None
        self.snapshot_name = None
        self.location = None
        self.tags = None
        self.os_type = None
        self.hyper_vgeneration = None
        self.creation_data = None
        self.disk_size_gb = None
        self.encryption_settings_collection = None
        self.incremental = None
        self.encryption = None
        self.network_access_policy = None
        self.disk_access_id = None
        self.name = None
        self.access = None
        self.duration_in_seconds = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMSnapshot, self).__init__(derived_arg_spec=self.module_arg_spec,
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
            response = self.mgmt_client.snapshots.create_or_update(resource_group_name=self.resource_group_name,
                                                                   snapshot_name=self.snapshot_name,
                                                                   location=self.location)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the Snapshot instance.')
            self.fail('Error creating the Snapshot instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.snapshots.delete(resource_group_name=self.resource_group_name,
                                                         snapshot_name=self.snapshot_name)
        except CloudError as e:
            self.log('Error attempting to delete the Snapshot instance.')
            self.fail('Error deleting the Snapshot instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        found = False
        try:
            response = self.mgmt_client.snapshots.get(resource_group_name=self.resource_group_name,
                                                      snapshot_name=self.snapshot_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMSnapshot()


if __name__ == '__main__':
    main()
