import pandas as pd

def load_work_orders():

    df = pd.read_excel("Work_Order_Tracker Data.xlsx")

    # Clean column names
    df.columns = df.columns.str.strip().str.lower()

    today = pd.Timestamp.today()

    # Detect possible columns
    due_col = [col for col in df.columns if "due" in col]
    complete_col = [col for col in df.columns if "complete" in col]

    delayed = pd.DataFrame()

    if due_col and complete_col:
        df[due_col[0]] = pd.to_datetime(df[due_col[0]], errors='coerce')
        df[complete_col[0]] = pd.to_datetime(df[complete_col[0]], errors='coerce')

        delayed = df[
            (df[due_col[0]] < today) &
            (df[complete_col[0]].isna())
        ]

    priority_col = [col for col in df.columns if "priority" in col]
    status_col = [col for col in df.columns if "status" in col]

    high_priority = df[df[priority_col[0]].str.lower() == "high"] if priority_col else pd.DataFrame()
    pending = df[df[status_col[0]].str.lower() == "pending"] if status_col else pd.DataFrame()

    return {
        "total": len(df),
        "delayed": len(delayed),
        "high_priority": len(high_priority),
        "pending": len(pending)
    }