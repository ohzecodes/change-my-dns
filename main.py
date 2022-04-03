import subprocess
import rumps
import os

dns = ["192.168.1.1", "192.168.1.10"]

[router, pihole] = dns


class DNS_changing(rumps.App):

    def __init__(self):
        super(DNS_changing, self).__init__("DNS Changing", title="DNS Change")
        ns = os.popen(f"networksetup -getdnsservers Wi-Fi").read()
        self.menu.add(ns)
        self.first = True

    # button function
    @rumps.clicked("Router!")
    def router(self, _):

        os.system(f"networksetup -setdnsservers Wi-Fi {router}")
        if self.first:
            self.menu.pop(self.menu.items()[0][0])
            self.first = False
        else:
            self.menu.pop(self.menu.items()[len(self.menu) - 1][0])
        self.menu.add("Router")

    # button function
    @rumps.clicked("Pihole!")
    def pi_hole(self, _):
        os.system(f"networksetup -setdnsservers Wi-Fi {pihole}")
        if self.first:
            self.menu.pop(self.menu.items()[0][0])
            self.first = False
        else:
            self.menu.pop(self.menu.items()[len(self.menu) - 1][0])
        self.menu.add("Pihole")


if __name__ == "__main__":
    DNS_changing().run()
