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
bin/demo DEVICE_ID LOCAL_KEY IP
```

The demo:
* connects to your device,
* prints its state out,
* starts cleaning,
* waits 30 seconds,
* sends the device home,
* waits 10 seconds,
* disconnects & exits
