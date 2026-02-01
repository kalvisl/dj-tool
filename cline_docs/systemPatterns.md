# System Patterns

## How the system is built

The DJ BPM Analyzer follows a client-server architecture with background job processing:

### Backend (FastAPI with Background Jobs) - DEPLOYED

- **app_working.py**: **COMPLETE AND DEPLOYED** - Fixed truncated file, now fully functional
- **app_with_jobs_complete.py**: Source for cache functions (reference)
- **Design Pattern**: Always-returns-success with smart fallbacks and background processing
- **API Endpoints (DEPLOYED)**:
  - `GET /`: Health check and instructions - VERIFIED
  - `GET /analyze?url=YOUTUBE_URL`: Main analysis endpoint (immediate response) - VERIFIED
  - `GET /analyze/background`: Submit background analysis job
  - `GET /analyze/background/{job_id}`: Check background job status
  - `GET /analyze/progress/{video_id}`: Get analysis progress updates
  - `GET /cache/stats`: Get cache statistics
  - `POST /cache/clear`: Clear all cache entries
  - `POST /cache/cleanup`: Clean up expired cache entries
- **Key Components (ALL DEPLOYED)**:
  - CORS middleware for cross-origin requests
  - noembed API integration for YouTube metadata
  - Real audio analysis using librosa and yt-dlp
  - Background job queue with worker threads (2 concurrent workers)
  - Audio caching with automatic cleanup (7-day expiry, 1GB limit)
  - Progress tracking with real-time updates

### Frontend (HTML/JavaScript) - DEPLOYED

- **index.html**: Single-page application - DEPLOYED
- **Design Pattern**: Progressive enhancement with fallback and progress tracking
- **Key Features (ALL WORKING)**:
  - Real-time API status monitoring with visual indicators
  - Responsive DJ-themed UI with modern CSS gradients
  - Progress tracking with visual progress bar
  - Demo mode when API is unavailable
  - Error handling with user feedback and auto-hide
  - Demo URLs with hover effects and pointer cursors
  - **✅ FIXED**: API_BASE_URL updated to "https://dj-tool.onrender.com" - VERIFIED

### Deployment (Render) - ACTIVE

- **render.yaml**: Infrastructure as code - CONFIGURED
- **Build Command**: `pip install -r requirements_clean.txt` - ACTIVE
- **Start Command**: `uvicorn app_working:app --host 0.0.0.0 --port 10000` - ACTIVE
- **Python Runtime**: Specified in runtime.txt (3.11.0) - CONFIGURED (updated to fix deployment)
- **Auto-deploy**: Enabled from GitHub repository - ACTIVE
- **Application URL**: https://dj-tool.onrender.com/ - VERIFIED WORKING

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
10. **Memory Bank documentation**: Comprehensive documentation for memory reset scenarios

## Architecture patterns

1. **Fallback Pattern**: Multiple layers of fallback ensure service reliability
2. **Background Job Pattern**: Asynchronous processing for long-running tasks
3. **Caching Pattern**: Audio and results caching for performance
4. **Progress Tracking Pattern**: Real-time updates for user feedback
5. **Separation of Concerns**: Backend handles analysis, frontend handles presentation
6. **Progressive Enhancement**: Basic functionality works even without full API
7. **Configuration as Code**: Deployment settings in render.yaml
8. **Deployment Synchronization**: Local ↔ GitHub ↔ Render auto-sync pattern
9. **Memory Reset Preparedness**: Complete documentation for continuity after memory loss

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
├── app_working.py               # ✅ MAIN APPLICATION - Complete and deployed
├── app_with_jobs_complete.py    # ✅ SOURCE - Used for cache functions
├── app_working_backup.py        # ✅ BACKUP - Simple version without background jobs
├── app_with_jobs.py             # ✅ REFERENCE - Intermediate version
├── app_with_simple_jobs.py      # ✅ REFERENCE - Simpler job implementation
├── app_with_jobs_final.py       # ✅ REFERENCE - Alternative complete version
├── index.html                   # ✅ FRONTEND UI - API_BASE_URL updated to production
├── requirements.txt             # ✅ DEVELOPMENT - Full development dependencies
├── requirements_clean.txt       # ✅ PRODUCTION - Clean dependencies for deployment
├── render.yaml                  # ✅ DEPLOYMENT - Render deployment config
├── runtime.txt                  # ✅ CONFIG - Python version (3.11.0 - updated to fix deployment)
├── test_simple.py              # ✅ TEST - Basic package test
├── test_background_jobs.py     # ✅ TEST - Background job system test
├── test_audio_analysis.py      # ✅ TEST - Audio analysis function test
├── push_to_github.bat          # ✅ SCRIPT - Git push script
├── .gitignore                  # ✅ CONFIG - Excludes cache, venv, temp files
├── cache/                      # ✅ DATA - Audio cache directory (auto-created)
└── cline_docs/                 # ✅ DOCUMENTATION - Memory Bank documentation
    ├── activeContext.md        # ✅ Current status and recent changes
    ├── productContext.md       # ✅ Project purpose and goals
    ├── progress.md            # ✅ Progress tracking
    ├── systemPatterns.md      # ✅ Technical architecture and patterns
    └── techContext.md         # ✅ Technologies and development setup
