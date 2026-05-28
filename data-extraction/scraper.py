"""
Web Data Extraction Service
Scrapes websites and organizes data
"""
import requests
from bs4 import BeautifulSoup

def extract_data(url, selectors):
    """Extract data from a webpage"""
    resp = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(resp.text, 'html.parser')
    
    results = {}
    for name, selector in selectors.items():
        elements = soup.select(selector)
        results[name] = [el.text.strip() for el in elements]
    
    return results

# Example: Extract competitor prices
if __name__ == '__main__':
    # Example usage
    pass
