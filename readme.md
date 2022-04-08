# Change my dns
A Mac menu bar app used to change the dns on the spot

## Overview 
Change my dns allows you to change your DNS from the menu bar.
A DNS or a Domain Name Server is a device that maps your website to the corresponding IP address. 
Typically, the DNS is the same as your router, however at times you may need to change it. 
For instance, if you want to employ a PiHole or an ad blocker running on your network. 

##  The complexities of the interface (Traditional Approach)
Changing the dns is possible but its not very convenient. Here are the steps:

```System Preferences > Network > Wifi > Advanced... > DNS Tab > add a new one here and remove the old one ```

As you can see this process is super complicated. That's where this App comes into play. 

##  Introducing this App!
You can store your favorite DNS servers in the array. When the apps runs the menu bar with show: ```Change DNS``` 
click this and you will be prompted to choose your favorite DNS through the drop down menu. 
Once successful it will show you an alert with the ip of your new dns. 

## Get Started
Get started by adding your dns to the dns list in line 5 in main.py: 
```{"DNSNAME": "IP_Address"}```
where DNSNAME and IP_Address is coresponds to actual values. 
Also remember to delete the placeholder values. 
        
        
##  Technologies used
   1.  Python
   2.  [Python Rumps](https://github.com/jaredks/rumps)
   3.  Shell Scripts  

    
## Approach Taken
I have used the Python Rumps package to generate the menu-bar stand alone application.
 Behind the scenes, when you click the DNS setting a Shell Script runs, changing your dns to the new one. 
    

## Wins and Blockers
### Wins
I found it very time consuming to use the traditional way to change my DNS, so I created the app for personal use. 
Soon after that I saw that I could share the app on github. 

### Blockers
* Instead of the find my dns button, I would like to see my current DNS configuration in the menu update in real time. 
This could not be done with the current version of the rumps package, because each of the button is a menuitem, 
and there is not a way to reach the parent from the menu item in the current version.
* Allow users to add their own dns without having to see code


## Visuals and code samples
![visual of the menu bar](https://github.com/ohzecodes/changemyDns/blob/main/assets/visual%201.png?raw=true)


## Disclaimer 
I acknowledge the following: 
1. This application is built with good intent. 
2. I dont and will not take responsibility for any misuse of this application.  
3. License: You can use this for you project. Just make sure to say where you got it from

## Py2App
Ofcourse, you can build an app out this code after you add your configuration follow [this tutorial](http://www.marinamele.com/from-a-python-script-to-a-portable-mac-application-with-py2app)
