# Product Context

## Why this project exists

The DJ BPM Analyzer is a web application that analyzes YouTube music tracks to extract DJ-friendly information including BPM (beats per minute), musical key, Camelot wheel notation, and energy levels. It helps DJs and music producers quickly analyze tracks for harmonic mixing and set building.

## What problems it solves

1. **Time-saving**: DJs can quickly analyze tracks without manually tapping BPM or analyzing keys
2. **Harmonic mixing**: Provides Camelot wheel notation for easy harmonic mixing
3. **Accessibility**: Works with any YouTube URL, no need for local files
4. **Educational**: Helps new DJs understand track analysis concepts
5. **Demo-friendly**: Always works with fallback data when real analysis isn't possible

## How it should work

1. User submits a YouTube URL through the web interface
2. Backend extracts video information using noembed API
3. System analyzes track (currently uses smart genre detection with fallback to realistic random data)
4. Returns BPM, key, Camelot notation, energy level, and track metadata
5. Frontend displays results in a visually appealing DJ-friendly interface

## Target Users

- DJs looking to analyze tracks for mixing
- Music producers checking track compatibility
- Beginners learning about harmonic mixing
- Anyone interested in music analysis

## Success Metrics

- Fast response time (< 3 seconds)
- High accuracy for genre-based BPM/key detection
- Reliable fallback when real analysis fails
- User-friendly interface with clear results
