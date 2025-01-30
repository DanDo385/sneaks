# Import required libraries
import requests  # For making HTTP requests
from bs4 import BeautifulSoup  # For parsing HTML content
import os  # For file and directory operations
from datetime import datetime  # For generating timestamps

# Prompt user to input the target webpage URL
url = input("Please enter the webpage URL: ")

# Create a timestamped folder name to store the webpage data
# Format: webpage_data_YYYYMMDD_HHMMSS
folder_name = "webpage_data_" + datetime.now().strftime("%Y%m%d_%H%M%S")
# Create the folder if it doesn't exist, or use existing one
os.makedirs(folder_name, exist_ok=True)

try:
    # Send HTTP GET request to fetch the webpage content
    response = requests.get(url)
    # Check if request was successful (raises exception if status code is 4XX/5XX)
    response.raise_for_status()
    
    # Create BeautifulSoup object to parse the HTML content
    # Using 'html.parser' as it's built into Python
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Save the complete webpage HTML to full_page.html
    # Using UTF-8 encoding to properly handle special characters
    with open(f"{folder_name}/full_page.html", "w", encoding="utf-8") as f:
        f.write(soup.prettify())  # prettify() formats the HTML with proper indentation
    
    # Find all <form> elements in the HTML and save them separately
    forms = soup.find_all('form')
    with open(f"{folder_name}/forms.html", "w", encoding="utf-8") as f:
        # Enumerate through forms starting from 1 for human-readable numbering
        for i, form in enumerate(forms, 1):
            # Add a comment before each form for better readability
            f.write(f"\n\n<!-- Form {i} -->\n")
            f.write(form.prettify())
    
    # Print success message with folder location and form count
    print(f"\nData saved successfully in folder: {folder_name}")
    print(f"Found {len(forms)} forms on the page")

except requests.RequestException as e:
    # Handle specific HTTP request-related errors (network issues, invalid URLs, etc.)
    print(f"Error fetching the webpage: {e}")
except Exception as e:
    # Catch any other unexpected errors that might occur
    print(f"An error occurred: {e}")
