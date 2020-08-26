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
module: azure_rm_image
version_added: '2.9'
short_description: Manage Azure Image instance.
description:
  - 'Create, update and delete instance of Azure Image.'
options:
  resource_group_name:
    description:
      - The name of the resource group.
    type: str
  image_name:
    description:
      - The name of the image.
    type: str
  location:
    description:
      - Resource location
    type: str
  hyper_vgeneration:
    description:
      - >-
        Gets the HyperVGenerationType of the VirtualMachine created from the
        image
    type: choice
  os_disk:
    description:
      - >-
        Specifies information about the operating system disk used by the
        virtual machine. :code:`<br>`:code:`<br>` For more information about
        disks, see `About disks and VHDs for Azure virtual machines
        <https://docs.microsoft.com/azure/virtual-machines/virtual-machines-windows-about-disks-vhds?toc=%2fazure%2fvirtual-machines%2fwindows%2ftoc.json>`_.
    type: dict
    suboptions:
      os_type:
        description:
          - >-
            This property allows you to specify the type of the OS that is
            included in the disk if creating a VM from a custom image.
            :code:`<br>`:code:`<br>` Possible values are:
            :code:`<br>`:code:`<br>` **Windows** :code:`<br>`:code:`<br>`
            **Linux**
        required: true
        type: sealed-choice
      os_state:
        description:
          - The OS State.
        required: true
        type: sealed-choice
  data_disks:
    description:
      - >-
        Specifies the parameters that are used to add a data disk to a virtual
        machine. :code:`<br>`:code:`<br>` For more information about disks, see
        `About disks and VHDs for Azure virtual machines
        <https://docs.microsoft.com/azure/virtual-machines/virtual-machines-windows-about-disks-vhds?toc=%2fazure%2fvirtual-machines%2fwindows%2ftoc.json>`_.
    type: list
  zone_resilient:
    description:
      - >-
        Specifies whether an image is zone resilient or not. Default is false.
        Zone resilient images can be created only in regions that provide Zone
        Redundant Storage (ZRS).
    type: bool
  id:
    description:
      - Resource Id
    type: str
  expand:
    description:
      - The expand expression to apply on the operation.
    type: str
  state:
    description:
      - Assert the state of the Image.
      - Use C(present) to create or update an Image and C(absent) to delete it.
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


class AzureRMImage(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str'
            ),
            image_name=dict(
                type='str'
            ),
            location=dict(
                type='str',
                disposition='/location'
            ),
            hyper_vgeneration=dict(
                type='choice',
                disposition='/hyper_vgeneration'
            ),
            os_disk=dict(
                type='dict',
                disposition='/os_disk',
                options=dict(
                    os_type=dict(
                        type='sealed-choice',
                        disposition='os_type',
                        required=True
                    ),
                    os_state=dict(
                        type='sealed-choice',
                        disposition='os_state',
                        required=True
                    )
                )
            ),
            data_disks=dict(
                type='list',
                disposition='/data_disks'
            ),
            zone_resilient=dict(
                type='bool',
                disposition='/zone_resilient'
            ),
            id=dict(
                type='str',
                disposition='/id'
            ),
            expand=dict(
                type='str'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group_name = None
        self.image_name = None
        self.expand = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMImage, self).__init__(derived_arg_spec=self.module_arg_spec,
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
                                                    api_version='2020-06-01')

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
                response = self.mgmt_client.images.create(resource_group_name=self.resource_group_name,
                                                          image_name=self.image_name,
                                                          parameters=self.body)
            else:
                response = self.mgmt_client.images.update(resource_group_name=self.resource_group_name,
                                                          image_name=self.image_name,
                                                          parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the Image instance.')
            self.fail('Error creating the Image instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.images.delete(resource_group_name=self.resource_group_name,
                                                      image_name=self.image_name)
        except CloudError as e:
            self.log('Error attempting to delete the Image instance.')
            self.fail('Error deleting the Image instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        found = False
        try:
            response = self.mgmt_client.images.get(resource_group_name=self.resource_group_name,
                                                   image_name=self.image_name,
                                                   expand=self.expand)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMImage()


if __name__ == '__main__':
    main()
