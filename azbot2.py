import concurrent.futures
import time
import azure.mgmt.compute
import azure.mgmt.resource


def create_vm(compute_client, region, resource_group_name, vm_name):
    print(f"Creating virtual machine '{vm_name}' in region '{region}'")

    async_vm_creation = compute_client.virtual_machines.create_or_update(
        resource_group_name,
        vm_name,
        {
            "location": region,
            "hardware_profile": {
                "vm_size": VirtualMachineSizeTypes.standard_f8s
            },
            "storage_profile": {
                "image_reference": {
                    "publisher": "Canonical",
                    "offer": "UbuntuServer",
                    "sku": "20.04-LTS",
                    "version": "latest"
                }
            },
            "os_profile": {
                "admin_username": "azureuser",
                "admin_password": "AzureUserPassword123!",
                "computer_name": vm_name
            },
            "network_profile": {
                "network_interfaces": [{
                    "id": nic.id,
                }]
            },
        }
    )
    async_vm_creation.wait()

    print(f"Virtual machine '{vm_name}' created successfully.")

    print(f"Running 'apt update' on virtual machine '{vm_name}'")
    command = "sudo apt update"
    run_command_result = compute_client.virtual_machines.run_command(
        resource_group_name,
        vm_name,
        {
            "command_id": "RunShellScript",
            "script": [command]
        }
    )

    print(f"Output of 'apt update' on virtual machine '{vm_name}': {run_command_result.value}")

# Authenticate to Azure and create an instance of the Azure Compute client
compute_client = get_compute_client()

# Get all Azure regions
regions = compute_client.providers.list_by_namespace("Microsoft.Compute")
f8s_regions = []
for region in regions:
    vm_sizes = compute_client.virtual_machine_sizes.list(region.location)
    for vm_size in vm_sizes:
        if vm_size.name == VirtualMachineSizeTypes.standard_f8s:
            f8s_regions.append(region.location)
            break

# Create a virtual machine in each eligible region in parallel
resource_group_name = "my-resource-group"
with concurrent.futures.ThreadPoolExecutor() as executor:
    results = [executor.submit(create_vm, compute_client, region, resource_group_name, f"my-vm-{i}") for i, region in enumerate(f8s_regions)]
    for f in concurrent.futures.as_completed(results):
        print(f.result())

print("Virtual machine creation and package update complete.")
