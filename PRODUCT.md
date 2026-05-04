# Product

## Register

brand

## Users

Tomás: engenheiro de software brasileiro, estudante de chinês autodidata (~1h/dia), ~10 hanzi reconhecidos no início. Gosta de taoismo, wuxia, comida, geografia, tecnologia, política chinesa. Não infantilizar. Pode ter humor seco.

Contexto de uso: leitura diária de matérias longas (~1500 palavras, ~15 min) em dispositivo mobile, frequentemente offline (metrô, café, antes de dormir). Precisa de tipografia confortável para leitura prolongada e modo escuro para uso noturno.

## Product Purpose

Site estático gerado a partir de matérias markdown sobre hanzi (caracteres chineses). Cada matéria combina:
- Campo semântico / família fonética / tema cultural
- 3 caracteres do dia com etimologia, pinyin, palavras comuns
- Costura cultural (história, filosofia, política)
- Deriva (aprofundamento tangencial)
- Cards para Anki

Sucesso = leitura confortável de 15min no celular, offline, com estética editorial que respeite a densidade intelectual do conteúdo.

## Brand Personality

- Editorial sofisticado (piauí encontra National Geographic)
- Voz com personalidade, ritmo cuidado, densidade informacional alta
- Concreto em vez de genérico
- Honestidade epistêmica
- Sem fórmula SEO, sem emojis, sem "espero que tenha gostado"

## Anti-references

- Blog genérico com chamadas pra ação no final
- Design SaaS-cream (gradientes, hero metrics, cards idênticas)
- Clichê "cultura oriental mística"
- Tipografia genérica de sistema sem cuidado tipográfico
- Side-stripe borders em citações
- Gradient text
- Glassmorphism decorativo

## Design Principles

1. **A tipografia é o design** — em conteúdo longo, a fonte e o ritmo visual fazem mais que qualquer decoração.
2. **Offline-first** — deve funcionar quase 100% offline (podem haver exceções onde for complicar muito o código), pois o uso principal é no metrô/café.
3. **Respeito pela atenção do leitor** — sem distrações, sem popups, sem tracking, sem chamadas para ação.
4. **Contraste cultural sutil** — o design deve evocar revista editorial ocidental com toques tipográficos chineses (hanzi serifados), não exotismo.
5. **Claro-escuro natural** — respeitar `prefers-color-scheme` sem forçar modos artificiais.

## Accessibility & Inclusion

- WCAG 2.1 AA como mínimo
- Contraste de texto em ambos os modos
- Fonte base 18px mínimo para leitura mobile
- Respeito a `prefers-reduced-motion`
- Hanzi devem ser distinguíveis mesmo em tamanhos pequenos (fonte serifada de qualidade)
