@echo off

call venv\Scripts\activate.bat
cd .\src\

uvicorn webui:app --reload

exit