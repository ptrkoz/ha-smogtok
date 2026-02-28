# SmogTok integration for Home Assistant

🇬🇧 English | [🇵🇱 Polski](README.pl.md)


SmogTok custom integration provides air quality data from [SmogTok](https://smogtok.com/) stations to [Home Assistant](https://www.home-assistant.io/).

<img width="778" height="498" alt="SmogTok integration entities screenshot" src="https://github.com/user-attachments/assets/f1abb101-79f0-472c-afa4-37fe2ea36efd" />


The integration provides following entities with data from configured SmogTok station:
- temperature (*°C*)
- humidity (*%*)
- air pressure (*hPa*)
- PM10 pollution (*μg/m³*)
- PM2.5 pollution (*μg/m³*)
- PM0.1 pollution (*μg/m³*)
- air quality (*Very good*, *Good*, *Moderate*, *Sufficient*, *Bad* or *Very bad*)
- air quality index (scale of *1* to *6*)

Each entity has a *last_updated* attribute with time of the recent measurement.

Some stations may not include all entities listed above.

**Disclaimer** This is not an official integration from or supported by the SmogTok

## Installation

This integration can be installed either via HACS or manually.

### Install integration via HACS (recommended)
1. Make sure you have [HACS](https://hacs.xyz) installed in your Home Assistant

2. Add custom repository to HACS by clicking the button below:

	[![Open your Home Assistant instance and open a repository inside the Home Assistant Community Store.](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=ptrkoz&category=integration&repository=ha-smogtok)
	
	Or go to: **HACS** → **3 dots (⋮)** → **Custom repositories**

	- Repository: https://github.com/ptrkoz/ha-smogtok
	- Type: **Integration**
	
    And click **ADD**

4. Search "SmogTok" in HACS and click on the found integration, next click **DOWNLOAD** (blue button in the bottom right corner)

5. Restart Home Assistant

### Install integration manually

1. Download [smogtok.zip](https://github.com/ptrkoz/ha-smogtok/releases/latest/download/smogtok.zip) from the [latest release](https://github.com/ptrkoz/ha-smogtok/releases/latest), unzip it, and add/merge the `custom_components/` folder with its contents in your configuration directory

2. Restart Home Assistant

## Configuration

To configure this integration in Home Assistant click the button below:

[![Open your Home Assistant instance and start setting up a new integration.](https://my.home-assistant.io/badges/config_flow_start.svg)](https://my.home-assistant.io/redirect/config_flow_start/?domain=smogtok)

Or go to: **Settings** → **Devices & services** → **Add integration** → **SmogTok**


<img width="450" height="276" alt="SmogTok integration select configuration method screenshot" src="https://github.com/user-attachments/assets/f4903d8d-919c-4401-933e-b5234e7e56c4" />


You can add your SmogTok station in 3 ways:
- by finding the nearest stations and picking one of them
  
  <img width="446" height="296" alt="SmogTok integration select station from the nearest ones screenshot" src="https://github.com/user-attachments/assets/132b4652-219f-4aa8-a4da-f377f0c21a2b" />
- by picking it from alphabetical list of active stations

  <img width="453" height="246" alt="SmogTok integration select station from the alphabetical list screenshot" src="https://github.com/user-attachments/assets/62eab8bd-0beb-45cb-ac4e-b0839f1844a6" />
- by manually entering station ID

  <img width="456" height="309" alt="SmogTok integration select station by ID screenshot" src="https://github.com/user-attachments/assets/e6b1239a-6323-4201-a824-92ebc914e891" />
