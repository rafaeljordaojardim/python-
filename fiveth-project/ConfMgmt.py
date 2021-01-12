# importing necessary modules
import difflib
import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from netmiko import ConnectHandler

# defining tge device to monitor
ip = '10.10.10.2'

# defining the device type for running netmiko
device_type = 'arista_eos'

# defining the username and password for running netmiko
username = 'admin'
password = 'python'

# defining the command to send to each device
command = 'show running'

# connecting to the device via SSH
session = ConnectHandler(device_type = device_type, ip = ip, username = username, password = password, global_delay_factor = 3)

# entering enable model
enable = session.enable()

# sending the commmand agd storing the output (running configuration)
output = session.send_command(command)

# defining the file from yesterday for comparison
device_cfg_old = 'cfgfiles/' + ip + '_' + (datetime.date.today() - datetime.timedelta(days=1)).isoformat()

# writing the command output to a file for today
with open('cfgfiles/'+ ip + "_" + datetime.date.today().isoformat(), 'w') as device_cfg_new:
    device_cfg_new.write(output + '\n')

# extracting the differences between yesterday's and today's files in HTML format
with open(device_cfg_old, 'r') as old_file, open('cfgfiles/' + ip + '_' + datetime.date.today().isoformat(), 'r') as new_file:
    difference = difflib.HtmlDiff().make_file(fromlines = old_file.readlines(), tolines = new_file.readlines(), fromdesc='Yesterday', todesc='Today')

# sending the differences via email
# defining the e-email parameters
fromaddr = "rafaeljardim22@gmail.com"
toaddr = "rafaeljardim22@gmail.com"

# more on MIME and multipart: https://en.wikipedia.org/wiki/MIME#Multpart_messages
msg = MIMEMultipart()
msg["From"] = fromaddr
msg["To"] = toaddr
msg["Subject"] = 'Daily Configuration Management Report'
msg.attach(MIMEText(difference, 'html'))

# sending email via Gmail's SMTP server on port 587
server = smtplib.SMTP('smtp.gmail.com', 587)

# SMTP connection is in TLS (Transport Layer Security) mode. All SMTP commands that follow will be encrypted
server.starttls()

# Logging into gmail and sending the email
server.login("mail", "pass")
server.sendmail(fromaddr, toaddr, msg.as_string())
server.quit()