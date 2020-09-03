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
module: azure_rm_galleryapplicationversion_info
version_added: '2.9'
short_description: Get GalleryApplicationVersion info.
description:
  - Get info of GalleryApplicationVersion.
options:
  resource_group_name:
    description:
      - The name of the resource group.
    required: true
    type: str
  gallery_name:
    description:
      - >-
        The name of the Shared Application Gallery in which the Application
        Definition resides.
    required: true
    type: str
  gallery_application_name:
    description:
      - >-
        The name of the gallery Application Definition in which the Application
        Version resides.
      - >-
        The name of the Shared Application Gallery Application Definition from
        which the Application Versions are to be listed.
    required: true
    type: str
  gallery_application_version_name:
    description:
      - The name of the gallery Application Version to be retrieved.
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
    - name: Get a gallery Application Version with replication status.
      azure_rm_galleryapplicationversion_info: 
        gallery_application_name: myGalleryApplicationName
        gallery_application_version_name: 1.0.0
        gallery_name: myGalleryName
        resource_group_name: myResourceGroup
        

    - name: Get a gallery Application Version.
      azure_rm_galleryapplicationversion_info: 
        gallery_application_name: myGalleryApplicationName
        gallery_application_version_name: 1.0.0
        gallery_name: myGalleryName
        resource_group_name: myResourceGroup
        

    - name: List gallery Application Versions in a gallery Application Definition.
      azure_rm_galleryapplicationversion_info: 
        gallery_application_name: myGalleryApplicationName
        gallery_name: myGalleryName
        resource_group_name: myResourceGroup
        

'''

RETURN = '''
gallery_application_versions:
  description: >-
    A list of dict results where the key is the name of the
    GalleryApplicationVersion and the values are the facts for that
    GalleryApplicationVersion.
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
    source:
      description:
        - The source image from which the Image Version is going to be created.
      returned: always
      type: dict
      sample: null
      contains:
        file_name:
          description:
            - Required. The fileName of the artifact.
          returned: always
          type: str
          sample: null
        media_link:
          description:
            - >-
              Required. The mediaLink of the artifact, must be a readable
              storage blob.
          returned: always
          type: str
          sample: null
    content_type:
      description:
        - >-
          Optional. May be used to help process this file. The type of file
          contained in the source, e.g. zip, json, etc.
      returned: always
      type: str
      sample: null
    enable_health_check:
      description:
        - Optional. Whether or not this application reports health.
      returned: always
      type: bool
      sample: null
    value:
      description:
        - A list of gallery Application Versions.
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
        source:
          description:
            - >-
              The source image from which the Image Version is going to be
              created.
          returned: always
          type: dict
          sample: null
          contains:
            file_name:
              description:
                - Required. The fileName of the artifact.
              returned: always
              type: str
              sample: null
            media_link:
              description:
                - >-
                  Required. The mediaLink of the artifact, must be a readable
                  storage blob.
              returned: always
              type: str
              sample: null
        content_type:
          description:
            - >-
              Optional. May be used to help process this file. The type of file
              contained in the source, e.g. zip, json, etc.
          returned: always
          type: str
          sample: null
        enable_health_check:
          description:
            - Optional. Whether or not this application reports health.
          returned: always
          type: bool
          sample: null
    next_link:
      description:
        - >-
          The uri to fetch the next page of gallery Application Versions. Call
          ListNext() with this to fetch the next page of gallery Application
          Versions.
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


class AzureRMGalleryApplicationVersionInfo(AzureRMModuleBase):
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
            gallery_application_name=dict(
                type='str',
                required=True
            ),
            gallery_application_version_name=dict(
                type='str'
            ),
            expand=dict(
                type='str',
                choices=['ReplicationStatus']
            )
        )

        self.resource_group_name = None
        self.gallery_name = None
        self.gallery_application_name = None
        self.gallery_application_version_name = None
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
        super(AzureRMGalleryApplicationVersionInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(ComputeManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2019-12-01')

        if (self.resource_group_name is not None and
            self.gallery_name is not None and
            self.gallery_application_name is not None and
            self.gallery_application_version_name is not None):
            self.results['gallery_application_versions'] = self.format_item(self.get())
        elif (self.resource_group_name is not None and
              self.gallery_name is not None and
              self.gallery_application_name is not None):
            self.results['gallery_application_versions'] = self.format_item(self.listbygalleryapplication())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.gallery_application_versions.get(resource_group_name=self.resource_group_name,
                                                                         gallery_name=self.gallery_name,
                                                                         gallery_application_name=self.gallery_application_name,
                                                                         gallery_application_version_name=self.gallery_application_version_name,
                                                                         expand=self.expand)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbygalleryapplication(self):
        response = None

        try:
            response = self.mgmt_client.gallery_application_versions.list_by_gallery_application(resource_group_name=self.resource_group_name,
                                                                                                 gallery_name=self.gallery_name,
                                                                                                 gallery_application_name=self.gallery_application_name)
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
    AzureRMGalleryApplicationVersionInfo()


if __name__ == '__main__':
    main()
