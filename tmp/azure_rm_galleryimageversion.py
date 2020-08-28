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
      - >-
        The name of the gallery Image Definition in which the Image Version is
        to be updated.
      - >-
        The name of the gallery Image Definition in which the Image Version
        resides.
    required: true
    type: str
  gallery_image_version_name:
    description:
      - >-
        The name of the gallery Image Version to be created. Needs to follow
        semantic version name pattern: The allowed characters are digit and
        period. Digits must be within the range of a 32-bit integer. Format:
        :code:`<MajorVersion>`.:code:`<MinorVersion>`.:code:`<Patch>`
      - >-
        The name of the gallery Image Version to be updated. Needs to follow
        semantic version name pattern: The allowed characters are digit and
        period. Digits must be within the range of a 32-bit integer. Format:
        :code:`<MajorVersion>`.:code:`<MinorVersion>`.:code:`<Patch>`
      - The name of the gallery Image Version to be retrieved.
      - The name of the gallery Image Version to be deleted.
    required: true
    type: str
  gallery_image_version:
    description:
      - >-
        Parameters supplied to the create or update gallery Image Version
        operation.
      - Parameters supplied to the update gallery Image Version operation.
    type: dict
    suboptions:
      publishing_profile:
        description:
          - Describes the basic gallery artifact publishing profile.
        type: dict
        suboptions:
          target_regions:
            description:
              - >-
                The target regions where the Image Version is going to be
                replicated to. This property is updatable.
            type: list
            suboptions:
              name:
                description:
                  - The name of the region.
                required: true
                type: str
              regional_replica_count:
                description:
                  - >-
                    The number of replicas of the Image Version to be created
                    per region. This property is updatable.
                type: integer
              storage_account_type:
                description:
                  - >-
                    Specifies the storage account type to be used to store the
                    image. This property is not updatable.
                type: choice
              encryption:
                description:
                  - >-
                    Optional. Allows users to provide customer managed keys for
                    encrypting the OS and data disks in the gallery artifact.
                type: dict
                suboptions:
                  os_disk_image:
                    description:
                      - This is the disk image encryption base class.
                    type: dict
                    suboptions:
                      disk_encryption_set_id:
                        description:
                          - >-
                            A relative URI containing the resource ID of the
                            disk encryption set.
                        type: str
                  data_disk_images:
                    description:
                      - >-
                        A list of encryption specifications for data disk
                        images.
                    type: list
                    suboptions:
                      lun:
                        description:
                          - >-
                            This property specifies the logical unit number of
                            the data disk. This value is used to identify data
                            disks within the Virtual Machine and therefore must
                            be unique for each data disk attached to the Virtual
                            Machine.
                        required: true
                        type: integer
          replica_count:
            description:
              - >-
                The number of replicas of the Image Version to be created per
                region. This property would take effect for a region when
                regionalReplicaCount is not specified. This property is
                updatable.
            type: integer
          exclude_from_latest:
            description:
              - >-
                If set to true, Virtual Machines deployed from the latest
                version of the Image Definition won't use this Image Version.
            type: bool
          published_date:
            description:
              - The timestamp for when the gallery Image Version is published.
            type: str
          end_of_life_date:
            description:
              - >-
                The end of life date of the gallery Image Version. This property
                can be used for decommissioning purposes. This property is
                updatable.
            type: str
          storage_account_type:
            description:
              - >-
                Specifies the storage account type to be used to store the
                image. This property is not updatable.
            type: choice
      provisioning_state:
        description:
          - 'The provisioning state, which only appears in the response.'
        type: choice
      storage_profile:
        description:
          - This is the storage profile of a Gallery Image Version.
        type: dict
        suboptions:
          source:
            description:
              - The gallery artifact version source.
            type: dict
            suboptions:
              id:
                description:
                  - >-
                    The id of the gallery artifact version source. Can specify a
                    disk uri, snapshot uri, or user image.
                type: str
          os_disk_image:
            description:
              - This is the disk image base class.
            type: dict
            suboptions:
              size_in_gb:
                description:
                  - This property indicates the size of the VHD to be created.
                type: integer
              host_caching:
                description:
                  - >-
                    The host caching of the disk. Valid values are 'None',
                    'ReadOnly', and 'ReadWrite'
                type: sealed-choice
              source:
                description:
                  - The gallery artifact version source.
                type: dict
                suboptions:
                  id:
                    description:
                      - >-
                        The id of the gallery artifact version source. Can
                        specify a disk uri, snapshot uri, or user image.
                    type: str
          data_disk_images:
            description:
              - A list of data disk images.
            type: list
            suboptions:
              lun:
                description:
                  - >-
                    This property specifies the logical unit number of the data
                    disk. This value is used to identify data disks within the
                    Virtual Machine and therefore must be unique for each data
                    disk attached to the Virtual Machine.
                required: true
                type: integer
      replication_status:
        description:
          - This is the replication status of the gallery Image Version.
        type: dict
        suboptions:
          aggregated_state:
            description:
              - >-
                This is the aggregated replication status based on all the
                regional replication status flags.
            type: choice
          summary:
            description:
              - This is a summary of replication status for each region.
            type: list
            suboptions:
              region:
                description:
                  - >-
                    The region to which the gallery Image Version is being
                    replicated to.
                type: str
              state:
                description:
                  - This is the regional replication state.
                type: choice
              details:
                description:
                  - The details of the replication status.
                type: str
              progress:
                description:
                  - It indicates progress of the replication job.
                type: integer
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

