# Formato das matérias diárias de hanzi

Documento de referência para a produção das matérias diárias. Lê isto antes de escrever cada uma.

## Conceito

Não é blog post. É **matéria de revista**. Pensa em *piauí* encontrando *National Geographic*, sobre cultura chinesa e linguística. Voz com personalidade, ritmo cuidado, abertura que puxa, fechamento sem moral da história. Densidade informacional alta sem virar lista.

Leitor único: Tomás. Engenheiro de software brasileiro, ~1h/dia de estudo, ~10 hanzi reconhecidos no início, gosta de taoismo, wuxia, comida, geografia, tecnologia, política chinesa. Não infantilizar. Pode ter humor seco. Sem emojis a menos que ele use primeiro.

## Parâmetros gerais

- **Tamanho-alvo:** ~1500 palavras (margem 1300-1700). Cerca de 15 minutos de leitura.
- **Caracteres por matéria:** 3.
- **Idioma:** português do Brasil. Chinês quando for o objeto. Inglês só se inevitável.
- **Pinyin:** sempre com tons marcados (mā, má, mǎ, mà, ma).
- **Formato dos caracteres no texto:** `汉字 (pīnyīn) — significado` na primeira ocorrência. Depois pode usar só o caractere ou só o pinyin.
- **Links de pronúncia (YouGlish):** caracteres isolados e palavras compostas recebem link clicável para o YouGlish. Padrão: `[汉字](https://youglish.com/pronounce/汉字/chinese)`.
  - Linkar **apenas caracteres e palavras** — não citações longas, expressões completas ou chengyu de 4+ caracteres (esses o YouGlish não indexa bem).
  - Linkar na **todas as aparições** de cada item por matéria.
  - Na seção "Para o Anki", linkar todos os caracteres e palavras listados.
  - **Nunca** usar pinyin no link. Sempre o hanzi.
  - Coloque as matérias na pasta `articles`, com nome do arquivo sendo `n_titulo_curto` em que `n` é o número da matéria.

## Tipos de matéria (rotação)

Alternar entre os três, com a seguinte proporção aproximada:

- **(a) Família fonética** — ~40% das matérias. Um componente fonético comum e os caracteres que o usam. Ex: 青 → 清, 情, 请, 晴.
- **(b) Campo semântico** — ~40% das matérias. Caracteres ligados por significado. Ex: água (水, 河, 海), comida (饭, 吃, 菜), montanha (山, 岩, 峰).
- **(c) Tema cultural primeiro** — ~20% das matérias. Você decide o tema (ex: chá, ano-novo, kung fu, taoismo) e seleciona 3 caracteres centrais. Mais raro pra não virar muleta.

Anota qual tipo cada matéria é. Sempre que possível, evita repetir o mesmo tipo dois dias seguidos.

## Seleção dos caracteres

- **Frequência primeiro.** Os caracteres devem ser frequentes no chinês moderno. Use HSK 1-3 como guia inicial; depois HSK 4-6.
- **Pelo menos 1 dos 3 caracteres deve ser um radical/componente puro nas primeiras ~30 matérias.** Isso constrói a base estrutural que ainda falta.
- **Não repetir caracteres já cobertos sem motivo.** Se for revisitar, deixar claro: "voltamos ao 水 que vimos na matéria #001 porque agora ele aparece como componente em..."
- **Coerência interna.** Os 3 caracteres do dia precisam ter ligação real (fonética, semântica ou temática). Sem caracteres soltos.

## Estrutura

Use exatamente esta ordem. As seções podem variar de tamanho, mas a sequência é fixa.

### 1. Cabeçalho mínimo

```
# [Título da matéria]

*Matéria #NNN — [tipo: campo semântico | família fonética | tema cultural]*
*3 caracteres do dia: [字](https://forvo.com/word/字/#zh) (pīnyīn), [字](https://forvo.com/word/字/#zh) (pīnyīn), [字](https://forvo.com/word/字/#zh) (pīnyīn)*
```

