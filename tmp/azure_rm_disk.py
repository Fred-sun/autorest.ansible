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
module: azure_rm_disk
version_added: '2.9'
short_description: Manage Azure Disk instance.
description:
  - 'Create, update and delete instance of Azure Disk.'
options:
  resource_group_name:
    description:
      - The name of the resource group.
    required: true
    type: str
  disk_name:
    description:
      - >-
        The name of the managed disk that is being created. The name can't be
        changed after the disk is created. Supported characters for the name are
        a-z, A-Z, 0-9 and _. The maximum name length is 80 characters.
    required: true
    type: str
  disk:
    description:
      - Disk object supplied in the body of the Put disk operation.
      - Disk object supplied in the body of the Patch disk operation.
    type: dict
    suboptions:
      managed_by:
        description:
          - >-
            A relative URI containing the ID of the VM that has the disk
            attached.
        type: str
      managed_by_extended:
        description:
          - >-
            List of relative URIs containing the IDs of the VMs that have the
            disk attached. maxShares should be set to a value greater than one
            for disks to allow attaching them to multiple VMs.
        type: list
      sku:
        description:
          - >-
            The disks sku name. Can be Standard_LRS, Premium_LRS,
            StandardSSD_LRS, or UltraSSD_LRS.
        type: dict
        suboptions:
          name:
            description:
              - The sku name.
            type: choice
          tier:
            description:
              - The sku tier.
            type: str
      zones:
        description:
          - The Logical zone list for Disk.
        type: list
      time_created:
        description:
          - The time when the disk was created.
        type: str
      os_type:
        description:
          - The Operating System type.
        type: sealed-choice
      hyper_vgeneration:
        description:
          - >-
            The hypervisor generation of the Virtual Machine. Applicable to OS
            disks only.
        type: choice
      creation_data:
        description:
          - >-
            Disk source information. CreationData information cannot be changed
            after the disk has been created.
        type: dict
        suboptions:
          create_option:
            description:
              - This enumerates the possible sources of a disk's creation.
            required: true
            type: choice
          storage_account_id:
            description:
              - >-
                Required if createOption is Import. The Azure Resource Manager
                identifier of the storage account containing the blob to import
                as a disk.
            type: str
          image_reference:
            description:
              - Disk source information.
            type: dict
            suboptions:
              id:
                description:
                  - >-
                    A relative uri containing either a Platform Image Repository
                    or user image reference.
                required: true
                type: str
              lun:
                description:
                  - >-
                    If the disk is created from an image's data disk, this is an
                    index that indicates which of the data disks in the image to
                    use. For OS disks, this field is null.
                type: integer
          gallery_image_reference:
            description:
              - >-
                Required if creating from a Gallery Image. The id of the
                ImageDiskReference will be the ARM id of the shared galley image
                version from which to create a disk.
            type: dict
            suboptions:
              id:
                description:
                  - >-
                    A relative uri containing either a Platform Image Repository
                    or user image reference.
                required: true
                type: str
              lun:
                description:
                  - >-
                    If the disk is created from an image's data disk, this is an
                    index that indicates which of the data disks in the image to
                    use. For OS disks, this field is null.
                type: integer
          source_uri:
            description:
              - >-
                If createOption is Import, this is the URI of a blob to be
                imported into a managed disk.
            type: str
          source_resource_id:
            description:
              - >-
                If createOption is Copy, this is the ARM id of the source
                snapshot or disk.
            type: str
          source_unique_id:
            description:
              - >-
                If this field is set, this is the unique id identifying the
                source of this resource.
            type: str
          upload_size_bytes:
            description:
              - >-
                If createOption is Upload, this is the size of the contents of
                the upload including the VHD footer. This value should be
                between 20972032 (20 MiB + 512 bytes for the VHD footer) and
                35183298347520 bytes (32 TiB + 512 bytes for the VHD footer).
            type: integer
      disk_size_gb:
        description:
          - >-
            If creationData.createOption is Empty, this field is mandatory and
            it indicates the size of the disk to create. If this field is
            present for updates or creation with other options, it indicates a
            resize. Resizes are only allowed if the disk is not attached to a
            running VM, and can only increase the disk's size.
        type: integer
      disk_size_bytes:
        description:
          - The size of the disk in bytes. This field is read only.
        type: integer
      unique_id:
        description:
          - Unique Guid identifying the resource.
        type: str
      encryption_settings_collection:
        description:
          - >-
            Encryption settings collection used for Azure Disk Encryption, can
            contain multiple encryption settings per disk or snapshot.
        type: dict
        suboptions:
          enabled:
            description:
              - >-
                Set this flag to true and provide DiskEncryptionKey and optional
                KeyEncryptionKey to enable encryption. Set this flag to false
                and remove DiskEncryptionKey and KeyEncryptionKey to disable
                encryption. If EncryptionSettings is null in the request object,
                the existing settings remain unchanged.
            required: true
            type: bool
          encryption_settings:
            description:
              - 'A collection of encryption settings, one for each disk volume.'
            type: list
            suboptions:
              disk_encryption_key:
                description:
                  - Key Vault Secret Url and vault id of the disk encryption key
                type: dict
                suboptions:
                  source_vault:
                    description:
                      - Resource id of the KeyVault containing the key or secret
                    required: true
                    type: dict
                    suboptions:
                      id:
                        description:
                          - Resource Id
                        type: str
                  secret_url:
                    description:
                      - Url pointing to a key or secret in KeyVault
                    required: true
                    type: str
              key_encryption_key:
                description:
                  - >-
                    Key Vault Key Url and vault id of the key encryption key.
                    KeyEncryptionKey is optional and when provided is used to
                    unwrap the disk encryption key.
                type: dict
                suboptions:
                  source_vault:
                    description:
                      - Resource id of the KeyVault containing the key or secret
                    required: true
                    type: dict
                    suboptions:
                      id:
                        description:
                          - Resource Id
                        type: str
                  key_url:
                    description:
                      - Url pointing to a key or secret in KeyVault
                    required: true
                    type: str
          encryption_settings_version:
            description:
              - >-
                Describes what type of encryption is used for the disks. Once
                this field is set, it cannot be overwritten. '1.0' corresponds
                to Azure Disk Encryption with AAD app.'1.1' corresponds to Azure
                Disk Encryption.
            type: str
      provisioning_state:
        description:
          - The disk provisioning state.
        type: str
      disk_iops_read_write:
        description:
          - >-
            The number of IOPS allowed for this disk; only settable for UltraSSD
            disks. One operation can transfer between 4k and 256k bytes.
        type: integer
      disk_mbps_read_write:
        description:
          - >-
            The bandwidth allowed for this disk; only settable for UltraSSD
            disks. MBps means millions of bytes per second - MB here uses the
            ISO notation, of powers of 10.
        type: integer
      disk_iops_read_only:
        description:
          - >-
            The total number of IOPS that will be allowed across all VMs
            mounting the shared disk as ReadOnly. One operation can transfer
            between 4k and 256k bytes.
        type: integer
      disk_mbps_read_only:
        description:
          - >-
            The total throughput (MBps) that will be allowed across all VMs
            mounting the shared disk as ReadOnly. MBps means millions of bytes
            per second - MB here uses the ISO notation, of powers of 10.
        type: integer
      disk_state:
        description:
          - The state of the disk.
        type: choice
      encryption:
        description:
          - >-
            Encryption property can be used to encrypt data at rest with
            customer managed keys or platform managed keys.
        type: dict
        suboptions:
          disk_encryption_set_id:
            description:
              - >-
                ResourceId of the disk encryption set to use for enabling
                encryption at rest.
            type: str
          type:
            description:
              - The type of key used to encrypt the data of the disk.
            type: choice
      max_shares:
        description:
          - >-
            The maximum number of VMs that can attach to the disk at the same
            time. Value greater than one indicates a disk that can be mounted on
            multiple VMs at the same time.
        type: integer
      share_info:
        description:
          - >-
            Details of the list of all VMs that have the disk attached.
            maxShares should be set to a value greater than one for disks to
            allow attaching them to multiple VMs.
        type: list
        suboptions:
          vm_uri:
            description:
              - >-
                A relative URI containing the ID of the VM that has the disk
                attached.
            type: str
      network_access_policy:
        description:
          - Policy for accessing the disk via network.
        type: choice
      disk_access_id:
        description:
          - >-
            ARM id of the DiskAccess resource for using private endpoints on
            disks.
        type: str
  state:
    description:
      - Assert the state of the Disk.
      - Use C(present) to create or update an Disk and C(absent) to delete it.
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
    - name: Create a managed disk and associate with disk access resource.
      azure_rm_disk: 
        disk:
          location: West US
          properties:
            creation_data:
              create_option: Empty
            disk_access_id: >-
              /subscriptions/{subscription-id}/resourceGroups/myResourceGroup/providers/Microsoft.Compute/diskAccesses/{existing-diskAccess-name}
            disk_size_gb: 200
            network_access_policy: AllowPrivate
        disk_name: myDisk
        resource_group_name: myResourceGroup
        

    - name: Create a managed disk and associate with disk encryption set.
      azure_rm_disk: 
        disk:
          location: West US
          properties:
            creation_data:
              create_option: Empty
            disk_size_gb: 200
            encryption:
              disk_encryption_set_id: >-
                /subscriptions/{subscription-id}/resourceGroups/myResourceGroup/providers/Microsoft.Compute/diskEncryptionSets/{existing-diskEncryptionSet-name}
        disk_name: myDisk
        resource_group_name: myResourceGroup
        

    - name: Create a managed disk by copying a snapshot.
      azure_rm_disk: 
        disk:
          location: West US
          properties:
            creation_data:
              create_option: Copy
              source_resource_id: >-
                subscriptions/{subscriptionId}/resourceGroups/myResourceGroup/providers/Microsoft.Compute/snapshots/mySnapshot
        disk_name: myDisk
        resource_group_name: myResourceGroup
        

    - name: Create a managed disk by importing an unmanaged blob from a different subscription.
      azure_rm_disk: 
        disk:
          location: West US
          properties:
            creation_data:
              create_option: Import
              source_uri: 'https://mystorageaccount.blob.core.windows.net/osimages/osimage.vhd'
              storage_account_id: >-
                subscriptions/{subscriptionId}/resourceGroups/myResourceGroup/providers/Microsoft.Storage/storageAccounts/myStorageAccount
        disk_name: myDisk
        resource_group_name: myResourceGroup
        

    - name: Create a managed disk by importing an unmanaged blob from the same subscription.
      azure_rm_disk: 
        disk:
          location: West US
          properties:
            creation_data:
              create_option: Import
              source_uri: 'https://mystorageaccount.blob.core.windows.net/osimages/osimage.vhd'
        disk_name: myDisk
        resource_group_name: myResourceGroup
        

    - name: Create a managed disk from a platform image.
      azure_rm_disk: 
        disk:
          location: West US
          properties:
            creation_data:
              create_option: FromImage
              image_reference:
                id: >-
                  /Subscriptions/{subscriptionId}/Providers/Microsoft.Compute/Locations/uswest/Publishers/Microsoft/ArtifactTypes/VMImage/Offers/{offer}
            os_type: Windows
        disk_name: myDisk
        resource_group_name: myResourceGroup
        

    - name: Create a managed disk from an existing managed disk in the same or different subscription.
      azure_rm_disk: 
        disk:
          location: West US
          properties:
            creation_data:
              create_option: Copy
              source_resource_id: >-
                subscriptions/{subscriptionId}/resourceGroups/myResourceGroup/providers/Microsoft.Compute/disks/myDisk1
        disk_name: myDisk2
        resource_group_name: myResourceGroup
        

    - name: Create a managed upload disk.
      azure_rm_disk: 
        disk:
          location: West US
          properties:
            creation_data:
              create_option: Upload
              upload_size_bytes: 10737418752
        disk_name: myDisk
        resource_group_name: myResourceGroup
        

    - name: Create an empty managed disk.
      azure_rm_disk: 
        disk:
          location: West US
          properties:
            creation_data:
              create_option: Empty
            disk_size_gb: 200
        disk_name: myDisk
        resource_group_name: myResourceGroup
        

    - name: Update managed disk to remove disk access resource association.
      azure_rm_disk: 
        disk:
          properties:
            network_access_policy: AllowAll
        disk_name: myDisk
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
managed_by:
  description:
    - A relative URI containing the ID of the VM that has the disk attached.
  returned: always
  type: str
  sample: null
