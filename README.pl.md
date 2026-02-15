# Integracja SmogTok dla Home Assistant

[🇬🇧 English](https://github.com/ptrkoz/ha-smogtok) | 🇵🇱 Polski


Niestandardowa integracja SmogTok dostarczająca dane o jakości powietrza z stacji SmogTok do Home Assistant.

<img width="678" height="511" alt="Zrzut ekranu encji integracji SmogTok" src="https://github.com/user-attachments/assets/0bedd2e0-7467-4bf5-97ca-95f8374705fb" />


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

Możesz dodać stację SmogTok wybierając ją z listy stacji aktywnych w ostatnich 30 dniach lub wprowadzić manualnie ID stacji.

<img width="231" height="159" alt="Zrzut ekranu metody konfiguracji integracji SmogTok" src="https://github.com/user-attachments/assets/ef567768-7e74-4cdb-ae42-92fabe56a9ff" />
<img width="278" height="175" alt="Zrzut ekranu konfiguracji integracji SmogTok przez liste stacji" src="https://github.com/user-attachments/assets/92c436b3-f757-4e01-a33f-9191fc92bbd0" />
<img width="282" height="187" alt="Zrzut ekranu konfiguracji integracji SmogTok przez podanie ID stacji" src="https://github.com/user-attachments/assets/395c8b6e-11c5-4c2c-8a93-d913988e3f24" />

