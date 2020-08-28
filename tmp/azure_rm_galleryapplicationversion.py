#!/usr/bin/python,#,# Copyright (c) 2020 GuopengLin, (@t-glin),#,# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt),,from __future__ import absolute_import, division, print_function,__metaclass__ = type,,,ANSIBLE_METADATA = {'metadata_version': '1.1',,                    'status': ['preview'],,                    'supported_by': 'community'},,,DOCUMENTATION = ''',---,module: azure_rm_galleryapplicationversion
version_added: '2.9'
short_description: Manage Azure GalleryApplicationVersion instance.
description:
  - 'Create, update and delete instance of Azure GalleryApplicationVersion.'
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
        Version is to be created.
      - >-
        The name of the gallery Application Definition in which the Application
        Version is to be updated.
      - >-
        The name of the gallery Application Definition in which the Application
        Version resides.
    required: true
    type: str
  gallery_application_version_name:
    description:
      - >-
        The name of the gallery Application Version to be created. Needs to
        follow semantic version name pattern: The allowed characters are digit
        and period. Digits must be within the range of a 32-bit integer. Format:
        :code:`<MajorVersion>`.:code:`<MinorVersion>`.:code:`<Patch>`
      - >-
        The name of the gallery Application Version to be updated. Needs to
        follow semantic version name pattern: The allowed characters are digit
        and period. Digits must be within the range of a 32-bit integer. Format:
        :code:`<MajorVersion>`.:code:`<MinorVersion>`.:code:`<Patch>`
      - The name of the gallery Application Version to be retrieved.
      - The name of the gallery Application Version to be deleted.
    required: true
    type: str
  location:
    description:
      - Resource location
    type: str
  target_regions:
    description:
      - >-
        The target regions where the Image Version is going to be replicated to.
        This property is updatable.
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
            The number of replicas of the Image Version to be created per
            region. This property is updatable.
        type: integer
      storage_account_type:
        description:
          - >-
            Specifies the storage account type to be used to store the image.
            This property is not updatable.
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
                    A relative URI containing the resource ID of the disk
                    encryption set.
                type: str
          data_disk_images:
            description:
              - A list of encryption specifications for data disk images.
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
  source:
    description:
      - The source image from which the Image Version is going to be created.
    type: dict
    suboptions:
      file_name:
        description:
          - Required. The fileName of the artifact.
        required: true
        type: str
      media_link:
        description:
          - >-
            Required. The mediaLink of the artifact, must be a readable storage
            blob.
        required: true
        type: str
  content_type:
    description:
      - >-
        Optional. May be used to help process this file. The type of file
        contained in the source, e.g. zip, json, etc.
    type: str
  enable_health_check:
    description:
      - Optional. Whether or not this application reports health.
    type: bool
  expand:
    description:
      - The expand expression to apply on the operation.
    type: choice
  state:
    description:
      - Assert the state of the GalleryApplicationVersion.
      - >-
        Use C(present) to create or update an GalleryApplicationVersion and
        C(absent) to delete it.
    default: present
    choices:
      - absent
      - present
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)
,''',,EXAMPLES = ''',    - name: Create or update a simple gallery Application Version.,      azure_rm_galleryapplicationversion: ,        gallery_application_name: myGalleryApplicationName,        gallery_application_version_name: 1.0.0,        gallery_name: myGalleryName,        resource_group_name: myResourceGroup,        ,,    - name: Update a simple gallery Application Version.,      azure_rm_galleryapplicationversion: ,        gallery_application_name: myGalleryApplicationName,        gallery_application_version_name: 1.0.0,        gallery_name: myGalleryName,        resource_group_name: myResourceGroup,        ,,    - name: Delete a gallery Application Version.,      azure_rm_galleryapplicationversion: ,        gallery_application_name: myGalleryApplicationName,        gallery_application_version_name: 1.0.0,        gallery_name: myGalleryName,        resource_group_name: myResourceGroup,        ,,''',,RETURN = ''',id:,  description:,    - Resource Id,  returned: always,  type: str,  sample: null,name:,  description:,    - Resource name,  returned: always,  type: str,  sample: null,type:,  description:,    - Resource type,  returned: always,  type: str,  sample: null,location:,  description:,    - Resource location,  returned: always,  type: str,  sample: null,tags:,  description:,    - Resource tags,  returned: always,  type: dictionary,  sample: null,provisioning_state:,  description:,    - 'The provisioning state, which only appears in the response.',  returned: always,  type: choice,  sample: null,replication_status:,  description:,    - This is the replication status of the gallery Image Version.,  returned: always,  type: dict,  sample: null,  contains:,    aggregated_state:,      description:,        - >-,          This is the aggregated replication status based on all the regional,          replication status flags.,      returned: always,      type: choice,      sample: null,    summary:,      description:,        - This is a summary of replication status for each region.,      returned: always,      type: list,      sample: null,      contains:,        region:,          description:,            - >-,              The region to which the gallery Image Version is being replicated,              to.,          returned: always,          type: str,          sample: null,        state:,          description:,            - This is the regional replication state.,          returned: always,          type: choice,          sample: null,        details:,          description:,            - The details of the replication status.,          returned: always,          type: str,          sample: null,        progress:,          description:,            - It indicates progress of the replication job.,          returned: always,          type: integer,          sample: null,target_regions:,  description:,    - >-,      The target regions where the Image Version is going to be replicated to.,      This property is updatable.,  returned: always,  type: list,  sample: null,  contains:,    name:,      description:,        - The name of the region.,      returned: always,      type: str,      sample: null,    regional_replica_count:,      description:,        - >-,          The number of replicas of the Image Version to be created per region.,          This property is updatable.,      returned: always,      type: integer,      sample: null,    storage_account_type:,      description:,        - >-,          Specifies the storage account type to be used to store the image. This,          property is not updatable.,      returned: always,      type: choice,      sample: null,    encryption:,      description:,        - >-,          Optional. Allows users to provide customer managed keys for encrypting,          the OS and data disks in the gallery artifact.,      returned: always,      type: dict,      sample: null,      contains:,        os_disk_image:,          description:,            - This is the disk image encryption base class.,          returned: always,          type: dict,          sample: null,          contains:,            disk_encryption_set_id:,              description:,                - >-,                  A relative URI containing the resource ID of the disk,                  encryption set.,              returned: always,              type: str,              sample: null,        data_disk_images:,          description:,            - A list of encryption specifications for data disk images.,          returned: always,          type: list,          sample: null,          contains:,            lun:,              description:,                - >-,                  This property specifies the logical unit number of the data,                  disk. This value is used to identify data disks within the,                  Virtual Machine and therefore must be unique for each data,                  disk attached to the Virtual Machine.,              returned: always,              type: integer,              sample: null,replica_count:,  description:,    - >-,      The number of replicas of the Image Version to be created per region. This,      property would take effect for a region when regionalReplicaCount is not,      specified. This property is updatable.,  returned: always,  type: integer,  sample: null,exclude_from_latest:,  description:,    - >-,      If set to true, Virtual Machines deployed from the latest version of the,      Image Definition won't use this Image Version.,  returned: always,  type: bool,  sample: null,published_date:,  description:,    - The timestamp for when the gallery Image Version is published.,  returned: always,  type: str,  sample: null,end_of_life_date:,  description:,    - >-,      The end of life date of the gallery Image Version. This property can be,      used for decommissioning purposes. This property is updatable.,  returned: always,  type: str,  sample: null,storage_account_type:,  description:,    - >-,      Specifies the storage account type to be used to store the image. This,      property is not updatable.,  returned: always,  type: choice,  sample: null,source:,  description:,    - The source image from which the Image Version is going to be created.,  returned: always,  type: dict,  sample: null,  contains:,    file_name:,      description:,        - Required. The fileName of the artifact.,      returned: always,      type: str,      sample: null,    media_link:,      description:,        - >-,          Required. The mediaLink of the artifact, must be a readable storage,          blob.,      returned: always,      type: str,      sample: null,content_type:,  description:,    - >-,      Optional. May be used to help process this file. The type of file,      contained in the source, e.g. zip, json, etc.,  returned: always,  type: str,  sample: null,enable_health_check:,  description:,    - Optional. Whether or not this application reports health.,  returned: always,  type: bool,  sample: null,,''',,import time,import json,import re,from ansible.module_utils.azure_rm_common_ext import AzureRMModuleBaseExt,from copy import deepcopy,try:,    from msrestazure.azure_exceptions import CloudError,    from azure.mgmt.compute import ComputeManagementClient,    from msrestazure.azure_operation import AzureOperationPoller,    from msrest.polling import LROPoller,except ImportError:,    # This is handled in azure_rm_common,    pass,,,class Actions:,    NoAction, Create, Update, Delete = range(4),,,class AzureRMGalleryApplicationVersion(AzureRMModuleBaseExt):,    def __init__(self):,        self.module_arg_spec = dict(,            resource_group_name=dict(,                type='str',,                required=True,            ),,            gallery_name=dict(,                type='str',,                required=True,            ),,            gallery_application_name=dict(,                type='str',,                required=True,            ),,            gallery_application_version_name=dict(,                type='str',,                required=True,            ),,            location=dict(,                type='str',,                disposition='/location',            ),,            target_regions=dict(,                type='list',,                disposition='/target_regions',,                elements='dict',,                options=dict(,                    name=dict(,                        type='str',,                        disposition='name',,                        required=True,                    ),,                    regional_replica_count=dict(,                        type='integer',,                        disposition='regional_replica_count',                    ),,                    storage_account_type=dict(,                        type='choice',,                        disposition='storage_account_type',                    ),,                    encryption=dict(,                        type='dict',,                        disposition='encryption',,                        options=dict(,                            os_disk_image=dict(,                                type='dict',,                                disposition='os_disk_image',,                                options=dict(,                                    disk_encryption_set_id=dict(,                                        type='str',,                                        disposition='disk_encryption_set_id',                                    ),                                ),                            ),,                            data_disk_images=dict(,                                type='list',,                                disposition='data_disk_images',,                                elements='dict',,                                options=dict(,                                    lun=dict(,                                        type='integer',,                                        disposition='lun',,                                        required=True,                                    ),                                ),                            ),                        ),                    ),                ),            ),,            replica_count=dict(,                type='integer',,                disposition='/replica_count',            ),,            exclude_from_latest=dict(,                type='bool',,                disposition='/exclude_from_latest',            ),,            end_of_life_date=dict(,                type='str',,                disposition='/end_of_life_date',            ),,            storage_account_type=dict(,                type='choice',,                disposition='/storage_account_type',            ),,            source=dict(,                type='dict',,                disposition='/source',,                options=dict(,                    file_name=dict(,                        type='str',,                        disposition='file_name',,                        required=True,                    ),,                    media_link=dict(,                        type='str',,                        disposition='media_link',,                        required=True,                    ),                ),            ),,            content_type=dict(,                type='str',,                disposition='/content_type',            ),,            enable_health_check=dict(,                type='bool',,                disposition='/enable_health_check',            ),,            expand=dict(,                type='choice',            ),,            state=dict(,                type='str',,                default='present',,                choices=['present', 'absent'],            ),        ),,        self.resource_group_name = None,        self.gallery_name = None,        self.gallery_application_name = None,        self.gallery_application_version_name = None,        self.expand = None,        self.body = {},,        self.results = dict(changed=False),        self.mgmt_client = None,        self.state = None,        self.to_do = Actions.NoAction,,        super(AzureRMGalleryApplicationVersion, self).__init__(derived_arg_spec=self.module_arg_spec,,                                                               supports_check_mode=True,,                                                               supports_tags=True),,    def exec_module(self, **kwargs):,        for key in list(self.module_arg_spec.keys()):,            if hasattr(self, key):,                setattr(self, key, kwargs[key]),            elif kwargs[key] is not None:,                self.body[key] = kwargs[key],,        self.inflate_parameters(self.module_arg_spec, self.body, 0),,        old_response = None,        response = None,,        self.mgmt_client = self.get_mgmt_svc_client(ComputeManagementClient,,                                                    base_url=self._cloud_environment.endpoints.resource_manager,,                                                    api_version='2019-12-01'),,        old_response = self.get_resource(),,        if not old_response:,            if self.state == 'present':,                self.to_do = Actions.Create,        else:,            if self.state == 'absent':,                self.to_do = Actions.Delete,            else:,                modifiers = {},                self.create_compare_modifiers(self.module_arg_spec, '', modifiers),                self.results['modifiers'] = modifiers,                self.results['compare'] = [],                if not self.default_compare(modifiers, self.body, old_response, '', self.results):,                    self.to_do = Actions.Update,,        if (self.to_do == Actions.Create) or (self.to_do == Actions.Update):,            self.results['changed'] = True,            if self.check_mode:,                return self.results,            response = self.create_update_resource(),        elif self.to_do == Actions.Delete:,            self.results['changed'] = True,            if self.check_mode:,                return self.results,            self.delete_resource(),        else:,            self.results['changed'] = False,            response = old_response,,        return self.results,,    def create_update_resource(self):,        try:,            response = self.mgmt_client.gallery_application_versions.create_or_update(resource_group_name=self.resource_group_name,,                                                                                      gallery_name=self.gallery_name,,                                                                                      gallery_application_name=self.gallery_application_name,,                                                                                      gallery_application_version_name=self.gallery_application_version_name,,                                                                                      gallery_application_version=self.body),            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):,                response = self.get_poller_result(response),        except CloudError as exc:,            self.log('Error attempting to create the GalleryApplicationVersion instance.'),            self.fail('Error creating the GalleryApplicationVersion instance: {0}'.format(str(exc))),        return response.as_dict(),,    def delete_resource(self):,        try:,            response = self.mgmt_client.gallery_application_versions.delete(resource_group_name=self.resource_group_name,,                                                                            gallery_name=self.gallery_name,,                                                                            gallery_application_name=self.gallery_application_name,,                                                                            gallery_application_version_name=self.gallery_application_version_name),        except CloudError as e:,            self.log('Error attempting to delete the GalleryApplicationVersion instance.'),            self.fail('Error deleting the GalleryApplicationVersion instance: {0}'.format(str(e))),,        return True,,    def get_resource(self):,        try:,            response = self.mgmt_client.gallery_application_versions.get(resource_group_name=self.resource_group_name,,                                                                         gallery_name=self.gallery_name,,                                                                         gallery_application_name=self.gallery_application_name,,                                                                         gallery_application_version_name=self.gallery_application_version_name,,                                                                         expand=self.expand),        except CloudError as e:,            return False,        return response.as_dict(),,,def main():,    AzureRMGalleryApplicationVersion(),,,if __name__ == '__main__':,    main(),