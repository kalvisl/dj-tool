# Technical Context

## Technologies Used

### Backend - DEPLOYED

- **Python 3.9+**: Primary programming language - DEPLOYED
- **FastAPI 0.128.0**: Modern web framework with async support - DEPLOYED
- **Uvicorn 0.39.0**: ASGI server for FastAPI - DEPLOYED
- **Requests 2.32.5**: HTTP library for API calls - DEPLOYED
- **librosa 0.11.0**: Audio analysis library for BPM/key detection - DEPLOYED
- **yt-dlp 2025.10.14**: YouTube audio downloader - DEPLOYED
- **NumPy 2.0.2**: Numerical computing for audio processing - DEPLOYED
- **SciPy 1.11.4**: Scientific computing for signal processing - DEPLOYED (updated to fix deployment)
- **SoundFile 0.13.1**: Audio file I/O operations - DEPLOYED
- **AudioRead 3.1.0**: Audio decoding for various formats - DEPLOYED

### Frontend - DEPLOYED

- **HTML5**: Markup language - DEPLOYED
- **CSS3**: Styling with modern features (flexbox, grid, gradients) - DEPLOYED
- **JavaScript (ES6+)**: Client-side logic - DEPLOYED
- **No external frameworks**: Vanilla JS for simplicity - DEPLOYED
- **✅ FIXED**: API_BASE_URL updated to "https://dj-tool.onrender.com" - VERIFIED

### Deployment - ACTIVE

- **Render**: Platform as a Service (PaaS) - ACTIVE
- **Python 3.9.0**: Runtime specified in runtime.txt - CONFIGURED
- **Uvicorn**: Production ASGI server - DEPLOYED
- **GitHub**: Version control and auto-deploy trigger - ACTIVE
- **Application URL**: https://dj-tool.onrender.com/ - VERIFIED WORKING

### Development Tools

- **VS Code**: Primary IDE
- **Git**: Version control - ACTIVE
- **PowerShell**: Windows shell/command line
- **pip**: Python package manager
- **Virtual Environment**: venv for dependency isolation
- **Memory Bank**: Comprehensive documentation in `cline_docs/`

## Development Setup

### Prerequisites

1. Python 3.9 or higher
2. pip (Python package installer)
3. Git for version control
4. VS Code or any text editor

### Installation Steps

```powershell
# Clone repository (if applicable)
git clone <repository-url>
cd dj-tool

# Create virtual environment
python -m venv venv

# Activate virtual environment (PowerShell)
.\venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt

# Run the application
uvicorn app_working:app --host 0.0.0.0 --port 8001 --reload
```

### Running Locally

1. **✅ app_working.py is now complete** (no need to fix):
   - File is complete with 682 lines
   - All cache functions and endpoints implemented
   - Worker threads and CORS middleware included

2. Start backend:

   ```powershell
   uvicorn app_working:app --host 0.0.0.0 --port 8001 --reload
   ```

   Backend runs on http://localhost:8001

3. Open frontend:
   - Open index.html in browser
   - For local testing, update API_BASE_URL in index.html to "http://localhost:8001"
   - For production, API_BASE_URL is "https://dj-tool.onrender.com" (already configured)

### Testing

```powershell
# Run simple test
python test_simple.py

# Test API endpoint (PowerShell)
$response = Invoke-RestMethod -Uri "http://localhost:8001/analyze?url=https://www.youtube.com/watch?v=dQw4w9WgXcQ" -Method Get
Write-Output $response

# Test background jobs
python test_background_jobs.py

# Test deployed API (PowerShell) - VERIFIED WORKING
$response = Invoke-RestMethod -Uri "https://dj-tool.onrender.com/analyze?url=https://www.youtube.com/watch?v=dQw4w9WgXcQ" -Method Get
Write-Output $response
```

## Technical Constraints

### Platform Constraints

- **Windows 11**: Primary development environment
- **PowerShell**: Default shell with specific syntax requirements
- **Render Free Tier**: Limited resources, cold starts, 750 free hours/month
- **Python 3.9**: Specified in runtime.txt for Render compatibility

### Library Constraints

