import csv
from collections import Counter

# Open the log file
with open('server_logs.csv', 'r') as file:
    reader = csv.DictReader(file)
    
    print("--- SECURITY INCIDENT REPORT ---")
    
    # Create a list to store every bad IP we find
    attack_ips = []

    # Loop through every row in the data
    for row in reader:
        # Check for 403 (Forbidden) OR 401 (Unauthorized)
        if row['Status_Code'] == '403' or row['Status_Code'] == '401':
            # Add the IP to our list of suspects
            attack_ips.append(row['IP_Address'])

    # Count the duplicates in our list
    # This automatically turns ["10.0.0.1", "10.0.0.1"] into {"10.0.0.1": 2}
    ip_counts = Counter(attack_ips)

    # Print the summary
    for ip, count in ip_counts.items():
        print(f"Target: {ip} - Failed Attempts: {count}")
    
    if not attack_ips:
        print("No threats detected.")
        
    print("--- END OF REPORT ---")
