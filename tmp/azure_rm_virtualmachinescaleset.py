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
from ansible.module_utils.azure_rm_common_rest import GenericRestClient
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
except ImportError:
    # this is handled in azure_rm_common
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
                        disposition='/name'
                    ),
                    tier=dict(
                        type='str',
                        disposition='/tier'
                    ),
                    capacity=dict(
                        type='integer',
                        disposition='/capacity'
                    )
                )
            ),
            plan=dict(
                type='dict',
                disposition='/properties/plan',
                options=dict(
                    name=dict(
                        type='str',
                        disposition='/name'
                    ),
                    publisher=dict(
                        type='str',
                        disposition='/publisher'
                    ),
                    product=dict(
                        type='str',
                        disposition='/product'
                    ),
                    promotion_code=dict(
                        type='str',
                        disposition='/promotionCode'
                    )
                )
            ),
            zones=dict(
                type='list',
                disposition='/properties/zones'
            ),
            type=dict(
                type='sealed-choice',
                disposition='/properties/type'
            ),
            user_assigned_identities=dict(
                type='dictionary',
                disposition='/properties/userAssignedIdentities'
            ),
            upgrade_policy=dict(
                type='dict',
                disposition='/properties/upgradePolicy',
                options=dict(
                    mode=dict(
                        type='sealed-choice',
                        disposition='/mode'
                    ),
                    rolling_upgrade_policy=dict(
                        type='dict',
                        disposition='/rollingUpgradePolicy',
                        options=dict(
                            max_batch_instance_percent=dict(
                                type='integer',
                                disposition='/maxBatchInstancePercent'
                            ),
                            max_unhealthy_instance_percent=dict(
                                type='integer',
                                disposition='/maxUnhealthyInstancePercent'
                            ),
                            max_unhealthy_upgraded_instance_percent=dict(
                                type='integer',
                                disposition='/maxUnhealthyUpgradedInstancePercent'
                            ),
                            pause_time_between_batches=dict(
                                type='str',
                                disposition='/pauseTimeBetweenBatches'
                            )
                        )
                    ),
                    automatic_os_upgrade_policy=dict(
                        type='dict',
                        disposition='/automaticOsUpgradePolicy',
                        options=dict(
                            enable_automatic_os_upgrade=dict(
                                type='bool',
                                disposition='/enableAutomaticOsUpgrade'
                            ),
                            disable_automatic_rollback=dict(
                                type='bool',
                                disposition='/disableAutomaticRollback'
                            )
                        )
                    )
                )
            ),
            automatic_repairs_policy=dict(
                type='dict',
                disposition='/properties/automaticRepairsPolicy',
                options=dict(
                    enabled=dict(
                        type='bool',
                        disposition='/enabled'
                    ),
                    grace_period=dict(
                        type='str',
                        disposition='/gracePeriod'
                    )
                )
            ),
            virtual_machine_profile=dict(
                type='dict',
                disposition='/properties/virtualMachineProfile',
                options=dict(
                    os_profile=dict(
                        type='dict',
                        disposition='/osProfile',
                        options=dict(
                            computer_name_prefix=dict(
                                type='str',
                                disposition='/computerNamePrefix'
                            ),
                            admin_username=dict(
                                type='str',
                                disposition='/adminUsername'
                            ),
                            admin_password=dict(
                                type='str',
                                disposition='/adminPassword'
                            ),
                            custom_data=dict(
                                type='str',
                                disposition='/customData'
                            ),
                            windows_configuration=dict(
                                type='dict',
                                disposition='/windowsConfiguration',
                                options=dict(
                                    provision_vm_agent=dict(
                                        type='bool',
                                        disposition='/provisionVmAgent'
                                    ),
                                    enable_automatic_updates=dict(
                                        type='bool',
                                        disposition='/enableAutomaticUpdates'
                                    ),
                                    time_zone=dict(
                                        type='str',
                                        disposition='/timeZone'
                                    ),
                                    additional_unattend_content=dict(
                                        type='list',
                                        disposition='/additionalUnattendContent'
                                    ),
                                    patch_settings=dict(
                                        type='dict',
                                        disposition='/patchSettings',
                                        options=dict(
                                            patch_mode=dict(
                                                type='choice',
                                                disposition='/patchMode'
                                            )
                                        )
                                    ),
                                    win_rm=dict(
                                        type='dict',
                                        disposition='/winRm',
                                        options=dict(
                                            listeners=dict(
                                                type='list',
                                                disposition='/listeners'
                                            )
                                        )
                                    )
                                )
                            ),
                            linux_configuration=dict(
                                type='dict',
                                disposition='/linuxConfiguration',
                                options=dict(
                                    disable_password_authentication=dict(
                                        type='bool',
                                        disposition='/disablePasswordAuthentication'
                                    ),
                                    ssh=dict(
                                        type='dict',
                                        disposition='/ssh',
                                        options=dict(
                                            public_keys=dict(
                                                type='list',
                                                disposition='/publicKeys'
                                            )
                                        )
                                    ),
                                    provision_vm_agent=dict(
                                        type='bool',
                                        disposition='/provisionVmAgent'
                                    )
                                )
                            ),
                            secrets=dict(
                                type='list',
                                disposition='/secrets'
                            )
                        )
                    ),
                    storage_profile=dict(
                        type='dict',
                        disposition='/storageProfile',
                        options=dict(
                            image_reference=dict(
                                type='dict',
                                disposition='/imageReference',
                                options=dict(
                                    publisher=dict(
                                        type='str',
                                        disposition='/publisher'
                                    ),
                                    offer=dict(
                                        type='str',
                                        disposition='/offer'
                                    ),
                                    sku=dict(
                                        type='str',
                                        disposition='/sku'
                                    ),
                                    version=dict(
                                        type='str',
                                        disposition='/version'
                                    ),
                                    exact_version=dict(
                                        type='str',
                                        disposition='/exactVersion'
                                    )
                                )
                            ),
                            os_disk=dict(
                                type='dict',
                                disposition='/osDisk',
                                options=dict(
                                    name=dict(
                                        type='str',
                                        disposition='/name'
                                    ),
                                    caching=dict(
                                        type='sealed-choice',
                                        disposition='/caching'
                                    ),
                                    write_accelerator_enabled=dict(
                                        type='bool',
                                        disposition='/writeAcceleratorEnabled'
                                    ),
                                    create_option=dict(
                                        type='choice',
                                        disposition='/createOption',
                                        required=true
                                    ),
                                    diff_disk_settings=dict(
                                        type='dict',
                                        disposition='/diffDiskSettings',
                                        options=dict(
                                            option=dict(
                                                type='choice',
                                                disposition='/option'
                                            ),
                                            placement=dict(
                                                type='choice',
                                                disposition='/placement'
                                            )
                                        )
                                    ),
                                    disk_size_gb=dict(
                                        type='integer',
                                        disposition='/diskSizeGB'
                                    ),
                                    os_type=dict(
                                        type='sealed-choice',
                                        disposition='/osType'
                                    ),
                                    image=dict(
                                        type='dict',
                                        disposition='/image',
                                        options=dict(
                                            uri=dict(
                                                type='str',
                                                disposition='/uri'
                                            )
                                        )
                                    ),
                                    vhd_containers=dict(
                                        type='list',
                                        disposition='/vhdContainers'
                                    ),
                                    managed_disk=dict(
                                        type='dict',
                                        disposition='/managedDisk',
                                        options=dict(
                                            storage_account_type=dict(
                                                type='choice',
                                                disposition='/storageAccountType'
                                            ),
                                            disk_encryption_set=dict(
                                                type='dict',
                                                disposition='/diskEncryptionSet',
                                                options=dict(
                                                    id=dict(
                                                        type='str',
                                                        disposition='/id'
                                                    )
                                                )
                                            )
                                        )
                                    )
                                )
                            ),
                            data_disks=dict(
                                type='list',
                                disposition='/dataDisks'
                            )
                        )
                    ),
                    network_profile=dict(
                        type='dict',
                        disposition='/networkProfile',
                        options=dict(
                            health_probe=dict(
                                type='dict',
                                disposition='/healthProbe',
                                options=dict(
                                    id=dict(
                                        type='str',
                                        disposition='/id'
                                    )
                                )
                            ),
                            network_interface_configurations=dict(
                                type='list',
                                disposition='/networkInterfaceConfigurations'
                            )
                        )
                    ),
                    security_profile=dict(
                        type='dict',
                        disposition='/securityProfile',
                        options=dict(
                            encryption_at_host=dict(
                                type='bool',
                                disposition='/encryptionAtHost'
                            )
                        )
                    ),
                    diagnostics_profile=dict(
                        type='dict',
                        disposition='/diagnosticsProfile',
                        options=dict(
                            boot_diagnostics=dict(
                                type='dict',
                                disposition='/bootDiagnostics',
                                options=dict(
                                    enabled=dict(
                                        type='bool',
                                        disposition='/enabled'
                                    ),
                                    storage_uri=dict(
                                        type='str',
                                        disposition='/storageUri'
                                    )
                                )
                            )
                        )
                    ),
                    extension_profile=dict(
                        type='dict',
                        disposition='/extensionProfile',
                        options=dict(
                            extensions=dict(
                                type='list',
                                disposition='/extensions'
                            ),
                            extensions_time_budget=dict(
                                type='str',
                                disposition='/extensionsTimeBudget'
                            )
                        )
                    ),
                    license_type=dict(
                        type='str',
                        disposition='/licenseType'
                    ),
                    priority=dict(
                        type='choice',
                        disposition='/priority'
                    ),
                    eviction_policy=dict(
                        type='choice',
                        disposition='/evictionPolicy'
                    ),
                    billing_profile=dict(
                        type='dict',
                        disposition='/billingProfile',
                        options=dict(
                            max_price=dict(
                                type='number',
                                disposition='/maxPrice'
                            )
                        )
                    ),
                    scheduled_events_profile=dict(
                        type='dict',
                        disposition='/scheduledEventsProfile',
                        options=dict(
                            terminate_notification_profile=dict(
                                type='dict',
                                disposition='/terminateNotificationProfile',
                                options=dict(
                                    not_before_timeout=dict(
                                        type='str',
                                        disposition='/notBeforeTimeout'
                                    ),
                                    enable=dict(
                                        type='bool',
                                        disposition='/enable'
                                    )
                                )
                            )
                        )
                    )
                )
            ),
            overprovision=dict(
                type='bool',
                disposition='/properties/overprovision'
            ),
            do_not_run_extensions_on_overprovisioned_vms=dict(
                type='bool',
                disposition='/properties/doNotRunExtensionsOnOverprovisionedVMs'
            ),
            single_placement_group=dict(
                type='bool',
                disposition='/properties/singlePlacementGroup'
            ),
            zone_balance=dict(
                type='bool',
                disposition='/properties/zoneBalance'
            ),
            platform_fault_domain_count=dict(
                type='integer',
                disposition='/properties/platformFaultDomainCount'
            ),
            proximity_placement_group=dict(
                type='dict',
                disposition='/properties/proximityPlacementGroup',
                options=dict(
                    id=dict(
                        type='str',
                        disposition='/id'
                    )
                )
            ),
            host_group=dict(
                type='dict',
                disposition='/properties/hostGroup',
                options=dict(
                    id=dict(
                        type='str',
                        disposition='/id'
                    )
                )
            ),
            additional_capabilities=dict(
                type='dict',
                disposition='/properties/additionalCapabilities',
                options=dict(
                    ultra_ssd_enabled=dict(
                        type='bool',
                        disposition='/ultraSsdEnabled'
                    )
                )
            ),
            scale_in_policy=dict(
                type='dict',
                disposition='/properties/scaleInPolicy',
                options=dict(
                    rules=dict(
                        type='list',
                        disposition='/rules'
                    )
                )
            ),
            id=dict(
                type='str',
                disposition='/properties/id'
            ),
            ultra_ssd_enabled=dict(
                type='bool',
                disposition='/properties/ultraSsdEnabled'
            ),
            os_profile=dict(
                type='dict',
                disposition='/properties/osProfile',
                options=dict(
                    custom_data=dict(
                        type='str',
                        disposition='/customData'
                    ),
                    windows_configuration=dict(
                        type='dict',
                        disposition='/windowsConfiguration',
                        options=dict(
                            provision_vm_agent=dict(
                                type='bool',
                                disposition='/provisionVmAgent'
                            ),
                            enable_automatic_updates=dict(
                                type='bool',
                                disposition='/enableAutomaticUpdates'
                            ),
                            time_zone=dict(
                                type='str',
                                disposition='/timeZone'
                            ),
                            additional_unattend_content=dict(
                                type='list',
                                disposition='/additionalUnattendContent'
                            ),
                            patch_settings=dict(
                                type='dict',
                                disposition='/patchSettings',
                                options=dict(
                                    patch_mode=dict(
                                        type='choice',
                                        disposition='/patchMode'
                                    )
                                )
                            ),
                            win_rm=dict(
                                type='dict',
                                disposition='/winRm',
                                options=dict(
                                    listeners=dict(
                                        type='list',
                                        disposition='/listeners'
                                    )
                                )
                            )
                        )
                    ),
                    linux_configuration=dict(
                        type='dict',
                        disposition='/linuxConfiguration',
                        options=dict(
                            disable_password_authentication=dict(
                                type='bool',
                                disposition='/disablePasswordAuthentication'
                            ),
                            ssh=dict(
                                type='dict',
                                disposition='/ssh',
                                options=dict(
                                    public_keys=dict(
                                        type='list',
                                        disposition='/publicKeys'
                                    )
                                )
                            ),
                            provision_vm_agent=dict(
                                type='bool',
                                disposition='/provisionVmAgent'
                            )
                        )
                    ),
                    secrets=dict(
                        type='list',
                        disposition='/secrets'
                    )
                )
            ),
            storage_profile=dict(
                type='dict',
                disposition='/properties/storageProfile',
                options=dict(
                    image_reference=dict(
                        type='dict',
                        disposition='/imageReference',
                        options=dict(
                            publisher=dict(
                                type='str',
                                disposition='/publisher'
                            ),
                            offer=dict(
                                type='str',
                                disposition='/offer'
                            ),
                            sku=dict(
                                type='str',
                                disposition='/sku'
                            ),
                            version=dict(
                                type='str',
                                disposition='/version'
                            ),
                            exact_version=dict(
                                type='str',
                                disposition='/exactVersion'
                            )
                        )
                    ),
                    os_disk=dict(
                        type='dict',
                        disposition='/osDisk',
                        options=dict(
                            caching=dict(
                                type='sealed-choice',
                                disposition='/caching'
                            ),
                            write_accelerator_enabled=dict(
                                type='bool',
                                disposition='/writeAcceleratorEnabled'
                            ),
                            disk_size_gb=dict(
                                type='integer',
                                disposition='/diskSizeGB'
                            ),
                            image=dict(
                                type='dict',
                                disposition='/image',
                                options=dict(
                                    uri=dict(
                                        type='str',
                                        disposition='/uri'
                                    )
                                )
                            ),
                            vhd_containers=dict(
                                type='list',
                                disposition='/vhdContainers'
                            ),
                            managed_disk=dict(
                                type='dict',
                                disposition='/managedDisk',
                                options=dict(
                                    storage_account_type=dict(
                                        type='choice',
                                        disposition='/storageAccountType'
                                    ),
                                    disk_encryption_set=dict(
                                        type='dict',
                                        disposition='/diskEncryptionSet',
                                        options=dict(
                                            id=dict(
                                                type='str',
                                                disposition='/id'
                                            )
                                        )
                                    )
                                )
                            )
                        )
                    ),
                    data_disks=dict(
                        type='list',
                        disposition='/dataDisks'
                    )
                )
            ),
            network_profile=dict(
                type='dict',
                disposition='/properties/networkProfile',
                options=dict(
                    health_probe=dict(
                        type='dict',
                        disposition='/healthProbe',
                        options=dict(
                            id=dict(
                                type='str',
                                disposition='/id'
                            )
                        )
                    ),
                    network_interface_configurations=dict(
                        type='list',
                        disposition='/networkInterfaceConfigurations'
                    )
                )
            ),
            security_profile=dict(
                type='dict',
                disposition='/properties/securityProfile',
                options=dict(
                    encryption_at_host=dict(
                        type='bool',
                        disposition='/encryptionAtHost'
                    )
                )
            ),
            diagnostics_profile=dict(
                type='dict',
                disposition='/properties/diagnosticsProfile',
                options=dict(
                    boot_diagnostics=dict(
                        type='dict',
                        disposition='/bootDiagnostics',
                        options=dict(
                            enabled=dict(
                                type='bool',
                                disposition='/enabled'
                            ),
                            storage_uri=dict(
                                type='str',
                                disposition='/storageUri'
                            )
                        )
                    )
                )
            ),
            extension_profile=dict(
                type='dict',
                disposition='/properties/extensionProfile',
                options=dict(
                    extensions=dict(
                        type='list',
                        disposition='/extensions'
                    ),
                    extensions_time_budget=dict(
                        type='str',
                        disposition='/extensionsTimeBudget'
                    )
                )
            ),
            license_type=dict(
                type='str',
                disposition='/properties/licenseType'
            ),
            billing_profile=dict(
                type='dict',
                disposition='/properties/billingProfile',
                options=dict(
                    max_price=dict(
                        type='number',
                        disposition='/maxPrice'
                    )
                )
            ),
            scheduled_events_profile=dict(
                type='dict',
                disposition='/properties/scheduledEventsProfile',
                options=dict(
                    terminate_notification_profile=dict(
                        type='dict',
                        disposition='/terminateNotificationProfile',
                        options=dict(
                            not_before_timeout=dict(
                                type='str',
                                disposition='/notBeforeTimeout'
                            ),
                            enable=dict(
                                type='bool',
                                disposition='/enable'
                            )
                        )
                    )
                )
            ),
            mode=dict(
                type='sealed-choice',
                disposition='/properties/mode'
            ),
            rolling_upgrade_policy=dict(
                type='dict',
                disposition='/properties/rollingUpgradePolicy',
                options=dict(
                    max_batch_instance_percent=dict(
                        type='integer',
                        disposition='/maxBatchInstancePercent'
                    ),
                    max_unhealthy_instance_percent=dict(
                        type='integer',
                        disposition='/maxUnhealthyInstancePercent'
                    ),
                    max_unhealthy_upgraded_instance_percent=dict(
                        type='integer',
                        disposition='/maxUnhealthyUpgradedInstancePercent'
                    ),
                    pause_time_between_batches=dict(
                        type='str',
                        disposition='/pauseTimeBetweenBatches'
                    )
                )
            ),
            automatic_os_upgrade_policy=dict(
                type='dict',
                disposition='/properties/automaticOsUpgradePolicy',
                options=dict(
                    enable_automatic_os_upgrade=dict(
                        type='bool',
                        disposition='/enableAutomaticOsUpgrade'
                    ),
                    disable_automatic_rollback=dict(
                        type='bool',
                        disposition='/disableAutomaticRollback'
                    )
                )
            ),
            instance_ids=dict(
                type='list',
                disposition='/properties/instanceIds'
            ),
            skip_shutdown=dict(
                type='bool'
            ),
            temp_disk=dict(
                type='bool',
                disposition='/properties/tempDisk'
            ),
            platform_update_domain=dict(
                type='integer'
            ),
            active_placement_group_id=dict(
                type='str',
                disposition='/properties/activePlacementGroupId'
            ),
            service_name=dict(
                type='choice',
                disposition='/properties/serviceName'
            ),
            action=dict(
                type='choice',
                disposition='/properties/action'
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

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200, 201, 202]
        self.to_do = Actions.NoAction

        self.body = {}
        self.query_parameters = {}
        self.query_parameters['api-version'] = '2020-06-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

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

        self.mgmt_client = self.get_mgmt_svc_client(GenericRestClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        self.url= '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName}'
        self.url = self.url.replace('{subscriptionId}', self.subscription_id)
        self.url = self.url.replace('{resourceGroupName}', self.resource_group_name)
        self.url = self.url.replace('{vmScaleSetName}', self.vm_scale_set_name)

        old_response = self.get_resource()

        if not old_response:
            self.log("VirtualMachineScaleSet instance doesn't exist")

            if self.state == 'absent':
                self.log("Old instance didn't exist")
            else:
                self.to_do = Actions.Create
        else:
            self.log('VirtualMachineScaleSet instance already exists')

            if self.state == 'absent':
                self.to_do = Actions.Delete
            else:
                modifiers = {}
                self.create_compare_modifiers(self.module_arg_spec, '', modifiers)
                self.results['modifiers'] = modifiers
                self.results['compare'] = []
                self.create_compare_modifiers(self.module_arg_spec, '', modifiers)
                if not self.default_compare(modifiers, self.body, old_response, '', self.results):
                    self.to_do = Actions.Update

        if (self.to_do == Actions.Create) or (self.to_do == Actions.Update):
            self.log('Need to Create / Update the VirtualMachineScaleSet instance')

            if self.check_mode:
                self.results['changed'] = True
                return self.results

            response = self.create_update_resource()

            # if not old_response:
            self.results['changed'] = True
            # else:
            #     self.results['changed'] = old_response.__ne__(response)
            self.log('Creation / Update done')
        elif self.to_do == Actions.Delete:
            self.log('VirtualMachineScaleSet instance deleted')
            self.results['changed'] = True

            if self.check_mode:
                return self.results

            self.delete_resource()

            # make sure instance is actually deleted, for some Azure resources, instance is hanging around
            # for some time after deletion -- this should be really fixed in Azure
            while self.get_resource():
                time.sleep(20)
        else:
            self.log('VirtualMachineScaleSet instance unchanged')
            self.results['changed'] = False
            response = old_response

        return self.results

    def create_update_resource(self):

        try:
            response = self.mgmt_client.query(self.url,
                                              'PUT',
                                              self.query_parameters,
                                              self.header_parameters,
                                              self.body,
                                              self.status_code,
                                              600,
                                              30)
        except CloudError as exc:
            self.log('Error attempting to create the VirtualMachineScaleSet instance.')
            self.fail('Error creating the VirtualMachineScaleSet instance: {0}'.format(str(exc)))

        try:
            response = json.loads(response.text)
        except Exception:
            response = {'text': response.text}
            pass

        return response

    def delete_resource(self):
        try:
            response = self.mgmt_client.query(self.url,
                                              'DELETE',
                                              self.query_parameters,
                                              self.header_parameters,
                                              None,
                                              self.status_code,
                                              600,
                                              30)
        except CloudError as e:
            self.log('Error attempting to delete the VirtualMachineScaleSet instance.')
            self.fail('Error deleting the VirtualMachineScaleSet instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        found = False
        try:
            response = self.mgmt_client.query(self.url,
                                              'GET',
                                              self.query_parameters,
                                              self.header_parameters,
                                              None,
                                              self.status_code,
                                              600,
                                              30)
            found = True
            self.log("Response : {0}".format(response))
            # self.log("VirtualMachineScaleSet instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the VirtualMachineScaleSet instance.')
        if found is True:
            return response

        return False


def main():
    AzureRMVirtualMachineScaleSet()


if __name__ == '__main__':
    main()
