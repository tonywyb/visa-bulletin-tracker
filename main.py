from datetime import datetime
from app.scraper import fetch
from app.parser import find_tables, extract_eb3_china
from app.db import init_db, insert_or_update, load_all
from app.plotter import plot
from app.notifier import send_telegram

def run():
    init_db()

    url = "https://travel.state.gov/content/travel/en/legal/visa-law0/visa-bulletin.html"
    html = fetch(url)

    tables = find_tables(html)
    result = extract_eb3_china(tables)

    month_key = datetime.utcnow().strftime("%Y-%m")

    insert_or_update(month_key, result["final_action"], result["filing"], url)

    data = load_all()
    plot(data)

    msg = f"""Visa Bulletin Update {month_key}
EB-3 China:
Final: {result['final_action']}
Filing: {result['filing']}"""

    send_telegram(msg)

if __name__ == "__main__":
    run()
