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

2. Dodaj niestandardowe repozytorium do HACS klikając przycisk poniżej:

	[![Open your Home Assistant instance and open a repository inside the Home Assistant Community Store.](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=ptrkoz&category=integration&repository=ha-smogtok)
	
	Lub przejdź do: **HACS** -> **3 kropki (⋮)** -> **Niestandardowe repozytoria**

	- Repozytorium: https://github.com/ptrkoz/ha-smogtok
	- Typ: **Integracja**
	
    Następnie kliknij **DODAJ**

3. Wyszukaj "SmogTok" w HACS i kliknij na wyszukaną integrację, a następnie kliknij **POBIERZ** (niebieski przycisk w prawym dolnym rogu)

4. Zrestartuj Home Assistant

### Instalacja integracji manualnie

1. Sklonuj to repozytorium lub pobierz jako plik zip, a następnie dodaj/scal z zawartością folderu `custom_components/` w twoim katalogu konfiguracji

2. Zrestartuj Home Assistant

## Konfiguracja

Skonfiguruj tą integrację w Home Assistant używając przycisku poniżej:

[![Open your Home Assistant instance and start setting up a new integration.](https://my.home-assistant.io/badges/config_flow_start.svg)](https://my.home-assistant.io/redirect/config_flow_start/?domain=smogtok)

Lub przejdź do: **Ustawienia** >> **Urządzenia oraz usługi** >> **Dodaj integrację** >> **SmogTok**

<img width="453" height="283" alt="Zrzut ekranu metody konfiguracji integracji SmogTok" src="https://github.com/user-attachments/assets/7f006523-ecca-4dad-a1f5-3fc1ee9aacf4" />

Możesz dodać stację SmogTok na 3 sposoby:
- znajdując najbliższe stacje i wybierając jedną z nich

  <img width="457" height="315" alt="Zrzut ekranu konfiguracji integracji SmogTok przez znalezienie najbliższych stacji" src="https://github.com/user-attachments/assets/8493aa4e-5fad-4150-982b-3cc031208847" />

- wybierając z alfabetycznej listy aktywnych stacji

  <img width="453" height="272" alt="Zrzut ekranu konfiguracji integracji SmogTok przez alfabetyczna liste stacji" src="https://github.com/user-attachments/assets/49705672-5e4e-44e5-b064-c458efe85b7d" />
- wprowadzić manualnie ID stacji

  <img width="454" height="314" alt="Zrzut ekranu konfiguracji integracji SmogTok przez podanie ID stacji" src="https://github.com/user-attachments/assets/61029b0f-57eb-45dc-98a8-9823ea242d47" />

