from netmiko import ConnectHandler

# Define device parameters
device = {
    'device_type': 'cisco_ios',
    'ip': '192.168.1.1',
    'username': 'admin',
    'password': 'password',
}

# Connect to the device
conn = ConnectHandler(**device)

# Backup device configuration
output = conn.send_command('show running-config')
with open('backup.txt', 'w') as f:
    f.write(output)

# Disconnect from the device
conn.disconnect()


# Connect to the device
net_connect = ConnectHandler(**device)

# Send a command and capture the output
output = net_connect.send_command('show interfaces')

# Use regex to search for specific patterns in the output
pattern = re.compile(r'GigabitEthernet\d/\d')
interfaces = pattern.findall(output)

# Print the interfaces found
print(interfaces)

# Disconnect from the device
net_connect.disconnect()
