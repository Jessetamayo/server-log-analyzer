import csv

# Open the log file
with open('server_logs.csv', 'r') as file:
    reader = csv.DictReader(file)
    
    print("--- SUSPICIOUS ACTIVITY REPORT ---")
    print("Scanning for Access Denied for IP (403 errors)...")
    
    # Loop through every row in the data
    for row in reader:
        # Check if the status code is '403'
        if row['Status_Code'] == '403':
            print(f"ALERT: Access Denied for IP {row['IP_Address']}")

    print("--- SCAN COMPLETE ---")

