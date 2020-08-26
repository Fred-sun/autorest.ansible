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
module: azure_rm_virtualmachinescaleset
version_added: '2.9'
short_description: Manage Azure VirtualMachineScaleSet instance.
description:
  - 'Create, update and delete instance of Azure VirtualMachineScaleSet.'
options:
  resource_group_name:
    description:
      - The name of the resource group.
    type: str
  vm_scale_set_name:
    description:
      - The name of the VM scale set to create or update.
    type: str
  location:
    description:
      - Resource location
    type: str
  sku:
    description:
      - The virtual machine scale set sku.
    type: dict
    suboptions:
      name:
        description:
          - The sku name.
        type: str
      tier:
        description:
          - >-
            Specifies the tier of virtual machines in a scale set.:code:`<br
            />`:code:`<br />` Possible Values::code:`<br />`:code:`<br />`
            **Standard**\ :code:`<br />`:code:`<br />` **Basic**
        type: str
      capacity:
        description:
          - Specifies the number of virtual machines in the scale set.
        type: integer
  plan:
    description:
      - >-
        Specifies information about the marketplace image used to create the
        virtual machine. This element is only used for marketplace images.
        Before you can use a marketplace image from an API, you must enable the
        image for programmatic use.  In the Azure portal, find the marketplace
        image that you want to use and then click **Want to deploy
        programmatically, Get Started ->**. Enter any required information and
        then click **Save**.
    type: dict
    suboptions:
      name:
        description:
          - The plan ID.
        type: str
      publisher:
        description:
          - The publisher ID.
        type: str
      product:
        description:
          - >-
            Specifies the product of the image from the marketplace. This is the
            same value as Offer under the imageReference element.
        type: str
      promotion_code:
        description:
          - The promotion code.
        type: str
  zones:
    description:
      - >-
        The virtual machine scale set zones. NOTE: Availability zones can only
        be set when you create the scale set
    type: list
  type:
    description:
      - >-
        The type of identity used for the virtual machine scale set. The type
        'SystemAssigned, UserAssigned' includes both an implicitly created
        identity and a set of user assigned identities. The type 'None' will
        remove any identities from the virtual machine scale set.
    type: sealed-choice
  user_assigned_identities:
    description:
      - >-
        The list of user identities associated with the virtual machine scale
        set. The user identity dictionary key references will be ARM resource
        ids in the form:
        '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{identityName}'.
    type: dictionary
  upgrade_policy:
    description:
      - The upgrade policy.
    type: dict
    suboptions:
      mode:
        description:
          - >-
            Specifies the mode of an upgrade to virtual machines in the scale
            set.:code:`<br />`:code:`<br />` Possible values are::code:`<br
            />`:code:`<br />` **Manual** - You  control the application of
            updates to virtual machines in the scale set. You do this by using
            the manualUpgrade action.:code:`<br />`:code:`<br />` **Automatic**
            - All virtual machines in the scale set are  automatically updated
            at the same time.
        type: sealed-choice
      rolling_upgrade_policy:
        description:
          - >-
            The configuration parameters used while performing a rolling
            upgrade.
        type: dict
        suboptions:
          max_batch_instance_percent:
            description:
              - >-
                The maximum percent of total virtual machine instances that will
                be upgraded simultaneously by the rolling upgrade in one batch.
                As this is a maximum, unhealthy instances in previous or future
                batches can cause the percentage of instances in a batch to
                decrease to ensure higher reliability. The default value for
                this parameter is 20%.
            type: integer
          max_unhealthy_instance_percent:
            description:
              - >-
                The maximum percentage of the total virtual machine instances in
                the scale set that can be simultaneously unhealthy, either as a
                result of being upgraded, or by being found in an unhealthy
                state by the virtual machine health checks before the rolling
                upgrade aborts. This constraint will be checked prior to
                starting any batch. The default value for this parameter is 20%.
            type: integer
          max_unhealthy_upgraded_instance_percent:
            description:
              - >-
                The maximum percentage of upgraded virtual machine instances
                that can be found to be in an unhealthy state. This check will
                happen after each batch is upgraded. If this percentage is ever
                exceeded, the rolling update aborts. The default value for this
                parameter is 20%.
            type: integer
          pause_time_between_batches:
            description:
              - >-
                The wait time between completing the update for all virtual
                machines in one batch and starting the next batch. The time
                duration should be specified in ISO 8601 format. The default
                value is 0 seconds (PT0S).
            type: str
      automatic_os_upgrade_policy:
        description:
          - Configuration parameters used for performing automatic OS Upgrade.
        type: dict
        suboptions:
          enable_automatic_os_upgrade:
            description:
              - >-
                Indicates whether OS upgrades should automatically be applied to
                scale set instances in a rolling fashion when a newer version of
                the OS image becomes available. Default value is false.
                :code:`<br>`:code:`<br>` If this is set to true for Windows
                based scale sets, `enableAutomaticUpdates
                <https://docs.microsoft.com/dotnet/api/microsoft.azure.management.compute.models.windowsconfiguration.enableautomaticupdates?view=azure-dotnet>`_
                is automatically set to false and cannot be set to true.
            type: bool
          disable_automatic_rollback:
            description:
              - >-
                Whether OS image rollback feature should be disabled. Default
                value is false.
            type: bool
  automatic_repairs_policy:
    description:
      - Policy for automatic repairs.
    type: dict
    suboptions:
      enabled:
        description:
          - >-
            Specifies whether automatic repairs should be enabled on the virtual
            machine scale set. The default value is false.
        type: bool
      grace_period:
        description:
          - >-
            The amount of time for which automatic repairs are suspended due to
            a state change on VM. The grace time starts after the state change
            has completed. This helps avoid premature or accidental repairs. The
            time duration should be specified in ISO 8601 format. The minimum
            allowed grace period is 30 minutes (PT30M), which is also the
            default value. The maximum allowed grace period is 90 minutes
            (PT90M).
        type: str
  virtual_machine_profile:
    description:
      - The virtual machine profile.
    type: dict
    suboptions:
      os_profile:
        description:
          - >-
            Specifies the operating system settings for the virtual machines in
            the scale set.
        type: dict
        suboptions:
          computer_name_prefix:
            description:
              - >-
                Specifies the computer name prefix for all of the virtual
                machines in the scale set. Computer name prefixes must be 1 to
                15 characters long.
            type: str
          admin_username:
            description:
              - >-
                Specifies the name of the administrator account.
                :code:`<br>`:code:`<br>` **Windows-only restriction:** Cannot
                end in "." :code:`<br>`:code:`<br>` **Disallowed values:**
                "administrator", "admin", "user", "user1", "test", "user2",
                "test1", "user3", "admin1", "1", "123", "a", "actuser", "adm",
                "admin2", "aspnet", "backup", "console", "david", "guest",
                "john", "owner", "root", "server", "sql", "support",
                "support_388945a0", "sys", "test2", "test3", "user4", "user5".
                :code:`<br>`:code:`<br>` **Minimum-length (Linux):** 1 
                character :code:`<br>`:code:`<br>` **Max-length (Linux):** 64
                characters :code:`<br>`:code:`<br>` **Max-length (Windows):** 20
                characters  :code:`<br>`:code:`<br>`:code:`<li>` For root access
                to the Linux VM, see `Using root privileges on Linux virtual
                machines in Azure
                <https://docs.microsoft.com/azure/virtual-machines/virtual-machines-linux-use-root-privileges?toc=%2fazure%2fvirtual-machines%2flinux%2ftoc.json>`_\
                :code:`<br>`:code:`<li>` For a list of built-in system users on
                Linux that should not be used in this field, see `Selecting User
                Names for Linux on Azure
                <https://docs.microsoft.com/azure/virtual-machines/virtual-machines-linux-usernames?toc=%2fazure%2fvirtual-machines%2flinux%2ftoc.json>`_
            type: str
          admin_password:
            description:
              - >-
                Specifies the password of the administrator account.
                :code:`<br>`:code:`<br>` **Minimum-length (Windows):** 8
                characters :code:`<br>`:code:`<br>` **Minimum-length (Linux):**
                6 characters :code:`<br>`:code:`<br>` **Max-length (Windows):**
                123 characters :code:`<br>`:code:`<br>` **Max-length (Linux):**
                72 characters :code:`<br>`:code:`<br>` **Complexity
                requirements:** 3 out of 4 conditions below need to be fulfilled
                :code:`<br>` Has lower characters :code:`<br>`Has upper
                characters :code:`<br>` Has a digit :code:`<br>` Has a special
                character (Regex match [\W_]) :code:`<br>`:code:`<br>`
                **Disallowed values:** "abc@123", "P@$$w0rd", "P@ssw0rd",
                "P@ssword123", "Pa$$word", "pass@word1", "Password!",
                "Password1", "Password22", "iloveyou!" :code:`<br>`:code:`<br>`
                For resetting the password, see `How to reset the Remote Desktop
                service or its login password in a Windows VM
                <https://docs.microsoft.com/azure/virtual-machines/virtual-machines-windows-reset-rdp?toc=%2fazure%2fvirtual-machines%2fwindows%2ftoc.json>`_
                :code:`<br>`:code:`<br>` For resetting root password, see
                `Manage users, SSH, and check or repair disks on Azure Linux VMs
                using the VMAccess Extension
                <https://docs.microsoft.com/azure/virtual-machines/virtual-machines-linux-using-vmaccess-extension?toc=%2fazure%2fvirtual-machines%2flinux%2ftoc.json#reset-root-password>`_
            type: str
          custom_data:
            description:
              - >-
                Specifies a base-64 encoded string of custom data. The base-64
                encoded string is decoded to a binary array that is saved as a
                file on the Virtual Machine. The maximum length of the binary
                array is 65535 bytes. :code:`<br>`:code:`<br>` For using
                cloud-init for your VM, see `Using cloud-init to customize a
                Linux VM during creation
                <https://docs.microsoft.com/azure/virtual-machines/virtual-machines-linux-using-cloud-init?toc=%2fazure%2fvirtual-machines%2flinux%2ftoc.json>`_
            type: str
          windows_configuration:
            description:
              - >-
                Specifies Windows operating system settings on the virtual
                machine.
            type: dict
            suboptions:
              provision_vm_agent:
                description:
                  - >-
                    Indicates whether virtual machine agent should be
                    provisioned on the virtual machine. :code:`<br>`:code:`<br>`
                    When this property is not specified in the request body,
                    default behavior is to set it to true.  This will ensure
                    that VM Agent is installed on the VM so that extensions can
                    be added to the VM later.
                type: bool
              enable_automatic_updates:
                description:
                  - >-
                    Indicates whether Automatic Updates is enabled for the
                    Windows virtual machine. Default value is true.
                    :code:`<br>`:code:`<br>` For virtual machine scale sets,
                    this property can be updated and updates will take effect on
                    OS reprovisioning.
                type: bool
              time_zone:
                description:
                  - >-
                    Specifies the time zone of the virtual machine. e.g.
                    "Pacific Standard Time". :code:`<br>`:code:`<br>` Possible
                    values can be `TimeZoneInfo.Id
                    <https://docs.microsoft.com/en-us/dotnet/api/system.timezoneinfo.id?#System_TimeZoneInfo_Id>`_
                    value from time zones returned by
                    `TimeZoneInfo.GetSystemTimeZones
                    <https://docs.microsoft.com/en-us/dotnet/api/system.timezoneinfo.getsystemtimezones>`_.
                type: str
              additional_unattend_content:
                description:
                  - >-
                    Specifies additional base-64 encoded XML formatted
                    information that can be included in the Unattend.xml file,
                    which is used by Windows Setup.
                type: list
              patch_settings:
                description:
                  - Specifies settings related to in-guest patching (KBs).
                type: dict
                suboptions:
                  patch_mode:
                    description:
                      - >-
                        Specifies the mode of in-guest patching to IaaS virtual
                        machine.:code:`<br />`:code:`<br />` Possible values
                        are::code:`<br />`:code:`<br />` **Manual** - You 
                        control the application of patches to a virtual machine.
                        You do this by applying patches manually inside the VM.
                        In this mode, automatic updates are disabled; the
                        property WindowsConfiguration.enableAutomaticUpdates
                        must be false:code:`<br />`:code:`<br />`
                        **AutomaticByOS** - The virtual machine will
                        automatically be updated by the OS. The property
                        WindowsConfiguration.enableAutomaticUpdates must be
                        true. :code:`<br />`:code:`<br />` **
                        AutomaticByPlatform** - the virtual machine will
                        automatically updated by the platform. The properties
                        provisionVMAgent and
                        WindowsConfiguration.enableAutomaticUpdates must be true
                    type: choice
              win_rm:
                description:
                  - >-
                    Specifies the Windows Remote Management listeners. This
                    enables remote Windows PowerShell.
                type: dict
                suboptions:
                  listeners:
                    description:
                      - The list of Windows Remote Management listeners
                    type: list
          linux_configuration:
            description:
              - >-
                Specifies the Linux operating system settings on the virtual
                machine. :code:`<br>`:code:`<br>`For a list of supported Linux
                distributions, see `Linux on Azure-Endorsed Distributions
                <https://docs.microsoft.com/azure/virtual-machines/virtual-machines-linux-endorsed-distros?toc=%2fazure%2fvirtual-machines%2flinux%2ftoc.json>`_
                :code:`<br>`:code:`<br>` For running non-endorsed distributions,
                see `Information for Non-Endorsed Distributions
                <https://docs.microsoft.com/azure/virtual-machines/virtual-machines-linux-create-upload-generic?toc=%2fazure%2fvirtual-machines%2flinux%2ftoc.json>`_.
            type: dict
            suboptions:
              disable_password_authentication:
                description:
                  - >-
                    Specifies whether password authentication should be
                    disabled.
                type: bool
              ssh:
                description:
                  - Specifies the ssh key configuration for a Linux OS.
                type: dict
                suboptions:
                  public_keys:
                    description:
                      - >-
                        The list of SSH public keys used to authenticate with
                        linux based VMs.
                    type: list
              provision_vm_agent:
                description:
                  - >-
                    Indicates whether virtual machine agent should be
                    provisioned on the virtual machine. :code:`<br>`:code:`<br>`
                    When this property is not specified in the request body,
                    default behavior is to set it to true.  This will ensure
                    that VM Agent is installed on the VM so that extensions can
                    be added to the VM later.
                type: bool
          secrets:
            description:
              - >-
                Specifies set of certificates that should be installed onto the
                virtual machines in the scale set.
            type: list
      storage_profile:
        description:
          - Specifies the storage settings for the virtual machine disks.
        type: dict
        suboptions:
          image_reference:
            description:
              - >-
                Specifies information about the image to use. You can specify
                information about platform images, marketplace images, or
                virtual machine images. This element is required when you want
                to use a platform image, marketplace image, or virtual machine
                image, but is not used in other creation operations.
            type: dict
            suboptions:
              publisher:
                description:
                  - The image publisher.
                type: str
              offer:
                description:
                  - >-
                    Specifies the offer of the platform image or marketplace
                    image used to create the virtual machine.
                type: str
              sku:
                description:
                  - The image SKU.
                type: str
              version:
                description:
                  - >-
                    Specifies the version of the platform image or marketplace
                    image used to create the virtual machine. The allowed
                    formats are Major.Minor.Build or 'latest'. Major, Minor, and
                    Build are decimal numbers. Specify 'latest' to use the
                    latest version of an image available at deploy time. Even if
                    you use 'latest', the VM image will not automatically update
                    after deploy time even if a new version becomes available.
                type: str
              exact_version:
                description:
                  - >-
                    Specifies in decimal numbers, the version of platform image
                    or marketplace image used to create the virtual machine.
                    This readonly field differs from 'version', only if the
                    value specified in 'version' field is 'latest'.
                type: str
          os_disk:
            description:
              - >-
                Specifies information about the operating system disk used by
                the virtual machines in the scale set. :code:`<br>`:code:`<br>`
                For more information about disks, see `About disks and VHDs for
                Azure virtual machines
                <https://docs.microsoft.com/azure/virtual-machines/virtual-machines-windows-about-disks-vhds?toc=%2fazure%2fvirtual-machines%2fwindows%2ftoc.json>`_.
            type: dict
            suboptions:
              name:
                description:
                  - The disk name.
                type: str
              caching:
                description:
                  - >-
                    Specifies the caching requirements. :code:`<br>`:code:`<br>`
                    Possible values are: :code:`<br>`:code:`<br>` **None**
                    :code:`<br>`:code:`<br>` **ReadOnly**
                    :code:`<br>`:code:`<br>` **ReadWrite**
                    :code:`<br>`:code:`<br>` Default: **None for Standard
                    storage. ReadOnly for Premium storage**
                type: sealed-choice
              write_accelerator_enabled:
                description:
                  - >-
                    Specifies whether writeAccelerator should be enabled or
                    disabled on the disk.
                type: bool
              create_option:
                description:
                  - >-
                    Specifies how the virtual machines in the scale set should
                    be created.:code:`<br>`:code:`<br>` The only allowed value
                    is: **FromImage** \u2013 This value is used when you are
                    using an image to create the virtual machine. If you are
                    using a platform image, you also use the imageReference
                    element described above. If you are using a marketplace
                    image, you  also use the plan element previously described.
                required: true
                type: choice
              diff_disk_settings:
                description:
                  - >-
                    Specifies the ephemeral disk Settings for the operating
                    system disk used by the virtual machine scale set.
                type: dict
                suboptions:
                  option:
                    description:
                      - >-
                        Specifies the ephemeral disk settings for operating
                        system disk.
                    type: choice
                  placement:
                    description:
                      - >-
                        Specifies the ephemeral disk placement for operating
                        system disk.:code:`<br>`:code:`<br>` Possible values
                        are: :code:`<br>`:code:`<br>` **CacheDisk**
                        :code:`<br>`:code:`<br>` **ResourceDisk**
                        :code:`<br>`:code:`<br>` Default: **CacheDisk** if one
                        is configured for the VM size otherwise **ResourceDisk**
                        is used.:code:`<br>`:code:`<br>` Refer to VM size
                        documentation for Windows VM at
                        https://docs.microsoft.com/en-us/azure/virtual-machines/windows/sizes
                        and Linux VM at
                        https://docs.microsoft.com/en-us/azure/virtual-machines/linux/sizes
                        to check which VM sizes exposes a cache disk.
                    type: choice
              disk_size_gb:
                description:
                  - >-
                    Specifies the size of the operating system disk in
                    gigabytes. This element can be used to overwrite the size of
                    the disk in a virtual machine image.
                    :code:`<br>`:code:`<br>` This value cannot be larger than
                    1023 GB
                type: integer
              os_type:
                description:
                  - >-
                    This property allows you to specify the type of the OS that
                    is included in the disk if creating a VM from user-image or
                    a specialized VHD. :code:`<br>`:code:`<br>` Possible values
                    are: :code:`<br>`:code:`<br>` **Windows**
                    :code:`<br>`:code:`<br>` **Linux**
                type: sealed-choice
              image:
                description:
                  - >-
                    Specifies information about the unmanaged user image to base
                    the scale set on.
                type: dict
                suboptions:
                  uri:
                    description:
                      - Specifies the virtual hard disk's uri.
                    type: str
              vhd_containers:
                description:
                  - >-
                    Specifies the container urls that are used to store
                    operating system disks for the scale set.
                type: list
              managed_disk:
                description:
                  - The managed disk parameters.
                type: dict
                suboptions:
                  storage_account_type:
                    description:
                      - >-
                        Specifies the storage account type for the managed disk.
                        NOTE: UltraSSD_LRS can only be used with data disks, it
                        cannot be used with OS Disk.
                    type: choice
                  disk_encryption_set:
                    description:
                      - >-
                        Specifies the customer managed disk encryption set
                        resource id for the managed disk.
                    type: dict
                    suboptions:
                      id:
                        description:
                          - Resource Id
                        type: str
          data_disks:
            description:
              - >-
                Specifies the parameters that are used to add data disks to the
                virtual machines in the scale set. :code:`<br>`:code:`<br>` For
                more information about disks, see `About disks and VHDs for
                Azure virtual machines
                <https://docs.microsoft.com/azure/virtual-machines/virtual-machines-windows-about-disks-vhds?toc=%2fazure%2fvirtual-machines%2fwindows%2ftoc.json>`_.
            type: list
      network_profile:
        description:
          - >-
            Specifies properties of the network interfaces of the virtual
            machines in the scale set.
        type: dict
        suboptions:
          health_probe:
            description:
              - >-
                A reference to a load balancer probe used to determine the
                health of an instance in the virtual machine scale set. The
                reference will be in the form:
                '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/loadBalancers/{loadBalancerName}/probes/{probeName}'.
            type: dict
            suboptions:
              id:
                description:
                  - >-
                    The ARM resource id in the form of
                    /subscriptions/{SubscriptionId}/resourceGroups/{ResourceGroupName}/...
                type: str
          network_interface_configurations:
            description:
              - The list of network configurations.
            type: list
      security_profile:
        description:
          - >-
            Specifies the Security related profile settings for the virtual
            machines in the scale set.
        type: dict
        suboptions:
          encryption_at_host:
            description:
              - >-
                This property can be used by user in the request to enable or
                disable the Host Encryption for the virtual machine or virtual
                machine scale set. This will enable the encryption for all the
                disks including Resource/Temp disk at host itself.
                :code:`<br>`:code:`<br>` Default: The Encryption at host will be
                disabled unless this property is set to true for the resource.
            type: bool
      diagnostics_profile:
        description:
          - >-
            Specifies the boot diagnostic settings state.
            :code:`<br>`:code:`<br>`Minimum api-version: 2015-06-15.
        type: dict
        suboptions:
          boot_diagnostics:
            description:
              - >-
                Boot Diagnostics is a debugging feature which allows you to view
                Console Output and Screenshot to diagnose VM status.
                :code:`<br>`:code:`<br>` You can easily view the output of your
                console log. :code:`<br>`:code:`<br>` Azure also enables you to
                see a screenshot of the VM from the hypervisor.
            type: dict
            suboptions:
              enabled:
                description:
                  - >-
                    Whether boot diagnostics should be enabled on the Virtual
                    Machine.
                type: bool
              storage_uri:
                description:
                  - >-
                    Uri of the storage account to use for placing the console
                    output and screenshot. :code:`<br>`:code:`<br>`If storageUri
                    is not specified while enabling boot diagnostics, managed
                    storage will be used.
                type: str
      extension_profile:
        description:
          - >-
            Specifies a collection of settings for extensions installed on
            virtual machines in the scale set.
        type: dict
        suboptions:
          extensions:
            description:
              - The virtual machine scale set child extension resources.
            type: list
          extensions_time_budget:
            description:
              - >-
                Specifies the time alloted for all extensions to start. The time
                duration should be between 15 minutes and 120 minutes
                (inclusive) and should be specified in ISO 8601 format. The
                default value is 90 minutes (PT1H30M). :code:`<br>`:code:`<br>`
                Minimum api-version: 2020-06-01
            type: str
      license_type:
        description:
          - >-
            Specifies that the image or disk that is being used was licensed
            on-premises. This element is only used for images that contain the
            Windows Server operating system. :code:`<br>`:code:`<br>` Possible
            values are: :code:`<br>`:code:`<br>` Windows_Client
            :code:`<br>`:code:`<br>` Windows_Server :code:`<br>`:code:`<br>` If
            this element is included in a request for an update, the value must
            match the initial value. This value cannot be updated.
            :code:`<br>`:code:`<br>` For more information, see `Azure Hybrid Use
            Benefit for Windows Server
            <https://docs.microsoft.com/azure/virtual-machines/virtual-machines-windows-hybrid-use-benefit-licensing?toc=%2fazure%2fvirtual-machines%2fwindows%2ftoc.json>`_
            :code:`<br>`:code:`<br>` Minimum api-version: 2015-06-15
        type: str
      priority:
        description:
          - >-
            Specifies the priority for the virtual machines in the scale set.
            :code:`<br>`:code:`<br>`Minimum api-version: 2017-10-30-preview
        type: choice
      eviction_policy:
        description:
          - >-
            Specifies the eviction policy for the Azure Spot virtual machine and
            Azure Spot scale set. :code:`<br>`:code:`<br>`For Azure Spot virtual
            machines, both 'Deallocate' and 'Delete' are supported and the
            minimum api-version is 2019-03-01. :code:`<br>`:code:`<br>`For Azure
            Spot scale sets, both 'Deallocate' and 'Delete' are supported and
            the minimum api-version is 2017-10-30-preview.
        type: choice
      billing_profile:
        description:
          - >-
            Specifies the billing related details of a Azure Spot VMSS.
            :code:`<br>`:code:`<br>`Minimum api-version: 2019-03-01.
        type: dict
        suboptions:
          max_price:
            description:
              - >-
                Specifies the maximum price you are willing to pay for a Azure
                Spot VM/VMSS. This price is in US Dollars.
                :code:`<br>`:code:`<br>` This price will be compared with the
                current Azure Spot price for the VM size. Also, the prices are
                compared at the time of create/update of Azure Spot VM/VMSS and
                the operation will only succeed if  the maxPrice is greater than
                the current Azure Spot price. :code:`<br>`:code:`<br>` The
                maxPrice will also be used for evicting a Azure Spot VM/VMSS if
                the current Azure Spot price goes beyond the maxPrice after
                creation of VM/VMSS. :code:`<br>`:code:`<br>` Possible values
                are: :code:`<br>`:code:`<br>` - Any decimal value greater than
                zero. Example: 0.01538 :code:`<br>`:code:`<br>` -1 – indicates
                default price to be up-to on-demand. :code:`<br>`:code:`<br>`
                You can set the maxPrice to -1 to indicate that the Azure Spot
                VM/VMSS should not be evicted for price reasons. Also, the
                default max price is -1 if it is not provided by you.
                :code:`<br>`:code:`<br>`Minimum api-version: 2019-03-01.
            type: number
      scheduled_events_profile:
        description:
          - Specifies Scheduled Event related configurations.
        type: dict
        suboptions:
          terminate_notification_profile:
            description:
              - Specifies Terminate Scheduled Event related configurations.
            type: dict
            suboptions:
              not_before_timeout:
                description:
                  - >-
                    Configurable length of time a Virtual Machine being deleted
                    will have to potentially approve the Terminate Scheduled
                    Event before the event is auto approved (timed out). The
                    configuration must be specified in ISO 8601 format, the
                    default value is 5 minutes (PT5M)
                type: str
              enable:
                description:
                  - >-
                    Specifies whether the Terminate Scheduled event is enabled
                    or disabled.
                type: bool
  overprovision:
    description:
      - >-
        Specifies whether the Virtual Machine Scale Set should be
        overprovisioned.
    type: bool
  do_not_run_extensions_on_overprovisioned_vms:
    description:
      - >-
        When Overprovision is enabled, extensions are launched only on the
        requested number of VMs which are finally kept. This property will hence
        ensure that the extensions do not run on the extra overprovisioned VMs.
    type: bool
  single_placement_group:
    description:
      - >-
        When true this limits the scale set to a single placement group, of max
        size 100 virtual machines. NOTE: If singlePlacementGroup is true, it may
        be modified to false. However, if singlePlacementGroup is false, it may
        not be modified to true.
    type: bool
  zone_balance:
    description:
      - >-
        Whether to force strictly even Virtual Machine distribution cross
        x-zones in case there is zone outage.
    type: bool
  platform_fault_domain_count:
    description:
      - Fault Domain count for each placement group.
    type: integer
  proximity_placement_group:
    description:
      - >-
        Specifies information about the proximity placement group that the
        virtual machine scale set should be assigned to.
        :code:`<br>`:code:`<br>`Minimum api-version: 2018-04-01.
    type: dict
    suboptions:
      id:
        description:
          - Resource Id
        type: str
  host_group:
    description:
      - >-
        Specifies information about the dedicated host group that the virtual
        machine scale set resides in. :code:`<br>`:code:`<br>`Minimum
        api-version: 2020-06-01.
    type: dict
    suboptions:
      id:
        description:
          - Resource Id
        type: str
  additional_capabilities:
    description:
      - >-
        Specifies additional capabilities enabled or disabled on the Virtual
        Machines in the Virtual Machine Scale Set. For instance: whether the
        Virtual Machines have the capability to support attaching managed data
        disks with UltraSSD_LRS storage account type.
    type: dict
    suboptions:
      ultra_ssd_enabled:
        description:
          - >-
            The flag that enables or disables a capability to have one or more
            managed data disks with UltraSSD_LRS storage account type on the VM
            or VMSS. Managed disks with storage account type UltraSSD_LRS can be
            added to a virtual machine or virtual machine scale set only if this
            property is enabled.
        type: bool
  scale_in_policy:
    description:
      - >-
        Specifies the scale-in policy that decides which virtual machines are
        chosen for removal when a Virtual Machine Scale Set is scaled-in.
    type: dict
    suboptions:
      rules:
        description:
          - >-
            The rules to be followed when scaling-in a virtual machine scale
            set. :code:`<br>`:code:`<br>` Possible values are:
            :code:`<br>`:code:`<br>` **Default** When a virtual machine scale
            set is scaled in, the scale set will first be balanced across zones
            if it is a zonal scale set. Then, it will be balanced across Fault
            Domains as far as possible. Within each Fault Domain, the virtual
            machines chosen for removal will be the newest ones that are not
            protected from scale-in. :code:`<br>`:code:`<br>` **OldestVM** When
            a virtual machine scale set is being scaled-in, the oldest virtual
            machines that are not protected from scale-in will be chosen for
            removal. For zonal virtual machine scale sets, the scale set will
            first be balanced across zones. Within each zone, the oldest virtual
            machines that are not protected will be chosen for removal.
            :code:`<br>`:code:`<br>` **NewestVM** When a virtual machine scale
            set is being scaled-in, the newest virtual machines that are not
            protected from scale-in will be chosen for removal. For zonal
            virtual machine scale sets, the scale set will first be balanced
            across zones. Within each zone, the newest virtual machines that are
            not protected will be chosen for removal. :code:`<br>`:code:`<br>`
        type: list
  id:
    description:
      - Resource Id
    type: str
  ultra_ssd_enabled:
    description:
      - >-
        The flag that enables or disables a capability to have one or more
        managed data disks with UltraSSD_LRS storage account type on the VM or
        VMSS. Managed disks with storage account type UltraSSD_LRS can be added
        to a virtual machine or virtual machine scale set only if this property
        is enabled.
    type: bool
  os_profile:
    description:
      - The virtual machine scale set OS profile.
    type: dict
    suboptions:
      custom_data:
        description:
          - A base-64 encoded string of custom data.
        type: str
      windows_configuration:
        description:
          - The Windows Configuration of the OS profile.
        type: dict
        suboptions:
          provision_vm_agent:
            description:
              - >-
                Indicates whether virtual machine agent should be provisioned on
                the virtual machine. :code:`<br>`:code:`<br>` When this property
                is not specified in the request body, default behavior is to set
                it to true.  This will ensure that VM Agent is installed on the
                VM so that extensions can be added to the VM later.
            type: bool
          enable_automatic_updates:
            description:
              - >-
                Indicates whether Automatic Updates is enabled for the Windows
                virtual machine. Default value is true. :code:`<br>`:code:`<br>`
                For virtual machine scale sets, this property can be updated and
                updates will take effect on OS reprovisioning.
            type: bool
          time_zone:
            description:
              - >-
                Specifies the time zone of the virtual machine. e.g. "Pacific
                Standard Time". :code:`<br>`:code:`<br>` Possible values can be
                `TimeZoneInfo.Id
                <https://docs.microsoft.com/en-us/dotnet/api/system.timezoneinfo.id?#System_TimeZoneInfo_Id>`_
                value from time zones returned by
                `TimeZoneInfo.GetSystemTimeZones
                <https://docs.microsoft.com/en-us/dotnet/api/system.timezoneinfo.getsystemtimezones>`_.
            type: str
          additional_unattend_content:
            description:
              - >-
                Specifies additional base-64 encoded XML formatted information
                that can be included in the Unattend.xml file, which is used by
                Windows Setup.
            type: list
          patch_settings:
            description:
              - Specifies settings related to in-guest patching (KBs).
            type: dict
            suboptions:
              patch_mode:
                description:
                  - >-
                    Specifies the mode of in-guest patching to IaaS virtual
                    machine.:code:`<br />`:code:`<br />` Possible values
                    are::code:`<br />`:code:`<br />` **Manual** - You  control
                    the application of patches to a virtual machine. You do this
                    by applying patches manually inside the VM. In this mode,
                    automatic updates are disabled; the property
                    WindowsConfiguration.enableAutomaticUpdates must be
                    false:code:`<br />`:code:`<br />` **AutomaticByOS** - The
                    virtual machine will automatically be updated by the OS. The
                    property WindowsConfiguration.enableAutomaticUpdates must be
                    true. :code:`<br />`:code:`<br />` ** AutomaticByPlatform**
                    - the virtual machine will automatically updated by the
                    platform. The properties provisionVMAgent and
                    WindowsConfiguration.enableAutomaticUpdates must be true
                type: choice
          win_rm:
            description:
              - >-
                Specifies the Windows Remote Management listeners. This enables
                remote Windows PowerShell.
            type: dict
            suboptions:
              listeners:
                description:
                  - The list of Windows Remote Management listeners
                type: list
      linux_configuration:
        description:
          - The Linux Configuration of the OS profile.
        type: dict
        suboptions:
          disable_password_authentication:
            description:
              - Specifies whether password authentication should be disabled.
            type: bool
          ssh:
            description:
              - Specifies the ssh key configuration for a Linux OS.
            type: dict
            suboptions:
              public_keys:
                description:
                  - >-
                    The list of SSH public keys used to authenticate with linux
                    based VMs.
                type: list
          provision_vm_agent:
            description:
              - >-
                Indicates whether virtual machine agent should be provisioned on
                the virtual machine. :code:`<br>`:code:`<br>` When this property
                is not specified in the request body, default behavior is to set
                it to true.  This will ensure that VM Agent is installed on the
                VM so that extensions can be added to the VM later.
            type: bool
      secrets:
        description:
          - The List of certificates for addition to the VM.
        type: list
  storage_profile:
    description:
      - The virtual machine scale set storage profile.
    type: dict
    suboptions:
      image_reference:
        description:
          - The image reference.
        type: dict
        suboptions:
          publisher:
            description:
              - The image publisher.
            type: str
          offer:
            description:
              - >-
                Specifies the offer of the platform image or marketplace image
                used to create the virtual machine.
            type: str
          sku:
            description:
              - The image SKU.
            type: str
          version:
            description:
              - >-
                Specifies the version of the platform image or marketplace image
                used to create the virtual machine. The allowed formats are
                Major.Minor.Build or 'latest'. Major, Minor, and Build are
                decimal numbers. Specify 'latest' to use the latest version of
                an image available at deploy time. Even if you use 'latest', the
                VM image will not automatically update after deploy time even if
                a new version becomes available.
            type: str
          exact_version:
            description:
              - >-
                Specifies in decimal numbers, the version of platform image or
                marketplace image used to create the virtual machine. This
                readonly field differs from 'version', only if the value
                specified in 'version' field is 'latest'.
            type: str
      os_disk:
        description:
          - The OS disk.
        type: dict
        suboptions:
          caching:
            description:
              - The caching type.
            type: sealed-choice
          write_accelerator_enabled:
            description:
              - >-
                Specifies whether writeAccelerator should be enabled or disabled
                on the disk.
            type: bool
          disk_size_gb:
            description:
              - >-
                Specifies the size of the operating system disk in gigabytes.
                This element can be used to overwrite the size of the disk in a
                virtual machine image. :code:`<br>`:code:`<br>` This value
                cannot be larger than 1023 GB
            type: integer
          image:
            description:
              - >-
                The Source User Image VirtualHardDisk. This VirtualHardDisk will
                be copied before using it to attach to the Virtual Machine. If
                SourceImage is provided, the destination VirtualHardDisk should
                not exist.
            type: dict
            suboptions:
              uri:
                description:
                  - Specifies the virtual hard disk's uri.
                type: str
          vhd_containers:
            description:
              - The list of virtual hard disk container uris.
            type: list
          managed_disk:
            description:
              - The managed disk parameters.
            type: dict
            suboptions:
              storage_account_type:
                description:
                  - >-
                    Specifies the storage account type for the managed disk.
                    NOTE: UltraSSD_LRS can only be used with data disks, it
                    cannot be used with OS Disk.
                type: choice
              disk_encryption_set:
                description:
                  - >-
                    Specifies the customer managed disk encryption set resource
                    id for the managed disk.
                type: dict
                suboptions:
                  id:
                    description:
                      - Resource Id
                    type: str
      data_disks:
        description:
          - The data disks.
        type: list
  network_profile:
    description:
      - The virtual machine scale set network profile.
    type: dict
    suboptions:
      health_probe:
        description:
          - >-
            A reference to a load balancer probe used to determine the health of
            an instance in the virtual machine scale set. The reference will be
            in the form:
            '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/loadBalancers/{loadBalancerName}/probes/{probeName}'.
        type: dict
        suboptions:
          id:
            description:
              - >-
                The ARM resource id in the form of
                /subscriptions/{SubscriptionId}/resourceGroups/{ResourceGroupName}/...
            type: str
      network_interface_configurations:
        description:
          - The list of network configurations.
        type: list
  security_profile:
    description:
      - The virtual machine scale set Security profile
    type: dict
    suboptions:
      encryption_at_host:
        description:
          - >-
            This property can be used by user in the request to enable or
            disable the Host Encryption for the virtual machine or virtual
            machine scale set. This will enable the encryption for all the disks
            including Resource/Temp disk at host itself.
            :code:`<br>`:code:`<br>` Default: The Encryption at host will be
            disabled unless this property is set to true for the resource.
        type: bool
  diagnostics_profile:
    description:
      - The virtual machine scale set diagnostics profile.
    type: dict
    suboptions:
      boot_diagnostics:
        description:
          - >-
            Boot Diagnostics is a debugging feature which allows you to view
            Console Output and Screenshot to diagnose VM status.
            :code:`<br>`:code:`<br>` You can easily view the output of your
            console log. :code:`<br>`:code:`<br>` Azure also enables you to see
            a screenshot of the VM from the hypervisor.
        type: dict
        suboptions:
          enabled:
            description:
              - >-
                Whether boot diagnostics should be enabled on the Virtual
                Machine.
            type: bool
          storage_uri:
            description:
              - >-
                Uri of the storage account to use for placing the console output
                and screenshot. :code:`<br>`:code:`<br>`If storageUri is not
                specified while enabling boot diagnostics, managed storage will
                be used.
            type: str
  extension_profile:
    description:
      - The virtual machine scale set extension profile.
    type: dict
    suboptions:
      extensions:
        description:
          - The virtual machine scale set child extension resources.
        type: list
      extensions_time_budget:
        description:
          - >-
            Specifies the time alloted for all extensions to start. The time
            duration should be between 15 minutes and 120 minutes (inclusive)
            and should be specified in ISO 8601 format. The default value is 90
            minutes (PT1H30M). :code:`<br>`:code:`<br>` Minimum api-version:
            2020-06-01
        type: str
  license_type:
    description:
      - 'The license type, which is for bring your own license scenario.'
    type: str
  billing_profile:
    description:
      - >-
        Specifies the billing related details of a Azure Spot VMSS.
        :code:`<br>`:code:`<br>`Minimum api-version: 2019-03-01.
    type: dict
    suboptions:
      max_price:
        description:
          - >-
            Specifies the maximum price you are willing to pay for a Azure Spot
            VM/VMSS. This price is in US Dollars. :code:`<br>`:code:`<br>` This
            price will be compared with the current Azure Spot price for the VM
            size. Also, the prices are compared at the time of create/update of
            Azure Spot VM/VMSS and the operation will only succeed if  the
            maxPrice is greater than the current Azure Spot price.
            :code:`<br>`:code:`<br>` The maxPrice will also be used for evicting
            a Azure Spot VM/VMSS if the current Azure Spot price goes beyond the
            maxPrice after creation of VM/VMSS. :code:`<br>`:code:`<br>`
            Possible values are: :code:`<br>`:code:`<br>` - Any decimal value
            greater than zero. Example: 0.01538 :code:`<br>`:code:`<br>` -1 –
            indicates default price to be up-to on-demand.
            :code:`<br>`:code:`<br>` You can set the maxPrice to -1 to indicate
            that the Azure Spot VM/VMSS should not be evicted for price reasons.
            Also, the default max price is -1 if it is not provided by you.
            :code:`<br>`:code:`<br>`Minimum api-version: 2019-03-01.
        type: number
  scheduled_events_profile:
    description:
      - Specifies Scheduled Event related configurations.
    type: dict
    suboptions:
      terminate_notification_profile:
        description:
          - Specifies Terminate Scheduled Event related configurations.
        type: dict
        suboptions:
          not_before_timeout:
            description:
              - >-
                Configurable length of time a Virtual Machine being deleted will
                have to potentially approve the Terminate Scheduled Event before
                the event is auto approved (timed out). The configuration must
                be specified in ISO 8601 format, the default value is 5 minutes
                (PT5M)
            type: str
          enable:
            description:
              - >-
                Specifies whether the Terminate Scheduled event is enabled or
                disabled.
            type: bool
  mode:
    description:
      - >-
        Specifies the mode of an upgrade to virtual machines in the scale
        set.:code:`<br />`:code:`<br />` Possible values are::code:`<br
        />`:code:`<br />` **Manual** - You  control the application of updates
        to virtual machines in the scale set. You do this by using the
        manualUpgrade action.:code:`<br />`:code:`<br />` **Automatic** - All
        virtual machines in the scale set are  automatically updated at the same
        time.
    type: sealed-choice
  rolling_upgrade_policy:
    description:
      - The configuration parameters used while performing a rolling upgrade.
    type: dict
    suboptions:
      max_batch_instance_percent:
        description:
          - >-
            The maximum percent of total virtual machine instances that will be
            upgraded simultaneously by the rolling upgrade in one batch. As this
            is a maximum, unhealthy instances in previous or future batches can
            cause the percentage of instances in a batch to decrease to ensure
            higher reliability. The default value for this parameter is 20%.
        type: integer
      max_unhealthy_instance_percent:
        description:
          - >-
            The maximum percentage of the total virtual machine instances in the
            scale set that can be simultaneously unhealthy, either as a result
            of being upgraded, or by being found in an unhealthy state by the
            virtual machine health checks before the rolling upgrade aborts.
            This constraint will be checked prior to starting any batch. The
            default value for this parameter is 20%.
        type: integer
      max_unhealthy_upgraded_instance_percent:
        description:
          - >-
            The maximum percentage of upgraded virtual machine instances that
            can be found to be in an unhealthy state. This check will happen
            after each batch is upgraded. If this percentage is ever exceeded,
            the rolling update aborts. The default value for this parameter is
            20%.
        type: integer
      pause_time_between_batches:
        description:
          - >-
            The wait time between completing the update for all virtual machines
            in one batch and starting the next batch. The time duration should
            be specified in ISO 8601 format. The default value is 0 seconds
            (PT0S).
        type: str
  automatic_os_upgrade_policy:
    description:
      - Configuration parameters used for performing automatic OS Upgrade.
    type: dict
    suboptions:
      enable_automatic_os_upgrade:
        description:
          - >-
            Indicates whether OS upgrades should automatically be applied to
            scale set instances in a rolling fashion when a newer version of the
            OS image becomes available. Default value is false.
            :code:`<br>`:code:`<br>` If this is set to true for Windows based
            scale sets, `enableAutomaticUpdates
            <https://docs.microsoft.com/dotnet/api/microsoft.azure.management.compute.models.windowsconfiguration.enableautomaticupdates?view=azure-dotnet>`_
            is automatically set to false and cannot be set to true.
        type: bool
      disable_automatic_rollback:
        description:
          - >-
            Whether OS image rollback feature should be disabled. Default value
            is false.
        type: bool
  instance_ids:
    description:
      - >-
        The virtual machine scale set instance ids. Omitting the virtual machine
        scale set instance ids will result in the operation being performed on
        all virtual machines in the virtual machine scale set.
    type: list
  skip_shutdown:
    description:
      - >-
        The parameter to request non-graceful VM shutdown. True value for this
        flag indicates non-graceful shutdown whereas false indicates otherwise.
        Default value for this flag is false if not specified
    type: bool
  temp_disk:
    description:
      - >-
        Specifies whether to reimage temp disk. Default value: false. Note: This
        temp disk reimage parameter is only supported for VM/VMSS with Ephemeral
        OS disk.
    type: bool
  platform_update_domain:
    description:
      - The platform update domain for which a manual recovery walk is requested
    type: integer
  active_placement_group_id:
    description:
      - >-
        Id of the placement group in which you want future virtual machine
        instances to be placed. To query placement group Id, please use Virtual
        Machine Scale Set VMs - Get API. If not provided, the platform will
        choose one with maximum number of virtual machine instances.
    type: str
  service_name:
    description:
      - The name of the service.
    type: choice
  action:
    description:
      - The action to be performed.
    type: choice
  state:
    description:
      - Assert the state of the VirtualMachineScaleSet.
      - >-
        Use C(present) to create or update an VirtualMachineScaleSet and
        C(absent) to delete it.
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
                response = self.mgmt_client.virtual_machine_scale_sets.create(resource_group_name=self.resource_group_name,
                                                                              vm_scale_set_name=self.vm_scale_set_name,
                                                                              parameters=self.body)
            else:
                response = self.mgmt_client.virtual_machine_scale_sets.update(resource_group_name=self.resource_group_name,
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
