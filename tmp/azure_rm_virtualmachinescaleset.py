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


class AzureRMVirtualMachineScaleSet(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str'
            ),
            vm_scale_set_name=dict(
                type='str'
            ),
            location=dict(
                type='str',
                disposition='/location'
            ),
            sku=dict(
                type='dict',
                disposition='/sku',
                options=dict(
                    name=dict(
                        type='str',
                        disposition='name'
                    ),
                    tier=dict(
                        type='str',
                        disposition='tier'
                    ),
                    capacity=dict(
                        type='integer',
                        disposition='capacity'
                    )
                )
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
            upgrade_policy=dict(
                type='dict',
                disposition='/upgrade_policy',
                options=dict(
                    mode=dict(
                        type='sealed-choice',
                        disposition='mode'
                    ),
                    rolling_upgrade_policy=dict(
                        type='dict',
                        disposition='rolling_upgrade_policy',
                        options=dict(
                            max_batch_instance_percent=dict(
                                type='integer',
                                disposition='max_batch_instance_percent'
                            ),
                            max_unhealthy_instance_percent=dict(
                                type='integer',
                                disposition='max_unhealthy_instance_percent'
                            ),
                            max_unhealthy_upgraded_instance_percent=dict(
                                type='integer',
                                disposition='max_unhealthy_upgraded_instance_percent'
                            ),
                            pause_time_between_batches=dict(
                                type='str',
                                disposition='pause_time_between_batches'
                            )
                        )
                    ),
                    automatic_os_upgrade_policy=dict(
                        type='dict',
                        disposition='automatic_os_upgrade_policy',
                        options=dict(
                            enable_automatic_os_upgrade=dict(
                                type='bool',
                                disposition='enable_automatic_os_upgrade'
                            ),
                            disable_automatic_rollback=dict(
                                type='bool',
                                disposition='disable_automatic_rollback'
                            )
                        )
                    )
                )
            ),
            automatic_repairs_policy=dict(
                type='dict',
                disposition='/automatic_repairs_policy',
                options=dict(
                    enabled=dict(
                        type='bool',
                        disposition='enabled'
                    ),
                    grace_period=dict(
                        type='str',
                        disposition='grace_period'
                    )
                )
            ),
            virtual_machine_profile=dict(
                type='dict',
                disposition='/virtual_machine_profile',
                options=dict(
                    os_profile=dict(
                        type='dict',
                        disposition='os_profile',
                        options=dict(
                            computer_name_prefix=dict(
                                type='str',
                                disposition='computer_name_prefix'
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
                            )
                        )
                    ),
                    storage_profile=dict(
                        type='dict',
                        disposition='storage_profile',
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
                                    name=dict(
                                        type='str',
                                        disposition='name'
                                    ),
                                    caching=dict(
                                        type='sealed-choice',
                                        disposition='caching'
                                    ),
                                    write_accelerator_enabled=dict(
                                        type='bool',
                                        disposition='write_accelerator_enabled'
                                    ),
                                    create_option=dict(
                                        type='choice',
                                        disposition='create_option',
                                        required=True
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
                                    disk_size_gb=dict(
                                        type='integer',
                                        disposition='disk_size_gb'
                                    ),
                                    os_type=dict(
                                        type='sealed-choice',
                                        disposition='os_type'
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
                                    vhd_containers=dict(
                                        type='list',
                                        disposition='vhd_containers'
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
                    network_profile=dict(
                        type='dict',
                        disposition='network_profile',
                        options=dict(
                            health_probe=dict(
                                type='dict',
                                disposition='health_probe',
                                options=dict(
                                    id=dict(
                                        type='str',
                                        disposition='id'
                                    )
                                )
                            ),
                            network_interface_configurations=dict(
                                type='list',
                                disposition='network_interface_configurations'
                            )
                        )
                    ),
                    security_profile=dict(
                        type='dict',
                        disposition='security_profile',
                        options=dict(
                            encryption_at_host=dict(
                                type='bool',
                                disposition='encryption_at_host'
                            )
                        )
                    ),
                    diagnostics_profile=dict(
                        type='dict',
                        disposition='diagnostics_profile',
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
                    extension_profile=dict(
                        type='dict',
                        disposition='extension_profile',
                        options=dict(
                            extensions=dict(
                                type='list',
                                disposition='extensions'
                            ),
                            extensions_time_budget=dict(
                                type='str',
                                disposition='extensions_time_budget'
                            )
                        )
                    ),
                    license_type=dict(
                        type='str',
                        disposition='license_type'
                    ),
                    priority=dict(
                        type='choice',
                        disposition='priority'
                    ),
                    eviction_policy=dict(
                        type='choice',
                        disposition='eviction_policy'
                    ),
                    billing_profile=dict(
                        type='dict',
                        disposition='billing_profile',
                        options=dict(
                            max_price=dict(
                                type='number',
                                disposition='max_price'
                            )
                        )
                    ),
                    scheduled_events_profile=dict(
                        type='dict',
                        disposition='scheduled_events_profile',
                        options=dict(
                            terminate_notification_profile=dict(
                                type='dict',
                                disposition='terminate_notification_profile',
                                options=dict(
                                    not_before_timeout=dict(
                                        type='str',
                                        disposition='not_before_timeout'
                                    ),
                                    enable=dict(
                                        type='bool',
                                        disposition='enable'
                                    )
                                )
                            )
                        )
                    )
                )
            ),
            overprovision=dict(
                type='bool',
                disposition='/overprovision'
            ),
            do_not_run_extensions_on_overprovisioned_vms=dict(
                type='bool',
                disposition='/do_not_run_extensions_on_overprovisioned_vms'
            ),
            single_placement_group=dict(
                type='bool',
                disposition='/single_placement_group'
            ),
            zone_balance=dict(
                type='bool',
                disposition='/zone_balance'
            ),
            platform_fault_domain_count=dict(
                type='integer',
                disposition='/platform_fault_domain_count'
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
            scale_in_policy=dict(
                type='dict',
                disposition='/scale_in_policy',
                options=dict(
                    rules=dict(
                        type='list',
                        disposition='rules'
                    )
                )
            ),
            id=dict(
                type='str',
                disposition='/id'
            ),
            ultra_ssd_enabled=dict(
                type='bool',
                disposition='/ultra_ssd_enabled'
            ),
            os_profile=dict(
                type='dict',
                disposition='/os_profile',
                options=dict(
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
                            caching=dict(
                                type='sealed-choice',
                                disposition='caching'
                            ),
                            write_accelerator_enabled=dict(
                                type='bool',
                                disposition='write_accelerator_enabled'
                            ),
                            disk_size_gb=dict(
                                type='integer',
                                disposition='disk_size_gb'
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
                            vhd_containers=dict(
                                type='list',
                                disposition='vhd_containers'
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
            network_profile=dict(
                type='dict',
                disposition='/network_profile',
                options=dict(
                    health_probe=dict(
                        type='dict',
                        disposition='health_probe',
                        options=dict(
                            id=dict(
                                type='str',
                                disposition='id'
                            )
                        )
                    ),
                    network_interface_configurations=dict(
                        type='list',
                        disposition='network_interface_configurations'
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
            extension_profile=dict(
                type='dict',
                disposition='/extension_profile',
                options=dict(
                    extensions=dict(
                        type='list',
                        disposition='extensions'
                    ),
                    extensions_time_budget=dict(
                        type='str',
                        disposition='extensions_time_budget'
                    )
                )
            ),
            license_type=dict(
                type='str',
                disposition='/license_type'
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
            scheduled_events_profile=dict(
                type='dict',
                disposition='/scheduled_events_profile',
                options=dict(
                    terminate_notification_profile=dict(
                        type='dict',
                        disposition='terminate_notification_profile',
                        options=dict(
                            not_before_timeout=dict(
                                type='str',
                                disposition='not_before_timeout'
                            ),
                            enable=dict(
                                type='bool',
                                disposition='enable'
                            )
                        )
                    )
                )
            ),
            mode=dict(
                type='sealed-choice',
                disposition='/mode'
            ),
            rolling_upgrade_policy=dict(
                type='dict',
                disposition='/rolling_upgrade_policy',
                options=dict(
                    max_batch_instance_percent=dict(
                        type='integer',
                        disposition='max_batch_instance_percent'
                    ),
                    max_unhealthy_instance_percent=dict(
                        type='integer',
                        disposition='max_unhealthy_instance_percent'
                    ),
                    max_unhealthy_upgraded_instance_percent=dict(
                        type='integer',
                        disposition='max_unhealthy_upgraded_instance_percent'
                    ),
                    pause_time_between_batches=dict(
                        type='str',
                        disposition='pause_time_between_batches'
                    )
                )
            ),
            automatic_os_upgrade_policy=dict(
                type='dict',
                disposition='/automatic_os_upgrade_policy',
                options=dict(
                    enable_automatic_os_upgrade=dict(
                        type='bool',
                        disposition='enable_automatic_os_upgrade'
                    ),
                    disable_automatic_rollback=dict(
                        type='bool',
                        disposition='disable_automatic_rollback'
                    )
                )
            ),
            instance_ids=dict(
                type='list',
                disposition='/instance_ids'
            ),
            skip_shutdown=dict(
                type='bool'
            ),
            temp_disk=dict(
                type='bool',
                disposition='/temp_disk'
            ),
            platform_update_domain=dict(
                type='integer'
            ),
            active_placement_group_id=dict(
                type='str',
                disposition='/active_placement_group_id'
            ),
            service_name=dict(
                type='choice',
                disposition='/service_name'
            ),
            action=dict(
                type='choice',
                disposition='/action'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group_name = None
        self.vm_scale_set_name = None
        self.skip_shutdown = None
        self.platform_update_domain = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMVirtualMachineScaleSet, self).__init__(derived_arg_spec=self.module_arg_spec,
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
            response = self.mgmt_client.virtual_machine_scale_sets.create_or_update(resource_group_name=self.resource_group_name,
                                                                                    vm_scale_set_name=self.vm_scale_set_name,
                                                                                    parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the VirtualMachineScaleSet instance.')
            self.fail('Error creating the VirtualMachineScaleSet instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.virtual_machine_scale_sets.delete(resource_group_name=self.resource_group_name,
                                                                          vm_scale_set_name=self.vm_scale_set_name)
        except CloudError as e:
            self.log('Error attempting to delete the VirtualMachineScaleSet instance.')
            self.fail('Error deleting the VirtualMachineScaleSet instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        found = False
        try:
            response = self.mgmt_client.virtual_machine_scale_sets.get(resource_group_name=self.resource_group_name,
                                                                       vm_scale_set_name=self.vm_scale_set_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMVirtualMachineScaleSet()


if __name__ == '__main__':
    main()
