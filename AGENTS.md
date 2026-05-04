# Instruções para o Agente

## Contexto

Este é um projeto de aprendizado de chinês mandarim. O objetivo é produzir matérias diárias de hanzi em formato de revista, salvá-las na pasta `articles/` e gerar um site estático via `build.py`.

## Antes de agir

Sempre que for iniciar uma sessão ou quando o usuário pedir a criação de um artigo, **leia na seguinte ordem**:

1. `00_system_prompt.md` — contexto do projeto, tom, prioridades e estilo geral.
2. `01_perfil.md` — perfil do aluno (Tomás), nível atual, objetivos e restrições.
3. `02_interesses.md` — interesses culturais e temáticos para puxar exemplos.
4. `03_diretrizes_metodo.md` — como aplicar o método socrático, tratamento de erros, etimologia, ritmo.
5. `04_como_usar.md` — comandos úteis, sinais de ajuste, fluxo de estudo.

## Quando o usuário pedir a criação de um artigo

O processo é **two-pass**:

1. Leia também `05_formato_materias.md` — este é o **documento central de formatação** das matérias. Siga-o rigorosamente.
2. Verifique `memory.md` para evitar repetir caracteres e variar o tipo de matéria.
3. **Primeira passada:** escreva a matéria completa (corpo + seção "Para o Anki" com placeholder indicando que o CSV virá depois).
4. **Segunda passada:** com base no vocabulário da matéria, escolha os cards e gere o CSV em `site/cards/NNN-tema.csv` seguindo rigorosamente `06_instrucoes_csv_anki.md`.
5. Volte à matéria e reescreva a seção "Para o Anki" com:
   - Lista resumida dos cards (hanzi, pinyin, tipo — uma linha por card);
   - Link para baixar o CSV;
   - Instrução curta sobre como importar.
6. Salve o arquivo na pasta `articles/` com o formato de nome: `NNN_titulo_curto.md`, onde `NNN` é o número sequencial da matéria.
7. Atualize `memory.md` com os dados da nova matéria.

## Após criar ou modificar qualquer artigo

Execute obrigatoriamente (dentro do .venv):

```bash
python3 build.py
```

Isso regenera o site estático em `site/` a partir dos arquivos em `articles/`.

## Após o build

Faça commit e push das alterações:

```bash
git add .
git commit -m "feat: adiciona matéria #NNN — [título curto]"
git push
```

Se a branch local não estiver rastreando remoto, use:

```bash
git push -u origin main
```

> ⚠️ **Nunca commite arquivos de ambiente** (`.venv/`, credenciais, etc.). O `.gitignore` já deve excluí-los.

## Resumo do fluxo

1. Leia `00` a `04` para contexto.
2. Leia `05` para formatação ao criar artigos.
3. Escreva a matéria em `articles/NNN_titulo_curto.md` (incluindo placeholder no Anki).
4. Gere o CSV em `site/cards/NNN-tema.csv`.
5. Reescreva a seção "Para o Anki" na matéria.
6. Atualize `memory.md`.
7. Rode `python3 build.py`.
8. Commit e push.
