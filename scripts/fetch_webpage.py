import requests
from bs4 import BeautifulSoup
import os
from datetime import datetime

# Get URL from user
url = input("Please enter the webpage URL: ")

# Create a folder to store the results
folder_name = "webpage_data_" + datetime.now().strftime("%Y%m%d_%H%M%S")
os.makedirs(folder_name, exist_ok=True)

try:
    # Fetch the webpage
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for bad status codes
    
    # Parse the HTML
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Save the full HTML
    with open(f"{folder_name}/full_page.html", "w", encoding="utf-8") as f:
        f.write(soup.prettify())
    
    # Extract and save forms separately
    forms = soup.find_all('form')
    with open(f"{folder_name}/forms.html", "w", encoding="utf-8") as f:
        for i, form in enumerate(forms, 1):
            f.write(f"\n\n<!-- Form {i} -->\n")
            f.write(form.prettify())
    
    print(f"\nData saved successfully in folder: {folder_name}")
    print(f"Found {len(forms)} forms on the page")

except requests.RequestException as e:
    print(f"Error fetching the webpage: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
