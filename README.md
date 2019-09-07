# Eufy Robovac control for Python

Work in progress!

## Installation
Pre-requisites:
* openssl (used for encryption)

```
git clone https://github.com/mitchellrj/eufy_robovac.git
cd eufy_robovac
python3 -m venv .
bin/pip install -e .
```

## Demo usage
```
bin/demo DEVICE_ID IP LOCAL_KEY
```

The demo:
* connects to your device,
* prints its state out,
* starts cleaning,
* waits 30 seconds,
* sends the device home,
* waits 10 seconds,
* disconnects & exits

## Home Assistant integration

**EXPERIMENTAL!**

Copy the contents of the `eufy_robovac` folder to `custom_components/eufy_vacuum` in your home assistant configuration directory. Then add the following to your configuration file:

```
eufy_vacuum:
  devices:
  - name: Robovac
    address: 192.168.1.80
    access_token: YOUR LOCAL KEY HERE
    id: YOUR DEVICE ID HERE
    type: T2118
```