```

## Deployment Synchronization Pattern

1. **Local Development** → **Git Commit** → **GitHub Push** → **Render Auto-deploy**
2. **API_BASE_URL Configuration**: ✅ Must match deployed URL (https://dj-tool.onrender.com)
3. **Environment Consistency**: ✅ requirements_clean.txt for production, requirements.txt for development
4. **Version Control**: ✅ All configuration files committed to Git for reproducibility
5. **Current Status**: ✅ All changes deployed, production verified working

## Error Handling Patterns

1. **Try-Except with Fallback**: Always provide demo data on failure
2. **Graceful Degradation**: Frontend shows demo mode when API unavailable
3. **User Feedback**: Clear error messages with auto-hide functionality
4. **Progress Tracking**: Real-time updates during analysis
5. **Background Job Error Handling**: Job status updates with error details
6. **Cache Fallback**: Use cached results when available
7. **Logging**: Console logging for debugging with emoji indicators

## Extension Points

1. **✅ Real Audio Analysis**: Implemented with librosa + yt-dlp - DEPLOYED
2. **✅ Database**: Audio caching with file-based storage - DEPLOYED
3. **User Accounts**: Add authentication for saving favorite tracks
4. **Playlist Analysis**: Analyze entire YouTube playlists
5. **Export Features**: Export analysis results to CSV or DJ software formats
6. **✅ Audio Caching**: Implemented with 7-day expiry and 1GB limit - DEPLOYED
7. **✅ Background Jobs**: Implemented with worker threads and job queue - DEPLOYED
8. **✅ Progress Tracking**: Implemented with real-time updates - DEPLOYED
9. **✅ Memory Bank**: Complete documentation for memory reset scenarios

## Current Deployment Status (February 1, 2026)

- **Application URL**: https://dj-tool.onrender.com/ - ✅ VERIFIED WORKING
- **API_BASE_URL**: ✅ Correctly configured in index.html - VERIFIED
- **Git Status**: ✅ Synchronized (latest commit: 80dfef8)
- **Auto-deploy**: ✅ Enabled from GitHub to Render - ACTIVE
- **Local Testing**: ✅ Backend complete with app_working.py fixed
- **Production Testing**: ✅ Backend accessible and working at deployed URL
- **Real Audio Analysis**: ✅ Implemented with fallback mechanism - DEPLOYED
- **Background Jobs**: ✅ Implemented with progress tracking - DEPLOYED
- **Audio Caching**: ✅ Implemented with automatic cleanup - DEPLOYED
- **Critical Issues**: ✅ ALL RESOLVED (app_working.py fixed, API_BASE_URL updated)
- **Project Status**: ✅ COMPLETE AND DEPLOYED

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

### Dependencies in requirements_clean.txt (DEPLOYED - UPDATED Feb 1, 2026)

- fastapi==0.128.0
- uvicorn==0.39.0
- requests==2.32.5
- yt-dlp==2025.10.14
- librosa==0.11.0
- numpy==2.0.2
- scipy==1.11.4 # Updated from 1.13.1 to fix deployment (no Fortran compilation)
- soundfile==0.13.1
- audioread==3.1.0

## Background Job System

### Job Architecture

1. **Job Queue**: Thread-safe queue for job processing
2. **Worker Threads**: Multiple workers process jobs concurrently (2 workers)
3. **Job Storage**: Dictionary-based job tracking with locking
4. **Progress Integration**: Jobs update progress during execution

### Job Lifecycle

1. **Created**: Job added to queue
2. **Queued**: Waiting for worker
3. **Running**: Being processed by worker
4. **Completed**: Successfully finished
5. **Failed**: Error during processing

### Job Management

1. **Job Creation**: `GET /analyze/background` creates new job
2. **Status Checking**: `GET /analyze/background/{job_id}` checks job status
3. **Result Retrieval**: Completed jobs return analysis results
4. **Error Handling**: Failed jobs include error details

## Memory Reset Preparedness - CRITICAL

The system is fully documented for memory reset. Critical information is in activeContext.md with verification commands and next steps clearly outlined.

### Current State Summary

**PROJECT STATUS**: ✅ COMPLETE AND DEPLOYED

- Backend: FastAPI with audio analysis, caching, background jobs - DEPLOYED
- Frontend: Modern DJ-themed UI with progress tracking - DEPLOYED
- Deployment: Live at https://dj-tool.onrender.com/ - VERIFIED
- Documentation: Memory Bank complete - READY FOR MEMORY RESET
- Repository: Organized with .gitignore and all source files

### Critical Actions After Memory Reset

1. **Verify Production**: Check if application is working at https://dj-tool.onrender.com/

2. **Check Local Files**:

   ```powershell
   # Check critical files
   Get-Content index.html | Select-String "API_BASE_URL"
   Get-Content app_working.py | Measure-Object -Line

   # Should show:
   # - API_BASE_URL = "https://dj-tool.onrender.com"
   # - app_working.py has ~682 lines (complete)
   ```

3. **Test Application**:

   ```powershell
   # Start local server
   python app_working.py

   # Test endpoint (in separate terminal)
   Invoke-RestMethod -Uri "http://localhost:8000/analyze?url=https://www.youtube.com/watch?v=dQw4w9WgXcQ" -Method Get | ConvertTo-Json
   ```

4. **Check Git Status**:

   ```powershell
   git status
   git log --oneline -5

   # Latest commits should include:
   # - "Fix: Complete app_working.py and update frontend API_BASE_URL to production"
   # - "Add: Source files and documentation"
   ```

### Immediate Verification Commands (Post-Reset)

```powershell
# Check production deployment
Invoke-WebRequest -Uri "https://dj-tool.onrender.com/" -Method Get -UseBasicParsing
Invoke-WebRequest -Uri "https://dj-tool.onrender.com/analyze?url=https://www.youtube.com/watch?v=dQw4w9WgXcQ" -Method Get -UseBasicParsing

