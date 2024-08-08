# Networking-servers-assignment

## deploy a website on localhost using nginx

### 1.	Verify Nginx Installation =                      
                       “sudo systemctl status nginx”
### 2.	Create and Navigate a Directory awesomeweb =
         “sudo mkdir -p /var/www/awesomeweb”
           “cd /var/www/awesomeweb/”
### 3.	Create an HTML File =
 Create an index.html file inside the awesomeweb directory and add some basic HTML content.  “sudo nano index.html”
### 4.	Set Proper Permissions 
     Change the ownership and permissions of your website directory.
          “sudo chown -R www-data:www-data /var/www/awesomeweb”
            “sudo chmod -R 755 /var/www/awesomeweb”
### 5.	Configure Nginx to website =
 Create a new Nginx server block configuration file.
 “sudo nano /etc/nginx/sites-available/awesomeweb”
### 6.	Enable the New Configuration =
Create a symbolic link to enable the new site.
“sudo ln -s /etc/nginx/sites-available/awesomeweb /etc/nginx/sites-enabled/”
### 7.	Reload Nginx =
“sudo systemctl reload nginx”
### 8.	Update the Hosts File =
“sudo nano /etc/hosts”
### 9.	Verify the Setup =
“curl http://localhost”
“curl http://awesomeweb”


## Subdomain Status Checker Script

### 1.	Install python3 using pip =

“sudo apt install python3-pip”
### 2.	Libraries Installation =
“pip install requests tabulate schedule”
### 3.	Script: check_subdomains.py =
            Create a Py thon file named check_subdomains.py and add the following script:
### 4.	Running the Script =
“python3 checksubdomains.py”


## Setting Up VirtualBox and Virtual Machine

### 1.	Download VirtualBox =
Download Virtualbox on a web browser from the official Virtualbox website.
### 2.	Post-installation Configuration =
#### Group Permissions:
•	Ensure the user account is added to the "VirtualBox Users" group to manage VMs effectively.
#### Reboot or Log Out/In:
•	After modifying group memberships, it's a good practice to either reboot the machine or log out and log back in to apply changes.
### 3.	Setting Up a Virtual Machine with Ubuntu 22.04 =
#### Download Ubuntu 22.04:
•	Visit osboxes.org and download the Ubuntu 22.04 image file.
#### Create a New Virtual Machine in VirtualBox:
Created a virtual machine named “UbuntuMymachine” on Virtual Box.
#### Install Nginx:
Start the VM and install Nginx inside Ubuntu.
     “sudo apt update”
     “sudo apt install nginx”
            Configure Nginx to serve a simple HTML page.

### 4.	Network Scanning with Nmap =
















