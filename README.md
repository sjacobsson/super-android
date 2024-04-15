Git repo for super android project. Distributed computing on android phones.

# Table of available demos
| Name | Description |
| ---- | ----------- |
| `Render farm` | Render some rad fractals |


# Setting up a phone to be a server

(The next two steps can be skipped).

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
On the phone, install F-Droid from https://f-droid.org/. Then from F-Droid install
1. Termux. In termux, run
	1. `pkg update` (you might have to change repo)
	2. `pkg upgrade`
	3. `pkg install openssh`
	4. `pkg install rust`
2. Advanced Charging Controller (ACCA).
3. Keep Screen On, and add as quick settings tile.

<!-- Then install gcc in termux by `pkg install clang`, and `rust` by `pkg install rust openssl`. -->

### Network
Connect the phone to the router (dlink-5BF0) and set Static IP adress 192.168.0.X in the wifi settings.

In termux, run
1. `passwd` and set some easy to remember password
2. `sshd`

On the client, run
1. `git clone https://gitlab.kuleuven.be/numa/oppc/super-android/supanrf`

Then connect to the router and run
1. `cd supanrf`
2. `scp -P 8022 <publickey> 192.168.0.X:.ssh/authorized_keys`

where `<publickey>` is the path to your public ssh key. You are now queried for the password you set earlier. Lastly, run
1. `./copy-to-device 192.168.0.X`
<!-- TODO: Rename the supanrf to ETP -->
<!-- TODO: Write guide for the render farm as well -->

On the server, in Termux, run
1. `cd supannn`
2. `./supannn`

ETP should now be running on the server.

You are now ready to run any of the demos in the table above.


# What parts needs to be done each time

Each time a server is started, we just again run, in Termux,
1. `cd supannn`
2. `./supannn`

TODO: What about ACCA and Keep Screen On?
