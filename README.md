# Level 4: The Data Analyst (MCP Boss Fight)

Welcome to the final boss! The standard Large Language Model is terrible at executing complex financial formulas reliably. Your task is to deploy this custom Python Calculator Tool (an MCP Server) as a Google Cloud Run Service and connect it to your Agent.

**But there's a catch:** The calculation logic is incomplete! You must implement the formula yourself before deploying.

## Step 1: Clone the Repository

1. Open the **Google Cloud Console** (make sure you are in your assigned project).
2. Open the **Cloud Shell** (the terminal icon `>_` in the top right corner).
3. Clone this repository into your Cloud Shell by running:
   ```bash
   git clone https://github.com/aherzberg-go/start-up-tu-berlin-mcp.git
   ```
4. Navigate into the cloned directory:
   ```bash
   cd start-up-tu-berlin-mcp
   ```

## Step 2: Implement the Calculation

The file `main.py` contains the MCP tool skeleton, but the actual calculation is missing. You need to implement it!

1. Open the **Cloud Shell Editor** by clicking the pencil icon (✏️ **Open Editor**) at the top of the Cloud Shell terminal.
2. In the file explorer on the left, navigate to `start-up-tu-berlin-mcp/main.py`.
3. Find the section marked with `🚨 YOUR TASK` — it contains the formula as comments.
4. Replace the `raise NotImplementedError(...)` line with your Python implementation:
   ```python
   net_cost = incremental_power_cost_bn - end_user_savings_bn
   total_benefits = climate_benefits_bn + air_quality_benefits_bn
   net_benefit = total_benefits - net_cost
   return round(net_benefit, 2)
   ```
5. **Save the file** (`Ctrl+S` / `Cmd+S`).
6. Switch back to the **Cloud Shell Terminal** (click **Open Terminal** at the top).

> ⚠️ **Important:** If you deploy without implementing the calculation, the tool will crash when your Agent calls it!

## Step 3: Deploy to Google Cloud Run

Now deploy the server from the source code by running the following command in the Cloud Shell:

```bash
gcloud run deploy ecogrid-macro-economic-mcp \
    --source . \
    --allow-unauthenticated \
    --region europe-west1
```

*(Note: On the first run, you may be asked whether APIs should be enabled or if you want to create a default Artifact Registry repository. Confirm with `y` (Yes).)*

## Step 4: Connect the Tool in Agent Studio

After a successful deployment, the terminal will output a Service URL (e.g., `https://ecogrid-macro-economic-mcp-xyz-ew.a.run.app`). Copy this URL.

1. Go back to **Agent Studio** in the Cloud Console.
2. Navigate to the **Tools** tab and click **Create Tool**.
3. Select **Model Context Protocol (MCP)** as the tool type.
4. Set the **Endpoint URL** to the Cloud Run Service URL you copied.
5. Since we deployed with `--allow-unauthenticated`, you can set the authentication type to **None**.
6. Save the tool and make sure it is attached to your agent in the main configuration.
7. Update your Agent's Instructions so that it knows it *must* use this tool whenever it is asked to calculate the net financial benefit of a climate policy!

Good luck!
