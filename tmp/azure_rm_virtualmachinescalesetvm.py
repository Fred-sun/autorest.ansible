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


class AzureRMVirtualMachineScaleSetVM(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=true
            ),
            vm_scale_set_name=dict(
                type='str'
            ),
            instance_id=dict(
                type='str'
            ),
            temp_disk=dict(
                type='bool',
                disposition='/properties/tempDisk'
            ),
            location=dict(
                type='str',
                disposition='/location'
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
            hardware_profile=dict(
                type='dict',
                disposition='/properties/hardwareProfile',
                options=dict(
                    vm_size=dict(
                        type='choice',
                        disposition='/vmSize'
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
                            os_type=dict(
                                type='sealed-choice',
                                disposition='/osType'
                            ),
                            encryption_settings=dict(
                                type='dict',
                                disposition='/encryptionSettings',
                                options=dict(
                                    disk_encryption_key=dict(
                                        type='dict',
                                        disposition='/diskEncryptionKey',
                                        options=dict(
                                            secret_url=dict(
                                                type='str',
                                                disposition='/secretUrl',
                                                required=true
                                            ),
                                            source_vault=dict(
                                                type='dict',
                                                disposition='/sourceVault',
                                                required=true,
                                                options=dict(
                                                    id=dict(
                                                        type='str',
                                                        disposition='/id'
                                                    )
                                                )
                                            )
                                        )
                                    ),
                                    key_encryption_key=dict(
                                        type='dict',
                                        disposition='/keyEncryptionKey',
                                        options=dict(
                                            key_url=dict(
                                                type='str',
                                                disposition='/keyUrl',
                                                required=true
                                            ),
                                            source_vault=dict(
                                                type='dict',
                                                disposition='/sourceVault',
                                                required=true,
                                                options=dict(
                                                    id=dict(
                                                        type='str',
                                                        disposition='/id'
                                                    )
                                                )
                                            )
                                        )
                                    ),
                                    enabled=dict(
                                        type='bool',
                                        disposition='/enabled'
                                    )
                                )
                            ),
                            name=dict(
                                type='str',
                                disposition='/name'
                            ),
                            vhd=dict(
                                type='dict',
                                disposition='/vhd',
                                options=dict(
                                    uri=dict(
                                        type='str',
                                        disposition='/uri'
                                    )
                                )
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
                            caching=dict(
                                type='sealed-choice',
                                disposition='/caching'
                            ),
                            write_accelerator_enabled=dict(
                                type='bool',
                                disposition='/writeAcceleratorEnabled'
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
                            create_option=dict(
                                type='choice',
                                disposition='/createOption',
                                required=true
                            ),
                            disk_size_gb=dict(
                                type='integer',
                                disposition='/diskSizeGB'
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
            os_profile=dict(
                type='dict',
                disposition='/properties/osProfile',
                options=dict(
                    computer_name=dict(
                        type='str',
                        disposition='/computerName'
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
                    ),
                    allow_extension_operations=dict(
                        type='bool',
                        disposition='/allowExtensionOperations'
                    ),
                    require_guest_provision_signal=dict(
                        type='bool',
                        disposition='/requireGuestProvisionSignal'
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
            network_profile=dict(
                type='dict',
                disposition='/properties/networkProfile',
                options=dict(
                    network_interfaces=dict(
                        type='list',
                        disposition='/networkInterfaces'
                    )
                )
            ),
            network_profile_configuration=dict(
                type='dict',
                disposition='/properties/networkProfileConfiguration',
                options=dict(
                    network_interface_configurations=dict(
                        type='list',
                        disposition='/networkInterfaceConfigurations'
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
            availability_set=dict(
                type='dict',
                disposition='/properties/availabilitySet',
                options=dict(
                    id=dict(
                        type='str',
                        disposition='/id'
                    )
                )
            ),
            license_type=dict(
                type='str',
                disposition='/properties/licenseType'
            ),
            protection_policy=dict(
                type='dict',
                disposition='/properties/protectionPolicy',
                options=dict(
                    protect_from_scale_in=dict(
                        type='bool',
                        disposition='/protectFromScaleIn'
                    ),
                    protect_from_scale_set_actions=dict(
                        type='bool',
                        disposition='/protectFromScaleSetActions'
                    )
                )
            ),
            expand=dict(
                type='constant'
            ),
            virtual_machine_scale_set_name=dict(
                type='str'
            ),
            filter=dict(
                type='str'
            ),
            select=dict(
                type='str'
            ),
            expand=dict(
                type='str'
            ),
            skip_shutdown=dict(
                type='bool'
            ),
            sas_uri_expiration_time_in_minutes=dict(
                type='integer'
            ),
            command_id=dict(
                type='str',
                disposition='/properties/commandId'
            ),
            script=dict(
                type='list',
                disposition='/properties/script'
            ),
            parameters=dict(
                type='list',
                disposition='/properties/parameters'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group_name = None
        self.vm_scale_set_name = None
        self.instance_id = None
        self.expand = None
        self.virtual_machine_scale_set_name = None
        self.filter = None
        self.select = None
        self.expand = None
        self.skip_shutdown = None
        self.sas_uri_expiration_time_in_minutes = None

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

        super(AzureRMVirtualMachineScaleSetVM, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.url= '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName}/virtualmachines/{instanceId}'
        self.url = self.url.replace('{subscriptionId}', self.subscription_id)
        self.url = self.url.replace('{resourceGroupName}', self.resource_group_name)
        self.url = self.url.replace('{vmScaleSetName}', self.vm_scale_set_name)
        self.url = self.url.replace('{instanceId}', self.instance_id)

        old_response = self.get_resource()

        if not old_response:
            self.log("VirtualMachineScaleSetVM instance doesn't exist")

            if self.state == 'absent':
                self.log("Old instance didn't exist")
            else:
                self.to_do = Actions.Create
        else:
            self.log('VirtualMachineScaleSetVM instance already exists')

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
            self.log('Need to Create / Update the VirtualMachineScaleSetVM instance')

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
            self.log('VirtualMachineScaleSetVM instance deleted')
            self.results['changed'] = True

            if self.check_mode:
                return self.results

            self.delete_resource()

            # make sure instance is actually deleted, for some Azure resources, instance is hanging around
            # for some time after deletion -- this should be really fixed in Azure
            while self.get_resource():
                time.sleep(20)
        else:
            self.log('VirtualMachineScaleSetVM instance unchanged')
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
            self.log('Error attempting to create the VirtualMachineScaleSetVM instance.')
            self.fail('Error creating the VirtualMachineScaleSetVM instance: {0}'.format(str(exc)))

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
            self.log('Error attempting to delete the VirtualMachineScaleSetVM instance.')
            self.fail('Error deleting the VirtualMachineScaleSetVM instance: {0}'.format(str(e)))

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
            # self.log("VirtualMachineScaleSetVM instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the VirtualMachineScaleSetVM instance.')
        if found is True:
            return response

        return False


def main():
    AzureRMVirtualMachineScaleSetVM()


if __name__ == '__main__':
    main()