EXAMPLES = '''
    - name: Create or update a simple Gallery Image Version (Managed Image as source).
      azure_rm_galleryimageversion: 
        gallery_image_name: myGalleryImageName
        gallery_image_version:
          location: West US
          properties:
            publishing_profile:
              target_regions:
                - encryption:
                    data_disk_images:
                      - disk_encryption_set_id: >-
                          /subscriptions/{subscriptionId}/resourceGroups/myResourceGroup/providers/Microsoft.Compute/diskEncryptionSet/myOtherDiskEncryptionSet
                        lun: 0
                      - disk_encryption_set_id: >-
                          /subscriptions/{subscriptionId}/resourceGroups/myResourceGroup/providers/Microsoft.Compute/diskEncryptionSet/myDiskEncryptionSet
                        lun: 1
                    os_disk_image:
                      disk_encryption_set_id: >-
                        /subscriptions/{subscriptionId}/resourceGroups/myResourceGroup/providers/Microsoft.Compute/diskEncryptionSet/myDiskEncryptionSet
                  name: West US
                  regional_replica_count: 1
                - name: East US
                  regional_replica_count: 2
                  storage_account_type: Standard_ZRS
            storage_profile:
              source:
                id: >-
                  /subscriptions/{subscriptionId}/resourceGroups/{resourceGroup}/providers/Microsoft.Compute/images/{imageName}
        gallery_image_version_name: 1.0.0
        gallery_name: myGalleryName
        resource_group_name: myResourceGroup
        

    - name: Create or update a simple Gallery Image Version using snapshots as a source.
      azure_rm_galleryimageversion: 
        gallery_image_name: myGalleryImageName
        gallery_image_version:
          location: West US
          properties:
            publishing_profile:
              target_regions:
                - encryption:
                    data_disk_images:
                      - disk_encryption_set_id: >-
                          /subscriptions/{subscriptionId}/resourceGroups/myResourceGroup/providers/Microsoft.Compute/diskEncryptionSet/myOtherDiskEncryptionSet
                        lun: 1
                    os_disk_image:
                      disk_encryption_set_id: >-
                        /subscriptions/{subscriptionId}/resourceGroups/myResourceGroup/providers/Microsoft.Compute/diskEncryptionSet/myDiskEncryptionSet
                  name: West US
                  regional_replica_count: 1
                - name: East US
                  regional_replica_count: 2
                  storage_account_type: Standard_ZRS
            storage_profile:
              data_disk_images:
                - host_caching: None
                  lun: 1
                  source:
                    id: >-
                      /subscriptions/{subscriptionId}/resourceGroups/{resourceGroup}/providers/Microsoft.Compute/snapshots/{diskSnapshotName}
              os_disk_image:
                host_caching: ReadOnly
                source:
                  id: >-
                    /subscriptions/{subscriptionId}/resourceGroups/{resourceGroup}/providers/Microsoft.Compute/snapshots/{snapshotName}
        gallery_image_version_name: 1.0.0
        gallery_name: myGalleryName
        resource_group_name: myResourceGroup
        

    - name: Update a simple Gallery Image Version (Managed Image as source).
      azure_rm_galleryimageversion: 
        gallery_image_name: myGalleryImageName
        gallery_image_version:
          properties:
            publishing_profile:
              target_regions:
                - name: West US
                  regional_replica_count: 1
                - name: East US
                  regional_replica_count: 2
                  storage_account_type: Standard_ZRS
            storage_profile:
              source:
                id: >-
                  /subscriptions/{subscriptionId}/resourceGroups/{resourceGroup}/providers/Microsoft.Compute/images/{imageName}
        gallery_image_version_name: 1.0.0
        gallery_name: myGalleryName
        resource_group_name: myResourceGroup
        

    - name: Delete a gallery Image Version.
      azure_rm_galleryimageversion: 
        gallery_image_name: myGalleryImageName
        gallery_image_version_name: 1.0.0
        gallery_name: myGalleryName
        resource_group_name: myResourceGroup
        

'''