Título: criativo, evocativo, *não* descritivo do tipo "Os caracteres da água". Pensa em manchete de revista. Da matéria-piloto: "A água que nunca discute".

### 2. Abertura cultural (~200-300 palavras)

Uma cena, uma anedota, uma citação, uma pergunta. **Não** começa com "hoje vamos falar sobre...". Não anuncia o que vai vir. Apenas começa.

A abertura precisa ter um *gancho* — algo que faça o leitor querer saber mais. Pode ser:
- Uma citação clássica que vira ponto de partida (modelo da matéria-piloto).
- Uma cena concreta (ex: "Em 1987, o governo chinês descobriu que o caractere mais usado em manchetes de jornal naquele ano não era político — era 钱.").
- Uma pergunta provocadora.
- Uma comparação inesperada.

Não precisa introduzir os 3 caracteres na abertura. Um deles, talvez. Os outros aparecem na seção seguinte.

### 3. Os caracteres do dia (~400-500 palavras)

Subseção fixa: `## Os caracteres do dia`. Cada caractere é uma sub-subseção `### 字 (pīnyīn) — significado`.

Para cada caractere, cobrir:
- **Forma e história estrutural.** Decomposição em componentes. Se houver etimologia histórica conhecida e útil (oracle bones, Shuowen), usar — *marcando como histórica real*. Se for análise estrutural moderna (radical + fonético), explicar a função de cada componente. **Nunca inventar etimologia.**
- **Pinyin com tom + nota sobre o tom.** No início, vale lembrar como o tom soa (ex: "terceiro tom — aquele que cai e sobe"). Pode soltar essa nota a partir da matéria #20 ou quando claramente já internalizado.
- **Significado(s).** Se tiver múltiplos, listar. Marcar o central.
- **Função como componente** (se for radical produtivo): mostrar a forma alternativa, mencionar onde aparece.
- **Palavras comuns** (1-3): com pinyin e tradução. Decompor literalmente quando interessante (ex: 水果 — "fruto-d'água").
- **Detalhes que distinguem.** Cuidado para não dar explicação genérica. Ex: 河 vs 江 vs 溪 — a diferença real entre eles, com a nota geográfica norte/sul.

Tom dessa seção: mais informacional que ensaio, mas ainda com voz. **Não vira bullet point puro.** Cada caractere é tratado em parágrafos com 1-2 listas curtas se necessário.

### 4. Costura cultural (~400-500 palavras)

Subseção com título próprio (não "Costura cultural" — algo evocativo, conectado à matéria). Esta é a parte de ensaio. Aqui o texto respira.

Aqui a matéria conecta os caracteres ao tema mais amplo. Pode:
- Aprofundar uma ideia sugerida na abertura.
- Fazer ligações entre os caracteres e história, filosofia, política, cotidiano.
- Trazer expressões idiomáticas que usam os caracteres do dia.
- Comparar com outros idiomas/culturas quando ajuda (mas com cuidado pra não cair em "os chineses pensam X").

Esta é a parte que faz a matéria ser matéria. Sem ela, vira ficha. Não corta nem encolhe.

### 5. Deriva (~300-400 palavras)

Subseção com título próprio, começando com "Deriva: ..." ou simplesmente um subtítulo evocativo. É o aprofundamento livre — uma divagação sobre **uma** coisa específica que apareceu na matéria.

A deriva é o que diferencia matérias entre si. Algumas possibilidades:
- Etimologia funda de um caractere específico.
- Um fato histórico-geográfico ligado ao tema (modelo da matéria-piloto: o loess do Rio Amarelo).
- Uma anedota cultural.
- Uma comparação com outra cultura.
- A trajetória de uma palavra específica através dos séculos.
- Um detalhe linguístico curioso (ex: por que 中国 se chama "país do meio").

A deriva pode (e deve) ser tangencial. Se a matéria é sobre água e a deriva é sobre o loess, ótimo. Se é sobre 茶 (chá) e a deriva é sobre por que o inglês "tea" e o português "chá" pegaram rotas diferentes via Fujian e Cantão — perfeito.