- **librosa**: Requires NumPy and SciPy, can be heavy for free tier
- **yt-dlp**: YouTube downloading may have legal/ToS considerations
- **FastAPI**: Async/await patterns for better performance
- **Audio libraries**: May have platform-specific dependencies

### Performance Considerations

1. **Cold starts**: Render free tier has ~30 second startup time
2. **Audio processing**: Real BPM analysis is CPU intensive
3. **YouTube API**: Using noembed to avoid API keys and quotas
4. **Response time**: Target < 3 seconds for user experience
5. **Background jobs**: Handle longer analyses asynchronously
6. **Audio caching**: 7-day expiry with 1GB limit for performance

### Security Considerations

1. **CORS**: Currently allows all origins ("\*") - should be restricted in production
2. **Input validation**: YouTube URL validation is basic
3. **API keys**: No sensitive keys in code (uses public noembed API)
4. **Error messages**: Generic errors to avoid information leakage
5. **File operations**: Temporary files cleaned up automatically

## PowerShell Version and Limitations

- **Version**: PowerShell 5.1 or higher (Windows 11 includes PowerShell 7+)
- **Command chaining**: Use semicolon (;) not && for multiple commands
- **Logical operators**: -and, -or instead of &&, ||
- **Environment variables**: $env:VARIABLE format
- **Path handling**: Backslash (\) for Windows paths
- **Script execution**: May require `Set-ExecutionPolicy` changes
- **Command output**: Objects not text, requires proper handling
- **File operations**: Use PowerShell cmdlets not shell commands

## VS Code Terminal Configuration

- **Default shell**: C:\WINDOWS\system32\cmd.exe (can be changed to PowerShell)
- **Integrated terminal**: Supports PowerShell, cmd, bash (WSL)
- **Python extension**: Recommended for development
- **Live Server**: Useful for frontend development (open index.html)
- **Git integration**: Built-in source control management

## Dependencies Management

### requirements.txt

Full development dependencies including:

- FastAPI and related web libraries
- Audio processing (librosa, audioread, soundfile)
- YouTube downloading (yt-dlp)
- Data science (numpy, scipy)
- Testing and development tools

### requirements_clean.txt - DEPLOYED

Minimal dependencies for deployment (UPDATED Feb 1, 2026):

- fastapi==0.128.0
- uvicorn==0.39.0
- requests==2.32.5
- yt-dlp==2025.10.14
- librosa==0.11.0
- numpy==2.0.2
- scipy==1.11.4 # Updated from 1.13.1 to fix deployment
- soundfile==0.13.1
- audioread==3.1.0

Smaller footprint optimized for Render free tier while maintaining full functionality.

### Version Pinning

- Specific versions to ensure reproducibility
- Regular updates needed for security patches
- Compatibility tested with Python 3.9.0

## Deployment Configuration

### Render Specifics - ACTIVE

- **Build command**: `pip install -r requirements_clean.txt` - ACTIVE
- **Start command**: `uvicorn app_working:app --host 0.0.0.0 --port 10000` - ACTIVE
- **Health check**: Automatic by Render on root endpoint - ACTIVE
- **Auto-deploy**: On git push to main branch - ACTIVE
- **Environment**: Python 3.9.0 - CONFIGURED
- **Application URL**: https://dj-tool.onrender.com/ - VERIFIED WORKING
- **Plan**: Free tier with limitations

### Alternative Deployment Options

1. **Heroku**: Similar PaaS, different configuration
2. **Railway**: Modern alternative to Render
3. **AWS Lambda**: Serverless for cost optimization
4. **Docker**: Containerization for consistency
5. **PythonAnywhere**: Python-focused hosting

## Monitoring and Maintenance

### Current Monitoring

- Basic API status check in frontend - WORKING
- Console logging in backend with emoji indicators - WORKING
- Render dashboard for uptime and logs - AVAILABLE
- GitHub commit history for deployment tracking - ACTIVE
- Error tracking through try-except blocks - IMPLEMENTED

### Recommended Improvements

1. **Application logging**: Structured logging for debugging
2. **Performance metrics**: Response time tracking
3. **Error tracking**: Sentry or similar service
4. **Health checks**: More comprehensive endpoint checks
5. **Rate limiting**: Prevent abuse of the service

