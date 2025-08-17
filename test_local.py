#!/usr/bin/env python3
"""
Local testing script for the Data Analyst Agent
"""

import requests
import json
from io import StringIO

def test_films_analysis():
    """Test the films analysis with sample questions"""
    
    questions_content = """Scrape the list of highest grossing films from Wikipedia. It is at the URL:
https://en.wikipedia.org/wiki/List_of_highest-grossing_films

Answer the following questions and respond with a JSON array of strings containing the answer.

1. How many $2 bn movies were released before 2000?
2. Which is the earliest film that grossed over $1.5 bn?
3. What's the correlation between the Rank and Peak?
4. Draw a scatterplot of Rank and Peak along with a dotted red regression line through it.
   Return as a base-64 encoded data URI, `"data:image/png;base64,iVBORw0KG..."` under 100,000 bytes.
"""

    # Test locally (update URL for your deployment)
    url = "http://localhost:5000/api/"  # Change to your Railway URL
    
    files = {
        'questions.txt': ('questions.txt', StringIO(questions_content), 'text/plain')
    }
    
    try:
        print("Testing films analysis...")
        response = requests.post(url, files=files, timeout=300)
        
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.text}")
        
        if response.status_code == 200:
            result = response.json()
            print(f"Analysis successful!")
            print(f"Number of answers: {len(result) if isinstance(result, list) else 'N/A'}")
            
            if isinstance(result, list) and len(result) >= 4:
                print(f"1. Movies $2bn before 2000: {result[0]}")
                print(f"2. Earliest $1.5bn film: {result[1]}")
                print(f"3. Correlation: {result[2]}")
                print(f"4. Plot length: {len(str(result[3]))}")
            
        else:
            print("Error in response")
            
    except Exception as e:
        print(f"Request failed: {e}")

def test_health():
    """Test health endpoint"""
    try:
        url = "http://localhost:5000/health"  # Change to your Railway URL
        response = requests.get(url, timeout=10)
        print(f"Health check - Status: {response.status_code}")
        print(f"Health response: {response.json()}")
    except Exception as e:
        print(f"Health check failed: {e}")

if __name__ == "__main__":
    print("=== Data Analyst Agent Test ===")
    test_health()
    print("\n" + "="*40 + "\n")
    test_films_analysis()