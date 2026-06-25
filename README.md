# Inventory Forecasting Agent

An intelligent, autonomous AI agent designed to help businesses reduce stockouts and excess inventory by analyzing historical sales data, forecasting demand, and recommending reorder quantities.

## Features

- **Demand Forecasting**: Analyzes recent sales history to predict future demand.
- **Reorder Recommendations**: Evaluates current inventory levels against historical trends to suggest optimal reorder quantities.
- **Supplier Delay Monitoring**: Takes potential supplier delays into account when generating reorder alerts.
- **Read-Only Safety**: The agent provides recommendations only and is restricted from automatically placing orders.
- **Dual Triggers**: Can be triggered interactively or via automated Pub/Sub ambient alerts.

## Setup & Local Development

1. **Configure Environment Variables**:
   Create a `.env` file in the root of the project with your API key:
   ```env
   GOOGLE_GENAI_USE_VERTEXAI=False
   GOOGLE_API_KEY="your-google-ai-studio-api-key"
   MODEL="gemini-2.5-flash"
   ```

2. **Run the FastAPI Server**:
   Ensure you have the virtual environment activated, then start the server:
   ```bash
   python app/fast_api_app.py
   ```

3. **Trigger the Agent**:
   With the server running on `http://localhost:8080`, you can send a Pub/Sub HTTP POST request to `/apps/app/trigger/pubsub` with a JSON payload to activate the forecasting flow.
