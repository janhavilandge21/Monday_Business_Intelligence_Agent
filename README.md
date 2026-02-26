#  Monday_Business_Intelligence_Agent

This project is an AI-powered Business Intelligence assistant built on top of monday.com.

It enables founders and decision-makers to ask business-level questions conversationally and receive insights directly from live operational data.

The system connects with monday.com boards using API calls at runtime and generates insights without preloading or caching any information.

---

## Overview

Business teams often need quick answers from operational data stored across multiple boards such as Work Orders and Deals.

However, this data is typically inconsistent, incomplete, and scattered.

This solution bridges that gap by allowing users to:

* Ask natural business questions
* Retrieve insights in real time
* Handle messy and missing data
* Combine insights across multiple boards

---

## Supported Questions

The agent currently supports founder-level queries such as:

* How many work orders do we have?
* Show delayed work orders
* Show deals at risk

The system dynamically retrieves data from monday.com and generates insights accordingly.

---

## System Architecture

The application follows a simple modular structure:

* Streamlit frontend for conversational interaction
* monday.com API integration for live data retrieval
* Insight engine for data interpretation and response generation

Each query triggers live API calls ensuring real-time insights.

---

## Features

* Live monday.com API integration
* No caching or preloading of data
* Handles missing values and inconsistent formats
* Conversational business query interface
* Cross-board insights
* Graceful fallback when data is incomplete

---


## Screenshots

### Work Orders Insight
![Work Orders](./assets/work_orders.png)

### Delayed Work Orders Insight
![Delayed Work Orders](./assets/delayed_orders.png)

### Deals at Risk Insight
![Deals Risk](./assets/deals_risk.png)

---

## How to Run Locally

Install dependencies:

pip install -r requirements.txt

Run the application:

streamlit run app.py

---

## Monday Boards Used

* Work Orders Board
* Deals Board

The system pulls data directly from these boards during query execution.

---

## Example Output

User Question:
Show delayed work orders

System Response:
There are 0 delayed work orders.

---

## Technology Stack

* Python
* Streamlit
* monday.com API
* Pandas

---

## Design Considerations

* Real-time data access
* Resilience to missing fields
* Flexible business query handling
* Simple conversational interface

---

## Future Improvements

* Multi-turn conversation support
* Sector-based insights
* Revenue trend analysis
* LLM-powered natural reasoning

---
