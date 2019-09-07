### HA support

"""Support for Eufy devices."""
import logging

import voluptuous as vol

from homeassistant.const import (
    CONF_ACCESS_TOKEN, CONF_ADDRESS, CONF_DEVICES, CONF_NAME,
    CONF_ID, CONF_TYPE)
from homeassistant.helpers import discovery
import homeassistant.helpers.config_validation as cv

_LOGGER = logging.getLogger(__name__)

DOMAIN = 'eufy_vacuum'

DEVICE_SCHEMA = vol.Schema({
    vol.Required(CONF_ADDRESS): cv.string,
    vol.Optional(CONF_ACCESS_TOKEN): cv.string,
    vol.Required(CONF_ID): cv.string,
    vol.Required(CONF_TYPE): cv.string,
    vol.Optional(CONF_NAME): cv.string
})

CONFIG_SCHEMA = vol.Schema({
    DOMAIN: vol.Schema({
        vol.Optional(CONF_DEVICES, default=[]):
            vol.All(cv.ensure_list, [DEVICE_SCHEMA]),
    }),
}, extra=vol.ALLOW_EXTRA)


def setup(hass, config):
    """Set up Eufy devices."""
    for device_info in config.get(DOMAIN, {}).get(CONF_DEVICES, []):
        device = {}
        device['address'] = device_info[CONF_ADDRESS]
        device['local_key'] = device_info.get(CONF_ACCESS_TOKEN)
        device['device_id'] = device_info[CONF_ID]
        device['name'] = device_info.get(CONF_NAME)
        device['model'] = device_info[CONF_TYPE]
        discovery.load_platform(hass, 'vacuum', DOMAIN, device, config)

    return True
