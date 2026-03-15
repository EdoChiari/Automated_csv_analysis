# 🤖 Automated CSV Analysis with Claude AI

## What is this project?
A Python script that automatically analyzes CSV datasets using the Anthropic Claude API. Instead of manually uploading files to Claude.ai, this tool processes data programmatically — making it scalable, repeatable, and integrable into larger pipelines.

## Current Features
- Reads any CSV file and sends it to Claude for analysis
- Asks structured questions about top products, revenue by country, and data patterns
- Saves the AI-generated analysis to a `.txt` file automatically

## Tech Stack
- Python 3.12
- Anthropic Claude API (`claude-sonnet-4-6`)
- `python-dotenv` for secure API key management

## How to Run
1. Clone the repository
2. Create a `.env` file with your Anthropic API key:
```
   ANTHROPIC_API_KEY=your-key-here
```
3. Install dependencies:
```
   pip install anthropic python-dotenv
```
4. Run the script:
```
   python script.py
```

## Roadmap
- [ ] Accept any CSV file as input dynamically (no hardcoded filename)
- [ ] Export analysis to a formatted `.docx` report
- [ ] Add structured JSON output for pipeline integration
- [ ] Build a text-to-SQL agent that queries a PostgreSQL database in natural language
- [ ] Schedule automated weekly reports