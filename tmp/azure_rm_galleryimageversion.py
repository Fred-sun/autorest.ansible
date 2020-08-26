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
module: azure_rm_galleryimageversion
version_added: '2.9'
short_description: Manage Azure GalleryImageVersion instance.
description:
  - 'Create, update and delete instance of Azure GalleryImageVersion.'
options:
  resource_group_name:
    description:
      - The name of the resource group.
    required: true
    type: str
  gallery_name:
    description:
      - >-
        The name of the Shared Image Gallery in which the Image Definition
        resides.
    required: true
    type: str
  gallery_image_name:
    description:
      - >-
        The name of the gallery Image Definition in which the Image Version is
        to be created.
    required: true
    type: str
  gallery_image_version_name:
    description:
      - >-
        The name of the gallery Image Version to be created. Needs to follow
        semantic version name pattern: The allowed characters are digit and
        period. Digits must be within the range of a 32-bit integer. Format:
        :code:`<MajorVersion>`.:code:`<MinorVersion>`.:code:`<Patch>`
    type: str
  location:
    description:
      - Resource location
    type: str
  data_disk_images:
    description:
      - A list of data disk images.
    type: list
  host_caching:
    description:
      - >-
        The host caching of the disk. Valid values are 'None', 'ReadOnly', and
        'ReadWrite'
    type: sealed-choice
  id:
    description:
      - >-
        The id of the gallery artifact version source. Can specify a disk uri,
        snapshot uri, or user image.
    type: str
  gallery_artifact_version_source_id:
    description:
      - >-
        The id of the gallery artifact version source. Can specify a disk uri,
        snapshot uri, or user image.
    type: str
  target_regions:
    description:
      - >-
        The target regions where the Image Version is going to be replicated to.
        This property is updatable.
    type: list
  replica_count:
    description:
      - >-
        The number of replicas of the Image Version to be created per region.
        This property would take effect for a region when regionalReplicaCount
        is not specified. This property is updatable.
    type: integer
  exclude_from_latest:
    description:
      - >-
        If set to true, Virtual Machines deployed from the latest version of the
        Image Definition won't use this Image Version.
    type: bool
  end_of_life_date:
    description:
      - >-
        The end of life date of the gallery Image Version. This property can be
        used for decommissioning purposes. This property is updatable.
    type: str
  storage_account_type:
    description:
      - >-
        Specifies the storage account type to be used to store the image. This
        property is not updatable.
    type: choice
  expand:
    description:
      - The expand expression to apply on the operation.
    type: choice
  state:
    description:
      - Assert the state of the GalleryImageVersion.
      - >-
        Use C(present) to create or update an GalleryImageVersion and C(absent)
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


class AzureRMGalleryImageVersion(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            gallery_name=dict(
                type='str',
                required=True
            ),
            gallery_image_name=dict(
                type='str',
                required=True
            ),
            gallery_image_version_name=dict(
                type='str'
            ),
            location=dict(
                type='str',
                disposition='/location'
            ),
            data_disk_images=dict(
                type='list',
                disposition='/data_disk_images'
            ),
            host_caching=dict(
                type='sealed-choice',
                disposition='/host_caching'
            ),
            id=dict(
                type='str',
                disposition='/id'
            ),
            gallery_artifact_version_source_id=dict(
                type='str',
                disposition='/gallery_artifact_version_source_id'
            ),
            target_regions=dict(
                type='list',
                disposition='/target_regions'
            ),
            replica_count=dict(
                type='integer',
                disposition='/replica_count'
            ),
            exclude_from_latest=dict(
                type='bool',
                disposition='/exclude_from_latest'
            ),
            end_of_life_date=dict(
                type='str',
                disposition='/end_of_life_date'
            ),
            storage_account_type=dict(
                type='choice',
                disposition='/storage_account_type'
            ),
            expand=dict(
                type='choice'
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
        self.gallery_image_version_name = None
        self.expand = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMGalleryImageVersion, self).__init__(derived_arg_spec=self.module_arg_spec,
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
                                                    api_version='2019-12-01')

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
                response = self.mgmt_client.gallery_image_versions.create(resource_group_name=self.resource_group_name,
                                                                          gallery_name=self.gallery_name,
                                                                          gallery_image_name=self.gallery_image_name,
                                                                          gallery_image_version_name=self.gallery_image_version_name,
                                                                          gallery_image_version=self.body)
            else:
                response = self.mgmt_client.gallery_image_versions.update(resource_group_name=self.resource_group_name,
                                                                          gallery_name=self.gallery_name,
                                                                          gallery_image_name=self.gallery_image_name,
                                                                          gallery_image_version_name=self.gallery_image_version_name,
                                                                          gallery_image_version=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the GalleryImageVersion instance.')
            self.fail('Error creating the GalleryImageVersion instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.gallery_image_versions.delete(resource_group_name=self.resource_group_name,
                                                                      gallery_name=self.gallery_name,
                                                                      gallery_image_name=self.gallery_image_name,
                                                                      gallery_image_version_name=self.gallery_image_version_name)
        except CloudError as e:
            self.log('Error attempting to delete the GalleryImageVersion instance.')
            self.fail('Error deleting the GalleryImageVersion instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        found = False
        try:
            response = self.mgmt_client.gallery_image_versions.get(resource_group_name=self.resource_group_name,
                                                                   gallery_name=self.gallery_name,
                                                                   gallery_image_name=self.gallery_image_name,
                                                                   gallery_image_version_name=self.gallery_image_version_name,
                                                                   expand=self.expand)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMGalleryImageVersion()


if __name__ == '__main__':
    main()
