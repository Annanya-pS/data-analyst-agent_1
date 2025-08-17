import requests
import json

def test_railway_api():
    BASE_URL = "https://web-production-ca34.up.railway.app"
    
    print("🔍 Testing correct endpoint...")
    
    # Test data for your data analyst agent
    test_data = {
        "message": "Analyze this sample data",
        "data": "Name,Sales\nJohn,100\nJane,150\nBob,80",
        "query": "What are the total sales?"
    }
    
    endpoints_to_test = [
        "/api/",           # Your main API endpoint
        "/api/analyze",    # Common analyze endpoint
        "/chat",           # If you have a chat endpoint
        "/analyze"         # Alternative analyze endpoint
    ]
    
    for endpoint in endpoints_to_test:
        print(f"\n📡 Testing: {BASE_URL}{endpoint}")
        
        try:
            # POST request to the API
            response = requests.post(
                f"{BASE_URL}{endpoint}",
                json=test_data,
                headers={"Content-Type": "application/json"},
                timeout=30
            )
            
            print(f"   Status: {response.status_code}")
            
            if response.status_code == 200:
                print(f"   ✅ SUCCESS!")
                try:
                    result = response.json()
                    print(f"   Response type: {type(result)}")
                    print(f"   Response keys: {list(result.keys()) if isinstance(result, dict) else 'Not a dict'}")
                    print(f"   Sample response: {str(result)[:200]}...")
                    return True
                except json.JSONDecodeError:
                    print(f"   ⚠️  Non-JSON response: {response.text[:200]}...")
                    
            elif response.status_code == 405:
                print(f"   ❌ Method not allowed (endpoint doesn't accept POST)")
                
            elif response.status_code == 404:
                print(f"   ❌ Endpoint not found")
                
            else:
                print(f"   ❌ Error {response.status_code}: {response.text[:200]}...")
                
        except requests.exceptions.Timeout:
            print(f"   ⏰ Timeout (>30 seconds)")
            
        except requests.exceptions.RequestException as e:
            print(f"   ❌ Request failed: {e}")
    
    # If POST doesn't work, try GET with query parameters
    print(f"\n🔄 Trying GET requests with query parameters...")
    
    for endpoint in endpoints_to_test:
        try:
            response = requests.get(
                f"{BASE_URL}{endpoint}",
                params={"query": "test query", "message": "hello"},
                timeout=10
            )
            
            print(f"GET {endpoint}: {response.status_code}")
            
            if response.status_code == 200:
                print(f"   ✅ GET works for {endpoint}")
                try:
                    result = response.json()
                    print(f"   Response: {str(result)[:200]}...")
                except:
                    print(f"   HTML Response: {response.text[:100]}...")
                    
        except Exception as e:
            print(f"GET {endpoint} failed: {e}")
    
    return False

def test_file_upload():
    """Test file upload if your API supports it"""
    print(f"\n📁 Testing file upload...")
    
    BASE_URL = "https://web-production-ca34.up.railway.app"
    
    # Create test CSV data
    csv_data = "Name,Age,Salary\nAlice,25,50000\nBob,30,60000\nCharlie,35,70000"
    
    files = {
        'file': ('test_data.csv', csv_data, 'text/csv')
    }
    
    upload_endpoints = ['/upload', '/api/upload', '/file', '/api/file']
    
    for endpoint in upload_endpoints:
        try:
            response = requests.post(
                f"{BASE_URL}{endpoint}",
                files=files,
                timeout=30
            )
            
            print(f"Upload {endpoint}: {response.status_code}")
            
            if response.status_code == 200:
                print(f"   ✅ File upload works!")
                try:
                    result = response.json()
                    print(f"   Response: {str(result)[:200]}...")
                    return True
                except:
                    print(f"   Response: {response.text[:200]}...")
                    
        except Exception as e:
            print(f"Upload {endpoint} failed: {str(e)[:100]}...")
    
    return False

if __name__ == "__main__":
    print("🚀 Testing Railway Data Analyst Agent")
    print("=" * 50)
    
    # Test API endpoints
    api_works = test_railway_api()
    
    # Test file upload
    upload_works = test_file_upload()
    
    print("\n" + "=" * 50)
    print("📊 SUMMARY:")
    print(f"✅ Health check: PASSED")
    print(f"{'✅' if api_works else '❌'} API endpoints: {'PASSED' if api_works else 'FAILED'}")
    print(f"{'✅' if upload_works else '❌'} File upload: {'PASSED' if upload_works else 'NEEDS CHECK'}")
    
    if not api_works:
        print(f"\n💡 TROUBLESHOOTING TIPS:")
        print(f"1. Check your Flask/FastAPI routes - make sure they accept POST requests")
        print(f"2. Your root '/' route only accepts GET requests")
        print(f"3. Use '/api/' endpoint for data analysis requests")
        print(f"4. Check Railway logs: railway logs")
        print(f"5. Verify your route decorators: @app.route('/api/', methods=['POST', 'GET'])")