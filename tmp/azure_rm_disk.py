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
from ansible.module_utils.azure_rm_common_rest import GenericRestClient
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
except ImportError:
    # this is handled in azure_rm_common
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
                disposition='/properties/zones'
            ),
            os_type=dict(
                type='sealed-choice',
                disposition='/properties/osType'
            ),
            hyper_vgeneration=dict(
                type='choice',
                disposition='/properties/hyperVGeneration'
            ),
            creation_data=dict(
                type='dict',
                disposition='/properties/creationData',
                options=dict(
                    create_option=dict(
                        type='choice',
                        disposition='/createOption',
                        required=true
                    ),
                    storage_account_id=dict(
                        type='str',
                        disposition='/storageAccountId'
                    ),
                    image_reference=dict(
                        type='dict',
                        disposition='/imageReference',
                        options=dict(
                            id=dict(
                                type='str',
                                disposition='/id',
                                required=true
                            ),
                            lun=dict(
                                type='integer',
                                disposition='/lun'
                            )
                        )
                    ),
                    gallery_image_reference=dict(
                        type='dict',
                        disposition='/galleryImageReference',
                        options=dict(
                            id=dict(
                                type='str',
                                disposition='/id',
                                required=true
                            ),
                            lun=dict(
                                type='integer',
                                disposition='/lun'
                            )
                        )
                    ),
                    source_uri=dict(
                        type='str',
                        disposition='/sourceUri'
                    ),
                    source_resource_id=dict(
                        type='str',
                        disposition='/sourceResourceId'
                    ),
                    source_unique_id=dict(
                        type='str',
                        disposition='/sourceUniqueId'
                    ),
                    upload_size_bytes=dict(
                        type='integer',
                        disposition='/uploadSizeBytes'
                    )
                )
            ),
            disk_size_gb=dict(
                type='integer',
                disposition='/properties/diskSizeGB'
            ),
            encryption_settings_collection=dict(
                type='dict',
                disposition='/properties/encryptionSettingsCollection',
                options=dict(
                    enabled=dict(
                        type='bool',
                        disposition='/enabled',
                        required=true
                    ),
                    encryption_settings=dict(
                        type='list',
                        disposition='/encryptionSettings'
                    ),
                    encryption_settings_version=dict(
                        type='str',
                        disposition='/encryptionSettingsVersion'
                    )
                )
            ),
            disk_iops_read_write=dict(
                type='integer',
                disposition='/properties/diskIopsReadWrite'
            ),
            disk_mbps_read_write=dict(
                type='integer',
                disposition='/properties/diskMBpsReadWrite'
            ),
            disk_iops_read_only=dict(
                type='integer',
                disposition='/properties/diskIopsReadOnly'
            ),
            disk_mbps_read_only=dict(
                type='integer',
                disposition='/properties/diskMBpsReadOnly'
            ),
            encryption=dict(
                type='dict',
                disposition='/properties/encryption',
                options=dict(
                    disk_encryption_set_id=dict(
                        type='str',
                        disposition='/diskEncryptionSetId'
                    ),
                    type=dict(
                        type='choice',
                        disposition='/type'
                    )
                )
            ),
            max_shares=dict(
                type='integer',
                disposition='/properties/maxShares'
            ),
            network_access_policy=dict(
                type='choice',
                disposition='/properties/networkAccessPolicy'
            ),
            disk_access_id=dict(
                type='str',
                disposition='/properties/diskAccessId'
            ),
            name=dict(
                type='choice',
                disposition='/properties/name'
            ),
            access=dict(
                type='choice',
                disposition='/properties/access'
            ),
            duration_in_seconds=dict(
                type='integer',
                disposition='/properties/durationInSeconds'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group_name = None
        self.disk_name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200, 201, 202]
        self.to_do = Actions.NoAction

        self.body = {}
        self.query_parameters = {}
        self.query_parameters['api-version'] = '2020-05-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

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

        self.mgmt_client = self.get_mgmt_svc_client(GenericRestClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        self.url= '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/disks/{diskName}'
        self.url = self.url.replace('{subscriptionId}', self.subscription_id)
        self.url = self.url.replace('{resourceGroupName}', self.resource_group_name)
        self.url = self.url.replace('{diskName}', self.disk_name)

        old_response = self.get_resource()

        if not old_response:
            self.log("Disk instance doesn't exist")

            if self.state == 'absent':
                self.log("Old instance didn't exist")
            else:
                self.to_do = Actions.Create
        else:
            self.log('Disk instance already exists')

            if self.state == 'absent':
                self.to_do = Actions.Delete
            else:
                modifiers = {}
                self.create_compare_modifiers(self.module_arg_spec, '', modifiers)
                self.results['modifiers'] = modifiers
                self.results['compare'] = []
                self.create_compare_modifiers(self.module_arg_spec, '', modifiers)
                if not self.default_compare(modifiers, self.body, old_response, '', self.results):
                    self.to_do = Actions.Update

        if (self.to_do == Actions.Create) or (self.to_do == Actions.Update):
            self.log('Need to Create / Update the Disk instance')

            if self.check_mode:
                self.results['changed'] = True
                return self.results

            response = self.create_update_resource()

            # if not old_response:
            self.results['changed'] = True
            # else:
            #     self.results['changed'] = old_response.__ne__(response)
            self.log('Creation / Update done')
        elif self.to_do == Actions.Delete:
            self.log('Disk instance deleted')
            self.results['changed'] = True

            if self.check_mode:
                return self.results

            self.delete_resource()

            # make sure instance is actually deleted, for some Azure resources, instance is hanging around
            # for some time after deletion -- this should be really fixed in Azure
            while self.get_resource():
                time.sleep(20)
        else:
            self.log('Disk instance unchanged')
            self.results['changed'] = False
            response = old_response

        return self.results

    def create_update_resource(self):

        try:
            response = self.mgmt_client.query(self.url,
                                              'PUT',
                                              self.query_parameters,
                                              self.header_parameters,
                                              self.body,
                                              self.status_code,
                                              600,
                                              30)
        except CloudError as exc:
            self.log('Error attempting to create the Disk instance.')
            self.fail('Error creating the Disk instance: {0}'.format(str(exc)))

        try:
            response = json.loads(response.text)
        except Exception:
            response = {'text': response.text}
            pass

        return response

    def delete_resource(self):
        try:
            response = self.mgmt_client.query(self.url,
                                              'DELETE',
                                              self.query_parameters,
                                              self.header_parameters,
                                              None,
                                              self.status_code,
                                              600,
                                              30)
        except CloudError as e:
            self.log('Error attempting to delete the Disk instance.')
            self.fail('Error deleting the Disk instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        found = False
        try:
            response = self.mgmt_client.query(self.url,
                                              'GET',
                                              self.query_parameters,
                                              self.header_parameters,
                                              None,
                                              self.status_code,
                                              600,
                                              30)
            found = True
            self.log("Response : {0}".format(response))
            # self.log("Disk instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the Disk instance.')
        if found is True:
            return response

        return False


def main():
    AzureRMDisk()


if __name__ == '__main__':
    main()
