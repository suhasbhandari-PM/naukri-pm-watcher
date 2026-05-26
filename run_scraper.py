"""
PM Job Dashboard — launches the pipeline dashboard.
Double-click to view the latest results.
"""
import webbrowser
from pathlib import Path

dashboard = Path(__file__).parent / "index.html"
if dashboard.exists():
    webbrowser.open(str(dashboard))
else:
    print("No dashboard yet. Run 'PM Job Scraper.bat' first to generate it.")
    input("Press Enter to exit...")