# Check local development
python -c "import fastapi; import librosa; import yt_dlp; print('All core libraries loaded')"
python app_working.py

# Check file status
Get-Content index.html | Select-String "API_BASE_URL"
Get-Content app_working.py | Select-Object -First 5

# Check Git
git status
git log --oneline -5
```

### If Issues Are Found After Memory Reset

1. **If app_working.py is truncated**: Copy from app_with_jobs_complete.py

   ```powershell
   Copy-Item app_with_jobs_complete.py app_working.py -Force
   ```

2. **If API_BASE_URL is incorrect**: Update index.html line ~150

   ```javascript
   const API_BASE_URL = "https://dj-tool.onrender.com";
   ```

3. **If dependencies missing**: Install production dependencies

   ```powershell
   pip install -r requirements_clean.txt
   ```

4. **If Git changes needed**: Commit and push
   ```powershell
   git add .
   git commit -m "Fix after memory reset"
   git push origin main
   ```

### Success Criteria Verification

After memory reset, verify ALL of these are working:

- [ ] Production: https://dj-tool.onrender.com/ returns 200 OK
- [ ] Production: `/analyze` endpoint returns analysis results
- [ ] Local: `app_working.py` starts without errors
- [ ] Local: `/analyze` endpoint works on localhost:8000
- [ ] Frontend: `index.html` has correct API_BASE_URL
- [ ] Git: Repository is clean and up to date
- [ ] Documentation: Memory Bank files are complete and accurate

## Project Completion Status

### ✅ ALL TASKS COMPLETED

1. **✅ Code Repair**: Fixed truncated `app_working.py` with complete functionality
2. **✅ Frontend Integration**: Updated `API_BASE_URL` to production
3. **✅ Deployment**: Committed, pushed, and deployed to Render
4. **✅ Verification**: Production tested and working
5. **✅ Documentation**: Memory Bank complete for memory reset scenarios
6. **✅ Repository**: Organized with .gitignore and all source files

### ✅ APPLICATION READY FOR USE

The DJ BPM Analyzer is now a complete, production-ready application:

- **Backend**: FastAPI with audio analysis, caching, and background jobs
- **Frontend**: Modern DJ-themed UI with real-time progress tracking
- **Deployment**: Live at
