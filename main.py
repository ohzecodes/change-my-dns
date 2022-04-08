# icon from https://www.flaticon.com/premium-icon/browser_1779307
import rumps
import os

dns = [{"router": "192.168.1.1"}, {"Dns1": "192.168.1.2"}, {"Dns2": "192.168.1.4"}]


class DNS_changing(rumps.App):
    def __init__(self):
        super(DNS_changing, self).__init__("DNS Changing", title="Change DNS")
        self.first = True

    @rumps.clicked("Find my Dns?")
    def find(self,_):
        rumps.alert("Your DNS is at", os.popen(f"networksetup -getdnsservers Wi-Fi").read(), icon_path="assets/icon.png", )

    for i in range(len(dns)):
        n= str(list(dns)[i]).replace("{", "").replace("'", "").replace("}", "").replace(": ", "-")
        @rumps.clicked(n)
        def router(self, _=None):
            if _ is None:
                name = self.title
            else:
                name = _.title
            ip = name.split('-')[1]

            cmd = f"networksetup -setdnsservers Wi-Fi {ip}"
            os.system(cmd)
            rumps.alert("DNS Changed", os.popen(f"networksetup -getdnsservers Wi-Fi").read(), icon_path="assets/icon.png")






if __name__ == "__main__":
    DNS_changing().run()
