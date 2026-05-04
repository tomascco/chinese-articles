"""
gerar_template_anki.py
Gera o arquivo hanzi-reader-template.apkg com o note type "Hanzi-Reader"
para ser importado no AnkiDroid uma única vez.

Uso:
    pip install genanki
    python gerar_template_anki.py

Saída:
    hanzi-reader-template.apkg (no diretório atual)

Após importar no AnkiDroid:
    1. Abra o deck "Chinês::Hanzi-Reader"
    2. Apague a nota dummy (significado = "exemplo, apague esta nota...")
    3. O note type fica instalado para uso com CSVs futuros.
"""

import genanki

# IDs fixos — não mude depois de gerar a primeira vez.
# O Anki usa esses IDs para identificar o model e o deck na sua coleção.
MODEL_ID = 1_718_000_001
DECK_ID  = 1_718_000_002

# ─────────────────────────────────────────────────────────────────────────────
# CSS — design editorial: papel cremoso, hanzi serif, acentos carmim
# ─────────────────────────────────────────────────────────────────────────────

SHARED_CSS = """
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;1,400&family=Noto+Serif+SC:wght@500;700&family=JetBrains+Mono:wght@400&display=swap');

.card {
  --paper:        #f5ede0;
  --paper-edge:   #ebe0cb;
  --ink:          #1a1612;
  --ink-soft:     #4a3f33;
  --ink-faint:    #8a7d6b;
  --rule:         #d9cdb4;
  --carmim:       #8b1a1a;
  --carmim-soft:  #b94545;
  --gold:         #a87932;

  font-family: 'Cormorant Garamond', 'Iowan Old Style', 'Palatino', 'Book Antiqua', Georgia, serif;
  background:
    radial-gradient(circle at 20% 10%, rgba(184,160,120,0.08) 0%, transparent 40%),
    radial-gradient(circle at 80% 90%, rgba(139,26,26,0.04) 0%, transparent 50%),
    var(--paper);
  color: var(--ink);
  padding: 32px 28px 28px;
  position: relative;
  max-width: 420px;
  margin: 12px auto;
  box-shadow:
    0 1px 2px rgba(0,0,0,0.1),
    0 8px 24px rgba(0,0,0,0.15),
    inset 0 0 60px rgba(139,90,40,0.04);
  border: 1px solid var(--paper-edge);
  text-align: left;
}

.card::before {
  content: '';
  position: absolute;
  inset: 0;
  pointer-events: none;
  opacity: 0.4;
  mix-blend-mode: multiply;
  background-image: url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='200' height='200'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='2' stitchTiles='stitch'/><feColorMatrix values='0 0 0 0 0.3 0 0 0 0 0.25 0 0 0 0 0.18 0 0 0 0.08 0'/></filter><rect width='100%25' height='100%25' filter='url(%23n)'/></svg>");
}

.card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-family: 'JetBrains Mono', 'SF Mono', Menlo, Consolas, monospace;
  font-size: 9px;
  letter-spacing: 0.25em;
  text-transform: uppercase;
  color: var(--ink-faint);
  border-bottom: 1px solid var(--rule);
  padding-bottom: 10px;
  margin-bottom: 32px;
  position: relative;
  z-index: 1;
}
.card-header .tipo { color: var(--carmim); }

.hanzi {
  font-family: 'Noto Serif SC', 'Songti SC', 'STSong', 'SimSun', serif;
  font-weight: 500;
  font-size: 124px;
  line-height: 1;
  color: var(--ink);
  text-align: center;
  margin: 0 0 8px;
  position: relative;
  z-index: 1;
  text-shadow: 0 1px 0 rgba(255,255,255,0.4);
}

.pinyin {
  font-style: italic;
  font-size: 28px;
  font-weight: 500;
  text-align: center;
  color: var(--carmim);
  margin: 28px 0 4px;
  letter-spacing: 0.02em;
  position: relative;
  z-index: 1;
}
.significado {
  font-size: 19px;
  font-weight: 400;
  text-align: center;
  color: var(--ink-soft);
  margin: 0 0 24px;
  position: relative;
  z-index: 1;
}

.rule-ornament {
  text-align: center;
  color: var(--ink-faint);
  font-size: 14px;
  margin: 20px 0 12px;
  position: relative;
  z-index: 1;
}

.label {
  font-family: 'JetBrains Mono', 'SF Mono', Menlo, Consolas, monospace;
  font-size: 9px;
  letter-spacing: 0.22em;
  text-transform: uppercase;
  color: var(--ink-faint);
  margin: 16px 0 6px;
  position: relative;
  z-index: 1;
}
.label::before {
  content: '— ';
  color: var(--carmim-soft);
}
.detalhe {
  font-size: 16px;
  line-height: 1.55;
  color: var(--ink);
  text-align: left;
  position: relative;
  z-index: 1;
}
.detalhe.notas {
  font-style: italic;
  color: var(--ink-soft);
  border-left: 2px solid var(--carmim-soft);
  padding-left: 12px;
}

.youglish {
  margin-top: 28px;
  text-align: center;
  position: relative;
  z-index: 1;
}
.youglish-link {
  display: inline-block;
  font-family: 'JetBrains Mono', 'SF Mono', Menlo, Consolas, monospace;
  font-size: 10px;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: var(--carmim);
  text-decoration: none;
  border: 1px solid var(--carmim);
  padding: 8px 16px 7px;
  background: transparent;
}

.producao-prompt {
  text-align: center;
  margin: 28px 0;
  position: relative;
  z-index: 1;
}
.producao-prompt .pinyin-big {
  font-style: italic;
  font-size: 56px;
  font-weight: 500;
  color: var(--carmim);
  line-height: 1.1;
  margin-bottom: 12px;
}
.producao-prompt .significado-big {
  font-size: 22px;
  color: var(--ink-soft);
}
.producao-hint {
  font-family: 'JetBrains Mono', 'SF Mono', Menlo, Consolas, monospace;
  font-size: 9px;
  letter-spacing: 0.22em;
  text-transform: uppercase;
  color: var(--ink-faint);
  text-align: center;
  margin-top: 28px;
  position: relative;
  z-index: 1;
}
.producao-hint::before, .producao-hint::after {
  content: '·';
  margin: 0 12px;
  color: var(--carmim-soft);
}

hr.separator {
  border: none;
  height: 1px;
  background: linear-gradient(to right, transparent, var(--rule), transparent);
  margin: 24px 0 8px;
  position: relative;
  z-index: 1;
}

.card.nightMode,
.card.night_mode {
  --paper:        #2d2420;
  --paper-edge:   #3d3428;
  --ink:          #f7f2e8;
  --ink-soft:     #d8c8a8;
  --ink-faint:    #a89878;
  --rule:         #5a5048;
  --carmim:       #ff8080;
  --carmim-soft:  #e88888;
  background: var(--paper);
  box-shadow: none;
  border-color: var(--paper-edge);
}

.card.nightMode::before,
.card.night_mode::before {
  display: none;
}

.card.nightMode .hanzi,
.card.night_mode .hanzi {
  color: #ffffff;
  text-shadow: none;
}

.card.nightMode .pinyin,
.card.night_mode .pinyin {
  color: #ff9e9e;
}

.card.nightMode .significado,
.card.night_mode .significado {
  color: #e8dcc4;
}

.card.nightMode .detalhe,
.card.night_mode .detalhe {
  color: #f0e8d8;
}

.card.nightMode .detalhe.notas,
.card.night_mode .detalhe.notas {
  color: #d8c8a8;
  border-color: #e88888;
}

.card.nightMode .youglish-link,
.card.night_mode .youglish-link {
  color: #ff9e9e;
  border-color: #ff9e9e;
}

.card.nightMode .producao-prompt .pinyin-big,
.card.night_mode .producao-prompt .pinyin-big {
  color: #ff9e9e;
}

.card.nightMode .producao-prompt .significado-big,
.card.night_mode .producao-prompt .significado-big {
  color: #e8dcc4;
}
"""

