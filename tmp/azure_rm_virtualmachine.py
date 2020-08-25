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


class AzureRMVirtualMachine(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            location=dict(
                type='str'
            ),
            resource_group_name=dict(
                type='str'
            ),
            vm_name=dict(
                type='str'
            ),
            vhd_prefix=dict(
                type='str',
                disposition='/vhd_prefix'
            ),
            destination_container_name=dict(
                type='str',
                disposition='/destination_container_name'
            ),
            overwrite_vhds=dict(
                type='bool',
                disposition='/overwrite_vhds'
            ),
            plan=dict(
                type='dict',
                disposition='/plan',
                options=dict(
                    name=dict(
                        type='str',
                        disposition='name'
                    ),
                    publisher=dict(
                        type='str',
                        disposition='publisher'
                    ),
                    product=dict(
                        type='str',
                        disposition='product'
                    ),
                    promotion_code=dict(
                        type='str',
                        disposition='promotion_code'
                    )
                )
            ),
            zones=dict(
                type='list',
                disposition='/zones'
            ),
            type=dict(
                type='sealed-choice',
                disposition='/type'
            ),
            user_assigned_identities=dict(
                type='dictionary',
                disposition='/user_assigned_identities'
            ),
            hardware_profile=dict(
                type='dict',
                disposition='/hardware_profile',
                options=dict(
                    vm_size=dict(
                        type='choice',
                        disposition='vm_size'
                    )
                )
            ),
            storage_profile=dict(
                type='dict',
                disposition='/storage_profile',
                options=dict(
                    image_reference=dict(
                        type='dict',
                        disposition='image_reference',
                        options=dict(
                            publisher=dict(
                                type='str',
                                disposition='publisher'
                            ),
                            offer=dict(
                                type='str',
                                disposition='offer'
                            ),
                            sku=dict(
                                type='str',
                                disposition='sku'
                            ),
                            version=dict(
                                type='str',
                                disposition='version'
                            ),
                            exact_version=dict(
                                type='str',
                                updatable=False,
                                disposition='exact_version'
                            )
                        )
                    ),
                    os_disk=dict(
                        type='dict',
                        disposition='os_disk',
                        options=dict(
                            os_type=dict(
                                type='sealed-choice',
                                disposition='os_type'
                            ),
                            encryption_settings=dict(
                                type='dict',
                                disposition='encryption_settings',
                                options=dict(
                                    disk_encryption_key=dict(
                                        type='dict',
                                        disposition='disk_encryption_key',
                                        options=dict(
                                            secret_url=dict(
                                                type='str',
                                                disposition='secret_url',
                                                required=True
                                            ),
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
                                            )
                                        )
                                    ),
                                    key_encryption_key=dict(
                                        type='dict',
                                        disposition='key_encryption_key',
                                        options=dict(
                                            key_url=dict(
                                                type='str',
                                                disposition='key_url',
                                                required=True
                                            ),
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
                                            )
                                        )
                                    ),
                                    enabled=dict(
                                        type='bool',
                                        disposition='enabled'
                                    )
                                )
                            ),
                            name=dict(
                                type='str',
                                disposition='name'
                            ),
                            vhd=dict(
                                type='dict',
                                disposition='vhd',
                                options=dict(
                                    uri=dict(
                                        type='str',
                                        disposition='uri'
                                    )
                                )
                            ),
                            image=dict(
                                type='dict',
                                disposition='image',
                                options=dict(
                                    uri=dict(
                                        type='str',
                                        disposition='uri'
                                    )
                                )
                            ),
                            caching=dict(
                                type='sealed-choice',
                                disposition='caching'
                            ),
                            write_accelerator_enabled=dict(
                                type='bool',
                                disposition='write_accelerator_enabled'
                            ),
                            diff_disk_settings=dict(
                                type='dict',
                                disposition='diff_disk_settings',
                                options=dict(
                                    option=dict(
                                        type='choice',
                                        disposition='option'
                                    ),
                                    placement=dict(
                                        type='choice',
                                        disposition='placement'
                                    )
                                )
                            ),
                            create_option=dict(
                                type='choice',
                                disposition='create_option',
                                required=True
                            ),
                            disk_size_gb=dict(
                                type='integer',
                                disposition='disk_size_gb'
                            ),
                            managed_disk=dict(
                                type='dict',
                                disposition='managed_disk',
                                options=dict(
                                    storage_account_type=dict(
                                        type='choice',
                                        disposition='storage_account_type'
                                    ),
                                    disk_encryption_set=dict(
                                        type='dict',
                                        disposition='disk_encryption_set',
                                        options=dict(
                                            id=dict(
                                                type='str',
                                                disposition='id'
                                            )
                                        )
                                    )
                                )
                            )
                        )
                    ),
                    data_disks=dict(
                        type='list',
                        disposition='data_disks'
                    )
                )
            ),
            additional_capabilities=dict(
                type='dict',
                disposition='/additional_capabilities',
                options=dict(
                    ultra_ssd_enabled=dict(
                        type='bool',
                        disposition='ultra_ssd_enabled'
                    )
                )
            ),
            os_profile=dict(
                type='dict',
                disposition='/os_profile',
                options=dict(
                    computer_name=dict(
                        type='str',
                        disposition='computer_name'
                    ),
                    admin_username=dict(
                        type='str',
                        disposition='admin_username'
                    ),
                    admin_password=dict(
                        type='str',
                        disposition='admin_password'
                    ),
                    custom_data=dict(
                        type='str',
                        disposition='custom_data'
                    ),
                    windows_configuration=dict(
                        type='dict',
                        disposition='windows_configuration',
                        options=dict(
                            provision_vm_agent=dict(
                                type='bool',
                                disposition='provision_vm_agent'
                            ),
                            enable_automatic_updates=dict(
                                type='bool',
                                disposition='enable_automatic_updates'
                            ),
                            time_zone=dict(
                                type='str',
                                disposition='time_zone'
                            ),
                            additional_unattend_content=dict(
                                type='list',
                                disposition='additional_unattend_content'
                            ),
                            patch_settings=dict(
                                type='dict',
                                disposition='patch_settings',
                                options=dict(
                                    patch_mode=dict(
                                        type='choice',
                                        disposition='patch_mode'
                                    )
                                )
                            ),
                            win_rm=dict(
                                type='dict',
                                disposition='win_rm',
                                options=dict(
                                    listeners=dict(
                                        type='list',
                                        disposition='listeners'
                                    )
                                )
                            )
                        )
                    ),
                    linux_configuration=dict(
                        type='dict',
                        disposition='linux_configuration',
                        options=dict(
                            disable_password_authentication=dict(
                                type='bool',
                                disposition='disable_password_authentication'
                            ),
                            ssh=dict(
                                type='dict',
                                disposition='ssh',
                                options=dict(
                                    public_keys=dict(
                                        type='list',
                                        disposition='public_keys'
                                    )
                                )
                            ),
                            provision_vm_agent=dict(
                                type='bool',
                                disposition='provision_vm_agent'
                            )
                        )
                    ),
                    secrets=dict(
                        type='list',
                        disposition='secrets'
                    ),
                    allow_extension_operations=dict(
                        type='bool',
                        disposition='allow_extension_operations'
                    ),
                    require_guest_provision_signal=dict(
                        type='bool',
                        disposition='require_guest_provision_signal'
                    )
                )
            ),
            network_profile=dict(
                type='dict',
                disposition='/network_profile',
                options=dict(
                    network_interfaces=dict(
                        type='list',
                        disposition='network_interfaces'
                    )
                )
            ),
            security_profile=dict(
                type='dict',
                disposition='/security_profile',
                options=dict(
                    encryption_at_host=dict(
                        type='bool',
                        disposition='encryption_at_host'
                    )
                )
            ),
            diagnostics_profile=dict(
                type='dict',
                disposition='/diagnostics_profile',
                options=dict(
                    boot_diagnostics=dict(
                        type='dict',
                        disposition='boot_diagnostics',
                        options=dict(
                            enabled=dict(
                                type='bool',
                                disposition='enabled'
                            ),
                            storage_uri=dict(
                                type='str',
                                disposition='storage_uri'
                            )
                        )
                    )
                )
            ),
            availability_set=dict(
                type='dict',
                disposition='/availability_set',
                options=dict(
                    id=dict(
                        type='str',
                        disposition='id'
                    )
                )
            ),
            virtual_machine_scale_set=dict(
                type='dict',
                disposition='/virtual_machine_scale_set',
                options=dict(
                    id=dict(
                        type='str',
                        disposition='id'
                    )
                )
            ),
            proximity_placement_group=dict(
                type='dict',
                disposition='/proximity_placement_group',
                options=dict(
                    id=dict(
                        type='str',
                        disposition='id'
                    )
                )
            ),
            priority=dict(
                type='choice',
                disposition='/priority'
            ),
            eviction_policy=dict(
                type='choice',
                disposition='/eviction_policy'
            ),
            billing_profile=dict(
                type='dict',
                disposition='/billing_profile',
                options=dict(
                    max_price=dict(
                        type='number',
                        disposition='max_price'
                    )
                )
            ),
            host=dict(
                type='dict',
                disposition='/host',
                options=dict(
                    id=dict(
                        type='str',
                        disposition='id'
                    )
                )
            ),
            host_group=dict(
                type='dict',
                disposition='/host_group',
                options=dict(
                    id=dict(
                        type='str',
                        disposition='id'
                    )
                )
            ),
            license_type=dict(
                type='str',
                disposition='/license_type'
            ),
            extensions_time_budget=dict(
                type='str',
                disposition='/extensions_time_budget'
            ),
            expand=dict(
                type='constant'
            ),
            status_only=dict(
                type='str'
            ),
            skip_shutdown=dict(
                type='bool'
            ),
            temp_disk=dict(
                type='bool',
                disposition='/temp_disk'
            ),
            sas_uri_expiration_time_in_minutes=dict(
                type='integer'
            ),
            command_id=dict(
                type='str',
                disposition='/command_id'
            ),
            script=dict(
                type='list',
                disposition='/script'
            ),
            parameters=dict(
                type='list',
                disposition='/parameters'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.location = None
        self.resource_group_name = None
        self.vm_name = None
        self.expand = None
        self.status_only = None
        self.skip_shutdown = None
        self.sas_uri_expiration_time_in_minutes = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMVirtualMachine, self).__init__(derived_arg_spec=self.module_arg_spec,
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
            response = self.mgmt_client.virtual_machines.create_or_update(resource_group_name=self.resource_group_name,
                                                                          vm_name=self.vm_name,
                                                                          parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the VirtualMachine instance.')
            self.fail('Error creating the VirtualMachine instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.virtual_machines.delete(resource_group_name=self.resource_group_name,
                                                                vm_name=self.vm_name)
        except CloudError as e:
            self.log('Error attempting to delete the VirtualMachine instance.')
            self.fail('Error deleting the VirtualMachine instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        found = False
        try:
            response = self.mgmt_client.virtual_machines.get(resource_group_name=self.resource_group_name,
                                                             vm_name=self.vm_name,
                                                             expand=self.expand)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMVirtualMachine()


if __name__ == '__main__':
    main()
