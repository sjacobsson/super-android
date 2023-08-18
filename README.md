Git repo for super android project. Distributed computing on android phones.

# Table of available applications
| Name | Description |
| ---- | ----------- |
| `julia_set` | Compute the Julia set |

# Cloning this repository
Clone this repository and got to its root folder. Then clone the submodules with
```sh
git submodule init
git submodule update
```

And then fetch the needed libraries for Rust to compile offline by running `online_fetch.sh` from within `copy to each phone/super-pi-ray/`.

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
Then install gcc in termux by `pkg install clang`, and `rust` by `pkg install rust openssl`.
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
	`g++ <application>_client.c -o <application>_client`  
to generate an executable. Here, the `<application>` can be any of the applications in the [table](#table-of-available-applications).

And/or,
	`offline_build.sh`
from within `super-pi-ray`.

# Running a compute

### Set up communication with the phones
Create an SSH key pair of type `ed25519` (`ssh-keygen -t ed25519`) and ask someone to place the public key on each of the phones. Then create a file named `.pkey` (which is ignored by Git) in the root of this repository, containing the **path to** your private key.

### Run the application server
Ensure Python 3 is installed on your machine. Then choose an application from the [table](#table-of-available-applications) and run
```python3
python3 <application>_server.py
```