managed_by_extended:
  description:
    - >-
      List of relative URIs containing the IDs of the VMs that have the disk
      attached. maxShares should be set to a value greater than one for disks to
      allow attaching them to multiple VMs.
  returned: always
  type: list
  sample: null
sku:
  description:
    - >-
      The disks sku name. Can be Standard_LRS, Premium_LRS, StandardSSD_LRS, or
      UltraSSD_LRS.
  returned: always
  type: dict
  sample: null
  contains:
    name:
      description:
        - The sku name.
      returned: always
      type: choice
      sample: null
    tier:
      description:
        - The sku tier.
      returned: always
      type: str
      sample: null
zones:
  description:
    - The Logical zone list for Disk.
  returned: always
  type: list
  sample: null
time_created:
  description:
    - The time when the disk was created.
  returned: always
  type: str
  sample: null
os_type:
  description:
    - The Operating System type.
  returned: always
  type: sealed-choice
  sample: null
hyper_vgeneration:
  description:
    - >-
      The hypervisor generation of the Virtual Machine. Applicable to OS disks
      only.
  returned: always
  type: choice
  sample: null
creation_data:
  description:
    - >-
      Disk source information. CreationData information cannot be changed after
      the disk has been created.
  returned: always
  type: dict
  sample: null
  contains:
    create_option:
      description:
        - This enumerates the possible sources of a disk's creation.
      returned: always
      type: choice
      sample: null
    storage_account_id:
      description:
        - >-
          Required if createOption is Import. The Azure Resource Manager
          identifier of the storage account containing the blob to import as a
          disk.
      returned: always
      type: str
      sample: null
    image_reference:
      description:
        - Disk source information.
      returned: always
      type: dict
      sample: null
      contains:
        id:
          description:
            - >-
              A relative uri containing either a Platform Image Repository or
              user image reference.
          returned: always
          type: str
          sample: null
        lun:
          description:
            - >-
              If the disk is created from an image's data disk, this is an index
              that indicates which of the data disks in the image to use. For OS
              disks, this field is null.
          returned: always
          type: integer
          sample: null
    gallery_image_reference:
      description:
        - >-
          Required if creating from a Gallery Image. The id of the
          ImageDiskReference will be the ARM id of the shared galley image
          version from which to create a disk.
      returned: always
      type: dict
      sample: null
      contains:
        id:
          description:
            - >-
              A relative uri containing either a Platform Image Repository or
              user image reference.
          returned: always
          type: str
          sample: null
        lun:
          description:
            - >-
              If the disk is created from an image's data disk, this is an index
              that indicates which of the data disks in the image to use. For OS
              disks, this field is null.
          returned: always
          type: integer
          sample: null
    source_uri:
      description:
        - >-
          If createOption is Import, this is the URI of a blob to be imported
          into a managed disk.
      returned: always
      type: str
      sample: null
    source_resource_id:
      description:
        - >-
          If createOption is Copy, this is the ARM id of the source snapshot or
          disk.
      returned: always
      type: str
      sample: null
    source_unique_id:
      description:
        - >-
          If this field is set, this is the unique id identifying the source of
          this resource.
      returned: always
      type: str
      sample: null
    upload_size_bytes:
      description:
        - >-
          If createOption is Upload, this is the size of the contents of the
          upload including the VHD footer. This value should be between 20972032
          (20 MiB + 512 bytes for the VHD footer) and 35183298347520 bytes (32
          TiB + 512 bytes for the VHD footer).
      returned: always
      type: integer
      sample: null