# ─────────────────────────────────────────────────────────────────────────────
# Templates HTML — Card 1 (Leitura) e Card 2 (Produção)
# ─────────────────────────────────────────────────────────────────────────────

LEITURA_FRONT = """
<div class="card-header">
  <span class="tipo">{{Tipo}}</span>
  <span>matéria {{Materia}}</span>
</div>
<div class="hanzi">{{Hanzi}}</div>
"""

LEITURA_BACK = """
<div class="card-header">
  <span class="tipo">{{Tipo}}</span>
  <span>matéria {{Materia}}</span>
</div>
<div class="hanzi">{{Hanzi}}</div>
<div class="pinyin">{{Pinyin}}</div>
<div class="significado">{{Significado}}</div>

<div class="rule-ornament">❦</div>

{{#Decomposicao}}
<div class="label">Decomposição</div>
<div class="detalhe">{{Decomposicao}}</div>
{{/Decomposicao}}

{{#Exemplos}}
<div class="label">Exemplos</div>
<div class="detalhe">{{Exemplos}}</div>
{{/Exemplos}}

{{#Notas}}
<div class="label">Notas</div>
<div class="detalhe notas">{{Notas}}</div>
{{/Notas}}

{{#YouGlish}}
<div class="youglish">
  <a href="{{YouGlish}}" class="youglish-link">▶ ouvir no contexto</a>
</div>
{{/YouGlish}}
"""

