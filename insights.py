from tools.monday_api import get_board_items
from config import DEALS_BOARD_ID, WORK_BOARD_ID
from datetime import datetime

def generate_insight(question):

    if "deals" in question.lower() and "risk" not in question.lower():
        deals = get_board_items(DEALS_BOARD_ID)
        return f"You currently have {len(deals)} deals."

    elif "work" in question.lower() and "delayed" not in question.lower():
        work = get_board_items(WORK_BOARD_ID)
        return f"You currently have {len(work)} work orders."

    elif "delayed" in question.lower():
        work = get_board_items(WORK_BOARD_ID)
        delayed = []

        for item in work:
            try:
                due_date = None
                for col in item["column_values"]:
                    if "date" in col["id"]:
                        due_date = col.get("text")

                if due_date:
                    due = datetime.strptime(due_date, "%Y-%m-%d")
                    if due < datetime.now():
                        delayed.append(item["name"])
            except:
                pass

        return f"There are {len(delayed)} delayed work orders."

    elif "risk" in question.lower():
        deals = get_board_items(DEALS_BOARD_ID)
        risky = []

        for item in deals:
            try:
                stage = None
                for col in item["column_values"]:
                    if "status" in col["id"]:
                        stage = col.get("text")

                if stage and stage.lower() in ["stuck", "pending", "negotiation"]:
                    risky.append(item["name"])
            except:
                pass

        return f"There are {len(risky)} deals at risk of delay."

    else:
        return "Ask about deals, delayed work orders, or risky deals."