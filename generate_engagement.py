import csv
import sqlite3
from datetime import date, timedelta

import numpy as np

DB_PATH  = "data/marketing.db"
OUT_PATH = "data/engagement_log.csv"
YEAR     = 2024
LAM_BASE = 3
LAM_DEC  = LAM_BASE * 2

EVENT_TYPES = ["page_view", "email_open", "ad_click", "purchase", "social_share"]

rng = np.random.default_rng(42)

conn = sqlite3.connect(DB_PATH)
customer_ids = [row[0] for row in conn.execute("SELECT ID FROM customers ORDER BY ID")]
conn.close()

# Build full date range for the year
start = date(YEAR, 1, 1)
dates = [start + timedelta(days=d) for d in range(366 if YEAR % 4 == 0 else 365)
         if (start + timedelta(days=d)).year == YEAR]

with open(OUT_PATH, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["customer_id", "event_date", "event_type", "event_count"])

    for cid in customer_ids:
        for day in dates:
            lam = LAM_DEC if day.month == 12 else LAM_BASE
            # Draw one count per event type; skip zeros to keep the log sparse
            for etype in EVENT_TYPES:
                count = int(rng.poisson(lam))
                if count > 0:
                    writer.writerow([cid, day.isoformat(), etype, count])

print(f"Done — written to {OUT_PATH}")
