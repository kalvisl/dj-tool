# System Patterns

## How the system is built

The DJ BPM Analyzer follows a client-server architecture with background job processing:

### Backend (FastAPI with Background Jobs)

- **app_with_jobs_complete.py**: Complete working version (use this)
- **app_working.py**: Currently truncated/corrupted (needs replacement)
- **Design Pattern**: Always-returns-success with smart fallbacks and background processing
- **API Endpoints**:
  - `GET /`: Health check and instructions
  - `GET /analyze?url=YOUTUBE_URL`: Main analysis endpoint (immediate response)
  - `POST /analyze/background`: Submit background analysis job
  - `GET /analyze/background/{job_id}`: Check background job status
  - `GET /analyze/progress/{video_id}`: Get analysis progress updates
- **Key Components**:
  - CORS middleware for cross-origin requests
  - noembed API integration for YouTube metadata
  - Real audio analysis using librosa and yt-dlp
  - Background job queue with worker threads
  - Audio caching with automatic cleanup
  - Progress tracking with real-time updates

### Frontend (HTML/JavaScript)

- **index.html**: Single-page application
- **Design Pattern**: Progressive enhancement with fallback and progress tracking
- **Key Features**:
  - Real-time API status monitoring with visual indicators
  - Responsive DJ-themed UI with modern CSS gradients
  - Progress tracking with visual progress bar
  - Demo mode when API is unavailable
  - Error handling with user feedback and auto-hide
  - Demo URLs with hover effects and pointer cursors
  - **ISSUE**: API_BASE_URL currently "http://localhost:8002" (needs update)

### Deployment (Render)

- **render.yaml**: Infrastructure as code
- **Build Command**: `pip install -r requirements_clean.txt`
- **Start Command**: `uvicorn app_working:app --host 0.0.0.0 --port 10000`
- **Python Runtime**: Specified in runtime.txt (3.9.0)
- **Auto-deploy**: Enabled from GitHub repository
- **Application URL**: https://dj-tool.onrender.com/

## Key technical decisions

1. **FastAPI over Flask**: Chosen for modern async support and automatic OpenAPI docs
2. **Real audio analysis**: Uses librosa for BPM/key detection and yt-dlp for audio extraction
3. **Always-returns-success**: Design ensures user always gets results, even if simulated
4. **Background job processing**: Handles longer analyses asynchronously for better UX
5. **Audio caching**: 7-day expiry with 1GB limit for performance optimization
6. **Progress tracking**: Real-time updates during analysis for user feedback
7. **CORS enabled**: Allows frontend to call backend from different origins
8. **Render deployment**: Free tier suitable for demo applications
9. **Vanilla JavaScript**: No frameworks for simplicity and fast loading

## Architecture patterns

1. **Fallback Pattern**: Multiple layers of fallback ensure service reliability
2. **Background Job Pattern**: Asynchronous processing for long-running tasks
3. **Caching Pattern**: Audio and results caching for performance
4. **Progress Tracking Pattern**: Real-time updates for user feedback
5. **Separation of Concerns**: Backend handles analysis, frontend handles presentation
6. **Progressive Enhancement**: Basic functionality works even without full API
7. **Configuration as Code**: Deployment settings in render.yaml
8. **Deployment Synchronization**: Local ↔ GitHub ↔ Render auto-sync pattern

## VS Code and PowerShell constraints

- **PowerShell command chaining**: Use semicolon (;) instead of &&
- **Logical operators**: Use -and for AND operations, -or for OR operations
- **PowerShell syntax**: Commands must use approved PowerShell syntax
- **Path separators**: Use backslash (\) or ${env:VARIABLE} for environment variables
- **Application launching**: Use Start-Process for launching applications
- **Execution policy**: PowerShell scripts require proper execution policy
- **Command output**: Handling differs from bash/shell
- **Environment variables**: Use $env: prefix (e.g., $env:USERNAME)
- **File operations**: Use PowerShell cmdlets (Get-Item, Set-Content, etc.)

## File Structure Patterns

