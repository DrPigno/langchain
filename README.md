# 🦜 Corso LangChain - Materiale Didattico

Benvenuti al corso pratico su LangChain! Questo repository contiene tutte le lezioni, esercizi e materiali necessari per il corso.

## 📋 Prerequisiti

- Python 3.10 o superiore
- [uv](https://docs.astral.sh/uv/) installato sul sistema
- Un account OpenAI con API key (o altri provider LLM)
- Git per clonare il repository

## 🚀 Setup Rapido

### 1. Clona il repository

```bash
git clone <URL_DEL_TUO_REPOSITORY>
cd LangChain_1
```

### 2. Installa uv (se non l'hai già)

**Windows:**
```powershell
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

**macOS/Linux:**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### 3. Configura l'ambiente e installa le dipendenze

```bash
uv sync
```

Questo comando creerà automaticamente un ambiente virtuale e installerà tutte le dipendenze necessarie.

### 4. Configura le API keys

1. Copia il file di esempio:
   ```bash
   cp .env.example .env
   ```

2. Modifica il file `.env` e inserisci la tua OpenAI API key:
   ```
   OPENAI_API_KEY=sk-your-actual-key-here
   ```

### 5. Avvia Jupyter

```bash
uv run jupyter notebook
```

Oppure usa VS Code con l'estensione Jupyter!

## 📚 Struttura del Corso

```
.
├── lezioni/          # Notebook delle lezioni principali
├── esercizi/         # Esercizi pratici da completare
├── soluzioni/        # Soluzioni degli esercizi
├── data/             # Dati di esempio
├── utils/            # Funzioni helper
├── pyproject.toml    # Configurazione del progetto e dipendenze
└── .env.example      # Template per le variabili d'ambiente
```

### Lezioni

1. **Introduzione** - Setup e concetti base di LangChain


## 💡 Comandi Utili

```bash
# Attivare l'ambiente virtuale
uv sync

# Eseguire un notebook specifico
uv run jupyter notebook lezioni/01_introduzione.ipynb

# Aggiungere una nuova dipendenza
uv add nome-pacchetto

# Aggiornare le dipendenze
uv sync --upgrade
```

## 🔧 Risoluzione Problemi

### L'ambiente virtuale non si attiva
```bash
# Ricrea l'ambiente da zero
rm -rf .venv
uv sync
```

### Problemi con Jupyter
```bash
# Reinstalla il kernel Jupyter
uv run python -m ipykernel install --user --name=langchain-corso
```

### Errori di import
```bash
# Verifica che tutte le dipendenze siano installate
uv sync --all-extras
```

## 📖 Risorse Aggiuntive

- [Documentazione LangChain](https://python.langchain.com/)
- [Documentazione uv](https://docs.astral.sh/uv/)
- [OpenAI API Reference](https://platform.openai.com/docs/)

## 🤝 Supporto

Per domande o problemi, contatta l'istruttore o apri una issue su GitHub.

## 📄 Licenza

Materiale del corso fornito per scopi educativi.

---

**Buon apprendimento! 🚀**
