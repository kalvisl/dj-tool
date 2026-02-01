#!/usr/bin/env python3
"""Test script for audio analysis functions"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Import functions from app_working
from app_working import download_audio_from_youtube, analyze_audio_file, analyze_youtube_audio
import tempfile
import os

def test_download_function():
    """Test the download function"""
    print("Testing download_audio_from_youtube function...")
    
    # Create a temporary file path
    with tempfile.NamedTemporaryFile(suffix='.mp3', delete=False) as tmp:
        temp_path = tmp.name
    
    try:
        # Test with a short YouTube video (public domain music)
        test_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"  # Rick Astley - short, known to work
        
        print(f"Testing download from: {test_url}")
        print(f"Output path: {temp_path}")
        
        # Try to download
        success = download_audio_from_youtube(test_url, temp_path)
        
        if success:
            print("✅ Download succeeded!")
            
            # Check if file exists and has content
            if os.path.exists(temp_path):
                file_size = os.path.getsize(temp_path)
                print(f"✅ File created: {temp_path} ({file_size} bytes)")
                
                # Try to analyze the file
                print("\nTesting analyze_audio_file function...")
                result = analyze_audio_file(temp_path)
                
                if result:
                    bpm, key, camelot, energy = result
                    print(f"✅ Audio analysis succeeded!")
                    print(f"   BPM: {bpm:.1f}")
                    print(f"   Key: {key}")
                    print(f"   Camelot: {camelot}")
                    print(f"   Energy: {energy:.2f}")
                else:
                    print("❌ Audio analysis failed")
            else:
                print("❌ File was not created")
        else:
            print("❌ Download failed")
            
    except Exception as e:
        print(f"❌ Error during test: {e}")
        import traceback
        traceback.print_exc()
        
    finally:
        # Clean up
        if os.path.exists(temp_path):
            os.remove(temp_path)
            print(f"✅ Cleaned up temporary file: {temp_path}")

def test_full_analysis():
    """Test the full YouTube audio analysis"""
    print("\n" + "="*50)
    print("Testing full analyze_youtube_audio function...")
    
    test_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    print(f"Testing with URL: {test_url}")
    
    result = analyze_youtube_audio(test_url)
    
    if result:
        bpm, key, camelot, energy = result
        print("✅ Full YouTube audio analysis succeeded!")
        print(f"   BPM: {bpm:.1f}")
        print(f"   Key: {key}")
        print(f"   Camelot: {camelot}")
        print(f"   Energy: {energy:.2f}")
    else:
        print("❌ Full YouTube audio analysis failed")
        print("This is expected if yt-dlp download fails or takes too long")

def test_librosa_basic():
    """Test basic librosa functionality"""
    print("\n" + "="*50)
    print("Testing basic librosa functionality...")
    
    try:
        import librosa
        import numpy as np
        
        # Create a simple test signal
        sr = 22050  # Sample rate
        duration = 5  # seconds
        t = np.linspace(0, duration, int(sr * duration))
        
        # Create a simple sine wave at 440 Hz (A4)
        test_signal = 0.5 * np.sin(2 * np.pi * 440 * t)
        
        # Test tempo estimation
        tempo, _ = librosa.beat.beat_track(y=test_signal, sr=sr)
        print(f"✅ Librosa beat tracking works")
        print(f"   Detected tempo: {tempo}")
        
        # Test chroma feature extraction
        chroma = librosa.feature.chroma_cqt(y=test_signal, sr=sr)
        print(f"✅ Chroma feature extraction works")
        print(f"   Chroma shape: {chroma.shape}")
        
        return True
        
    except Exception as e:
        print(f"❌ Librosa test failed: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    print("="*50)
    print("DJ BPM Analyzer - Audio Analysis Test")
    print("="*50)
    
    # Test basic librosa
    if test_librosa_basic():
        # Test download function
        test_download_function()
        
        # Test full analysis
        test_full_analysis()
    
    print("\n" + "="*50)
    print("Test completed!")
    print("="*50)