REM Replace file path with the project directory path

@echo off
cd /d "..\automated-corporate-financial-reporting-system"

python -m pipeline.main_pipeline

pause
