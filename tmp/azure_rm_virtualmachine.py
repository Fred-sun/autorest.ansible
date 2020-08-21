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
                disposition='null'
            ),
            destination_container_name=dict(
                type='str',
                disposition='null'
            ),
            overwrite_vhds=dict(
                type='bool',
                disposition='null'
            ),
            plan=dict(
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
                    ),
                    promotion_code=dict(
                        type='str',
                        disposition='null'
                    )
                )
            ),
            zones=dict(
                type='list',
                disposition='null'
            ),
            type=dict(
                type='sealed-choice',
                disposition='null'
            ),
            user_assigned_identities=dict(
                type='dictionary',
                disposition='null'
            ),
            hardware_profile=dict(
                type='dict',
                disposition='null',
                options=dict(
                    vm_size=dict(
                        type='choice',
                        disposition='null'
                    )
                )
            ),
            storage_profile=dict(
                type='dict',
                disposition='null',
                options=dict(
                    image_reference=dict(
                        type='dict',
                        disposition='null',
                        options=dict(
                            publisher=dict(
                                type='str',
                                disposition='null'
                            ),
                            offer=dict(
                                type='str',
                                disposition='null'
                            ),
                            sku=dict(
                                type='str',
                                disposition='null'
                            ),
                            version=dict(
                                type='str',
                                disposition='null'
                            ),
                            exact_version=dict(
                                type='str',
                                updatable=False,
                                disposition='null'
                            )
                        )
                    ),
                    os_disk=dict(
                        type='dict',
                        disposition='null',
                        options=dict(
                            os_type=dict(
                                type='sealed-choice',
                                disposition='null'
                            ),
                            encryption_settings=dict(
                                type='dict',
                                disposition='null',
                                options=dict(
                                    disk_encryption_key=dict(
                                        type='dict',
                                        disposition='null',
                                        options=dict(
                                            secret_url=dict(
                                                type='str',
                                                disposition='null',
                                                required=true
                                            ),
                                            source_vault=dict(
                                                type='dict',
                                                disposition='null',
                                                required=true,
                                                options=dict(
                                                    id=dict(
                                                        type='str',
                                                        disposition='null'
                                                    )
                                                )
                                            )
                                        )
                                    ),
                                    key_encryption_key=dict(
                                        type='dict',
                                        disposition='null',
                                        options=dict(
                                            key_url=dict(
                                                type='str',
                                                disposition='null',
                                                required=true
                                            ),
                                            source_vault=dict(
                                                type='dict',
                                                disposition='null',
                                                required=true,
                                                options=dict(
                                                    id=dict(
                                                        type='str',
                                                        disposition='null'
                                                    )
                                                )
                                            )
                                        )
                                    ),
                                    enabled=dict(
                                        type='bool',
                                        disposition='null'
                                    )
                                )
                            ),
                            name=dict(
                                type='str',
                                disposition='null'
                            ),
                            vhd=dict(
                                type='dict',
                                disposition='null',
                                options=dict(
                                    uri=dict(
                                        type='str',
                                        disposition='null'
                                    )
                                )
                            ),
                            image=dict(
                                type='dict',
                                disposition='null',
                                options=dict(
                                    uri=dict(
                                        type='str',
                                        disposition='null'
                                    )
                                )
                            ),
                            caching=dict(
                                type='sealed-choice',
                                disposition='null'
                            ),
                            write_accelerator_enabled=dict(
                                type='bool',
                                disposition='null'
                            ),
                            diff_disk_settings=dict(
                                type='dict',
                                disposition='null',
                                options=dict(
                                    option=dict(
                                        type='choice',
                                        disposition='null'
                                    ),
                                    placement=dict(
                                        type='choice',
                                        disposition='null'
                                    )
                                )
                            ),
                            create_option=dict(
                                type='choice',
                                disposition='null',
                                required=true
                            ),
                            disk_size_gb=dict(
                                type='integer',
                                disposition='null'
                            ),
                            managed_disk=dict(
                                type='dict',
                                disposition='null',
                                options=dict(
                                    storage_account_type=dict(
                                        type='choice',
                                        disposition='null'
                                    ),
                                    disk_encryption_set=dict(
                                        type='dict',
                                        disposition='null',
                                        options=dict(
                                            id=dict(
                                                type='str',
                                                disposition='null'
                                            )
                                        )
                                    )
                                )
                            )
                        )
                    ),
                    data_disks=dict(
                        type='list',
                        disposition='null'
                    )
                )
            ),
            additional_capabilities=dict(
                type='dict',
                disposition='null',
                options=dict(
                    ultra_ssd_enabled=dict(
                        type='bool',
                        disposition='null'
                    )
                )
            ),
            os_profile=dict(
                type='dict',
                disposition='null',
                options=dict(
                    computer_name=dict(
                        type='str',
                        disposition='null'
                    ),
                    admin_username=dict(
                        type='str',
                        disposition='null'
                    ),
                    admin_password=dict(
                        type='str',
                        disposition='null'
                    ),
                    custom_data=dict(
                        type='str',
                        disposition='null'
                    ),
                    windows_configuration=dict(
                        type='dict',
                        disposition='null',
                        options=dict(
                            provision_vm_agent=dict(
                                type='bool',
                                disposition='null'
                            ),
                            enable_automatic_updates=dict(
                                type='bool',
                                disposition='null'
                            ),
                            time_zone=dict(
                                type='str',
                                disposition='null'
                            ),
                            additional_unattend_content=dict(
                                type='list',
                                disposition='null'
                            ),
                            patch_settings=dict(
                                type='dict',
                                disposition='null',
                                options=dict(
                                    patch_mode=dict(
                                        type='choice',
                                        disposition='null'
                                    )
                                )
                            ),
                            win_rm=dict(
                                type='dict',
                                disposition='null',
                                options=dict(
                                    listeners=dict(
                                        type='list',
                                        disposition='null'
                                    )
                                )
                            )
                        )
                    ),
                    linux_configuration=dict(
                        type='dict',
                        disposition='null',
                        options=dict(
                            disable_password_authentication=dict(
                                type='bool',
                                disposition='null'
                            ),
                            ssh=dict(
                                type='dict',
                                disposition='null',
                                options=dict(
                                    public_keys=dict(
                                        type='list',
                                        disposition='null'
                                    )
                                )
                            ),
                            provision_vm_agent=dict(
                                type='bool',
                                disposition='null'
                            )
                        )
                    ),
                    secrets=dict(
                        type='list',
                        disposition='null'
                    ),
                    allow_extension_operations=dict(
                        type='bool',
                        disposition='null'
                    ),
                    require_guest_provision_signal=dict(
                        type='bool',
                        disposition='null'
                    )
                )
            ),
            network_profile=dict(
                type='dict',
                disposition='null',
                options=dict(
                    network_interfaces=dict(
                        type='list',
                        disposition='null'
                    )
                )
            ),
            security_profile=dict(
                type='dict',
                disposition='null',
                options=dict(
                    encryption_at_host=dict(
                        type='bool',
                        disposition='null'
                    )
                )
            ),
            diagnostics_profile=dict(
                type='dict',
                disposition='null',
                options=dict(
                    boot_diagnostics=dict(
                        type='dict',
                        disposition='null',
                        options=dict(
                            enabled=dict(
                                type='bool',
                                disposition='null'
                            ),
                            storage_uri=dict(
                                type='str',
                                disposition='null'
                            )
                        )
                    )
                )
            ),
            availability_set=dict(
                type='dict',
                disposition='null',
                options=dict(
                    id=dict(
                        type='str',
                        disposition='null'
                    )
                )
            ),
            virtual_machine_scale_set=dict(
                type='dict',
                disposition='null',
                options=dict(
                    id=dict(
                        type='str',
                        disposition='null'
                    )
                )
            ),
            proximity_placement_group=dict(
                type='dict',
                disposition='null',
                options=dict(
                    id=dict(
                        type='str',
                        disposition='null'
                    )
                )
            ),
            priority=dict(
                type='choice',
                disposition='null'
            ),
            eviction_policy=dict(
                type='choice',
                disposition='null'
            ),
            billing_profile=dict(
                type='dict',
                disposition='null',
                options=dict(
                    max_price=dict(
                        type='number',
                        disposition='null'
                    )
                )
            ),
            host=dict(
                type='dict',
                disposition='null',
                options=dict(
                    id=dict(
                        type='str',
                        disposition='null'
                    )
                )
            ),
            host_group=dict(
                type='dict',
                disposition='null',
                options=dict(
                    id=dict(
                        type='str',
                        disposition='null'
                    )
                )
            ),
            license_type=dict(
                type='str',
                disposition='null'
            ),
            extensions_time_budget=dict(
                type='str',
                disposition='null'
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
                disposition='null'
            ),
            sas_uri_expiration_time_in_minutes=dict(
                type='integer'
            ),
            command_id=dict(
                type='str',
                disposition='null'
            ),
            script=dict(
                type='list',
                disposition='null'
            ),
            parameters=dict(
                type='list',
                disposition='null'
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
        self.vhd_prefix = None
        self.destination_container_name = None
        self.overwrite_vhds = None
        self.tags = None
        self.plan = None
        self.zones = None
        self.type = None
        self.user_assigned_identities = None
        self.hardware_profile = None
        self.storage_profile = None
        self.additional_capabilities = None
        self.os_profile = None
        self.network_profile = None
        self.security_profile = None
        self.diagnostics_profile = None
        self.availability_set = None
        self.virtual_machine_scale_set = None
        self.proximity_placement_group = None
        self.priority = None
        self.eviction_policy = None
        self.billing_profile = None
        self.host = None
        self.host_group = None
        self.license_type = None
        self.extensions_time_budget = None
        self.expand = None
        self.status_only = None
        self.skip_shutdown = None
        self.temp_disk = None
        self.sas_uri_expiration_time_in_minutes = None
        self.command_id = None
        self.script = None
        self.parameters = None
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
            response = self.mgmt_client.virtualmachines.create_or_update(resource_group_name=self.resource_group_name,
                                                                         vm_name=self.vm_name,
                                                                         location=self.location)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the VirtualMachine instance.')
            self.fail('Error creating the VirtualMachine instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.virtualmachines.delete(resource_group_name=self.resource_group_name,
                                                               vm_name=self.vm_name)
        except CloudError as e:
            self.log('Error attempting to delete the VirtualMachine instance.')
            self.fail('Error deleting the VirtualMachine instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        found = False
        try:
            response = self.mgmt_client.virtualmachines.get(resource_group_name=self.resource_group_name,
                                                            vm_name=self.vm_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMVirtualMachine()


if __name__ == '__main__':
    main()
