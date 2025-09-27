# Python OOP Assignments + Contract Installment Scheduler

A single repository that contains **three small OOP assignments (pure Python)** and a **contracts installment scheduler** script (uses pandas). Everything is runnable from the terminal without frameworks.

---

## 📦 Project Structure
```
.
├─ 1_VacationPackage/
│  └─ main.py
├─ 2_HotelTour/
│  └─ main.py
├─ 3_PatientsDoctors/
│  └─ main.py
├─ ContractScheduler/
│  ├─ contract_project.py
│  ├─ Contracts.csv                # your input CSV (optional to keep public)
│  └─ contract_schedules/          # output folder (auto-created on first run)
├─ .gitignore
└─ README.md
```

> The three HW folders are pure-Python with **no external dependencies**.  
> The **ContractScheduler** requires `pandas` and `python-dateutil` (see below).

---

## 🛠️ Environment Setup (optional but recommended)

Create and activate a virtual environment (any OS):

```bash
# create venv
python -m venv .venv
# Windows
.\.venv\Scripts\activate
# macOS / Linux
source .venv/bin/activate
```

Install dependencies (needed for **ContractScheduler** only):

```bash
pip install pandas python-dateutil
```

---

## 🚀 How to Run

### 1 — Vacation Package
**Goal:** Abstract base class `VacationPackage` with two subclasses `AdventurePackage` and `RelaxationPackage`.  
**Run:**
```bash
python HW1_VacationPackage/main.py
```
**Expected output:**
```
Destination: Turkey
Price: $2500
Activities: Hiking, Rafting
---
Destination: Hurghada
Price: $3000
Spa Services: Massage, Yoga
```

---

### 2 — Hotel vs Tour Packages
**Goal:** Abstract base `TravelPackage` with two implementations — `HotelPackage` and `TourPackage`.  
`HotelPackage` multiplies nights × cost_per_night.  
`TourPackage` multiplies days × cost_per_day then applies **10% discount** in display.

**Run:**
```bash
python HW2_HotelTour/main.py
```
**Expected output:**
```
Total Cost for Hotel package: $1000.00
Total Cost for Tour package After 10% discount : $630.00
```

---

### 3 — Patients & Doctors
**Goal:** Inheritance from base `Person(name, age)` with subclasses `Patient(medical_history)` and `Doctor(specialty)`.  
`get_details()` returns a formatted string; a helper prints for both.

**Run:**
```bash
python HW3_PatientsDoctors/main.py
```
**Expected output:**
```
Patient Name: Omar, Age: 30, Medical History: Hypertension
Doctor Name: Dr. Hesham, Age: 45, Specialty: Cardiology
```

---

## 📑 ContractScheduler — Contract Installment Generator

**Script:** `ContractScheduler/contract_project.py`  
Reads `Contracts.csv`, calculates installment plan per contract, and writes one CSV per client/contract under `contract_schedules/`.

### Input CSV — Required Columns
| Column name              | Example            | Notes |
|--------------------------|--------------------|------|
| `contract_id`            | `12345`            | Used in output filename |
| `client_name`            | `Acme Corp`        | Spaces become `_` in filenames |
| `contract_startdate`     | `01-01-2025`       | Parsed with `dayfirst=True` (`DD-MM-YYYY` or `DD/MM/YYYY`) |
| `contract_enddate`       | `01-01-2026`       | **End date is exclusive** by default |
| `contract_total_fees`    | `12000`            | Gross fees before deposit |
| `contract_deposit_fees`  | `2000` or empty    | Missing treated as `0` |
| `contract_payment_type`  | `MONTHLY` \| `QUARTER` \| `HALF ANNUAL` \| `ANNUAL` | Case-insensitive; `HALF_ANNUAL` also accepted |

### Frequency Mapping
- `ANNUAL` → +1 year  
- `HALF ANNUAL` / `HALF_ANNUAL` → +6 months  
- `QUARTER` → +3 months  
- `MONTHLY` → +1 month

### How it computes
1. Fill missing deposits with `0`.
2. **Net = total_fees − deposit_fees** (deposit deducted once).
3. Create installment dates from **start date** forward by the frequency **while date < end date**.
4. Split the **net** evenly across installments (rounded to 2 decimals).
5. Write `contract_schedules/<client>_<id>.csv` with columns:
   - `installment_no`
   - `installment_date` (DD-MM-YYYY)
   - `installment_amount`

> 💡 To include an installment exactly **on** the end date, change the comparison to `<=` in the script.  
> 💡 If you want the final installment to absorb rounding remainders, compute the last one as `net - sum(previous)`.

### Run
```bash
# Make sure you installed pandas + python-dateutil (see setup section)
python ContractScheduler/contract_project.py
```
**Output example:** `ContractScheduler/contract_schedules/Acme_Corp_12345.csv`
```csv
installment_no,installment_date,installment_amount
1,01-01-2025,833.33
2,01-02-2025,833.33
...
```

---

## 🧪 Quick Checks
- Python version: `python --version` (3.9+ recommended)
- Packages (for scheduler): `pip show pandas python-dateutil`
- Folder paths: run from the repo root (as shown in commands).

---

## 🧰 Git: First Push (cheat sheet)
```bash
# from repo root (where this README.md lives)
git init
git add .
git commit -m "Initial commit: OOP assignments + contract scheduler"
git branch -M main
git remote add origin https://github.com/<YOUR_USER>/<YOUR_REPO>.git
git push -u origin main
```

If the remote already has a README and you get a rejection, do:
```bash
git pull origin main --allow-unrelated-histories
git push -u origin main
```


