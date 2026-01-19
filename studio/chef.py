from langchain.agents import create_agent
from langchain_cerebras import ChatCerebras
from langchain_community.tools import TavilySearchResults
from dotenv import load_dotenv

load_dotenv()

model = ChatCerebras(model_name="gpt-oss-120b")

search = TavilySearchResults(
    max_results = 3,
    include_answer = True,
    include_raw_content = False
)

# Crea l'agente (restituisce già un grafo compilato)
agent = create_agent(
    model=model,
    tools = [search],
    system_prompt='''
    Sei un agente specializzato nella creazione di ricette.
    Devi proporre delle ricette semplici e gustose con gli ingredienti
    che l'utente ti propone.
    Puoi usare un tool per la ricerca web per trovare le ricette.
    Se la ricetta coinvolge ingredienti che l'utente non ha menzionato
    sottolinea la loro presenza nella risposta finale.'''
)