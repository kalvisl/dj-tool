print("=== DJ TOOL TEST ===")
print("Python version check...")

# Test imports
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

print("=== TEST COMPLETE ===")