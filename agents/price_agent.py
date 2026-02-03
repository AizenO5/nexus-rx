import pandas as pd
import google.generativeai as genai
import json
import streamlit as st
from rapidfuzz import process, fuzz
from utils.scraper import fetch_online_results # Change this to return a LIST of results

# Initialize Gemini (Make sure to set your API key)
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

def get_fuzzy_local_matches(query, df):
    choices = df['medicine_name'].tolist()
    # We increase the limit to 5 so the AI has choices to reason with
    results = process.extract(query, choices, scorer=fuzz.token_sort_ratio, limit=5)
    matched_names = [res[0] for res in results if res[1] > 60]
    return df[df['medicine_name'].isin(matched_names)]

def hunt_best_deal(query):
    # 1. LOAD DATA
    df = pd.read_csv('data/local_inventory.csv')
    
    # 2. FUZZY SEARCH (Local)
    # Instead of strict .contains(), we use your new fuzzy function
    local_matches = get_fuzzy_local_matches(query, df)
    
    # Format local data for the prompt
    if not local_matches.empty:
        local_context = local_matches.to_json(orient='records')
    else:
        local_context = "[]"
    
    # 3. FETCH WIDE (Online)
    # Assume your scraper now returns a list of top 3 search results from 1mg
    online_results = fetch_online_results(query) 
    
    # 4. THE AGENTIC BRAIN (LLM Reasoning)
    prompt = f"""
    You are the NexusRx AI Engine. 
    User is searching for: "{query}"
    
    LOCAL DATA: {local_context}
    ONLINE DATA: {online_results}

    TASK:
    - Standardize the name and composition of the medicine.
    - Compare prices across Local and Online results.
    - If the exact medicine is unavailable, find the closest match.
    
    Return ONLY a JSON object:
    {{
        "medicine_info": {{
            "name": "Standardized Name",
            "composition": "Chemical Ingredients",
            "is_out_of_stock_everywhere": boolean
        }},
        "agent_verdict": "A 1-sentence sharp comparison of the best deal.",
        "listings": [
            {{
                "store_name": "Store/Site Name",
                "price": 123.45,
                "type": "Local" or "Online",
                "stock_status": "In Stock" or "Out of Stock",
                "badge": "Best Value" or "Fastest" or null
            }}
        ]
    }}
    """
    
    model = genai.GenerativeModel('models/gemini-2.0-flash')
    response = model.generate_content(prompt)
    
    # Clean and parse JSON
    try:
        clean_text = response.text.replace('```json', '').replace('```', '').strip()
        return json.loads(clean_text)
    except Exception as e:
        return {"error": "Agent parsing failed", "raw": response.text}