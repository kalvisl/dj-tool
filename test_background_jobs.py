#!/usr/bin/env python3
"""Test script for background job functionality"""

import requests
import time
import json

def test_background_jobs():
    """Test the background job system"""
    print("🧪 Testing background job system...")
    
    # Test URL
    test_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    base_url = "http://localhost:8001"
    
    try:
        # Test 1: Check if server is running
        print("1. Checking server status...")
        response = requests.get(f"{base_url}/", timeout=5)
        if response.status_code == 200:
            print(f"   ✅ Server is running: {response.json().get('message', 'Unknown')}")
        else:
            print(f"   ❌ Server not responding: {response.status_code}")
            return False
        
        # Test 2: Create a background job
        print("2. Creating background job...")
        response = requests.get(f"{base_url}/analyze/background", params={"url": test_url}, timeout=5)
        
        if response.status_code == 200:
            data = response.json()
            if data.get("status") == "job_created":
                job_id = data["job_id"]
                print(f"   ✅ Background job created: {job_id}")
                
                # Test 3: Check job status
                print("3. Checking job status...")
                for i in range(10):  # Check for up to 10 seconds
                    time.sleep(1)
                    status_response = requests.get(f"{base_url}/analyze/background/{job_id}", timeout=5)
                    
                    if status_response.status_code == 200:
                        status_data = status_response.json()
                        job_status = status_data.get("job_status")
                        progress = status_data.get("progress", 0)
                        message = status_data.get("message", "")
                        
                        print(f"   ⏳ Check {i+1}: Status={job_status}, Progress={progress}%, Message={message}")
                        
                        if job_status == "completed":
                            print(f"   ✅ Job completed successfully!")
                            result = status_data.get("result")
                            if result:
                                print(f"   📊 Result: BPM={result.get('bpm')}, Key={result.get('key')}")
                            return True
                        elif job_status == "failed":
                            print(f"   ❌ Job failed: {message}")
                            return False
                    else:
                        print(f"   ❌ Failed to get job status: {status_response.status_code}")
                        return False
                
                print("   ⚠️  Job timed out after 10 seconds")
                return False
            else:
                print(f"   ❌ Failed to create job: {data.get('message', 'Unknown error')}")
                return False
        else:
            print(f"   ❌ Failed to create background job: {response.status_code}")
            return False
            
    except requests.exceptions.ConnectionError:
        print("   ❌ Cannot connect to server. Make sure it's running on localhost:8001")
        print("   💡 Start the server with: uvicorn app_working:app --host 0.0.0.0 --port 8001 --reload")
        return False
    except Exception as e:
        print(f"   ❌ Test error: {e}")
        return False

def test_immediate_analysis():
    """Test the immediate analysis endpoint"""
    print("\n🧪 Testing immediate analysis...")
    
    test_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    base_url = "http://localhost:8001"
    
    try:
        response = requests.get(f"{base_url}/analyze", params={"url": test_url}, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            if data.get("status") == "success":
                print(f"   ✅ Immediate analysis successful!")
                print(f"   📊 Result: BPM={data.get('bpm')}, Key={data.get('key')}, Analysis Type={data.get('analysis_type')}")
                return True
            else:
                print(f"   ❌ Analysis failed: {data.get('message', 'Unknown error')}")
                return False
        else:
            print(f"   ❌ HTTP error: {response.status_code}")
            return False
            
    except Exception as e:
        print(f"   ❌ Test error: {e}")
        return False

def main():
    """Main test function"""
    print("🚀 Starting DJ BPM Analyzer Background Jobs Test")
    print("=" * 50)
    
    # Start server if not running
    print("Note: Make sure the server is running before testing.")
    print("You can start it with: uvicorn app_working:app --host 0.0.0.0 --port 8001 --reload")
    print("=" * 50)
    
    # Run tests
    success = True
    
    # Test immediate analysis first (should work even without server modifications)
    if test_immediate_analysis():
        print("\n✅ Immediate analysis test PASSED")
    else:
        print("\n❌ Immediate analysis test FAILED")
        success = False
    
    # Test background jobs (requires the new endpoints)
    if test_background_jobs():
        print("\n✅ Background jobs test PASSED")
    else:
        print("\n❌ Background jobs test FAILED - This is expected if you haven't updated app_working.py")
        print("   To implement background jobs, add the new endpoints to app_working.py")
    
    print("\n" + "=" * 50)
    if success:
        print("🎉 All tests completed!")
    else:
        print("⚠️  Some tests failed. See above for details.")
    
    return success

if __name__ == "__main__":
    main()