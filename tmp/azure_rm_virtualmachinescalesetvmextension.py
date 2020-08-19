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


class AzureRMVirtualMachineScaleSetVMExtension(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=true
            ),
            vm_scale_set_name=dict(
                type='str',
                required=true
            ),
            instance_id=dict(
                type='str',
                required=true
            ),
            vm_extension_name=dict(
                type='str'
            ),
            location=dict(
                type='str',
                disposition='/location'
            ),
            force_update_tag=dict(
                type='str',
                disposition='/properties/forceUpdateTag'
            ),
            publisher=dict(
                type='str',
                disposition='/properties/publisher'
            ),
            type=dict(
                type='str',
                disposition='/properties/type'
            ),
            type_handler_version=dict(
                type='str',
                disposition='/properties/typeHandlerVersion'
            ),
            auto_upgrade_minor_version=dict(
                type='bool',
                disposition='/properties/autoUpgradeMinorVersion'
            ),
            enable_automatic_upgrade=dict(
                type='bool',
                disposition='/properties/enableAutomaticUpgrade'
            ),
            settings=dict(
                type='any',
                disposition='/properties/settings'
            ),
            protected_settings=dict(
                type='any',
                disposition='/properties/protectedSettings'
            ),
            name=dict(
                type='str',
                disposition='/properties/name'
            ),
            virtual_machine_extension_instance_view_type=dict(
                type='str',
                disposition='/properties/virtualMachineExtensionInstanceViewType'
            ),
            virtual_machine_extension_instance_view_type_handler_version_type_handler_version=dict(
                type='str',
                disposition='/properties/virtualMachineExtensionInstanceViewTypeHandlerVersionTypeHandlerVersion'
            ),
            substatuses=dict(
                type='list',
                disposition='/properties/substatuses'
            ),
            statuses=dict(
                type='list',
                disposition='/properties/statuses'
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
        self.vm_scale_set_name = None
        self.instance_id = None
        self.vm_extension_name = None
        self.expand = None

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

        super(AzureRMVirtualMachineScaleSetVMExtension, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.url= '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName}/virtualMachines/{instanceId}/extensions/{vmExtensionName}'
        self.url = self.url.replace('{subscriptionId}', self.subscription_id)
        self.url = self.url.replace('{resourceGroupName}', self.resource_group_name)
        self.url = self.url.replace('{vmScaleSetName}', self.vm_scale_set_name)
        self.url = self.url.replace('{instanceId}', self.instance_id)
        self.url = self.url.replace('{vmExtensionName}', self.vm_extension_name)

        old_response = self.get_resource()

        if not old_response:
            self.log("VirtualMachineScaleSetVMExtension instance doesn't exist")

            if self.state == 'absent':
                self.log("Old instance didn't exist")
            else:
                self.to_do = Actions.Create
        else:
            self.log('VirtualMachineScaleSetVMExtension instance already exists')

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
            self.log('Need to Create / Update the VirtualMachineScaleSetVMExtension instance')

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
            self.log('VirtualMachineScaleSetVMExtension instance deleted')
            self.results['changed'] = True

            if self.check_mode:
                return self.results

            self.delete_resource()

            # make sure instance is actually deleted, for some Azure resources, instance is hanging around
            # for some time after deletion -- this should be really fixed in Azure
            while self.get_resource():
                time.sleep(20)
        else:
            self.log('VirtualMachineScaleSetVMExtension instance unchanged')
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
            self.log('Error attempting to create the VirtualMachineScaleSetVMExtension instance.')
            self.fail('Error creating the VirtualMachineScaleSetVMExtension instance: {0}'.format(str(exc)))

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
            self.log('Error attempting to delete the VirtualMachineScaleSetVMExtension instance.')
            self.fail('Error deleting the VirtualMachineScaleSetVMExtension instance: {0}'.format(str(e)))

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
            # self.log("VirtualMachineScaleSetVMExtension instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the VirtualMachineScaleSetVMExtension instance.')
        if found is True:
            return response

        return False


def main():
    AzureRMVirtualMachineScaleSetVMExtension()


if __name__ == '__main__':
    main()
