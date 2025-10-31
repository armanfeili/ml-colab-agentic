from pathlib import Path
import csv
from typing import Dict, Any, List

def ensure_dir(path: str) -> None:
    Path(path).mkdir(parents=True, exist_ok=True)

def log_metrics_csv(path: str, rows: List[Dict[str, Any]]) -> None:
    ensure_dir(Path(path).parent.as_posix())
    if not rows:
        return
    fieldnames = list(rows[0].keys())
    new_file = not Path(path).exists()
    with open(path, "a", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        if new_file:
            writer.writeheader()
        for r in rows:
            writer.writerow(r)
