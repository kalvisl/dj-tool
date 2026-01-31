print("=== TEST START ===")

# Test 1: Basic Python works
print("Python is working!")

# Test 2: Try to import our packages
try:
    from fastapi import FastAPI
    print("✅ FastAPI installed")
except ImportError as e:
    print(f"❌ FastAPI error: {e}")

try:
    import youtube_dl
    print("✅ youtube_dl installed")
except ImportError as e:
    print(f"❌ youtube_dl error: {e}")

print("=== TEST END ===")