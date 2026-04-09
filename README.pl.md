[![HACS Default][hacs_shield]][hacs]
[![GitHub Latest Release][releases_shield]][latest_release]
[![GitHub All Releases][downloads_total_shield]][releases]
[![Installations][installations_shield]][releases]

[hacs_shield]: https://img.shields.io/static/v1.svg?label=HACS&message=Default&color=green&labelColor=41bdf5&logo=HomeAssistantCommunityStore&logoColor=white&style=flat-square
[hacs]: https://github.com/hacs/default

[releases_shield]: https://img.shields.io/github/v/release/ptrkoz/ha-smogtok?style=flat-square
[latest_release]: https://github.com/ptrkoz/ha-smogtok/releases/latest

[downloads_total_shield]: https://img.shields.io/github/downloads/ptrkoz/ha-smogtok/total?style=flat-square
[releases]: https://github.com/ptrkoz/ha-smogtok/releases

[installations_shield]: https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fanalytics.home-assistant.io%2Fcustom_integrations.json&query=%24.smogtok.total&color=41bdf5&label=analytics&style=flat-square

# Integracja SmogTok dla Home Assistant

[🇬🇧 English](https://github.com/ptrkoz/ha-smogtok) | 🇵🇱 Polski


Niestandardowa integracja SmogTok dostarczająca dane o jakości powietrza z stacji [SmogTok](https://smogtok.com/) do [Home Assistant](https://www.home-assistant.io/).

<img width="778" height="498" alt="Zrzut ekranu encji integracji SmogTok" src="https://github.com/user-attachments/assets/9cea54df-b391-4dd5-a03b-8f175617f2fc" />


Integracja dostarcza następujące encje z skonfigurowanej stacji SmogTok:
- temperatura (*°C*)
- wilgotność (*%*)
- ciśnienie powietrza (*hPa*)
- poziom PM10 (*μg/m³*)
- poziom PM2,5 (*μg/m³*)
- poziom PM0,1 (*μg/m³*)
- jakość powietrza (*Bardzo dobra*, *Dobra*, *Umiarkowana*, *Dostateczna*, *Zła* or *Bardzo zła*)
- indeks jakości powietrza (skala od *1* do *6*)

Każda encja ma atrybut *last_updated* z czasem ostatniego pomiaru. 

Niektóre stacje mogę nie posiadać wszystkich encji wymienionych powyżej.

**Zastrzeżenie** To nie jest oficjalna integracja stworzona lub wspierana przez SmogTok

## Instalacja

Tą integrację można zainstalować przez HACS lub manualnie.

### Instalacja integracji przez HACS (zalecane)
1. Upewnij się, że [HACS](https://hacs.xyz) jest zainstalowany w twoim Home Assistant

2. Otwórz stronę integracji w HACS klikając przycisk poniżej:

	[![Open your Home Assistant instance and open a repository inside the Home Assistant Community Store.](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=ptrkoz&category=integration&repository=ha-smogtok)
	
	Lub wyszukaj "SmogTok" w HACS i kliknij na wyszukaną integrację

3. Kliknij **POBIERZ** na stronie integracji (niebieski przycisk w prawym dolnym rogu)

4. Zrestartuj Home Assistant

### Instalacja integracji manualnie

1. Pobierz [smogtok.zip](https://github.com/ptrkoz/ha-smogtok/releases/latest/download/smogtok.zip) z [ostatniego wydania](https://github.com/ptrkoz/ha-smogtok/releases/latest), rozpakuj go, a następnie dodaj/scal z zawartością folderu `custom_components/` w twoim katalogu konfiguracji

2. Zrestartuj Home Assistant

## Konfiguracja

Skonfiguruj tą integrację w Home Assistant używając przycisku poniżej:

[![Open your Home Assistant instance and start setting up a new integration.](https://my.home-assistant.io/badges/config_flow_start.svg)](https://my.home-assistant.io/redirect/config_flow_start/?domain=smogtok)

Lub przejdź do: **Ustawienia** → **Urządzenia oraz usługi** → **Dodaj integrację** → **SmogTok**

<img width="453" height="283" alt="Zrzut ekranu metody konfiguracji integracji SmogTok" src="https://github.com/user-attachments/assets/7f006523-ecca-4dad-a1f5-3fc1ee9aacf4" />

Możesz dodać stację SmogTok na 3 sposoby:
- znajdując najbliższe stacje i wybierając jedną z nich

  <img width="457" height="315" alt="Zrzut ekranu konfiguracji integracji SmogTok przez znalezienie najbliższych stacji" src="https://github.com/user-attachments/assets/8493aa4e-5fad-4150-982b-3cc031208847" />

- wybierając z alfabetycznej listy aktywnych stacji

  <img width="453" height="272" alt="Zrzut ekranu konfiguracji integracji SmogTok przez alfabetyczna liste stacji" src="https://github.com/user-attachments/assets/49705672-5e4e-44e5-b064-c458efe85b7d" />
- wprowadzić manualnie ID stacji

  <img width="454" height="314" alt="Zrzut ekranu konfiguracji integracji SmogTok przez podanie ID stacji" src="https://github.com/user-attachments/assets/61029b0f-57eb-45dc-98a8-9823ea242d47" />