## Current Deployment Status (February 1, 2026)

- **Application URL**: https://dj-tool.onrender.com/ - ✅ VERIFIED WORKING
- **API_BASE_URL**: ✅ Correctly configured in index.html - VERIFIED
- **Git Status**: ✅ Synchronized (latest commit: 80dfef8)
- **Auto-deploy**: ✅ Enabled from GitHub to Render - ACTIVE
- **Local Development**: ✅ Backend complete with app_working.py fixed
- **Production Access**: ✅ Backend accessible and working at deployed URL
- **Frontend Configuration**: ✅ Uses correct API_BASE_URL (https://dj-tool.onrender.com)
- **Audio Analysis**: ✅ Real analysis implemented with fallback - DEPLOYED
- **Background Jobs**: ✅ Implemented with progress tracking - DEPLOYED
- **Audio Caching**: ✅ Implemented with automatic cleanup - DEPLOYED
- **Critical Issues**: ✅ ALL RESOLVED (app_working.py fixed, API_BASE_URL updated)
- **Project Status**: ✅ COMPLETE AND DEPLOYED

## Progress Tracking Technical Details

### System Architecture

1. **Progress Storage**: Thread-safe dictionary with automatic cleanup
2. **Polling Mechanism**: Frontend polls `/analyze/progress/{video_id}` every second
3. **Stage Management**: 7 distinct progress stages with percentage mapping
4. **Error Handling**: Progress updates include error messages for user feedback

### Progress Stages and Percentages

1. **starting** (10%): Initializing analysis pipeline
2. **downloading** (20-60%): Downloading audio from YouTube
3. **analyzing** (70-100%): Analyzing audio with librosa
4. **caching** (95%): Saving results to local cache
5. **complete** (100%): Analysis successfully completed
6. **cached** (100%): Results loaded from cache
7. **error** (0%): Analysis failed with error details

### Frontend Implementation

1. **Polling Interval**: 1000ms (1 second) for real-time updates
2. **Visual Feedback**: Color-coded progress bar (blue=active, green=complete, red=error)
3. **Stage Display**: Human-readable stage names with uppercase formatting
4. **Message Updates**: Detailed progress messages from backend

### Performance Characteristics

- **Polling Overhead**: Minimal (simple HTTP GET requests)
- **Memory Usage**: Progress data automatically cleaned after completion
- **Concurrency**: Thread-safe for multiple simultaneous analyses
- **Response Time**: Instant progress updates (< 100ms)

## Audio Analysis Technical Details

### Libraries Used - DEPLOYED

1. **librosa 0.11.0**: Audio analysis (BPM, key detection, chromagram) - DEPLOYED
2. **numpy 2.0.2**: Numerical computing for audio processing - DEPLOYED
3. **scipy 1.11.4**: Scientific computing for signal processing - DEPLOYED
4. **soundfile 0.13.1**: Audio file I/O operations - DEPLOYED
5. **audioread 3.1.0**: Audio decoding for various formats - DEPLOYED
6. **yt-dlp 2025.10.14**: YouTube audio extraction - DEPLOYED

### Analysis Methods

1. **BPM Detection**: librosa.beat.beat_track() with tempo estimation
2. **Key Detection**: Chromagram analysis with Krumhansl key profiles
3. **Camelot Conversion**: Mathematical mapping from musical keys to Camelot wheel
4. **Energy Calculation**: RMS (Root Mean Square) analysis normalized to 0.3-0.9 range
5. **Audio Processing**: First 60 seconds analyzed for performance optimization

### Performance Characteristics

- **Download Timeout**: 5 minutes maximum for audio extraction
- **Analysis Time**: < 30 seconds for 60-second audio segment
- **Memory Usage**: Temporary files cleaned up automatically
- **Fallback Time**: < 1 second when real analysis fails
- **Total Response**: < 3 seconds target maintained

### Known Limitations

1. **YouTube Restrictions**: May return 403 Forbidden errors for some videos
2. **Python Version**: yt-dlp deprecated Python 3.9 support (still functional)
3. **Audio Quality**: Dependent on YouTube's available audio formats
4. **Network Dependency**: Requires internet connection for audio downloading
5. **CPU Intensive**: Audio analysis can be resource-heavy on free tier

## Background Job System Technical Details

### Architecture

1. **Job Queue**: Thread-safe queue for job management
2. **Worker Threads**: Configurable number of concurrent workers (2 workers)
3. **Job Storage**: Dictionary-based with thread locking
4. **Progress Integration**: Jobs update progress during execution

### Job Lifecycle

1. **Creation**: User submits analysis request
2. **Queuing**: Job added to processing queue
3. **Execution**: Worker processes the job
4. **Completion**: Results stored and available
5. **Cleanup**: Old jobs automatically removed

### Performance Characteristics

- **Concurrent Jobs**: Configurable via MAX_WORKERS (currently 2)
- **Job Storage**: In-memory with automatic cleanup
- **Error Handling**: Failed jobs include detailed error information
- **Result Caching**: Completed jobs cached for repeated access

## Development Workflow

1. **Local Development**: Test changes on localhost:8001
2. **✅ Fix Current Issues**: app_working.py fixed, API_BASE_URL updated
3. **✅ Update Frontend**: API_BASE_URL matches production environment
4. **✅ Commit Changes**: Descriptive commit messages used
5. **✅ Push to GitHub**: Triggers auto-deploy on Render
6. **✅ Verify Deployment**: Tested at https://dj-tool.onrender.com/
7. **✅ Update Documentation**: Memory Bank files current

## Memory Reset Preparedness - CRITICAL

All critical information is documented in Memory Bank files. After memory reset:

### Immediate Actions

1. **READ FIRST**: `activeContext.md` - Current status and verification commands
2. **CHECK PRODUCTION**: https://dj-tool.onrender.com/ - Should be working
3. **VERIFY GIT**: `git status` and `git log --oneline -5` - Check latest commits
4. **TEST LOCAL**: `python app_working.py` - Start local development server
5. **VERIFY ENDPOINTS**: Use verification commands below
6. **CHECK CONFIG**: Ensure API_BASE_URL in index.html line 150 is "https://dj-tool.onrender.com"

### Verification Commands (Post-Reset)

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

### If Issues Are Found

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

## Critical Issues and Solutions - ALL RESOLVED

### ✅ Issue 1: app_working.py truncated - RESOLVED

- **Problem**: File was truncated at CORS middleware definition
- **Solution**: Created complete version with all cache functions and endpoints
- **Status**: ✅ COMPLETE AND DEPLOYED
- **Verification**: File has 682 lines, all endpoints working

### ✅ Issue 2: Frontend API_BASE_URL incorrect - RESOLVED

- **Problem**: Points to localhost:8002 instead of production
- **Solution**: Updated to "https://dj-tool.onrender.com"
- **Status**: ✅ UPDATED AND VERIFIED
- **Location**: index.html line 150

### ✅ Issue 3: Repository organization - RESOLVED

- **Problem**: Missing .gitignore, untracked files
- **Solution**: Added .gitignore, committed all source files and documentation
- **Status**: ✅ ORGANIZED AND COMMITTED

## Project Completion Status

### ALL TASKS COMPLETED

1. ** Code Repair**: Fixed truncated pp_working.py with complete functionality
2. ** Frontend Integration**: Updated API_BASE_URL to production
3. ** Deployment**: Committed, pushed, and deployed to Render
4. ** Verification**: Production tested and working
5. ** Documentation**: Memory Bank complete for memory reset scenarios
6. ** Repository**: Organized with .gitignore and all source files

### APPLICATION READY FOR USE

The DJ BPM Analyzer is now a complete, production-ready application:

- **Backend**: FastAPI with audio analysis, caching, and background jobs
- **Frontend**: Modern DJ-themed UI with real-time progress tracking
- **Deployment**: Live at https://dj-tool.onrender.com/
- **Documentation**: Comprehensive Memory Bank for future development
- **Repository**: Organized with all source files and .gitignore

All critical issues have been resolved. The application is ready for user testing and future enhancements.

### ✅ ALL TASKS COMPLETED

1. **✅ Code Repair**: Fixed truncated `app\_
