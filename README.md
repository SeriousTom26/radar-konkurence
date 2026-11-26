# Radar konkurence

Veřejný statický dashboard osmi společností; filtry, profily firem, detail novinek a archiv týdenních reportů. Výchozí dataset má 14 položek, část tvoří existující funkce, nikoli aktuální novinky.

## Aktivace
- Settings → Pages → Build and deployment → Source → GitHub Actions.
- Actions → Týdenní monitoring konkurence → Run workflow. Plán: pondělí 06:30 UTC (07:30 v zimě, 08:30 v létě).
- Actions → Publish dashboard → Run workflow, pokud nasazení neproběhlo automaticky.
- Volitelně repository secret OPENAI_API_KEY pro české souhrny (placené API). Bez klíče se zobrazuje originální název a odkaz na zdroj.
- Screenshoty veřejných stránek jsou ve veřejném repozitáři vypnuté; až po ověření práv, podmínek a soukromí lze nastavit repository variable CAPTURE_PUBLIC_SCREENSHOTS=true. Žádné obcházení geografických omezení, CAPTCHA nebo přihlašování.

## Metodika
Sběr sleduje vybrané veřejné stránky, nápovědy a odkazy. První běh vytváří inventuru; následné identifikují změny a nové články. Výsledky jsou kandidáti k ověření, nikoli potvrzené produktové novinky. Nejde o kompletní vyhledávání internetu; funkce za přihlášením nemusí být zachyceny. Kategorie jsou heuristické. Zpráva obsahuje chyby dostupnosti. Prázdný výsledek neznamená, že firmy nic nevydaly. GitHub může plánované běhy zpozdit či deaktivovat při neaktivitě.

Lokální běh: pip install -r requirements.txt; python scripts/monitor.py; python scripts/build.py. Pro screenshoty nejprve nainstalujte Chromium přes Playwright.
