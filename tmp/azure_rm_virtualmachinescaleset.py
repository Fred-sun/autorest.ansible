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
                disposition='null'
            ),
            sku=dict(
                type='dict',
                disposition='null',
                options=dict(
                    name=dict(
                        type='str',
                        disposition='null'
                    ),
                    tier=dict(
                        type='str',
                        disposition='null'
                    ),
                    capacity=dict(
                        type='integer',
                        disposition='null'
                    )
                )
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
            upgrade_policy=dict(
                type='dict',
                disposition='null',
                options=dict(
                    mode=dict(
                        type='sealed-choice',
                        disposition='null'
                    ),
                    rolling_upgrade_policy=dict(
                        type='dict',
                        disposition='null',
                        options=dict(
                            max_batch_instance_percent=dict(
                                type='integer',
                                disposition='null'
                            ),
                            max_unhealthy_instance_percent=dict(
                                type='integer',
                                disposition='null'
                            ),
                            max_unhealthy_upgraded_instance_percent=dict(
                                type='integer',
                                disposition='null'
                            ),
                            pause_time_between_batches=dict(
                                type='str',
                                disposition='null'
                            )
                        )
                    ),
                    automatic_os_upgrade_policy=dict(
                        type='dict',
                        disposition='null',
                        options=dict(
                            enable_automatic_os_upgrade=dict(
                                type='bool',
                                disposition='null'
                            ),
                            disable_automatic_rollback=dict(
                                type='bool',
                                disposition='null'
                            )
                        )
                    )
                )
            ),
            automatic_repairs_policy=dict(
                type='dict',
                disposition='null',
                options=dict(
                    enabled=dict(
                        type='bool',
                        disposition='null'
                    ),
                    grace_period=dict(
                        type='str',
                        disposition='null'
                    )
                )
            ),
            virtual_machine_profile=dict(
                type='dict',
                disposition='null',
                options=dict(
                    os_profile=dict(
                        type='dict',
                        disposition='null',
                        options=dict(
                            computer_name_prefix=dict(
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
                                    name=dict(
                                        type='str',
                                        disposition='null'
                                    ),
                                    caching=dict(
                                        type='sealed-choice',
                                        disposition='null'
                                    ),
                                    write_accelerator_enabled=dict(
                                        type='bool',
                                        disposition='null'
                                    ),
                                    create_option=dict(
                                        type='choice',
                                        disposition='null',
                                        required=true
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
                                    disk_size_gb=dict(
                                        type='integer',
                                        disposition='null'
                                    ),
                                    os_type=dict(
                                        type='sealed-choice',
                                        disposition='null'
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
                                    vhd_containers=dict(
                                        type='list',
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
                    network_profile=dict(
                        type='dict',
                        disposition='null',
                        options=dict(
                            health_probe=dict(
                                type='dict',
                                disposition='null',
                                options=dict(
                                    id=dict(
                                        type='str',
                                        disposition='null'
                                    )
                                )
                            ),
                            network_interface_configurations=dict(
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
                    extension_profile=dict(
                        type='dict',
                        disposition='null',
                        options=dict(
                            extensions=dict(
                                type='list',
                                disposition='null'
                            ),
                            extensions_time_budget=dict(
                                type='str',
                                disposition='null'
                            )
                        )
                    ),
                    license_type=dict(
                        type='str',
                        disposition='null'
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
                    scheduled_events_profile=dict(
                        type='dict',
                        disposition='null',
                        options=dict(
                            terminate_notification_profile=dict(
                                type='dict',
                                disposition='null',
                                options=dict(
                                    not_before_timeout=dict(
                                        type='str',
                                        disposition='null'
                                    ),
                                    enable=dict(
                                        type='bool',
                                        disposition='null'
                                    )
                                )
                            )
                        )
                    )
                )
            ),
            overprovision=dict(
                type='bool',
                disposition='null'
            ),
            do_not_run_extensions_on_overprovisioned_vms=dict(
                type='bool',
                disposition='null'
            ),
            single_placement_group=dict(
                type='bool',
                disposition='null'
            ),
            zone_balance=dict(
                type='bool',
                disposition='null'
            ),
            platform_fault_domain_count=dict(
                type='integer',
                disposition='null'
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
            scale_in_policy=dict(
                type='dict',
                disposition='null',
                options=dict(
                    rules=dict(
                        type='list',
                        disposition='null'
                    )
                )
            ),
            id=dict(
                type='str',
                disposition='null'
            ),
            ultra_ssd_enabled=dict(
                type='bool',
                disposition='null'
            ),
            os_profile=dict(
                type='dict',
                disposition='null',
                options=dict(
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
                            caching=dict(
                                type='sealed-choice',
                                disposition='null'
                            ),
                            write_accelerator_enabled=dict(
                                type='bool',
                                disposition='null'
                            ),
                            disk_size_gb=dict(
                                type='integer',
                                disposition='null'
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
                            vhd_containers=dict(
                                type='list',
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
            network_profile=dict(
                type='dict',
                disposition='null',
                options=dict(
                    health_probe=dict(
                        type='dict',
                        disposition='null',
                        options=dict(
                            id=dict(
                                type='str',
                                disposition='null'
                            )
                        )
                    ),
                    network_interface_configurations=dict(
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
            extension_profile=dict(
                type='dict',
                disposition='null',
                options=dict(
                    extensions=dict(
                        type='list',
                        disposition='null'
                    ),
                    extensions_time_budget=dict(
                        type='str',
                        disposition='null'
                    )
                )
            ),
            license_type=dict(
                type='str',
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
            scheduled_events_profile=dict(
                type='dict',
                disposition='null',
                options=dict(
                    terminate_notification_profile=dict(
                        type='dict',
                        disposition='null',
                        options=dict(
                            not_before_timeout=dict(
                                type='str',
                                disposition='null'
                            ),
                            enable=dict(
                                type='bool',
                                disposition='null'
                            )
                        )
                    )
                )
            ),
            mode=dict(
                type='sealed-choice',
                disposition='null'
            ),
            rolling_upgrade_policy=dict(
                type='dict',
                disposition='null',
                options=dict(
                    max_batch_instance_percent=dict(
                        type='integer',
                        disposition='null'
                    ),
                    max_unhealthy_instance_percent=dict(
                        type='integer',
                        disposition='null'
                    ),
                    max_unhealthy_upgraded_instance_percent=dict(
                        type='integer',
                        disposition='null'
                    ),
                    pause_time_between_batches=dict(
                        type='str',
                        disposition='null'
                    )
                )
            ),
            automatic_os_upgrade_policy=dict(
                type='dict',
                disposition='null',
                options=dict(
                    enable_automatic_os_upgrade=dict(
                        type='bool',
                        disposition='null'
                    ),
                    disable_automatic_rollback=dict(
                        type='bool',
                        disposition='null'
                    )
                )
            ),
            instance_ids=dict(
                type='list',
                disposition='null'
            ),
            skip_shutdown=dict(
                type='bool'
            ),
            temp_disk=dict(
                type='bool',
                disposition='null'
            ),
            platform_update_domain=dict(
                type='integer'
            ),
            active_placement_group_id=dict(
                type='str',
                disposition='null'
            ),
            service_name=dict(
                type='choice',
                disposition='null'
            ),
            action=dict(
                type='choice',
                disposition='null'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group_name = None
        self.vm_scale_set_name = None
        self.location = None
        self.tags = None
        self.sku = None
        self.plan = None
        self.zones = None
        self.type = None
        self.user_assigned_identities = None
        self.upgrade_policy = None
        self.automatic_repairs_policy = None
        self.virtual_machine_profile = None
        self.overprovision = None
        self.do_not_run_extensions_on_overprovisioned_vms = None
        self.single_placement_group = None
        self.zone_balance = None
        self.platform_fault_domain_count = None
        self.proximity_placement_group = None
        self.host_group = None
        self.additional_capabilities = None
        self.scale_in_policy = None
        self.id = None
        self.ultra_ssd_enabled = None
        self.os_profile = None
        self.storage_profile = None
        self.network_profile = None
        self.security_profile = None
        self.diagnostics_profile = None
        self.extension_profile = None
        self.license_type = None
        self.billing_profile = None
        self.scheduled_events_profile = None
        self.mode = None
        self.rolling_upgrade_policy = None
        self.automatic_os_upgrade_policy = None
        self.instance_ids = None
        self.skip_shutdown = None
        self.temp_disk = None
        self.platform_update_domain = None
        self.active_placement_group_id = None
        self.service_name = None
        self.action = None
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
            response = self.mgmt_client.virtualmachinescalesets.create_or_update(resource_group_name=self.resource_group_name,
                                                                                 vm_scale_set_name=self.vm_scale_set_name,
                                                                                 location=self.location)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the VirtualMachineScaleSet instance.')
            self.fail('Error creating the VirtualMachineScaleSet instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.virtualmachinescalesets.delete(resource_group_name=self.resource_group_name,
                                                                       vm_scale_set_name=self.vm_scale_set_name)
        except CloudError as e:
            self.log('Error attempting to delete the VirtualMachineScaleSet instance.')
            self.fail('Error deleting the VirtualMachineScaleSet instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        found = False
        try:
            response = self.mgmt_client.virtualmachinescalesets.get(resource_group_name=self.resource_group_name,
                                                                    vm_scale_set_name=self.vm_scale_set_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMVirtualMachineScaleSet()


if __name__ == '__main__':
    main()
