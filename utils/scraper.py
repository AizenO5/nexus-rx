import requests
from bs4 import BeautifulSoup

def fetch_online_results(med_name):
    # Standard headers to prevent being blocked
    headers = {'User-Agent': 'Mozilla/5.0'}
    url = f"https://www.1mg.com/search/all?name={med_name}"
    
    try:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # 1mg usually stores price in a div with a specific class
        # NOTE: You'll need to right-click 'Inspect' on 1mg to get the exact class name
        price_tag = soup.find('div', class_='style__price-tag___D_Oos') 
        return price_tag.text if price_tag else "Not Found"
    except:
        return "Connection Error"