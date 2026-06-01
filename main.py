from mcp.server.fastmcp import FastMCP
from mcp.server.transport_security import TransportSecuritySettings

# Create FastMCP server optimized for Cloud Run and Vertex AI Agent Builder
mcp = FastMCP(
    "EcoGrid Level 4 - Macro Economic MCP Server",
    instructions="An agent tool that calculates the net financial benefit of a climate policy.",
    streamable_http_path="/",
    json_response=True,
    stateless_http=True,
    transport_security=TransportSecuritySettings(enable_dns_rebinding_protection=False)
)

@mcp.tool()
async def calculate_net_policy_benefit(incremental_power_cost_bn: float, end_user_savings_bn: float, climate_benefits_bn: float, air_quality_benefits_bn: float) -> float:
    """
    Calculates the net financial benefit of a climate policy in billions.
    
    Args:
        incremental_power_cost_bn: The incremental power-system costs (in billions).
        end_user_savings_bn: The net system savings resulting from differences in end-user costs (in billions).
        climate_benefits_bn: The value of avoided climate change damages (in billions).
        air_quality_benefits_bn: The value of air quality improvements (in billions).
        
    Returns:
        The calculated net policy benefit in billions (rounded to 2 decimal places).
    """
    # =========================================================================
    # 🚨 YOUR TASK: Implement the calculation below!
    # =========================================================================
    #
    # The CFO needs the NET POLICY BENEFIT. Here is the formula:
    #
    #   Step 1: Calculate the NET COST
    #           net_cost = incremental_power_cost_bn - end_user_savings_bn
    #
    #   Step 2: Calculate the TOTAL BENEFITS
    #           total_benefits = climate_benefits_bn + air_quality_benefits_bn
    #
    #   Step 3: Calculate the NET POLICY BENEFIT
    #           net_benefit = total_benefits - net_cost
    #
    #   Step 4: Return the result rounded to 2 decimal places
    #           return round(net_benefit, 2)
    #
    # Replace the line below with your implementation!
    # =========================================================================

    raise NotImplementedError("TODO: Implement the calculation using the formula above!")

# Expose as a Streamable HTTP ASGI/Starlette app.
app = mcp.streamable_http_app()
