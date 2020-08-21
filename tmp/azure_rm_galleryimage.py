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


class AzureRMGalleryImage(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=true
            ),
            gallery_name=dict(
                type='str',
                required=true
            ),
            gallery_image_name=dict(
                type='str'
            ),
            location=dict(
                type='str',
                disposition='null'
            ),
            description=dict(
                type='str',
                disposition='null'
            ),
            eula=dict(
                type='str',
                disposition='null'
            ),
            privacy_statement_uri=dict(
                type='str',
                disposition='null'
            ),
            release_note_uri=dict(
                type='str',
                disposition='null'
            ),
            os_type=dict(
                type='sealed-choice',
                disposition='null'
            ),
            os_state=dict(
                type='sealed-choice',
                disposition='null'
            ),
            hyper_vgeneration=dict(
                type='choice',
                disposition='null'
            ),
            end_of_life_date=dict(
                type='str',
                disposition='null'
            ),
            identifier=dict(
                type='dict',
                disposition='null',
                options=dict(
                    publisher=dict(
                        type='str',
                        disposition='null',
                        required=true
                    ),
                    offer=dict(
                        type='str',
                        disposition='null',
                        required=true
                    ),
                    sku=dict(
                        type='str',
                        disposition='null',
                        required=true
                    )
                )
            ),
            disallowed=dict(
                type='dict',
                disposition='null',
                options=dict(
                    disk_types=dict(
                        type='list',
                        disposition='null'
                    )
                )
            ),
            purchase_plan=dict(
                type='dict',
                disposition='null',
                options=dict(
                    name=dict(
                        type='str',
                        disposition='null'
                    ),
                    publisher=dict(
                        type='str',
                        disposition='null'
                    ),
                    product=dict(
                        type='str',
                        disposition='null'
                    )
                )
            ),
            v_cp_us=dict(
                type='dict',
                disposition='null',
                options=dict(
                    min=dict(
                        type='integer',
                        disposition='null'
                    ),
                    max=dict(
                        type='integer',
                        disposition='null'
                    )
                )
            ),
            memory=dict(
                type='dict',
                disposition='null',
                options=dict(
                    min=dict(
                        type='integer',
                        disposition='null'
                    ),
                    max=dict(
                        type='integer',
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
        self.gallery_name = None
        self.gallery_image_name = None
        self.location = None
        self.tags = None
        self.description = None
        self.eula = None
        self.privacy_statement_uri = None
        self.release_note_uri = None
        self.os_type = None
        self.os_state = None
        self.hyper_vgeneration = None
        self.end_of_life_date = None
        self.identifier = None
        self.disallowed = None
        self.purchase_plan = None
        self.v_cp_us = None
        self.memory = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMGalleryImage, self).__init__(derived_arg_spec=self.module_arg_spec,
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
            response = self.mgmt_client.galleryimages.create_or_update(resource_group_name=self.resource_group_name,
                                                                       gallery_name=self.gallery_name,
                                                                       gallery_image_name=self.gallery_image_name,
                                                                       location=self.location)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the GalleryImage instance.')
            self.fail('Error creating the GalleryImage instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.galleryimages.delete(resource_group_name=self.resource_group_name,
                                                             gallery_name=self.gallery_name,
                                                             gallery_image_name=self.gallery_image_name)
        except CloudError as e:
            self.log('Error attempting to delete the GalleryImage instance.')
            self.fail('Error deleting the GalleryImage instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        found = False
        try:
            response = self.mgmt_client.galleryimages.get(resource_group_name=self.resource_group_name,
                                                          gallery_name=self.gallery_name,
                                                          gallery_image_name=self.gallery_image_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMGalleryImage()


if __name__ == '__main__':
    main()
