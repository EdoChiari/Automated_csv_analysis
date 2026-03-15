import anthropic
from dotenv import load_dotenv

load_dotenv()

# Legge il contenuto del CSV
with open("Test_csv_analyzer.csv", "r") as file:
    csv_content = file.read()

# Crea la connessione con Claude
client = anthropic.Anthropic()

# Manda il CSV a Claude con istruzioni
message = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=1024,
    messages=[
        {"role": "user", "content": f"""
        Analizza questo dataset di vendite e dimmi:
        1. Quali sono i prodotti più venduti?
        2. Quali paesi generano più ricavi?
        3. Ci sono pattern o anomalie interessanti?
        
        Dati:
        {csv_content}
        """}
    ]
)

analisi = message.content[0].text

print(analisi)

with open("analisi.txt", "w") as file:
    file.write(analisi)

print("\nAnalisi salvata in analisi.txt!")