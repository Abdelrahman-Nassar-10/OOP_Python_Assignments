import pandas as pd
from dateutil.relativedelta import relativedelta
import os

#: Load Data
file_path = "Contracts.csv"   # <-- change extension if your file is .xlsx
contracts_df = pd.read_csv(file_path)

# Fill missing deposit values with 0
contracts_df["contract_deposit_fees"] = contracts_df["contract_deposit_fees"].fillna(0)

#: Payment Frequency Mapping
freq_map = {
    "ANNUAL": relativedelta(years=1),
    "HALF ANNUAL": relativedelta(months=6),
    "HALF_ANNUAL": relativedelta(months=6),  # handle both formats
    "QUARTER": relativedelta(months=3),
    "MONTHLY": relativedelta(months=1)
}

#: Process Contracts
output_dir = "contract_schedules"
os.makedirs(output_dir, exist_ok=True)

for _, row in contracts_df.iterrows():
    contract_id = row["contract_id"]
    client_name = str(row["client_name"]).replace(" ", "_")
    start_date = pd.to_datetime(row["contract_startdate"], dayfirst=True)
    end_date = pd.to_datetime(row["contract_enddate"], dayfirst=True)
    total_fees = row["contract_total_fees"]
    deposit = row["contract_deposit_fees"]
    payment_type = str(row["contract_payment_type"]).upper().replace("_", " ")
    
    # Step 3.1: Deduct deposit
    net_fees = total_fees - deposit
    
    # Generate installment dates (first installment on start date)
    dates = []
    date = start_date
    while date < end_date:
        dates.append(date)
        date += freq_map[payment_type]
    
    num_installments = len(dates)
    if num_installments == 0:
        continue  # skip invalid contracts
    
    #: Calculate installment amount
    installment_amount = net_fees / num_installments
    
    #: Build schedule 
    schedule = []
    for i, inst_date in enumerate(dates, 1):
        schedule.append({
            "installment_no": i,
            "installment_date": inst_date.strftime("%d-%m-%Y"),
            "installment_amount": round(installment_amount, 2)
        })
    
    #: Save schedule to CSV
    df_schedule = pd.DataFrame(schedule)
    output_file = os.path.join(output_dir, f"{client_name}_{contract_id}.csv")
    df_schedule.to_csv(output_file, index=False)

print(f"✅ Installment schedules saved in folder: {output_dir}")
