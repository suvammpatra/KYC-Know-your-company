import google.generativeai as genai
import os
from dotenv import load_dotenv
load_dotenv()
# Configure Gemini
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])
model = genai.GenerativeModel("gemini-1.5-flash")

def financial_analyst(company: str) -> str:
    prompt = f"Analyze the financial performance of {company}. Focus on revenue, profitability, and risks."
    response = model.generate_content(prompt)
    return response.text.strip()

def market_research_analyst(company: str) -> str:
    prompt = f"Do a market research analysis for {company}. Cover industry trends, competition, and market opportunities."
    response = model.generate_content(prompt)
    return response.text.strip()

def reporting_analyst(company: str) -> str:
    prompt = f"Write a clear, concise business report summary for {company} using inputs from financial and market analysis."
    response = model.generate_content(prompt)
    return response.text.strip()
