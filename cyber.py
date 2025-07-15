import streamlit as st
from crewai import Agent, Task, Crew

# Streamlit UI
st.title("AI Cyber TIX System - Multiagent Analysis")

# Data Ingestion Agent
ingestion_agent = Agent(
    name="Data Ingestion Agent",
    role="Collects cybersecurity data from external sources like MISP, CVE, and MITRE ATT&CK.",
    goal="Fetch and normalize data for further processing."
)

# Data Processing Agent
processing_agent = Agent(
    name="Data Processing Agent",
    role="Standardizes, resolves entities, and validates incoming data.",
    goal="Prepare clean data for threat analysis."
)

# Threat Analysis Agent
threat_analysis_agent = Agent(
    name="Threat Analysis Agent",
    role="Analyzes data for potential threats and anomalies.",
    goal="Detect threats using machine learning and generate alerts."
)

# Contextual Scoring Agent
context_scoring_agent = Agent(
    name="Contextual Scoring Agent",
    role="Scores threats based on organizational context and relevance.",
    goal="Provide scores to prioritize responses."
)

# Recommendation Agent
recommendation_agent = Agent(
    name="Recommendation Agent",
    role="Suggests preventive measures and mitigation strategies.",
    goal="Provide actionable recommendations to prevent cyberattacks."
)

# Define Tasks
ingestion_task = Task(
    description="Fetch data from external sources and normalize it.",
    agent=ingestion_agent
)

processing_task = Task(
    description="Standardize and validate the ingested data.",
    agent=processing_agent
)

threat_analysis_task = Task(
    description="Analyze processed data to detect threats.",
    agent=threat_analysis_agent
)

context_scoring_task = Task(
    description="Score detected threats based on organizational context.",
    agent=context_scoring_agent
)

recommendation_task = Task(
    description="Suggest preventive measures and mitigation strategies.",
    agent=recommendation_agent
)

# Assemble the Crew
cyber_tix_crew = Crew(
    tasks=[
        ingestion_task,
        processing_task,
        threat_analysis_task,
        context_scoring_task,
        recommendation_task
    ]
)

# Run the system with Streamlit
if st.button("Run Multiagent System"):
    results = cyber_tix_crew.kickoff()
    for i, result in enumerate(results):
        st.subheader(f"Step {i+1} Result:")
        st.write(result)
