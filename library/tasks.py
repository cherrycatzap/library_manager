from celery import shared_task
import json
import os
from datetime import datetime

@shared_task
def generate_monthly_report():
    report = {
        "report_type": "monthly",
        "generated_at": str(datetime.now()),
        "stats": {
            "borrowed_books": 123,
            "popular_authors": ["Author A", "Author B"]
        }
    }

    # Create the reports folder if it doesn't exist
    reports_dir = os.path.join(os.path.dirname(__file__), "..", "reports")
    os.makedirs(reports_dir, exist_ok=True)

    file_path = os.path.join(reports_dir, "monthly_report.json")

    with open(file_path, "w") as f:
        json.dump(report, f)
