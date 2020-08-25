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


class AzureRMDisk(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str'
            ),
            disk_name=dict(
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
            os_type=dict(
                type='sealed-choice',
                disposition='/os_type'
            ),
            hyper_vgeneration=dict(
                type='choice',
                disposition='/hyper_vgeneration'
            ),
            creation_data=dict(
                type='dict',
                disposition='/creation_data',
                options=dict(
                    create_option=dict(
                        type='choice',
                        disposition='create_option',
                        required=True
                    ),
                    storage_account_id=dict(
                        type='str',
                        disposition='storage_account_id'
                    ),
                    image_reference=dict(
                        type='dict',
                        disposition='image_reference',
                        options=dict(
                            id=dict(
                                type='str',
                                disposition='id',
                                required=True
                            ),
                            lun=dict(
                                type='integer',
                                disposition='lun'
                            )
                        )
                    ),
                    gallery_image_reference=dict(
                        type='dict',
                        disposition='gallery_image_reference',
                        options=dict(
                            id=dict(
                                type='str',
                                disposition='id',
                                required=True
                            ),
                            lun=dict(
                                type='integer',
                                disposition='lun'
                            )
                        )
                    ),
                    source_uri=dict(
                        type='str',
                        disposition='source_uri'
                    ),
                    source_resource_id=dict(
                        type='str',
                        disposition='source_resource_id'
                    ),
                    source_unique_id=dict(
                        type='str',
                        updatable=False,
                        disposition='source_unique_id'
                    ),
                    upload_size_bytes=dict(
                        type='integer',
                        disposition='upload_size_bytes'
                    )
                )
            ),
            disk_size_gb=dict(
                type='integer',
                disposition='/disk_size_gb'
            ),
            encryption_settings_collection=dict(
                type='dict',
                disposition='/encryption_settings_collection',
                options=dict(
                    enabled=dict(
                        type='bool',
                        disposition='enabled',
                        required=True
                    ),
                    encryption_settings=dict(
                        type='list',
                        disposition='encryption_settings'
                    ),
                    encryption_settings_version=dict(
                        type='str',
                        disposition='encryption_settings_version'
                    )
                )
            ),
            disk_iops_read_write=dict(
                type='integer',
                disposition='/disk_iops_read_write'
            ),
            disk_mbps_read_write=dict(
                type='integer',
                disposition='/disk_mbps_read_write'
            ),
            disk_iops_read_only=dict(
                type='integer',
                disposition='/disk_iops_read_only'
            ),
            disk_mbps_read_only=dict(
                type='integer',
                disposition='/disk_mbps_read_only'
            ),
            encryption=dict(
                type='dict',
                disposition='/encryption',
                options=dict(
                    disk_encryption_set_id=dict(
                        type='str',
                        disposition='disk_encryption_set_id'
                    ),
                    type=dict(
                        type='choice',
                        disposition='type'
                    )
                )
            ),
            max_shares=dict(
                type='integer',
                disposition='/max_shares'
            ),
            network_access_policy=dict(
                type='choice',
                disposition='/network_access_policy'
            ),
            disk_access_id=dict(
                type='str',
                disposition='/disk_access_id'
            ),
            name=dict(
                type='choice',
                disposition='/name'
            ),
            access=dict(
                type='choice',
                disposition='/access'
            ),
            duration_in_seconds=dict(
                type='integer',
                disposition='/duration_in_seconds'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group_name = None
        self.disk_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMDisk, self).__init__(derived_arg_spec=self.module_arg_spec,
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
            response = self.mgmt_client.disks.create_or_update(resource_group_name=self.resource_group_name,
                                                               disk_name=self.disk_name,
                                                               parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the Disk instance.')
            self.fail('Error creating the Disk instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.disks.delete(resource_group_name=self.resource_group_name,
                                                     disk_name=self.disk_name)
        except CloudError as e:
            self.log('Error attempting to delete the Disk instance.')
            self.fail('Error deleting the Disk instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        found = False
        try:
            response = self.mgmt_client.disks.get(resource_group_name=self.resource_group_name,
                                                  disk_name=self.disk_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMDisk()


if __name__ == '__main__':
    main()
