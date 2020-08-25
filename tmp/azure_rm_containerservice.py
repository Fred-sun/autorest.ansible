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


class AzureRMContainerService(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str'
            ),
            container_service_name=dict(
                type='str'
            ),
            location=dict(
                type='str',
                disposition='/location'
            ),
            orchestrator_profile=dict(
                type='dict',
                disposition='/orchestrator_profile',
                options=dict(
                    orchestrator_type=dict(
                        type='sealed-choice',
                        disposition='orchestrator_type',
                        required=True
                    )
                )
            ),
            custom_profile=dict(
                type='dict',
                disposition='/custom_profile',
                options=dict(
                    orchestrator=dict(
                        type='str',
                        disposition='orchestrator',
                        required=True
                    )
                )
            ),
            service_principal_profile=dict(
                type='dict',
                disposition='/service_principal_profile',
                options=dict(
                    client_id=dict(
                        type='str',
                        disposition='client_id',
                        required=True
                    ),
                    secret=dict(
                        type='str',
                        disposition='secret',
                        required=True
                    )
                )
            ),
            master_profile=dict(
                type='dict',
                disposition='/master_profile',
                options=dict(
                    count=dict(
                        type='choice',
                        disposition='count'
                    ),
                    dns_prefix=dict(
                        type='str',
                        disposition='dns_prefix',
                        required=True
                    ),
                    fqdn=dict(
                        type='str',
                        updatable=False,
                        disposition='fqdn'
                    )
                )
            ),
            agent_pool_profiles=dict(
                type='list',
                disposition='/agent_pool_profiles'
            ),
            windows_profile=dict(
                type='dict',
                disposition='/windows_profile',
                options=dict(
                    admin_username=dict(
                        type='str',
                        disposition='admin_username',
                        required=True
                    ),
                    admin_password=dict(
                        type='str',
                        disposition='admin_password',
                        required=True
                    )
                )
            ),
            linux_profile=dict(
                type='dict',
                disposition='/linux_profile',
                options=dict(
                    admin_username=dict(
                        type='str',
                        disposition='admin_username',
                        required=True
                    ),
                    ssh=dict(
                        type='dict',
                        disposition='ssh',
                        required=True,
                        options=dict(
                            public_keys=dict(
                                type='list',
                                disposition='public_keys',
                                required=True
                            )
                        )
                    )
                )
            ),
            diagnostics_profile=dict(
                type='dict',
                disposition='/diagnostics_profile',
                options=dict(
                    vm_diagnostics=dict(
                        type='dict',
                        disposition='vm_diagnostics',
                        required=True,
                        options=dict(
                            enabled=dict(
                                type='bool',
                                disposition='enabled',
                                required=True
                            ),
                            storage_uri=dict(
                                type='str',
                                updatable=False,
                                disposition='storage_uri'
                            )
                        )
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
        self.container_service_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMContainerService, self).__init__(derived_arg_spec=self.module_arg_spec,
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
            response = self.mgmt_client.container_services.create_or_update(resource_group_name=self.resource_group_name,
                                                                            container_service_name=self.container_service_name,
                                                                            parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the ContainerService instance.')
            self.fail('Error creating the ContainerService instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.container_services.delete(resource_group_name=self.resource_group_name,
                                                                  container_service_name=self.container_service_name)
        except CloudError as e:
            self.log('Error attempting to delete the ContainerService instance.')
            self.fail('Error deleting the ContainerService instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        found = False
        try:
            response = self.mgmt_client.container_services.get(resource_group_name=self.resource_group_name,
                                                               container_service_name=self.container_service_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMContainerService()


if __name__ == '__main__':
    main()
