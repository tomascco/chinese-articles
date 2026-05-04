#!/usr/bin/env python3
"""
Gera um site estático a partir dos artigos em articles/.
Uso: python3 build.py
"""

import markdown
import re
from pathlib import Path
from html import escape

ROOT = Path(__file__).parent
ARTICLES_DIR = ROOT / "articles"
OUTPUT_DIR = ROOT / "site"

# Configurações do Markdown
md = markdown.Markdown(extensions=["extra", "toc", "tables", "fenced_code"])


CSS_CORE = """
/* Reset */
*, *::before, *::after {
  box-sizing: border-box;
  margin: 0;
}

html {
  height: 100%;
  font-size: 112.5%; /* 18px base */
  -webkit-text-size-adjust: 100%;
  scroll-behavior: smooth;
}

@media (prefers-reduced-motion: reduce) {
  html {
    scroll-behavior: auto;
  }
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }
}

body {
  min-height: 100vh;
  min-height: 100dvh;
  font-family: var(--font-body);
  background: var(--bg);
  color: var(--text);
  line-height: 1.7;
  padding: 0;
}

/* Fade-in sutil no carregamento */
@keyframes fadeIn {
  from { opacity: 0; transform: translateY(8px); }
  to   { opacity: 1; transform: translateY(0); }
}

article {
  animation: fadeIn 0.5s var(--ease-out, cubic-bezier(0.25, 1, 0.5, 1)) both;
}

/* Skip link — acessibilidade */
.skip-link {
  position: absolute;
  top: -3rem;
  left: 1rem;
  z-index: 100;
  padding: 0.5rem 1rem;
  background: var(--surface);
  color: var(--accent);
  font-family: var(--font-ui);
  font-size: 0.85rem;
  text-decoration: none;
  border-radius: var(--radius);
  border: 1.5px solid var(--border);
  transition: top 0.15s ease;
}

.skip-link:focus {
  top: 1rem;
}

/* Layout */
.page {
  max-width: var(--line-length);
  margin: 0 auto;
  padding: 1.25rem;
}

@media (min-width: 640px) {
  .page {
    padding: 2rem 1.5rem 3rem;
  }
}

/* Tipografia — scale com contraste */
h1, h2, h3, h4 {
  font-family: var(--font-ui);
  font-weight: 650;
  line-height: 1.2;
  color: var(--text);
  letter-spacing: -0.02em;
}

h1 {
  font-size: 2.1rem;
  margin-top: 0.5rem;
  margin-bottom: 0.75rem;
  font-weight: 700;
}

/* Linha decorativa sutil antes do título principal — evoca divisória editorial */
h1::before {
  content: "";
  display: block;
  width: 2.5rem;
  height: 2.5px;
  background: var(--accent-soft);
  border-radius: 2px;
  margin-bottom: 0.6rem;
}

@media (min-width: 640px) {
  h1::before {
    width: 3rem;
    height: 3px;
  }
}

h2 {
  font-size: 1.4rem;
  margin-top: 2.4rem;
  margin-bottom: 0.8rem;
  padding-bottom: 0.35rem;
  border-bottom: 1.5px solid var(--rule);
  font-weight: 700;
}

h3 {
  font-size: 1.15rem;
  margin-top: 2rem;
  margin-bottom: 0.6rem;
  color: var(--text-muted);
  font-weight: 600;
}

h4 {
  font-size: 1rem;
  margin-top: 1.4rem;
  margin-bottom: 0.5rem;
}

p {
  margin-bottom: 1rem;
  hyphens: auto;
  overflow-wrap: break-word;
}

/* Metadados da matéria */
.meta {
  font-family: var(--font-ui);
  font-size: 0.8rem;
  color: var(--text-muted);
  line-height: 1.5;
  margin-bottom: 1.5rem;
}

.meta em {
  font-style: normal;
  display: block;
}

/* Links — editorial: cor de acento sem sublinhado, revela no hover/focus */
a {
  color: var(--accent);
  text-decoration: none;
  transition: color 0.2s ease, text-decoration-color 0.2s ease, background 0.2s ease;
}

a:hover {
  text-decoration: underline;
  text-decoration-thickness: 1.5px;
  text-underline-offset: 0.25em;
  text-decoration-color: var(--accent-soft);
}

a:focus-visible {
  outline: 2.5px solid var(--accent-soft);
  outline-offset: 0.15em;
  border-radius: 0.15em;
}

/* Links no cabeçalho de meta (hanzi) — pill sutil */
.meta a {
  display: inline-block;
  padding: 0.1em 0.35em;
  border-radius: 0.3em;
  background: transparent;
  transition: background 0.2s ease, transform 0.15s ease;
}

.meta a:hover {
  background: var(--surface);
  text-decoration: none;
  transform: translateY(-1px);
}

.meta a:active {
  transform: translateY(0);
}

/* Caracteres chineses inline (code e strong) */
code {
  font-family: var(--font-mono);
  font-size: 0.95em;
  background: var(--surface);
  padding: 0.15em 0.35em;
  border-radius: 0.25rem;
  color: var(--accent);
}

/* Hanzi — reforço tipográfico */
:lang(zh), [lang="zh"] {
  font-family: "Noto Serif SC", "Source Han Serif SC", "Songti SC", "STSong", serif;
}

/* Listas */
ul, ol {
  margin-bottom: 1.2rem;
  padding-left: 1.4rem;
}

li {
  margin-bottom: 0.4rem;
  padding-left: 0.2rem;
}

/* Citações em bloco — borda sutil completa + fundo */
blockquote {
  margin: 1.5rem 0;
  padding: 1rem 1.2rem;
  background: var(--surface);
  border-radius: var(--radius);
  border: 1px solid var(--border);
  color: var(--text-muted);
  font-style: italic;
  transition: border-color 0.2s ease, box-shadow 0.2s ease;
}

blockquote:hover {
  border-color: var(--accent-soft);
  box-shadow: 0 2px 8px var(--shadow);
}

blockquote p:last-child {
  margin-bottom: 0;
}

/* Separador temático */
hr {
  border: none;
  height: 1.5px;
  background: var(--rule);
  margin: 2rem 0;
}

/* Tabelas */
table {
  width: 100%;
  border-collapse: collapse;
  margin-bottom: 1.5rem;
  font-size: 0.9rem;
  font-family: var(--font-ui);
}

th, td {
  padding: 0.5rem 0.6rem;
  text-align: left;
  border-bottom: 1px solid var(--border);
}

th {
  font-weight: 600;
  color: var(--text-muted);
  font-size: 0.8rem;
  text-transform: uppercase;
  letter-spacing: 0.04em;
}

/* Imagem */
img {
  max-width: 100%;
  height: auto;
  border-radius: var(--radius);
  display: block;
  margin: 1.5rem auto;
}

/* Navegação / header */
.site-header {
  font-family: var(--font-ui);
  margin-bottom: 2rem;
  padding-bottom: 1rem;
  border-bottom: 1.5px solid var(--rule);
  display: flex;
  align-items: baseline;
  justify-content: space-between;
  gap: 1rem;
  flex-wrap: wrap;
}

.site-header a {
  text-decoration: none;
  color: var(--text);
  font-weight: 700;
  font-size: 1rem;
}

.site-header span {
  font-size: 0.75rem;
  color: var(--text-muted);
  text-transform: uppercase;
  letter-spacing: 0.06em;
}

/* Lista de artigos (index) — touch targets ≥ 44px */
.article-list {
  list-style: none;
  padding: 0;
  margin: 0;
}

.article-list li {
  padding: 0;
  margin-bottom: 0;
}

.article-list a {
  display: block;
  text-decoration: none;
  color: var(--text);
  padding: 1.125rem 0.75rem;
  border-bottom: 1px solid var(--border);
  transition: background 0.15s ease;
  min-height: 44px;
}

.article-list a:hover {
  background: var(--surface);
  border-radius: var(--radius);
}

.article-list .item-title {
  font-family: var(--font-ui);
  font-weight: 650;
  font-size: 1.05rem;
  line-height: 1.3;
  margin-bottom: 0.25rem;
}

.article-list .item-meta {
  font-size: 0.78rem;
  color: var(--text-muted);
}

/* Rodapé */
.site-footer {
  margin-top: 3rem;
  padding-top: 1.5rem;
  border-top: 1.5px solid var(--rule);
  font-family: var(--font-ui);
  font-size: 0.75rem;
  color: var(--text-muted);
  text-align: center;
}

/* TOC automática */
.toc {
  font-family: var(--font-ui);
  font-size: 0.85rem;
  background: var(--surface);
  padding: 1rem 1.2rem;
  border-radius: var(--radius);
  margin-bottom: 2rem;
}

.toc ul {
  list-style: none;
  padding-left: 0;
  margin: 0;
}

.toc li {
  margin: 0.35rem 0;
}

.toc a {
  text-decoration: none;
  color: var(--text-muted);
}

.toc a:hover {
  color: var(--accent);
}
""".strip()

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="description" content="{description}">
<meta name="theme-color" content="#f5f0e8" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#1a1f2e" media="(prefers-color-scheme: dark)">
<title>{title}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Noto+Serif+SC:wght@400;600;700&family=Source+Serif+4:ital,opsz,wght@0,8..60,400;0,8..60,600;1,8..60,400&display=swap" rel="stylesheet">
<style>
{css}
</style>
</head>
<body>
<a href="#conteudo" class="skip-link">Pular para conteúdo</a>
<div class="page">
{header}
<main id="conteudo">
{content}
</main>
{footer}
</div>
</body>
</html>
"""


def extract_title_and_meta(text: str):
    lines = text.splitlines()
    title = "Matéria"
    meta_lines = []
    body_start = 0

    for i, line in enumerate(lines):
        if line.startswith("# "):
            title = line.lstrip("# ").strip()
            body_start = i + 1
            break

    # Coleta metadados logo após o título (linhas em itálico)
    meta_end = body_start
    for j in range(body_start, min(body_start + 6, len(lines))):
        l = lines[j].strip()
        if l.startswith("*") and l.endswith("*"):
            meta_lines.append(l.strip("*"))
            meta_end = j + 1
        elif l == "":
            meta_end = j + 1
            continue
        else:
            break

    meta_raw = "\n".join(meta_lines)
    # Converte markdown inline nos metadados
    md_meta = markdown.Markdown(extensions=[])
    meta_html = md_meta.convert(meta_raw)
    # remove parágrafos envolventes para manter inline
    meta_html = meta_html.replace("<p>", "").replace("</p>", "").strip()

    body = "\n".join(lines[meta_end:])
    return title, meta_html, body


def wrap_cjk(html: str) -> str:
    """
    Envolve runs de caracteres CJK (Han) em <span lang="zh"> para acessibilidade.
    Opera apenas em nós de texto, preservando tags HTML intactas.
    """
    CJK_RE = re.compile(r"[\u4e00-\u9fff\u3400-\u4dbf\uf900-\ufaff]+")
    # Divide alternando entre tags e texto
    parts = re.split(r"(<[^>]+>)", html)
    result = []
    for i, part in enumerate(parts):
        if i % 2 == 1:
            # É uma tag — mantém intacta
            result.append(part)
        else:
            # É texto — envolve runs CJK
            result.append(CJK_RE.sub(r'<span lang="zh">\g<0></span>', part))
    return "".join(result)


def build():
    OUTPUT_DIR.mkdir(exist_ok=True)

    full_css = f""":root {{
  /* Paleta quente-editorial: evoca papel artesanal e selo de tinta */
  --bg: oklch(96.5% 0.012 75);
  --surface: oklch(93% 0.016 75);
  --text: oklch(24% 0.025 75);
  --text-muted: oklch(45% 0.018 75);
  --accent: oklch(42% 0.18 28);
  --accent-soft: oklch(62% 0.14 28);
  --border: oklch(84% 0.014 75);
  --rule: oklch(78% 0.018 75);
  --shadow: oklch(58% 0.012 75 / 0.12);
  --font-body: "Source Serif 4", "Noto Serif SC", Georgia, serif;
  --font-ui: system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
  --font-mono: "SF Mono", Monaco, "Cascadia Code", monospace;
  --line-length: 42rem;
  --radius: 0.5rem;
}}

