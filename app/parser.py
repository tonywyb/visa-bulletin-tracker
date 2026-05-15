import re
from bs4 import BeautifulSoup

def _clean_date(val):
    val = val.strip()
    if val in ["C", "CURRENT"]:
        return "C"
    if val in ["U", "UNAVAILABLE", "Unavailable"]:
        return None
    return val

def find_tables(html):
    soup = BeautifulSoup(html, "lxml")
    return soup.find_all("table")

def extract_eb3_china(tables):
    result = {"final_action": None, "filing": None}

    for table in tables:
        text = table.get_text(" ", strip=True)
        if "EB-3" not in text:
            continue
        if "CHINA" not in text:
            continue

        rows = table.find_all("tr")
        for row in rows:
            cols = [c.get_text(strip=True) for c in row.find_all("td")]
            if not cols:
                continue

            joined = " ".join(cols)
            if "CHINA" in joined:
                nums = [c for c in cols if re.search(r"\d|C|U", c)]
                if len(nums) >= 2:
                    result["final_action"] = _clean_date(nums[-2])
                    result["filing"] = _clean_date(nums[-1])
    return result
