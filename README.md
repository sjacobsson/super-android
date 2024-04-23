Git repo for super android project. Distributed computing on android phones.

# Table of available demos
| Name | Description |
| ---- | ----------- |
| `Render farm` | Render some rad fractals |

TODO: Link to these.


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
	1. `yes | pkg upgrade`
	2. `yes | pkg install rust git make clang`
2. Advanced Charging Controller (ACCA).
3. Keep Screen On, and add as quick settings tile.

<!-- Then install gcc in termux by `pkg install clang`, and `rust` by `pkg install rust openssl`. -->

### Network

In termux, run
1. `git clone https://github.com/eprovst/supanrf`
2. `cd supanrf`
3. `make`
4. `su` (optional)

Connect the phone to the router (dlink-5BF0) and set Static IP adress 192.168.0.X in the wifi settings.

5. `./start-server`

ETP should now be running on the server.

You are now ready to run any of the demos in the table above.


# What parts needs to be done each time

Start the ACCA app and make sure the Keep Screen On thing is active (it's in the drag-down menu).

Each time a server is started, we just again run, in Termux,
1. `cd supanrf`
2. `su` (optional)
3. `./start-server`

