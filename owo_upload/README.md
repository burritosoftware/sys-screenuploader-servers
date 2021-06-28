### [owo_upload.py](./owo_upload.py)
Sends media to the OwO service.

Install [requirements](./requirements.txt):

```bash
$ pip install -r requirements.txt
```

Please run `owo_upload.py --help`. You must specify a token, a host IP (your private IP on your LAN), and optionally, a custom base URL to use this.
For now, you should run this script on your local machine, as it will automatically copy your upload's URL to the system's clipboard.

### Installation
You should be using **Atmosphere CFW** and be connected to your network, with **90DNS** to prevent Nintendo connections.

Download the latest release of [sys-screenuploader](https://github.com/bakatrouble/sys-screenuploader/releases/) and extract it to the root of your SD card.  
Open `config/sys-screenuploader/config.ini`. Uncomment this line:  
```
; url = https://screenuploader.bakatrouble.me/upload/<destid>/
```
Replace the URL included with this URL, specifying your IP and changing `8080` if you set a different port.
```
url = http://<ip_address>:<port>
```
After you do this, save the config, and either restart your Switch back into CFW, or enable `sys-screenuploader` in [Hekate Toolbox](https://github.com/WerWolv/Hekate-Toolbox/releases/latest).

You should then make sure you have the requirements installed for the server, and run `owo_upload.py`, passing in parameters for `-h` as your private IP, `-t` for your OwO token, and `-b` for an optional base URL.
```
owo_upload.py -h 192.168.1.10 -t tokenhere -b https://owo.is-pretty.cool
```

Captures and videos from your Switch will now be sent to your computer and then uploaded to OwO. Videos may take a bit longer to process.