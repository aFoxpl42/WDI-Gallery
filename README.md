# WDI-Gallery Dokumentacja Projektu: Galeria Prac Studenckich 

**Projekt przygotowany na zaliczenie przedmiotu Wstep do Internetu**

## 1. Architektura i Technologia
Projekt stanowi wersję podstawową "mockup/frontend", zrealizowaną z zachowaniem zasady minimalizmu i wydajności:
- **Technologie:** Czysty HTML5, CSS3.
- **Rozwiązania specjalne:** Zrezygnowano z bibliotek zewnętrznych i JavaScriptu. Logika działania aplikacji (filtrowanie prac po semestrach, otwieranie widoku szczegółowego modali) została zaimplementowana za pomocą zaawansowanych selektorów CSS (`:checked`, `:target`).
- **Przygotowanie pod Backend:** Struktura HTML została napisana blokowo, aby umożliwić w kolejnym etapie łatwe wdrożenie renderowania po stronie serwera (SSR) za pomocą Pythona (np. Django Templates).

## 2. Zrealizowany minimalny zakres
1. **Strona główna:** Zaimplementowana sekcja Hero.
2. **Opis przedmiotu:** Zaimplementowana dedykowana sekcja tekstowa.
3. **Sekcja prowadzących:** Zaimplementowana (wersja wizytówkowa).
4. **Galeria prac:** Zaimplementowana funkcjonalna siatka z danymi testowymi oraz systemem nieniszczącego filtrowania.
5. **Widok szczegółowy:** Zaimplementowany mechanizm okien modalnych wyświetlających filmy w proporcji 16:9 (YouTube Embed).
6. **Responsywność:** Zaimplementowana logika Mobile First / Desktop za pomocą Flexbox oraz CSS Grid (`@media` queries).
7. **Dokumentacja i uruchomienie:** Niniejszy plik.

## 3. Raport z testowania (Etap 9)
Przeprowadzono testy poprawności:
* **Test responsywności:** Układ testowany w Chrome DevTools. Działa poprawnie w wymiarach: 360px, 390px, 768px (przełamanie na układ kolumnowy), 1024px oraz 1440px.
* **Test działania nawigacji:** Kotwice HTML nawigują po sekcjach płynnie. Menu adaptuje się do widoku mobilnego.
* **Test galerii:** Filtrowanie bez przeładowania strony ukrywa niechciane kategorie.
* **Test widoku szczegółowego:** Modal nakłada się poprawnie na warstwę wierzchnią z zachowaniem zablokowania tła. Odtwarzacze zachowują właściwy format.
* **Test obrazów/filmów:** Zastosowano `object-fit: cover` dla miniatur oraz `aspect-ratio: 16/9` dla iFrames z wideo, zapobiegając zniekształceniom.

## 4. Instrukcja uruchomienia projektu lokalnie

**Bezpośrednie otwarcie w przeglądarce**
1. Pobierz lub sklonuj folder z plikami projektu na swój komputer.
2. Wejdź do folderu projektu.
3. Kliknij dwukrotnie plik `index.html`. Projekt otworzy się i zadziała w Twojej domyślnej przeglądarce internetowej.
