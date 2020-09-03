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
module: azure_rm_galleryimageversion_info
version_added: '2.9'
short_description: Get GalleryImageVersion info.
description:
  - Get info of GalleryImageVersion.
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
        The name of the gallery Image Definition in which the Image Version
        resides.
      - >-
        The name of the Shared Image Gallery Image Definition from which the
        Image Versions are to be listed.
    required: true
    type: str
  gallery_image_version_name:
    description:
      - The name of the gallery Image Version to be retrieved.
    type: str
  expand:
    description:
      - The expand expression to apply on the operation.
    type: str
    choices:
      - ReplicationStatus
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: Get a gallery Image Version with replication status.
      azure_rm_galleryimageversion_info: 
        gallery_image_name: myGalleryImageName
        gallery_image_version_name: 1.0.0
        gallery_name: myGalleryName
        resource_group_name: myResourceGroup
        

    - name: Get a gallery Image Version with snapshots as a source.
      azure_rm_galleryimageversion_info: 
        gallery_image_name: myGalleryImageName
        gallery_image_version_name: 1.0.0
        gallery_name: myGalleryName
        resource_group_name: myResourceGroup
        

    - name: Get a gallery Image Version.
      azure_rm_galleryimageversion_info: 
        gallery_image_name: myGalleryImageName
        gallery_image_version_name: 1.0.0
        gallery_name: myGalleryName
        resource_group_name: myResourceGroup
        

    - name: List gallery Image Versions in a gallery Image Definition.
      azure_rm_galleryimageversion_info: 
        gallery_image_name: myGalleryImageName
        gallery_name: myGalleryName
        resource_group_name: myResourceGroup
        

'''

RETURN = '''
gallery_image_versions:
  description: >-
    A list of dict results where the key is the name of the GalleryImageVersion
    and the values are the facts for that GalleryImageVersion.
  returned: always
  type: complex
  contains:
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
    provisioning_state:
      description:
        - 'The provisioning state, which only appears in the response.'
      returned: always
      type: str
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
              This is the aggregated replication status based on all the
              regional replication status flags.
          returned: always
          type: str
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
                  The region to which the gallery Image Version is being
                  replicated to.
              returned: always
              type: str
              sample: null
            state:
              description:
                - This is the regional replication state.
              returned: always
              type: str
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
    size_in_gb:
      description:
        - This property indicates the size of the VHD to be created.
      returned: always
      type: integer
      sample: null
    host_caching:
      description:
        - >-
          The host caching of the disk. Valid values are 'None', 'ReadOnly', and
          'ReadWrite'
      returned: always
      type: sealed-choice
      sample: null
    id_properties_storage_profile_os_disk_image_source_id:
      description:
        - >-
          The id of the gallery artifact version source. Can specify a disk uri,
          snapshot uri, or user image.
      returned: always
      type: str
      sample: null
    id_properties_storage_profile_source_id:
      description:
        - >-
          The id of the gallery artifact version source. Can specify a disk uri,
          snapshot uri, or user image.
      returned: always
      type: str
      sample: null
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
          type: str
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
      type: str
      sample: null
    value:
      description:
        - A list of gallery Image Versions.
      returned: always
      type: list
      sample: null
      contains:
        provisioning_state:
          description:
            - 'The provisioning state, which only appears in the response.'
          returned: always
          type: str
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
                  This is the aggregated replication status based on all the
                  regional replication status flags.
              returned: always
              type: str
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
                      The region to which the gallery Image Version is being
                      replicated to.
                  returned: always
                  type: str
                  sample: null
                state:
                  description:
                    - This is the regional replication state.
                  returned: always
                  type: str
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
                  This property specifies the logical unit number of the data
                  disk. This value is used to identify data disks within the
                  Virtual Machine and therefore must be unique for each data
                  disk attached to the Virtual Machine.
              returned: always
              type: integer
              sample: null
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
        id_properties_storage_profile_os_disk_image_source_id:
          description:
            - >-
              The id of the gallery artifact version source. Can specify a disk
              uri, snapshot uri, or user image.
          returned: always
          type: str
          sample: null
        id_properties_storage_profile_source_id:
          description:
            - >-
              The id of the gallery artifact version source. Can specify a disk
              uri, snapshot uri, or user image.
          returned: always
          type: str
          sample: null
        target_regions:
          description:
            - >-
              The target regions where the Image Version is going to be
              replicated to. This property is updatable.
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
                  Specifies the storage account type to be used to store the
                  image. This property is not updatable.
              returned: always
              type: str
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
                          within the Virtual Machine and therefore must be
                          unique for each data disk attached to the Virtual
                          Machine.
                      returned: always
                      type: integer
                      sample: null
        replica_count:
          description:
            - >-
              The number of replicas of the Image Version to be created per
              region. This property would take effect for a region when
              regionalReplicaCount is not specified. This property is updatable.
          returned: always
          type: integer
          sample: null
        exclude_from_latest:
          description:
            - >-
              If set to true, Virtual Machines deployed from the latest version
              of the Image Definition won't use this Image Version.
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
              The end of life date of the gallery Image Version. This property
              can be used for decommissioning purposes. This property is
              updatable.
          returned: always
          type: str
          sample: null
        storage_account_type:
          description:
            - >-
              Specifies the storage account type to be used to store the image.
              This property is not updatable.
          returned: always
          type: str
          sample: null
    next_link:
      description:
        - >-
          The uri to fetch the next page of gallery Image Versions. Call
          ListNext() with this to fetch the next page of gallery Image Versions.
      returned: always
      type: str
      sample: null

'''

import time
import json
from ansible.module_utils.azure_rm_common import AzureRMModuleBase
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.compute import ComputeManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMGalleryImageVersionInfo(AzureRMModuleBase):
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
            expand=dict(
                type='str',
                choices=['ReplicationStatus']
            )
        )

        self.resource_group_name = None
        self.gallery_name = None
        self.gallery_image_name = None
        self.gallery_image_version_name = None
        self.expand = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2019-12-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMGalleryImageVersionInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(ComputeManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2019-12-01')

        if (self.resource_group_name is not None and
            self.gallery_name is not None and
            self.gallery_image_name is not None and
            self.gallery_image_version_name is not None):
            self.results['gallery_image_versions'] = self.format_item(self.get())
        elif (self.resource_group_name is not None and
              self.gallery_name is not None and
              self.gallery_image_name is not None):
            self.results['gallery_image_versions'] = self.format_item(self.listbygalleryimage())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.gallery_image_versions.get(resource_group_name=self.resource_group_name,
                                                                   gallery_name=self.gallery_name,
                                                                   gallery_image_name=self.gallery_image_name,
                                                                   gallery_image_version_name=self.gallery_image_version_name,
                                                                   expand=self.expand)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbygalleryimage(self):
        response = None

        try:
            response = self.mgmt_client.gallery_image_versions.list_by_gallery_image(resource_group_name=self.resource_group_name,
                                                                                     gallery_name=self.gallery_name,
                                                                                     gallery_image_name=self.gallery_image_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def format_item(self, item):
        if hasattr(item, 'as_dict'):
            return [item.as_dict()]
        else:
            result = []
            items = list(item)
            for tmp in items:
               result.append(tmp.as_dict())
            return result


def main():
    AzureRMGalleryImageVersionInfo()


if __name__ == '__main__':
    main()
