from pathlib import Path
import json
root=Path(__file__).resolve().parents[1]
data=json.loads((root/'data/news.json').read_text())
html=(root/'scripts/template.html').read_text().replace('/*__DATA__*/',json.dumps(data,ensure_ascii=False).replace('<','\\u003c'))
(root/'index.html').write_text(html)