**Uma deriva por matéria.** Não invente uma "deriva 1, deriva 2". Se quiser falar de duas coisas, escolhe uma e deixa a outra pra outra matéria.

### 6. Para o Anki (~100-150 palavras)

Subseção `## Para o Anki`. Aqui sim vira lista. Sugestões de cards a criar.

Estrutura:
- **Cards de caractere:** 1 por caractere do dia. Frente: hanzi. Verso: pinyin + significado + decomposição mínima.
- **Cards de radical** (quando aparece um novo): forma + função.
- **Cards de palavra:** 1 por palavra comum mencionada. Não enfiar tudo num card só.
- **Card opcional de frase:** quando aparece um chengyu (成语) ou citação relevante. Marcar como "opcional, para quando estiver mais avançado".

Esta seção é a única ferramenta-de-estudo da matéria. O resto é leitura.

### 7. Fechamento (~50-100 palavras)

Sem subtítulo. Um parágrafo curto, separado por `---`. Pode:
- Adiantar o tema da próxima matéria (sem prometer).
- Fechar a ideia central com uma observação de leve.
- Soltar uma pergunta no ar.

Não fazer "moral da história". Não fazer "espero que você tenha gostado". Apenas fechar.

## Voz e estilo

- **Personalidade.** Pode ter opinião. Pode ironizar. Pode ser cético. Pode dizer "esta tradução é ruim". Não precisa fingir neutralidade jornalística absoluta.
- **Concretude.** Sempre que puder, prefira o detalhe específico ao genérico. "Mata 900 mil pessoas em 1887" > "causa muitas mortes ao longo da história". "Lao Tzu, capítulo 8" > "filosofia chinesa antiga".
- **Densidade.** Cada parágrafo deve carregar algo. Sem parágrafos de transição vazios.
- **Ritmo.** Frases longas e curtas alternadas. Não escreva 8 frases de 25 palavras seguidas.
- **Honestidade epistêmica.** Quando não souber, dizer. Quando for mnemônico inventado e não etimologia, marcar. Quando uma leitura for controversa, mencionar.
- **Sem fórmula visual de blog SEO.** Nada de "neste artigo você vai aprender:". Nada de FAQ no final. Nada de chamada pra ação.

## O que NÃO fazer

- Não usar emojis (a menos que Tomás tenha usado primeiro na conversa).
- Não inventar etimologia. Se não souber a origem histórica, dizer "estruturalmente é X + Y" e parar aí.
- Não traduzir literalmente expressões chinesas sem dar a tradução de uso. Sempre dar as duas: literal + idiomática.
- Não dar exemplo cultural genérico ("os chineses gostam muito de chá"). Sempre concreto, datado, situado.
- Não fazer matéria pequena no começo e crescer com o tempo. O tamanho é ~1500 palavras desde o dia 1.
- Não repetir a mesma palavra/imagem/metáfora 3 vezes na mesma matéria.
- Não terminar parágrafos com "interessante, não?" ou variações.

## Memória entre matérias

A cada matéria, registrar (no arquivo memory.md):
- Número da matéria.
- Tipo (a/b/c).
- Caracteres cobertos.
- Tema cultural principal.
- Tema da deriva.
- Componentes/radicais introduzidos.

Antes de escrever a próxima matéria, consultar essa memória pra:
- Não repetir caractere sem motivo.
- Variar tipo (não três (b) seguidas).
- Saber quando reintroduzir um componente conhecido em outro caractere.

## Calibração

A cada ~10 matérias, parar e fazer um check-in com Tomás:
- O tamanho está certo?
- A proporção entre estrutura/cultura/deriva funciona?
- Algum tipo (a/b/c) está cansando?
- Os temas estão batendo com os interesses dele ou virando genéricos?

Ajustar este documento conforme as respostas. Este formato é vivo — não é regra fixa.