disk_size_gb:
  description:
    - >-
      If creationData.createOption is Empty, this field is mandatory and it
      indicates the size of the disk to create. If this field is present for
      updates or creation with other options, it indicates a resize. Resizes are
      only allowed if the disk is not attached to a running VM, and can only
      increase the disk's size.
  returned: always
  type: integer
  sample: null
disk_size_bytes:
  description:
    - The size of the disk in bytes. This field is read only.
  returned: always
  type: integer
  sample: null
unique_id:
  description:
    - Unique Guid identifying the resource.
  returned: always
  type: str
  sample: null
encryption_settings_collection:
  description:
    - >-
      Encryption settings collection used for Azure Disk Encryption, can contain
      multiple encryption settings per disk or snapshot.
  returned: always
  type: dict
  sample: null
  contains:
    enabled:
      description:
        - >-
          Set this flag to true and provide DiskEncryptionKey and optional
          KeyEncryptionKey to enable encryption. Set this flag to false and
          remove DiskEncryptionKey and KeyEncryptionKey to disable encryption.
          If EncryptionSettings is null in the request object, the existing
          settings remain unchanged.
      returned: always
      type: bool
      sample: null
    encryption_settings:
      description:
        - 'A collection of encryption settings, one for each disk volume.'
      returned: always
      type: list
      sample: null
      contains:
        disk_encryption_key:
          description:
            - Key Vault Secret Url and vault id of the disk encryption key
          returned: always
          type: dict
          sample: null
          contains:
            source_vault:
              description:
                - Resource id of the KeyVault containing the key or secret
              returned: always
              type: dict
              sample: null
              contains:
                id:
                  description:
                    - Resource Id
                  returned: always
                  type: str
                  sample: null
            secret_url:
              description:
                - Url pointing to a key or secret in KeyVault
              returned: always
              type: str
              sample: null
        key_encryption_key:
          description:
            - >-
              Key Vault Key Url and vault id of the key encryption key.
              KeyEncryptionKey is optional and when provided is used to unwrap
              the disk encryption key.
          returned: always
          type: dict
          sample: null
          contains:
            source_vault:
              description:
                - Resource id of the KeyVault containing the key or secret
              returned: always
              type: dict
              sample: null
              contains:
                id:
                  description:
                    - Resource Id
                  returned: always
                  type: str
                  sample: null
            key_url:
              description:
                - Url pointing to a key or secret in KeyVault
              returned: always
              type: str
              sample: null
    encryption_settings_version:
      description:
        - >-
          Describes what type of encryption is used for the disks. Once this
          field is set, it cannot be overwritten. '1.0' corresponds to Azure
          Disk Encryption with AAD app.'1.1' corresponds to Azure Disk
          Encryption.
      returned: always
      type: str
      sample: null
