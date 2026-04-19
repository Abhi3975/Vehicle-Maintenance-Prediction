# src/agent/workflow.py
from typing import TypedDict, Annotated
import pandas as pd
from src.agent.rag_engine import get_retriever
from src.agent.prompts import SYSTEM_PROMPT, REPORT_TEMPLATE

class AgentState(TypedDict):
    vehicle_row: dict
    ml_score: float
    importance_factors: list
    rag_context: str
    final_report: str

def run_maintenance_agent(df_row, risk_score, importance_factors):
    """
    Orchestrates the agentic workflow.
    df_row: A single row from the vehicle dataframe (dict)
    risk_score: The probability score from the ML model
    importance_factors: List of top feature importances
    """
    # 1. Initialize RAG
    retriever = get_retriever()
    context = retriever.get_maintenance_context(df_row.get('Vehicle_Model'), importance_factors)
    
    # 2. Reasoning (This will be expanded by the Agent Workflow Engineer using LangGraph)
    # For now, we return a mock structured output
    
    risk_level = "CRITICAL" if risk_score > 0.8 else "MODERATE" if risk_score > 0.5 else "LOW"
    
    report = REPORT_TEMPLATE.format(
        summary=f"Analysis for {df_row.get('Vehicle_Model')} with {df_row.get('Mileage')} miles.",
        risk_analysis=f"Risk Score: {risk_score:.2f} ({risk_level}). Key factors: {', '.join(importance_factors[:3])}.",
        actions="- Check brake pads immediately\n- Inspect oil quality\n- Schedule full diagnostic",
        reasoning=f"Based on historical data and {context}",
    )
    
    return report