PRODUCAO_FRONT = """
<div class="card-header">
  <span class="tipo">{{Tipo}}</span>
  <span>matéria {{Materia}}</span>
</div>
<div class="producao-prompt">
  <div class="pinyin-big">{{Pinyin}}</div>
  <div class="significado-big">{{Significado}}</div>
</div>
<div class="producao-hint">como se escreve</div>
"""

PRODUCAO_BACK = """
<div class="card-header">
  <span class="tipo">{{Tipo}}</span>
  <span>matéria {{Materia}}</span>
</div>
<div class="producao-prompt">
  <div class="pinyin-big">{{Pinyin}}</div>
  <div class="significado-big">{{Significado}}</div>
</div>
<hr class="separator">
<div class="hanzi">{{Hanzi}}</div>

<div class="rule-ornament">❦</div>

{{#Decomposicao}}
<div class="label">Decomposição</div>
<div class="detalhe">{{Decomposicao}}</div>
{{/Decomposicao}}

{{#Exemplos}}
<div class="label">Exemplos</div>
<div class="detalhe">{{Exemplos}}</div>
{{/Exemplos}}

{{#Notas}}
<div class="label">Notas</div>
<div class="detalhe notas">{{Notas}}</div>
{{/Notas}}

{{#YouGlish}}
<div class="youglish">
  <a href="{{YouGlish}}" class="youglish-link">▶ ouvir no contexto</a>
</div>
{{/YouGlish}}
"""

# ─────────────────────────────────────────────────────────────────────────────
# Construção do model
# ─────────────────────────────────────────────────────────────────────────────

model = genanki.Model(
    MODEL_ID,
    'Hanzi-Reader',
    fields=[
        {'name': 'Hanzi'},
        {'name': 'Pinyin'},
        {'name': 'Significado'},
        {'name': 'Decomposicao'},
        {'name': 'Exemplos'},
        {'name': 'Tipo'},
        {'name': 'Materia'},
        {'name': 'YouGlish'},
        {'name': 'Notas'},
    ],
    templates=[
        {'name': 'Leitura',  'qfmt': LEITURA_FRONT,  'afmt': LEITURA_BACK},
        {'name': 'Producao', 'qfmt': PRODUCAO_FRONT, 'afmt': PRODUCAO_BACK},
    ],
    css=SHARED_CSS,
)

# ─────────────────────────────────────────────────────────────────────────────
# Deck + nota dummy (necessária para AnkiDroid aceitar a importação)
# ─────────────────────────────────────────────────────────────────────────────

deck = genanki.Deck(DECK_ID, 'Chinês::Hanzi-Reader')

dummy = genanki.Note(
    model=model,
    fields=[
        '范例',                                                # Hanzi
        'fànlì',                                               # Pinyin
        'exemplo (apague esta nota após importar)',            # Significado
        'Nota dummy para instalar o note type Hanzi-Reader.',  # Decomposicao
        '',                                                    # Exemplos
        'word',                                                # Tipo
        '000',                                                 # Materia
        '',                                                    # YouGlish
        'Pode apagar esta nota — o template fica instalado mesmo sem ela.',  # Notas
    ],
)
deck.add_note(dummy)

# ─────────────────────────────────────────────────────────────────────────────
# Exportar
# ─────────────────────────────────────────────────────────────────────────────

OUTPUT = 'hanzi-reader-template.apkg'
genanki.Package(deck).write_to_file(OUTPUT)
print(f"✓ {OUTPUT} gerado.")
print("  Importe no AnkiDroid via Menu → Importar → selecione este arquivo.")
print("  Após importar, apague a nota dummy. O note type fica instalado.")