@media (prefers-color-scheme: dark) {{
  :root {{
    /* Modo escuro: azul-petróleo profundo, mantendo acento terroso */
    --bg: oklch(19% 0.025 255);
    --surface: oklch(24% 0.03 255);
    --text: oklch(90% 0.012 80);
    --text-muted: oklch(68% 0.018 75);
    --accent: oklch(66% 0.15 30);
    --accent-soft: oklch(76% 0.11 30);
    --border: oklch(34% 0.025 255);
    --rule: oklch(30% 0.022 255);
    --shadow: oklch(10% 0.015 255 / 0.35);
  }}
}}

{CSS_CORE}"""

    articles = []
    for path in sorted(ARTICLES_DIR.glob("*.md")):
        raw = path.read_text(encoding="utf-8")
        title, meta_html, body = extract_title_and_meta(raw)

        # Converte markdown para HTML
        md.reset()
        html_body = md.convert(body)

        # Envolve hanzi em <span lang="zh">
        html_body = wrap_cjk(html_body)
        meta_html = wrap_cjk(meta_html)

        # Tenta extrair número do arquivo para ordenação
        m = re.match(r"^(\d+)", path.stem)
        num = int(m.group(1)) if m else 999

        # Gera página individual
        header = f'<nav class="site-header"><a href="index.html">← Índice</a><span>Matéria #{num:03d}</span></nav>'
        meta_block = f'<p class="meta"><em>{meta_html}</em></p>' if meta_html else ""
        footer = '<footer class="site-footer">Gerado para leitura offline</footer>'

        desc = f"Matéria de hanzi: {re.sub(r'<[^>]+>', '', meta_html).replace(chr(10), ' ')[:120]}..."
        article_html = HTML_TEMPLATE.format(
            title=f"{title} — Hanzi",
            description=desc,
            css=full_css,
            header=header,
            content=f'<article>\n<h1>{escape(title)}</h1>\n{meta_block}\n{html_body}</article>',
            footer=footer,
        )

        out_path = OUTPUT_DIR / f"{path.stem}.html"
        out_path.write_text(article_html, encoding="utf-8")
        articles.append((num, title, meta_html, f"{path.stem}.html"))

    # Gera índice
    list_items = ""
    for num, title, meta_html, href in articles:
        meta_clean = re.sub(r"<[^>]+>", "", meta_html).replace("\n", " ")
        list_items += f'<li><a href="{href}"><div class="item-title">{escape(title)}</div><div class="item-meta">{escape(meta_clean)}</div></a></li>\n'

    if not list_items:
        index_content = '<p class="meta" style="margin-top:2rem;text-align:center;">Nenhuma matéria ainda. Adicione arquivos .md em <code>articles/</code>.</p>'
    else:
        index_content = f'<ul class="article-list">\n{list_items}</ul>'
    index_desc = f"Coleção de {len(articles)} matéria(s) sobre hanzi, cultura chinesa e linguística. Leitura offline otimizada para mobile."
    index_html = HTML_TEMPLATE.format(
        title="Matérias de Hanzi",
        description=index_desc,
        css=full_css,
        header='<nav class="site-header"><a href="index.html">Matérias de Hanzi</a><span>{len(articles)} matérias</span></nav>'.replace("{len(articles)}", str(len(articles))),
        content=index_content,
        footer='<footer class="site-footer">Leitura offline &middot; Tipografia serifada</footer>',
    )
    (OUTPUT_DIR / "index.html").write_text(index_html, encoding="utf-8")

    print(f"Gerado site em {OUTPUT_DIR}/ com {len(articles)} artigo(s).")


if __name__ == "__main__":
    build()
