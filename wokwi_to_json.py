import json
import os

def json_to_netlist(json_file, netlist_file):
    # Check if the file exists and is not empty
    if not os.path.exists(json_file) or os.path.getsize(json_file) == 0:
        print(f"Error: The file '{json_file}' does not exist or is empty.")
        return

    try:
        with open(json_file, 'r') as file:
            data = json.load(file)
    except json.JSONDecodeError as e:
        print(f"Error: Failed to decode JSON from the file '{json_file}'. {e}")
        return

    components = data.get('parts', [])
    connections = data.get('connections', [])

    netlist = []

    # Add components to netlist
    for component in components:
        comp_type = component['type']
        comp_id = component['id']
        netlist.append(f"{comp_id}  {comp_type}")

    netlist.append("\n* Connections")

    # Add connections to netlist
    for connection in connections:
        start, end, color, path = connection
        netlist.append(f"{start}  {end}")

    # Write netlist to file
    with open(netlist_file, 'w') as file:
        file.write("* Netlist generated from Wokwi JSON\n\n")
        file.write("\n".join(netlist))

    print(f"Netlist has been successfully written to '{netlist_file}'.")

# Example usage
json_file = 'wokwi_project.json'
netlist_file = 'netlist.txt'
json_to_netlist(json_file, netlist_file)
