# SmogTok integration for Home Assistant

🇬🇧 English | [🇵🇱 Polski](README.pl.md)


SmogTok custom integration provides air quality data from SmogTok stations to Home Assistant.

<img width="678" height="497" alt="SmogTok integration entities screenshot" src="https://github.com/user-attachments/assets/9d5cb66e-a48b-47bb-9bbb-449ba3147612" />


The integration provides following entities with data from configured SmogTok station:
- temperature (*°C*)
- humidity (*%*)
- air pressure (*hPa*)
- PM10 pollution (*μg/m³*)
- PM2.5 pollution (*μg/m³*)
- PM0.1 pollution (*μg/m³*)
- air quality (*Very good*, *Good*, *Moderate*, *Sufficient*, *Bad* or *Very bad*)
- air quality index (scale *1* to *6*)

Each entity has a *last_updated* attribute with time of the recent measurement.

Some stations may not include all entities listed above.


## Installation

This integration can be installed either via HACS or manually.

### Install integration via HACS (recommended)
1. Make sure you have [HACS](https://hacs.xyz) installed in Home Assistant

2. Add custom repository to HACS by clicking the button below:

	[![Open your Home Assistant instance and open a repository inside the Home Assistant Community Store.](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=ptrkoz&category=integration&repository=ha-smogtok)
	
	Or go to: **HACS** -> **3 dots (⋮)** -> **Custom repositories**

	- Repository: https://github.com/ptrkoz/ha-smogtok
	- Type: **Integration**
	
    And click **ADD**

4. Search "SmogTok" in HACS and download the integration

5. Restart  Home Assistant

### Install integration manually

1. Clone this repository or download the source code as a zip file and add/merge the `custom_components/` folder with its contents in your configuration directory

2. Restart Home Assistant

## Configuration

To configure this integration in Home Assistant click the button below:

[![Open your Home Assistant instance and start setting up a new integration.](https://my.home-assistant.io/badges/config_flow_start.svg)](https://my.home-assistant.io/redirect/config_flow_start/?domain=smogtok)

Or go to: **Settings** >> **Devices & services** >> **Add integration** >> **SmogTok**

You can add your SmogTok station be choosing it from list of stations active in the last 30 days or by manually entering station ID.

<img width="241" height="163" alt="SmogTok integration select configuration method screenshot" src="https://github.com/user-attachments/assets/1dc67251-8e9f-4ec1-8dbf-dce59114c880" />
<img width="282" height="176" alt="SmogTok integration select station from the list screenshot" src="https://github.com/user-attachments/assets/ea3fae98-8489-4b4f-aa8d-cede8510a54c" />
<img width="278" height="187" alt="SmogTok integration select station by ID screenshot" src="https://github.com/user-attachments/assets/4a9821b4-c4ac-4730-828b-063851c7101c" />
