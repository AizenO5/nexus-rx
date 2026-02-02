import pandas as pd
from utils.scraper import fetch_online_price

def hunt_best_deal(query):
    # 1. Load Local Data
    df = pd.read_csv('data/local_inventory.csv')
    
    # 2. Filter for the medicine (Case-insensitive)
    local_match = df[df['medicine_name'].str.contains(query, case=False)]
    
    # 3. Get Online Price
    online_price = fetch_online_price(query)
    
    # 4. Agent Decision
    if not local_match.empty:
        local_price = local_match.iloc[0]['final_price']
        store = local_match.iloc[0]['store_name']
        
        # Logic: Is local cheaper?
        if str(online_price) != "Not Found" and local_price < float(online_price.replace('₹','')):
            return f"Found a Deal! {store} is cheaper than online at ₹{local_price}."
        else:
            return f"Online is better or comparable: {online_price}"
    return "Medicine not found in local partner stores."