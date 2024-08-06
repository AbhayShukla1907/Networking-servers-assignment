import urllib.request
import time

# List of subdomains to check
subdomains = [
    "sub1.example.com",
    "www.google.com",
    "sub3.example.com"
]

# Function to check the status of a subdomain
def check_subdomain_status(subdomain):
    try:
        response = urllib.request.urlopen(f"http://{subdomain}", timeout=5)
        if response.getcode() == 200:
            return "Up"
        else:
            return "Down"
    except:
        return "Down"

# Main loop to check the status every minute
while True:
    print("Checking subdomains status...\n")
    for subdomain in subdomains:
        status = check_subdomain_status(subdomain)
        print(f"{subdomain}: {status}")
    print("\nWaiting for 60 seconds...\n")
    time.sleep(60)
