# Radar konkurence

Veřejný statický dashboard osmi společností; filtry, profily firem, detail novinek a archiv týdenních reportů. Výchozí dataset má 14 položek, část tvoří existující funkce, nikoli aktuální novinky.

## Aktivace
- Settings → Pages → Build and deployment → Source → GitHub Actions.
- Actions → Týdenní monitoring konkurence → Run workflow. Plán: pondělí 06:30 UTC (07:30 v zimě, 08:30 v létě).
- Actions → Publish dashboard → Run workflow, pokud nasazení neproběhlo automaticky.
- Volitelně repository secret OPENAI_API_KEY pro české souhrny (placené API). Bez klíče se zobrazuje originální název a odkaz na zdroj.
- Verze 2: skript enrich.py doplňuje odkazy na originální obrázky a videa, metadata a strukturovaný detail. Výřezy veřejných článků jsou omezeny na vybrané oficiální domény; nastavte repository variable CAPTURE_PUBLIC_SCREENSHOTS=false, pokud jejich publikace není povolena. Respektujte podmínky zdroje a práva třetích stran. Žádné obcházení geografických omezení, CAPTCHA nebo přihlašování.

## Metodika
Sběr sleduje vybrané veřejné stránky, nápovědy a odkazy. První běh vytváří inventuru; následné identifikují změny a nové články. Výsledky jsou kandidáti k ověření, nikoli potvrzené produktové novinky. Nejde o kompletní vyhledávání internetu; funkce za přihlášením nemusí být zachyceny. Kategorie jsou heuristické. Zpráva obsahuje chyby dostupnosti. Prázdný výsledek neznamená, že firmy nic nevydaly. GitHub může plánované běhy zpozdit či deaktivovat při neaktivitě.

Lokální běh: pip install -r requirements.txt; python scripts/monitor.py; python scripts/build.py. Pro screenshoty nejprve nainstalujte Chromium přes Playwright.

## Rozšířený detail (v2)
Po týdenním sběru běží `python scripts/enrich.py`, který doplní až 30 dosud neobohacených položek včetně staršího archivu. Bez OPENAI_API_KEY zůstává český původní popis a krátký výňatek ze zdroje; s klíčem vzniká strukturovaný český souhrn. Obrázky článků se zobrazují z původních URL a mohou být nedostupné kvůli omezením zdroje. Neověřená změna není vydání produktu. Sběr není kompletní rešerší webu.
