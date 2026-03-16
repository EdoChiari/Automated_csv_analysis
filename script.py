import anthropic
from dotenv import load_dotenv
from docx import Document
from docx.shared import Pt, RGBColor
from datetime import datetime
import re
import os
import json

load_dotenv()

# Chiede quali file analizzare
input_utente = input("Quali file CSV vuoi analizzare? (separali con una virgola) ")
lista_file = [f.strip() for f in input_utente.split(",")]

# Chiede cosa analizzare
tipo_analisi = input("Cosa vuoi analizzare? (es. profittabilità, trend, confronto segmenti) ")

# Crea la connessione con Claude
client = anthropic.Anthropic()

risultati = []

# Analizza ogni file
for nome_file in lista_file:
    print(f"\nAnalizzando {nome_file}...")
    
    with open(nome_file, "r") as file:
        csv_content = file.read()

    message = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=1024,
        messages=[
            {"role": "user", "content": f"""
            Analizza questo dataset di vendite con focus su: {tipo_analisi}
            
            Per ogni punto fornisci:
            - Osservazioni chiave
            - Numeri specifici dal dataset
            - Eventuali anomalie o pattern rilevanti
            
            IMPORTANTE: Non usare tabelle Markdown. Usa solo testo, titoli e liste con trattini.
            
            Dati:
            {csv_content}
            """}
        ]
    )
    
    analisi = message.content[0].text
    risultati.append({"file": nome_file, "analisi": analisi})
    print(analisi)

# Chiede il nome del file di output
nome_output = input("\nCome vuoi chiamare il report? (senza estensione) ")

# Crea la cartella
os.makedirs(nome_output, exist_ok=True)

def processa_testo(doc, testo):
    """Converte testo Markdown in formattazione Word"""
    righe = testo.split("\n")
    i = 0
    while i < len(righe):
        riga = righe[i]

        if riga.startswith("### "):
            doc.add_heading(riga.replace("### ", "").strip(), level=3)
        elif riga.startswith("## "):
            doc.add_heading(riga.replace("## ", "").strip(), level=2)
        elif riga.startswith("# "):
            doc.add_heading(riga.replace("# ", "").strip(), level=1)
        elif riga.strip() == "" or riga.strip() == "---":
            doc.add_paragraph("")
        else:
            para = doc.add_paragraph()
            parti = re.split(r'\*\*(.*?)\*\*', riga)
            for idx, parte in enumerate(parti):
                run = para.add_run(parte)
                if idx % 2 == 1:
                    run.bold = True

        i += 1

# Salva .docx nella cartella
doc = Document()
doc.add_heading("Report Analisi Dataset", level=1)
doc.add_paragraph(f"Data: {datetime.now().strftime('%d/%m/%Y %H:%M')}")
doc.add_paragraph(f"Focus analisi: {tipo_analisi}")

for r in risultati:
    doc.add_heading(f"Analisi: {r['file']}", level=2)
    processa_testo(doc, r["analisi"])

doc.save(f"{nome_output}/{nome_output}.docx")
print(f"\nReport salvato in {nome_output}/{nome_output}.docx!")

# Salva .json nella cartella
output_json = {
    "data": datetime.now().strftime("%d/%m/%Y %H:%M"),
    "focus_analisi": tipo_analisi,
    "file_analizzati": lista_file,
    "risultati": risultati
}
with open(f"{nome_output}/{nome_output}.json", "w", encoding="utf-8") as f:
    json.dump(output_json, f, ensure_ascii=False, indent=2)
print(f"Report salvato anche in {nome_output}/{nome_output}.json!")