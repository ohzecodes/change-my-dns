import rumps
import os
from DnsList import dns
icon="assets/icon.icns"
read_dns="networksetup -getdnsservers Wi-Fi"
set_dns_cmd=lambda ip : f'networksetup -setdnsservers Wi-Fi {ip}'
notifications=False

def issue_notification_or_alert(title):
    if (notifications):
        rumps.notification(title,"", os.popen(read_dns).read()  )
    else:
        rumps.alert(title, os.popen(read_dns).read(),icon_path=icon)

class DNS_changing(rumps.App):
    def __init__(self):
        super(DNS_changing, self).__init__("DNS Changing", title="Change DNS")
        self.first = True

    @rumps.clicked("Find my Dns?")
    def find(self,_):
       issue_notification("Your DNS is at")

    for i in range(len(dns)):
        n= str(list(dns)[i]).replace("{", "").replace("'", "").replace("}", "").replace(": ", "-")
        @rumps.clicked(n)
        def router(self, _=None):
            if _ is None:
                name = self.title
            else:
                name = _.title
            ip = name.split('-')[1]
            os.system(set_dns_cmd(ip))

            issue_notification("Your DNS is changed")

if __name__ == "__main__":
    DNS_changing().run()
