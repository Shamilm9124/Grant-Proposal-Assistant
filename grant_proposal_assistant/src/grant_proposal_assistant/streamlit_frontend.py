import streamlit as st
from datetime import datetime

from grant_proposal_assistant.crew import GrantProposalAssistant
from grant_proposal_assistant.tools.custom_tool import WordLimitChecker

word_checker = WordLimitChecker()
# ====================================
# Page Configuration
# ====================================

st.set_page_config(
    page_title="Grant Proposal Assistant",
    page_icon="📄",
    layout="centered"
)

# ====================================
# Title
# ====================================

st.title("📄 Grant Proposal Assistant")
st.write("Generate AI-powered grant proposals using CrewAI.")

# ====================================
# User Inputs
# ====================================

project_name = st.text_input(
    "Project Name",
    placeholder="Enter your project name"
)

project_goal = st.text_area(
    "Project Goal",
    placeholder="Describe the purpose of the project..."
)

funding_request = st.text_input(
    "Funding Request",
    placeholder="requested Amount"
)

project_duration = st.text_input(
    "Project Duration",
    placeholder="Duration"
)

target_beneficiaries = st.text_area(
    "Target Beneficiaries",
    placeholder="Who will benefit from this project?"
)

grant_type = st.text_input(
    "Grant Type",
    placeholder="Enter the type of grant"
)

# ====================================
# Generate Button
# ====================================

if st.button("Generate Grant Proposal"):

    if not project_name or not project_goal:
        st.warning("Please fill in the required fields.")
    else:

        inputs = {
            "project_name": project_name,
            "project_goal": project_goal,
            "funding_request": funding_request,
            "project_duration": project_duration,
            "target_beneficiaries": target_beneficiaries,
            "grant_type": grant_type,
            "current_year": str(datetime.now().year)
        }

        with st.spinner("Generating proposal..."):

            # Run CrewAI
            result = GrantProposalAssistant().crew().kickoff(inputs=inputs)

            # Word limit check
            word_limit_result = word_checker.check(
                text=str(result),
                limit=1500
            )

        # ====================================
        # Display Results
        # ====================================

        st.success("Grant Proposal Generated Successfully!")

        st.subheader("📑 Proposal Output")
        st.markdown(str(result))

        st.subheader("📊 Word Limit Check")
        st.write(word_limit_result)

        # ====================================
        # Download Option
        # ====================================

        st.download_button(
            label="Download Proposal",
            data=str(result),
            file_name="grant_proposal.md",
            mime="text/markdown"
        )