RETURN = '''
id:
  description:
    - Resource Id
  returned: always
  type: str
  sample: null
name:
  description:
    - Resource name
  returned: always
  type: str
  sample: null
type:
  description:
    - Resource type
  returned: always
  type: str
  sample: null
location:
  description:
    - Resource location
  returned: always
  type: str
  sample: null
tags:
  description:
    - Resource tags
  returned: always
  type: dictionary
  sample: null
publishing_profile:
  description:
    - Describes the basic gallery artifact publishing profile.
  returned: always
  type: dict
  sample: null
  contains:
    target_regions:
      description:
        - >-
          The target regions where the Image Version is going to be replicated
          to. This property is updatable.
      returned: always
      type: list
      sample: null
      contains:
        name:
          description:
            - The name of the region.
          returned: always
          type: str
          sample: null
        regional_replica_count:
          description:
            - >-
              The number of replicas of the Image Version to be created per
              region. This property is updatable.
          returned: always
          type: integer
          sample: null
        storage_account_type:
          description:
            - >-
              Specifies the storage account type to be used to store the image.
              This property is not updatable.
          returned: always
          type: choice
          sample: null
        encryption:
          description:
            - >-
              Optional. Allows users to provide customer managed keys for
              encrypting the OS and data disks in the gallery artifact.
          returned: always
          type: dict
          sample: null
          contains:
            os_disk_image:
              description:
                - This is the disk image encryption base class.
              returned: always
              type: dict
              sample: null
              contains:
                disk_encryption_set_id:
                  description:
                    - >-
                      A relative URI containing the resource ID of the disk
                      encryption set.
                  returned: always
                  type: str
                  sample: null
            data_disk_images:
              description:
                - A list of encryption specifications for data disk images.
              returned: always
              type: list
              sample: null
              contains:
                lun:
                  description:
                    - >-
                      This property specifies the logical unit number of the
                      data disk. This value is used to identify data disks
                      within the Virtual Machine and therefore must be unique
                      for each data disk attached to the Virtual Machine.
                  returned: always
                  type: integer
                  sample: null
    replica_count:
      description:
        - >-
          The number of replicas of the Image Version to be created per region.
          This property would take effect for a region when regionalReplicaCount
          is not specified. This property is updatable.
      returned: always
      type: integer
      sample: null
    exclude_from_latest:
      description:
        - >-
          If set to true, Virtual Machines deployed from the latest version of
          the Image Definition won't use this Image Version.
      returned: always
      type: bool
      sample: null
    published_date:
      description:
        - The timestamp for when the gallery Image Version is published.
      returned: always
      type: str
      sample: null
    end_of_life_date:
      description:
        - >-
          The end of life date of the gallery Image Version. This property can
          be used for decommissioning purposes. This property is updatable.
      returned: always
      type: str
      sample: null
    storage_account_type:
      description:
        - >-
          Specifies the storage account type to be used to store the image. This
          property is not updatable.
      returned: always
      type: choice
      sample: null
provisioning_state:
  description:
    - 'The provisioning state, which only appears in the response.'
  returned: always
  type: choice
  sample: null
storage_profile:
  description:
    - This is the storage profile of a Gallery Image Version.
  returned: always
  type: dict
  sample: null
  contains:
    source:
      description:
        - The gallery artifact version source.
      returned: always
      type: dict
      sample: null
      contains:
        id:
          description:
            - >-
              The id of the gallery artifact version source. Can specify a disk
              uri, snapshot uri, or user image.
          returned: always
          type: str
          sample: null
    os_disk_image:
      description:
        - This is the disk image base class.
      returned: always
      type: dict
      sample: null
      contains:
        size_in_gb:
          description:
            - This property indicates the size of the VHD to be created.
          returned: always
          type: integer
          sample: null
        host_caching:
          description:
            - >-
              The host caching of the disk. Valid values are 'None', 'ReadOnly',
              and 'ReadWrite'
          returned: always
          type: sealed-choice
          sample: null
        source:
          description:
            - The gallery artifact version source.
          returned: always
          type: dict
          sample: null
          contains:
            id:
              description:
                - >-
                  The id of the gallery artifact version source. Can specify a
                  disk uri, snapshot uri, or user image.
              returned: always
              type: str
              sample: null
    data_disk_images:
      description:
        - A list of data disk images.
      returned: always
      type: list
      sample: null
      contains:
        lun:
          description:
            - >-
              This property specifies the logical unit number of the data disk.
              This value is used to identify data disks within the Virtual
              Machine and therefore must be unique for each data disk attached
              to the Virtual Machine.
          returned: always
          type: integer
          sample: null
replication_status:
  description:
    - This is the replication status of the gallery Image Version.
  returned: always
  type: dict
  sample: null
  contains:
    aggregated_state:
      description:
        - >-
          This is the aggregated replication status based on all the regional
          replication status flags.
      returned: always
      type: choice
      sample: null
    summary:
      description:
        - This is a summary of replication status for each region.
      returned: always
      type: list
      sample: null
      contains:
        region:
          description:
            - >-
              The region to which the gallery Image Version is being replicated
              to.
          returned: always
          type: str
          sample: null
        state:
          description:
            - This is the regional replication state.
          returned: always
          type: choice
          sample: null
        details:
          description:
            - The details of the replication status.
          returned: always
          type: str
          sample: null
        progress:
          description:
            - It indicates progress of the replication job.
          returned: always
          type: integer
          sample: null

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
                type='str',
                required=True
            ),
            gallery_image_version=dict(
                type='dict',
                disposition='/gallery_image_version',
                options=dict(
                    publishing_profile=dict(
                        type='dict',
                        disposition='publishing_profile',
                        options=dict(
                            target_regions=dict(
                                type='list',
                                disposition='target_regions',
                                elements='dict',
                                options=dict(
                                    name=dict(
                                        type='str',
                                        disposition='name',
                                        required=True
                                    ),
                                    regional_replica_count=dict(
                                        type='integer',
                                        disposition='regional_replica_count'
                                    ),
                                    storage_account_type=dict(
                                        type='choice',
                                        disposition='storage_account_type'
                                    ),
                                    encryption=dict(
                                        type='dict',
                                        disposition='encryption',
                                        options=dict(
                                            os_disk_image=dict(
                                                type='dict',
                                                disposition='os_disk_image',
                                                options=dict(
                                                    disk_encryption_set_id=dict(
                                                        type='str',
                                                        disposition='disk_encryption_set_id'
                                                    )
                                                )
                                            ),
                                            data_disk_images=dict(
                                                type='list',
                                                disposition='data_disk_images',
                                                elements='dict',
                                                options=dict(
                                                    lun=dict(
                                                        type='integer',
                                                        disposition='lun',
                                                        required=True
                                                    )
                                                )
                                            )
                                        )
                                    )
                                )
                            ),
                            replica_count=dict(
                                type='integer',
                                disposition='replica_count'
                            ),
                            exclude_from_latest=dict(
                                type='bool',
                                disposition='exclude_from_latest'
                            ),
                            published_date=dict(
                                type='str',
                                disposition='published_date'
                            ),
                            end_of_life_date=dict(
                                type='str',
                                disposition='end_of_life_date'
                            ),
                            storage_account_type=dict(
                                type='choice',
                                disposition='storage_account_type'
                            )
                        )
                    ),
                    provisioning_state=dict(
                        type='choice',
                        disposition='provisioning_state'
                    ),
                    storage_profile=dict(
                        type='dict',
                        disposition='storage_profile',
                        options=dict(
                            source=dict(
                                type='dict',
                                disposition='source',
                                options=dict(
                                    id=dict(
                                        type='str',
                                        disposition='id'
                                    )
                                )
                            ),
                            os_disk_image=dict(
                                type='dict',
                                disposition='os_disk_image',
                                options=dict(
                                    size_in_gb=dict(
                                        type='integer',
                                        disposition='size_in_gb'
                                    ),
                                    host_caching=dict(
                                        type='sealed-choice',
                                        disposition='host_caching'
                                    ),
                                    source=dict(
                                        type='dict',
                                        disposition='source',
                                        options=dict(
                                            id=dict(
                                                type='str',
                                                disposition='id'
                                            )
                                        )
                                    )
                                )
                            ),
                            data_disk_images=dict(
                                type='list',
                                disposition='data_disk_images',
                                elements='dict',
                                options=dict(
                                    lun=dict(
                                        type='integer',
                                        disposition='lun',
                                        required=True
                                    )
                                )
                            )
                        )
                    ),
                    replication_status=dict(
                        type='dict',
                        disposition='replication_status',
                        options=dict(
                            aggregated_state=dict(
                                type='choice',
                                disposition='aggregated_state'
                            ),
                            summary=dict(
                                type='list',
                                disposition='summary',
                                elements='dict',
                                options=dict(
                                    region=dict(
                                        type='str',
                                        disposition='region'
                                    ),
                                    state=dict(
                                        type='choice',
                                        disposition='state'
                                    ),
                                    details=dict(
                                        type='str',
                                        disposition='details'
                                    ),
                                    progress=dict(
                                        type='integer',
                                        disposition='progress'
                                    )
                                )
                            )
                        )
                    )
                )
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
            response = self.mgmt_client.gallery_image_versions.create_or_update(resource_group_name=self.resource_group_name,
                                                                                gallery_name=self.gallery_name,
                                                                                gallery_image_name=self.gallery_image_name,
                                                                                gallery_image_version_name=self.gallery_image_version_name,
                                                                                parameters=self.body)
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