provisioning_state:
  description:
    - The disk provisioning state.
  returned: always
  type: str
  sample: null
disk_iops_read_write:
  description:
    - >-
      The number of IOPS allowed for this disk; only settable for UltraSSD
      disks. One operation can transfer between 4k and 256k bytes.
  returned: always
  type: integer
  sample: null
disk_mbps_read_write:
  description:
    - >-
      The bandwidth allowed for this disk; only settable for UltraSSD disks.
      MBps means millions of bytes per second - MB here uses the ISO notation,
      of powers of 10.
  returned: always
  type: integer
  sample: null
disk_iops_read_only:
  description:
    - >-
      The total number of IOPS that will be allowed across all VMs mounting the
      shared disk as ReadOnly. One operation can transfer between 4k and 256k
      bytes.
  returned: always
  type: integer
  sample: null
disk_mbps_read_only:
  description:
    - >-
      The total throughput (MBps) that will be allowed across all VMs mounting
      the shared disk as ReadOnly. MBps means millions of bytes per second - MB
      here uses the ISO notation, of powers of 10.
  returned: always
  type: integer
  sample: null
disk_state:
  description:
    - The state of the disk.
  returned: always
  type: choice
  sample: null
encryption:
  description:
    - >-
      Encryption property can be used to encrypt data at rest with customer
      managed keys or platform managed keys.
  returned: always
  type: dict
  sample: null
  contains:
    disk_encryption_set_id:
      description:
        - >-
          ResourceId of the disk encryption set to use for enabling encryption
          at rest.
      returned: always
      type: str
      sample: null
    type:
      description:
        - The type of key used to encrypt the data of the disk.
      returned: always
      type: choice
      sample: null
