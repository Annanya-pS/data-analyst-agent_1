@echo off
echo Installing Data Analyst Agent Dependencies
echo ==========================================

REM Update pip first
echo Updating pip...
python -m pip install --upgrade pip

REM Install packages individually to handle any conflicts
echo.
echo Installing core dependencies...

python -m pip install Flask>=2.3.0
python -m pip install requests>=2.31.0
python -m pip install beautifulsoup4>=4.12.0
python -m pip install lxml>=4.9.0
python -m pip install html5lib>=1.1
python -m pip install Werkzeug>=2.3.0
python -m pip install gunicorn>=21.0.0

echo.
echo Installing scientific computing packages...
python -m pip install numpy>=1.25.0
python -m pip install pandas>=2.1.0
python -m pip install scipy>=1.11.0
python -m pip install matplotlib>=3.8.0
python -m pip install seaborn>=0.13.0

echo.
echo Installing database package...
python -m pip install duckdb>=0.9.0

echo.
echo Installation complete!
echo.
echo Testing imports...
python -c "import flask, pandas, numpy, matplotlib, requests, duckdb; print('✅ All imports successful!')"

pause
