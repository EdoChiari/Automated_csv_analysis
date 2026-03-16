# Automated CSV Analysis with Claude AI

## What is this project?
A Python script that automatically analyzes CSV datasets using the Anthropic Claude API. Instead of manually uploading files to Claude.ai, this tool processes data programmatically — making it scalable, repeatable, and integrable into larger pipelines.

## Current Features
- Accepts one or multiple CSV files as input (comma-separated)
- Lets you specify the analysis focus at runtime (e.g. profitability, trends, segment comparison)
- Sends each file to Claude (`claude-sonnet-4-6`) with a structured analysis prompt
- Exports results to a formatted `.docx` report with proper headings and bold text
- Exports results to a structured `.json` file for pipeline integration
- Saves all outputs in a dedicated folder named after the report

## Tech Stack
- Python 3.12
- Anthropic Claude API (`claude-sonnet-4-6`)
- `python-dotenv` for secure API key management
- `python-docx` for Word document generation

## How to Run
1. Clone the repository
2. Create a `.env` file with your Anthropic API key:
```
ANTHROPIC_API_KEY=your-key-here
```
3. Install dependencies:
```
pip install anthropic python-dotenv python-docx
```
4. Run the script:
```
python script.py
```
5. Follow the prompts:
   - Enter one or more CSV filenames (comma-separated)
   - Describe the analysis focus
   - Enter a name for the output report

## Output
All outputs are saved in a folder named after the report:
- `report_name/report_name.docx` — formatted Word document
- `report_name/report_name.json` — structured JSON with full results