max_shares:
  description:
    - >-
      The maximum number of VMs that can attach to the disk at the same time.
      Value greater than one indicates a disk that can be mounted on multiple
      VMs at the same time.
  returned: always
  type: integer
  sample: null
share_info:
  description:
    - >-
      Details of the list of all VMs that have the disk attached. maxShares
      should be set to a value greater than one for disks to allow attaching
      them to multiple VMs.
  returned: always
  type: list
  sample: null
  contains:
    vm_uri:
      description:
        - A relative URI containing the ID of the VM that has the disk attached.
      returned: always
      type: str
      sample: null
network_access_policy:
  description:
    - Policy for accessing the disk via network.
  returned: always
  type: choice
  sample: null
disk_access_id:
  description:
    - ARM id of the DiskAccess resource for using private endpoints on disks.
  returned: always
  type: str
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


class AzureRMDisk(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            disk_name=dict(
                type='str',
                required=True
            ),
            disk=dict(
                type='dict',
                disposition='/disk',
                options=dict(
                    managed_by=dict(
                        type='str',
                        disposition='managed_by'
                    ),
                    managed_by_extended=dict(
                        type='list',
                        disposition='managed_by_extended',
                        elements='str'
                    ),
                    sku=dict(
                        type='dict',
                        disposition='sku',
                        options=dict(
                            name=dict(
                                type='choice',
                                disposition='name'
                            ),
                            tier=dict(
                                type='str',
                                disposition='tier'
                            )
                        )
                    ),
                    zones=dict(
                        type='list',
                        disposition='zones',
                        elements='str'
                    ),
                    time_created=dict(
                        type='str',
                        disposition='time_created'
                    ),
                    os_type=dict(
                        type='sealed-choice',
                        disposition='os_type'
                    ),
                    hyper_vgeneration=dict(
                        type='choice',
                        disposition='hyper_vgeneration'
                    ),
                    creation_data=dict(
                        type='dict',
                        disposition='creation_data',
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
                        disposition='disk_size_gb'
                    ),
                    disk_size_bytes=dict(
                        type='integer',
                        disposition='disk_size_bytes'
                    ),
                    unique_id=dict(
                        type='str',
                        disposition='unique_id'
                    ),
                    encryption_settings_collection=dict(
                        type='dict',
                        disposition='encryption_settings_collection',
                        options=dict(
                            enabled=dict(
                                type='bool',
                                disposition='enabled',
                                required=True
                            ),
                            encryption_settings=dict(
                                type='list',
                                disposition='encryption_settings',
                                elements='dict',
                                options=dict(
                                    disk_encryption_key=dict(
                                        type='dict',
                                        disposition='disk_encryption_key',
                                        options=dict(
                                            source_vault=dict(
                                                type='dict',
                                                disposition='source_vault',
                                                required=True,
                                                options=dict(
                                                    id=dict(
                                                        type='str',
                                                        disposition='id'
                                                    )
                                                )
                                            ),
                                            secret_url=dict(
                                                type='str',
                                                disposition='secret_url',
                                                required=True
                                            )
                                        )
                                    ),
                                    key_encryption_key=dict(
                                        type='dict',
                                        disposition='key_encryption_key',
                                        options=dict(
                                            source_vault=dict(
                                                type='dict',
                                                disposition='source_vault',
                                                required=True,
                                                options=dict(
                                                    id=dict(
                                                        type='str',
                                                        disposition='id'
                                                    )
                                                )
                                            ),
                                            key_url=dict(
                                                type='str',
                                                disposition='key_url',
                                                required=True
                                            )
                                        )
                                    )
                                )
                            ),
                            encryption_settings_version=dict(
                                type='str',
                                disposition='encryption_settings_version'
                            )
                        )
                    ),
                    provisioning_state=dict(
                        type='str',
                        disposition='provisioning_state'
                    ),
                    disk_iops_read_write=dict(
                        type='integer',
                        disposition='disk_iops_read_write'
                    ),
                    disk_mbps_read_write=dict(
                        type='integer',
                        disposition='disk_mbps_read_write'
                    ),
                    disk_iops_read_only=dict(
                        type='integer',
                        disposition='disk_iops_read_only'
                    ),
                    disk_mbps_read_only=dict(
                        type='integer',
                        disposition='disk_mbps_read_only'
                    ),
                    disk_state=dict(
                        type='choice',
                        disposition='disk_state'
                    ),
                    encryption=dict(
                        type='dict',
                        disposition='encryption',
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
                        disposition='max_shares'
                    ),
                    share_info=dict(
                        type='list',
                        disposition='share_info',
                        elements='dict',
                        options=dict(
                            vm_uri=dict(
                                type='str',
                                disposition='vm_uri'
                            )
                        )
                    ),
                    network_access_policy=dict(
                        type='choice',
                        disposition='network_access_policy'
                    ),
                    disk_access_id=dict(
                        type='str',
                        disposition='disk_access_id'
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
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-05-01')

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
