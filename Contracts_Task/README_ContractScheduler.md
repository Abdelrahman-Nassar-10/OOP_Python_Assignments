# Contract Installment Scheduler (Python)

Generate per‑contract installment schedules from a CSV, and export each schedule as its own CSV file.

> **Script:** `contract_project.py`  
> **Input:** `Contracts.csv`  
> **Output folder:** `contract_schedules/` (auto-created)

---

## What it does
1. Reads `Contracts.csv` into a DataFrame.
2. Fills missing deposits with `0`.
3. Maps the **payment frequency** to a calendar delta:
   - `ANNUAL` → +1 year  
   - `HALF ANNUAL` / `HALF_ANNUAL` → +6 months  
   - `QUARTER` → +3 months  
   - `MONTHLY` → +1 month
4. **Deducts the deposit** from the total fees once, then **splits the net amount evenly** across installments.
5. Generates installment dates **starting from the contract start date** and repeating by the selected frequency **until (but not including) the end date**.
6. Writes each schedule to `contract_schedules/<client_name>_<contract_id>.csv` with columns:
   - `installment_no`
   - `installment_date` (format: `DD-MM-YYYY`)
   - `installment_amount` (rounded to 2 decimals)

---

## Project layout
```
.
├─ contract_project.py
├─ Contracts.csv
└─ contract_schedules/           # created on first run
   ├─ <ClientA>_<ID>.csv
   └─ <ClientB>_<ID>.csv
```

---

## CSV schema (required columns)
| Column name              | Type / Example              | Notes |
|--------------------------|-----------------------------|------|
| `contract_id`            | `12345`                     | Used in output filename |
| `client_name`            | `Acme Corp`                 | Spaces are converted to `_` for filenames |
| `contract_startdate`     | `01-01-2025`                | Parsed with `dayfirst=True`; allow `DD-MM-YYYY` or `DD/MM/YYYY` |
| `contract_enddate`       | `01-01-2026`                | End date is **exclusive** in schedule generation |
| `contract_total_fees`    | `12000`                     | Total fees before deposit deduction |
| `contract_deposit_fees`  | `2000` or blank             | Missing values treated as `0` |
| `contract_payment_type`  | `MONTHLY` / `QUARTER` / `HALF ANNUAL` / `ANNUAL` | Case-insensitive; underscores/spaces both handled for HALF‑ANNUAL |

---

## How to run
```bash
# In the same folder as contract_project.py and Contracts.csv
python contract_project.py
```

You’ll see:
```
✅ Installment schedules saved in folder: contract_schedules
```

---

## Example output (per-client file)
`contract_schedules/Acme_Corp_12345.csv`
```csv
installment_no,installment_date,installment_amount
1,01-01-2025,833.33
2,01-02-2025,833.33
...
```

---

## Notes & assumptions
- **Rounding:** amounts are rounded to 2 decimals. Minor rounding penny differences may occur; if you need the last installment to absorb the remainder, adjust the loop to compute the last row as `net - sum(previous)`.
- **End date rule:** installments are generated while `date < end_date`. To include an installment exactly on the end date, change the condition to `<=`.
- **Invalid payment type:** add it to the `freq_map` or validate before processing.
- **Zero installments:** if `start_date >= end_date` no schedule is written.
- **Date parsing:** uses `pandas.to_datetime(..., dayfirst=True)`—ensure your dates are `DD-MM-YYYY` or `DD/MM/YYYY`.

---

## Dependencies
- Python 3.9+
- `pandas`
- `python-dateutil` (for `relativedelta`)

Install:
```bash
pip install pandas python-dateutil
```

---

## Customization ideas
- Different discount/deposit rules (e.g., distribute deposit across first N installments).
- Per‑client frequency overrides.
- Write XLSX using `to_excel` or add a combined master schedule.

---

