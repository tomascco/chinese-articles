# Instruções: gerar CSV de cards de uma matéria

Use estas instruções para gerar o CSV de cards Anki ao final de cada matéria nova.

## ⚠️ AVISO CRÍTICO: escaping e campos vazios

O separador é **ponto e vírgula (`;`)**. Isso significa que **qualquer `;` ou `,` dentro de um campo quebra o CSV** se não estiver entre aspas.

### Quando ASPAS são obrigatórias

Aspas duplas (`"`) são obrigatórias se o campo contiver:
- **ponto e vírgula** (`;`)
- **vírgula** (`,`)
- **aspas duplas** (`"`) → escape como `""` (duas aspas)

**Exemplo de campo que PRECISA de aspas:**
```csv
"Pictograma: pessoa de braços abertos, gesto de ""era deste tamanho"""
```
A vírgula depois de "abertos" e as aspas internas exigem aspas externas. No CSV, aspas internas viram duas aspas (`""`).

**Exemplo de campo que NÃO precisa de aspas:**
```
água
```
Sem vírgula nem ponto-e-vírgula, sem aspas.

### Campos que podem ficar vazios

| Campo | Quando pode estar vazio |
|-------|------------------------|
| **Hanzi** | NUNCA |
| **Pinyin** | NUNCA |
| **Significado** | NUNCA |
| **Decomposicao** | NUNCA (pode ser breve, mas sempre preencha) |
| **Exemplos** | ✅ SEMPRE vazio para cards do tipo `word` |
| **Tipo** | NUNCA |
| **Materia** | NUNCA |
| **YouGlish** | NUNCA |
| **Notas** | ✅ Pode estar vazio para qualquer tipo |

Um campo vazio aparece como `;;` (dois delimitadores seguidos) ou `;` no final da linha. **Isso é correto.** O erro é quando uma linha tem **mais ou menos de 9 campos** — isso indica escaping quebrado.

### Como detectar erro de escaping

Se você validar o CSV e uma linha tiver **10 campos** em vez de 9, é porque um ponto-e-vírgula dentro de um campo não foi escapado com aspas. Corrija envolvendo o campo inteiro em `"..."`.

## Formato

- **Separador:** ponto e vírgula (`;`)
- **Encoding:** UTF-8
- **Sem cabeçalho** (a primeira linha já é dado)
- **Nome do arquivo:** `NNN-tema.csv` (ex: `002-qing.csv`)

## Colunas (nesta ordem exata)

| # | Campo | Conteúdo |
|---|-------|----------|
| 1 | Hanzi | O caractere ou palavra em chinês |
| 2 | Pinyin | Pinyin com tons marcados (shuǐ, não shui3) |
| 3 | Significado | Tradução em pt-br, concisa |
| 4 | Decomposicao | Componentes / etimologia (radical + fonético, ou pictograma) |
| 5 | Exemplos | 1-2 palavras onde aparece, com pinyin e tradução |
| 6 | Tipo | `radical`, `character`, `word` ou `phrase` |
| 7 | Materia | Número da matéria com 3 dígitos (`001`, `042`) |
| 8 | YouGlish | `https://youglish.com/pronounce/HANZI/chinese` |
| 9 | Notas | Observações livres — pode ficar vazio |

## Quais cards gerar

Para cada matéria, gere uma linha por:

- **Cada um dos 3 caracteres do dia** (Tipo: `character` ou `radical`)
- **Cada palavra/composto** mencionado nos "Exemplos" das seções dos caracteres (Tipo: `word`)
- **Não gerar** cards para: chengyu de 4+ caracteres, citações clássicas, expressões longas — esses ficam só na matéria, não no Anki

Total típico por matéria: **6-8 cards** (3 caracteres + 3-5 palavras).

## Regras de conteúdo por campo

**Decomposicao:** se for caractere composto, formato `氵 (radical-significado) + 可 kě (fonético)`. Se for pictograma puro, descreva a imagem original. Se for palavra composta, mostre os caracteres e o sentido literal: `大 (grande) + 海 (mar)`.

**Exemplos:** só para cards do tipo `character`/`radical`. Para cards do tipo `word`, deixe vazio. Formato: `水果 (shuǐguǒ) — fruta; 喝水 (hē shuǐ) — beber água`.

**Notas:** use para coisas que não cabem nos outros campos: tom + descrição, distinções (`Diferente de 江 que é rio do sul`), classifier, registro. Pode ficar vazio. Para cards do tipo `word`, normalmente fica vazio.

## Exemplo (matéria #NNN — água)

```
水;shuǐ;água;Pictograma: linha vertical (corrente) + traços diagonais (respingo). Forma comprimida como componente: 氵 (três pontinhos à esquerda);水果 (shuǐguǒ) — fruta; 喝水 (hē shuǐ) — beber água;radical;001;https://youglish.com/pronounce/水/chinese;Tom 3 (cai e sobe). Como radical, vira 氵 à esquerda de outros caracteres.
河;hé;rio (especialmente rios do norte);氵(água, semântico) + 可 kě (fonético — a leitura mudou com o tempo);河流 (héliú) — rio, corrente fluvial; 黄河 (Huánghé) — Rio Amarelo;character;001;https://youglish.com/pronounce/河/chinese;Tom 2 (sobe, como pergunta). Diferente de 江 (jiāng), que é rio do sul.
水果;shuǐguǒ;fruta;水 (água) + 果 (fruto) — literalmente "fruto-d'água";;word;001;https://youglish.com/pronounce/水果/chinese;
```

Note como os campos vazios aparecem como `;;` consecutivos.

## Output esperado

Bloco de código com o CSV pronto pra copiar e salvar como arquivo. Sem comentários, sem cabeçalho, sem linhas extras.
