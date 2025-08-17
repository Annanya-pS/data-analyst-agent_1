#!/usr/bin/env python3
"""
Test script for Data Analyst Agent API
Run this to test your deployed API or local instance
"""

import requests
import json
import base64
import time
from pathlib import Path

# Configuration
API_URL = "http://localhost:5000/api/"  # Change this to your deployed URL
HEALTH_URL = "http://localhost:5000/health"

def test_health_check():
    """Test the health check endpoint"""
    print("🏥 Testing health check...")
    try:
        response = requests.get(HEALTH_URL, timeout=10)
        if response.status_code == 200:
            print("✅ Health check passed:", response.json())
            return True
        else:
            print("❌ Health check failed:", response.status_code)
            return False
    except Exception as e:
        print("❌ Health check error:", e)
        return False

def create_test_questions():
    """Create test questions files"""
    
    # Film analysis questions
    film_questions = """Scrape the list of highest grossing films from Wikipedia. It is at the URL:
https://en.wikipedia.org/wiki/List_of_highest-grossing_films

Answer the following questions and respond with a JSON array of strings containing the answer.

1. How many $2 bn movies were released before 2000?
2. Which is the earliest film that grossed over $1.5 bn?
3. What's the correlation between the Rank and Peak?
4. Draw a scatterplot of Rank and Peak along with a dotted red regression line through it.
   Return as a base-64 encoded data URI, `"data:image/png;base64,iVBORw0KG..."` under 100,000 bytes."""
   
    # Court data questions
    court_questions = """The Indian high court judgement dataset contains judgements from the Indian High Courts, downloaded from ecourts website. It contains judgments of 25 high courts, along with raw metadata (as .json) and structured metadata (as .parquet).

This DuckDB query counts the number of decisions in the dataset:

```sql
INSTALL httpfs; LOAD httpfs;
INSTALL parquet; LOAD parquet;

SELECT COUNT(*) FROM read_parquet('s3://indian-high-court-judgments/metadata/parquet/year=*/court=*/bench=*/metadata.parquet?s3_region=ap-south-1');
```

Answer the following questions and respond with a JSON object containing the answer.

{
  "Which high court disposed the most cases from 2019 - 2022?": "...",
  "What's the regression slope of the date_of_registration - decision_date by year in the court=33_10?": "...",
  "Plot the year and # of days of delay from the above question as a scatterplot with a regression line. Encode as a base64 data URI under 100,000 characters": "data:image/webp:base64,..."
}"""

    # Write test files
    Path("test_film_questions.txt").write_text(film_questions)
    Path("test_court_questions.txt").write_text(court_questions)
    
    print("📝 Created test question files:")
    print("   - test_film_questions.txt")
    print("   - test_court_questions.txt")

def test_film_analysis():
    """Test film analysis endpoint"""
    print("\n🎬 Testing film analysis...")
    
    try:
        with open("test_film_questions.txt", "rb") as f:
            files = {"questions.txt": f}
            
            start_time = time.time()
            response = requests.post(API_URL, files=files, timeout=300)
            end_time = time.time()
            
            print(f"⏱️  Response time: {end_time - start_time:.2f} seconds")
            print(f"📊 Status code: {response.status_code}")
            
            if response.status_code == 200:
                result = response.json()
                print("✅ Film analysis response:")
                print(f"   Type: {type(result)}")
                
                if isinstance(result, list) and len(result) == 4:
                    print(f"   1. Movies before 2000: {result[0]}")
                    print(f"   2. Earliest $1.5bn film: {result[1]}")
                    print(f"   3. Correlation: {result[2]}")
                    print(f"   4. Plot size: {len(str(result[3]))} characters")
                    
                    # Validate plot
                    if str(result[3]).startswith("data:image/png;base64,"):
                        print("   ✅ Plot format valid")
                        if len(str(result[3])) < 100000:
                            print("   ✅ Plot size under 100KB")
                        else:
                            print("   ⚠️  Plot size over 100KB")
                    else:
                        print("   ❌ Invalid plot format")
                        
                    return True
                else:
                    print(f"   ❌ Invalid response format: expected 4-element array")
                    print(f"   Got: {result}")
                    return False
            else:
                print(f"❌ Request failed: {response.text}")
                return False
                
    except FileNotFoundError:
        print("❌ test_film_questions.txt not found. Run create_test_questions() first.")
        return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def test_court_analysis():
    """Test court data analysis endpoint"""
    print("\n⚖️  Testing court analysis...")
    
    try:
        with open("test_court_questions.txt", "rb") as f:
            files = {"questions.txt": f}
            
            start_time = time.time()
            response = requests.post(API_URL, files=files, timeout=300)
            end_time = time.time()
            
            print(f"⏱️  Response time: {end_time - start_time:.2f} seconds")
            print(f"📊 Status code: {response.status_code}")
            
            if response.status_code == 200:
                result = response.json()
                print("✅ Court analysis response:")
                print(f"   Type: {type(result)}")
                
                if isinstance(result, dict):
                    for question, answer in result.items():
                        print(f"   Q: {question[:50]}...")
                        print(f"   A: {str(answer)[:100]}...")
                        print()
                    return True
                else:
                    print(f"   ❌ Invalid response format: expected dict")
                    print(f"   Got: {result}")
                    return False
            else:
                print(f"❌ Request failed: {response.text}")
                return False
                
    except FileNotFoundError:
        print("❌ test_court_questions.txt not found. Run create_test_questions() first.")
        return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def validate_base64_image(base64_string):
    """Validate base64 encoded image"""
    try:
        if not base64_string.startswith("data:image/"):
            return False, "Invalid data URI format"
            
        # Extract base64 data
        _, data = base64_string.split(",", 1)
        img_data = base64.b64decode(data)
        
        size_kb = len(img_data) / 1024
        
        if size_kb > 100:
            return False, f"Image too large: {size_kb:.1f}KB"
            
        return True, f"Valid image: {size_kb:.1f}KB"
        
    except Exception as e:
        return False, f"Error validating image: {e}"

def run_all_tests():
    """Run complete test suite"""
    print("🧪 Running Data Analyst Agent Tests")
    print("=" * 50)
    
    # Step 1: Health check
    if not test_health_check():
        print("❌ Health check failed. Ensure the API is running.")
        return False
    
    # Step 2: Create test questions
    create_test_questions()
    
    # Step 3: Test film analysis
    film_success = test_film_analysis()
    
    # Step 4: Test court analysis
    court_success = test_court_analysis()
    
    # Summary
    print("\n📋 Test Summary")
    print("=" * 20)
    print(f"Health Check: ✅")
    print(f"Film Analysis: {'✅' if film_success else '❌'}")
    print(f"Court Analysis: {'✅' if court_success else '❌'}")
    
    if film_success and court_success:
        print("\n🎉 All tests passed! Your API is ready for submission.")
        return True
    else:
        print("\n⚠️  Some tests failed. Check the logs above.")
        return False

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        API_URL = sys.argv[1].rstrip('/') + '/api/'
        HEALTH_URL = sys.argv[1].rstrip('/') + '/health'
        print(f"Using API URL: {API_URL}")
    
    run_all_tests()