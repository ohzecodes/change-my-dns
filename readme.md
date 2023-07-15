
# Change my dns
A Mac menu bar app used to change the dns on the spot.

## Overview 
Change my dns allows you to change your DNS from the menu bar.
A DNS or a Domain Name Server is a device that maps your website to the corresponding IP address. 
Typically, the DNS is the same as your router, however at times you may need to change it. 
For instance, if you want to employ a PiHole or an ad blocker running on your network. 

###  The complexities of the interface (Traditional Approach)
   Changing the dns is possible but its not very convenient. Here are the steps:

   ```System Preferences > Network > Wifi > Advanced... > DNS Tab > add a new one here and remove the old one ```

   As you can see this process is not very simple. That's where this App comes into play. 

###  Introducing this App!

   When the app runs, the menu bar will display the option "Change DNS". By clicking on this option, a drop-down menu will appear, prompting you to select your preferred DNS (Domain Name System). After making your selection, a successful confirmation alert will appear, displaying the IP address of your newly chosen DNS.

## Geting Started

1.  Get started by adding your dns to the list in DnsList.py: 
```python
 {"DNSNAME": "IP_Address"}
```

* Replace "DNSNAME" with the actual name of your DNS and "IP_Address" with the corresponding IP address.
* Make sure to delete any placeholder values in the list, replacing them with your actual DNS information.

2. Adding the necessary requirements to do this run the following command in the terminal application after changing directory to the project folder
   ```bash
   pip install -r requirements.txt
   ```
4. run main.py `python3 main.py`

## Technologies used
   
   1. Python
   2. [Python Rumps](https://github.com/jaredks/rumps)
   3. Shell Scripts  

    
## Approach Taken

I have utilized the Python's Rumps package to help develop the menu bar application. When you click on the DNS setting, Shell Scripts are executed in the background. These scripts work together to modify your DNS settings to the newly selected one.
    

## Wins and Blockers
### Wins
I found it very time consuming, and annoying to use interface way to change my DNS, so I created the app. 


### Blockers
* Instead of the find my dns button, I would like to see my current DNS configuration in the menu update in real time. 
* Allow users to add their own dns configuration without having to see code


## Visuals and code samples
![visual of the menu bar](https://github.com/ohzecodes/changemyDns/blob/main/assets/visual%201.png?raw=true)


## [PyInstaller](https://pyinstaller.org/)

```bash 
pyinstaller --onefile -w --add-data "assets/icon.icns:assets" --icon="assets/icon.icns"  main.py
```

## Background App 

To run the application in the background mode without displaying it in the dock, follow these steps:

1. Build the application as per the required specifications.
2. Right-click on the application and select "Open Package Contents."
3. Navigate to the "Contents" folder.
4. Locate the info.plist file within this folder.
5. Open the info.plist file and make the necessary modifications. Just before the closing </dict> tag add the following XML code:
```xml
<key>LSUIElement</key><true/> 
```
## Issues: 
Please use the Issues tab in the repository to raise the Issue. 



