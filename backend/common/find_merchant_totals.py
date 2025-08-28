from fastapi import FastAPI
import Database.mongo_db as mongo_db
import json


# common/find_merchant_totals.py

from collections import defaultdict
from typing import Optional, Dict, List
import json, re

import Database.mongo_db as mongo_db  # you already have this

# ---- Small helper functions ----


def _normalize(text: str) -> str:
    """
    Make text easy to compare by:
    - lowercasing
    - removing spaces and punctuation
    So: "WHOLE FOODS" -> "wholefoods"
    """
    return re.sub(r"[^a-z0-9]", "", text.lower())


def _to_float(value) -> float:
    """
    Turn numbers or strings like "103.74" or "1,234.56" into a float.
    If it can't parse, return 0.0 (so your API doesn't crash).
    """
    if isinstance(value, (int, float)):
        return float(value)
    try:
        return float(str(value).replace(",", ""))
    except Exception:
        return 0.0


# ---- Main function your route will call ----


def readMerchantTotals(query: Optional[str] = None, limit: int = 10) -> Dict:
    """
    - If query is given (e.g., 'target'), return totals for merchants whose
      name CONTAINS that text (case-insensitive).
    - If query is None, return totals for ALL merchants.
    """

    # 1) Get your Mongo collection
    mongo_db.get_database()
    col = mongo_db.get_collection()

    search_key = _normalize(query) if query else None

    # We'll build these up as we scan documents
    totals = defaultdict(float)  # normalized merchant -> sum(total_cost)
    counts = defaultdict(int)  # normalized merchant -> how many transactions
    display: Dict[str, str] = {}  # normalized merchant -> nice original name

    # 2) Read only 'json_output' from each document
    for doc in col.find({}, {"json_output": 1, "_id": 0}):
        raw = doc.get("json_output")
        if not raw:
            continue

        # Your json_output is stored as a STRING, so parse it into a dict
        try:
            data = json.loads(raw) if isinstance(raw, str) else raw
        except Exception:
            continue  # skip bad rows

        name = data.get("merchant_name")
        if not isinstance(name, str):
            continue

        norm = _normalize(name)  # e.g., "TARGET" -> "target"

        # If searching, only keep matches (substring match)
        if search_key and search_key not in norm:
            continue

        totals[norm] += _to_float(data.get("total_cost"))
        counts[norm] += 1
        # Remember a pretty display name the first time we see this merchant
        display.setdefault(norm, name)

    # 3) Turn the dicts into a list, sorted by biggest spender first
    matches: List[Dict] = [
        {
            "merchant_name": display[k],
            "total_spent": round(totals[k], 2),
            "transactions": counts[k],
        }
        for k in sorted(totals, key=lambda kk: totals[kk], reverse=True)
    ]

    # If this was a search, apply a limit (keep it reasonable)
    if query:
        limit = max(1, min(limit, 100))
        matches = matches[:limit]

    # 4) Final response shape
    return {
        "query": query,
        "matches": matches,
        "message": (
            None
            if matches
            else (f"No merchants found for '{query}'." if query else "No data found.")
        ),
    }
