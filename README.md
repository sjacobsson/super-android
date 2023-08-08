Git repo for super android project. Distributed computing on android phones.

# Setting up a phone

### Install LineageOS
Look up if the device is supported and then follow the corresponding guide: https://wiki.lineageos.org/devices/

### Root
Usually, if using the LineageOS custom recovery or TWRP, this is just  
	1. Download the Magisk .apk to the phone from their github  
 	2. Rename the .apk to .zip  
  	3. Boot into recovery  
   	4. Install > Install Zip > X.zip > Flash  
    	5. Reboot  
     	6. Open the Magisk app and follow the suggested setup there  

### Apps
On the phone, install F-Droid, then SimpleSSHD and Termux from F-Droid.
Then install gcc in termux by `pkg install clang`.
Also set SimpleSSHD to start on boot.

### Network
Connect the phone to the router (dlink-5BF0) and set Static IP adress 192.168.0.X in the wifi settings.

### Compiling on the phone
Run  
	`scp -rP 2222 copy\ to\ each\ phone/* 192.168.0.X:~`  
from this repo.
Then ssh into the phone  
	`ssh -p 2222 192.168.0.X mv profile .profile`  
	`ssh -p 2222 192.168.0.X`  
and grant SimpleSSHD super user rights in the Magisk popup on the phone.

While ssh'd into the phone, run  
	`g++ julia.c`  
to generate an executable.


# Running a compute

TODO.