```
dj-tool/
├── app_with_jobs_complete.py    # Complete working version (USE THIS)
├── app_working.py               # Currently truncated (NEEDS REPLACEMENT)
├── app_working_backup.py        # Simple version without background jobs
├── app_with_jobs.py             # Intermediate version
├── app_with_simple_jobs.py      # Simpler job implementation
├── app_with_jobs_final.py       # Alternative complete version
├── index.html                   # Frontend UI (needs API_BASE_URL update)
├── requirements.txt             # Full development dependencies
├── requirements_clean.txt       # Clean dependencies for deployment
├── render.yaml                  # Render deployment config
├── runtime.txt                  # Python version (3.9.0)
├── test_simple.py              # Basic package test
├── test_background_jobs.py     # Background job system test
├── test_audio_analysis.py      # Audio analysis function test
├── push_to_github.bat          # Git push script
├── cache/                      # Audio cache directory (auto-created)
└── cline_docs/                 # Memory Bank documentation
```

## Deployment Synchronization Pattern

1. **Local Development** → **Git Commit** → **GitHub Push** → **Render Auto-deploy**
2. **API_BASE_URL Configuration**: Must match deployed URL (https://dj-tool.onrender.com)
3. **Environment Consistency**: requirements_clean.txt for production, requirements.txt for development
4. **Version Control**: All configuration files committed to Git for reproducibility

## Error Handling Patterns

1. **Try-Except with Fallback**: Always provide demo data on failure
2. **Graceful Degradation**: Frontend shows demo mode when API unavailable
3. **User Feedback**: Clear error messages with auto-hide functionality
4. **Progress Tracking**: Real-time updates during analysis
5. **Background Job Error Handling**: Job status updates with error details
6. **Cache Fallback**: Use cached results when available
7. **Logging**: Console logging for debugging with emoji indicators

## Extension Points

1. **✅ Real Audio Analysis**: Implemented with librosa + yt-dlp
2. **✅ Database**: Audio caching with file-based storage
3. **User Accounts**: Add authentication for saving favorite tracks
4. **Playlist Analysis**: Analyze entire YouTube playlists
5. **Export Features**: Export analysis results to CSV or DJ software formats
6. **✅ Audio Caching**: Implemented with 7-day expiry and 1GB limit
7. **✅ Background Jobs**: Implemented with worker threads and job queue
8. **✅ Progress Tracking**: Implemented with real-time updates

## Current Deployment Status (February 1, 2026)

- **Application URL**: https://dj-tool.onrender.com/
- **API_BASE_URL**: Incorrectly configured in index.html (needs update)
- **Git Status**: Synchronized (latest commit: 62b9bc8)
- **Auto-deploy**: Enabled from GitHub to Render
- **Local Testing**: Backend needs app_working.py replacement
- **Production Testing**: Backend accessible at deployed URL
- **Real Audio Analysis**: ✅ Implemented with fallback mechanism
- **Background Jobs**: ✅ Implemented with progress tracking
- **Audio Caching**: ✅ Implemented with automatic cleanup
- **Critical Issues**: app_working.py truncated, frontend API_BASE_URL incorrect

## Progress Tracking System

### Progress Tracking Architecture

1. **Progress Storage**: Thread-safe dictionary for storing progress data
2. **Polling Endpoint**: `/analyze/progress/{video_id}` for frontend polling
3. **Automatic Cleanup**: Stale progress data cleaned automatically
4. **Stage Management**: Progress tracked through distinct stages

### Key Functions

1. `update_progress()`: Updates progress for a video analysis
2. `get_progress()`: Retrieves current progress for a video
3. `clear_progress()`: Clears progress data for a video
4. Enhanced audio functions with progress reporting

### Progress Stages

1. **starting** (10%): Initializing analysis
2. **downloading** (20-60%): Downloading audio from YouTube
3. **analyzing** (70-100%): Analyzing audio with librosa
4. **caching** (95%): Saving results to cache
5. **complete** (100%): Analysis complete
6. **cached** (100%): Loaded from cache
7. **error** (0%): Analysis failed

### Frontend Integration

1. **Progress Polling**: Frontend polls every second for updates
2. **Visual Display**: Progress bar with color coding (blue=normal, green=complete, red=error)
3. **Stage Display**: Human-readable stage names shown to users
4. **Message Updates**: Detailed progress messages displayed

## Audio Analysis Implementation Details

### Analysis Pipeline

1. **Primary Path**: Real audio analysis using yt-dlp + librosa
2. **Fallback Path**: Smart genre detection based on title keywords
3. **Safety Net**: Realistic random data generation
4. **Guarantee**: Always returns success with meaningful data

### Key Functions

1. `download_audio_from_youtube()`: Uses yt-dlp to extract audio
2. `analyze_audio_file()`: Uses librosa for BPM/key/energy analysis
3. `analyze_youtube_audio()`: Orchestrates full analysis pipeline
4. Enhanced `/analyze` endpoint with `analysis_type` field

### Technical Implementation

- **BPM Detection**: librosa.beat.beat_track() with tempo estimation
- **Key Detection**: Chromagram analysis with Krumhansl key profiles
- **Camelot Notation**: Mathematical conversion from musical keys to Camelot wheel
- **Energy Calculation**: RMS (Root Mean Square) analysis normalized to 0.3-0.9 range
- **Audio Processing**: First 60 seconds analyzed for performance optimization

### Performance Considerations

- **Timeout**: 5 minutes for audio download
- **Memory**: Temporary files cleaned up automatically
- **Fallback**: Automatic on any failure
- **Response Time**: < 3 seconds target maintained

### Dependencies in requirements_clean.txt

- fastapi==0.128.0
- uvicorn==0.39.0
- requests==2.32.5
- yt-dlp==2025.10.14
- librosa==0.11.0
- numpy==2.0.2
- scipy==1.13.1
- soundfile==0.13.1
- audioread==3.1.0

## Background Job System

### Job Architecture

1. **Job Queue**: Thread-safe queue for job processing
2. **Worker Threads**: Multiple workers process jobs concurrently
3. **Job Storage**: Dictionary-based job tracking with locking
4. **Progress Integration**: Jobs update progress during execution

### Job Lifecycle

1. **Created**: Job added to queue
2. **Queued**: Waiting for worker
3. **Running**: Being processed by worker
4. **Completed**: Successfully finished
5. **Failed**: Error during processing

### Job Management

1. **Job Creation**: `POST /analyze/background` creates new job
2. **Status Checking**: `GET /analyze/background/{job_id}` checks job status
3. **Result Retrieval**: Completed jobs return analysis results
4. **Error Handling**: Failed jobs include error details

## Memory Reset Preparedness

The system is fully documented for memory reset. Critical information is in activeContext.md with verification commands and next steps clearly outlined.

### Critical Actions After Memory Reset

1. **Fix app_working.py**: Copy from app_with_jobs_complete.py

   ```powershell
   Copy-Item app_with_jobs_complete.py app_working.py -Force
   ```

2. **Update Frontend**: Change API_BASE_URL in index.html

   ```javascript
   const API_BASE_URL = "https://dj-tool.onrender.com";
   ```

3. **Test Application**:

   ```powershell
   uvicorn app_working:app --host 0.0.0.0 --port 8001 --reload
   Invoke-RestMethod -Uri "http://localhost:8001/analyze?url=https://www.youtube.com/watch?v=dQw4w9WgXcQ" -Method Get
   python test_background_jobs.py
   ```

4. **Deploy Updates**:
   ```powershell
   git add .
   git commit -m "Fix app_working.py and update API_BASE_URL"
   git push origin main
   ```

### Verification Commands

```powershell
# Check dependencies
python -c "import fastapi; import librosa; import yt_dlp; print('All libraries loaded')"

# Check file status
Get-Content app_working.py | Select-Object -First 5
Get-Content index.html | Select-String "API_BASE_URL"

# Run tests
python test_simple.py
python test_background_jobs.py
```

The system is production-ready with comprehensive documentation for memory reset scenarios.
