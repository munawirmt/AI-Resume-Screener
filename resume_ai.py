import streamlit as st
import pdfplumber
from google import genai
import re
import pandas as pd

# 1. Executive Web Workspace Configuration
st.set_page_config(
    page_title="AI Talent Screening Suite Pro", 
    page_icon="💼", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# 2. Premium Enterprise-Grade Custom Layout Styling
st.markdown("""
    <style>
    /* Deep Corporate Dark Space Base */
    .stApp {
        background: linear-gradient(145deg, #090d16 0%, #111827 50%, #070a12 100%);
        color: #f1f5f9;
        font-family: 'Inter', system-ui, -apple-system, sans-serif;
    }
    
    /* Sleek Kinetic Typography for Titles */
    .main-title {
        font-size: 2.8rem;
        font-weight: 800;
        background: linear-gradient(135deg, #38bdf8 0%, #6366f1 50%, #ec4899 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 2px;
        letter-spacing: -1px;
    }
    .subtitle {
        text-align: center;
        color: #64748b;
        font-size: 1.05rem;
        margin-bottom: 35px;
        font-weight: 400;
    }
    
    /* Clean Minimalist Structural UI Grouping */
    div[data-testid="stVerticalBlock"] > div {
        background: rgba(17, 24, 39, 0.45);
        backdrop-filter: blur(16px);
        -webkit-backdrop-filter: blur(16px);
        border: 1px solid rgba(255, 255, 255, 0.05);
        border-radius: 14px;
        padding: 24px;
        box-shadow: 0 10px 40px -10px rgba(0, 0, 0, 0.5);
    }
    
    /* High-Fidelity Data Field Interactivity */
    textarea {
        background-color: rgba(3, 7, 18, 0.6) !important;
        color: #e2e8f0 !important;
        border: 1px solid rgba(99, 102, 241, 0.2) !important;
        border-radius: 10px !important;
        font-size: 0.95rem !important;
    }
    textarea:focus {
        border-color: #6366f1 !important;
        box-shadow: 0 0 12px rgba(99, 102, 241, 0.3) !important;
    }
    
    /* Refined Clean Navigation Panel */
    section[data-testid="stSidebar"] {
        background-color: #030712 !important;
        border-right: 1px solid rgba(255, 255, 255, 0.04);
    }
    
    /* Executive Processing Trigger Elements */
    div.stButton > button {
        background: linear-gradient(135deg, #4f46e5 0%, #7c3aed 100%) !important;
        color: #ffffff !important;
        font-weight: 600 !important;
        font-size: 1rem !important;
        letter-spacing: 0.5px !important;
        padding: 14px 28px !important;
        border-radius: 10px !important;
        border: none !important;
        box-shadow: 0 4px 20px rgba(99, 102, 241, 0.3) !important;
        transition: all 0.25s ease-in-out !important;
    }
    div.stButton > button:hover {
        transform: translateY(-1px) !important;
        box-shadow: 0 6px 24px rgba(124, 58, 237, 0.45) !important;
    }
    
    /* Standard Analytics Data Grid Structure */
    div[data-testid="stDataFrame"] {
        border: 1px solid rgba(255, 255, 255, 0.04);
        border-radius: 10px;
    }

    /* Minimalist Professional Footer Badge */
    .corporate-footer {
        text-align: center;
        padding-top: 45px;
        padding-bottom: 15px;
        margin-top: 60px;
        border-top: 1px solid rgba(255, 255, 255, 0.04);
        color: #475569;
        font-size: 0.88rem;
        letter-spacing: 0.3px;
    }
    .corporate-footer b {
        color: #94a3b8;
    }
    .corporate-footer a {
        color: #38bdf8 !important;
        text-decoration: none;
        transition: color 0.2s ease;
    }
    .corporate-footer a:hover {
        color: #6366f1 !important;
    }
    </style>
""", unsafe_allow_html=True)

# 3. App Header System Layout
st.markdown('<h1 class="main-title">AI Talent Screening Suite Pro</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Enterprise-grade bulk resume filtering engine driven by Google Gemini 2.5 Flash</p>', unsafe_allow_html=True)

# 4. Workspace Parameter Control Panel
st.sidebar.markdown("### ⚙️ Authentication Control")
api_key_input = st.sidebar.text_input("Gemini API Credentials:", type="password", help="Provision your application instance key via Google AI Studio console.")

# 5. Dual Dashboard Ingestion Controls
col1, col2 = st.columns(2)

with col1:
    st.markdown("### 💼 Operational Mandate (Job Specification)")
    jd_text = st.text_area("", height=240, placeholder="Paste structural job matrix parameters, technological stacks, or competency profiles here...")

with col2:
    st.markdown("### 📤 Pipeline Resource Ingestion (Batch PDF)")
    uploaded_files = st.file_uploader("", type=["pdf"], accept_multiple_files=True)

st.markdown("<br>", unsafe_allow_html=True)
# 6. Evaluation Logic Execution Pipeline
if st.button("🚀 INITIATE SYSTEM TALENT FILTER PIPELINE", use_container_width=True):
    if not api_key_input:
        st.error("❌ Authentication Fault: Verified API configuration credentials missing from system terminal panel.")
    elif not jd_text:
        st.warning("⚠️ Input Parameter Fault: Operational job directive workspace cannot accept empty vectors.")
    elif not uploaded_files:
        st.warning("⚠️ File Stream Fault: Upload queue contains zero candidate profile data files.")
    else:
        results_list = []
        detailed_reports = {}
        
        try:
            client = genai.Client(api_key=api_key_input)
        except Exception as e:
            st.error(f"Failed to securely initiate local processing pipeline client node: {e}")
            st.stop()

        for uploaded_file in uploaded_files:
            file_name = uploaded_file.name
            
            with st.spinner(f"⚡ Executing natural language synthesis matrices for: {file_name}..."):
                try:
                    resume_text = ""
                    with pdfplumber.open(uploaded_file) as pdf:
                        for page in pdf.pages:
                            text = page.extract_text()
                            if text:
                                resume_text += text
                    
                    if not resume_text.strip():
                        results_list.append({"Candidate Profile": file_name, "Fit Index (%)": 0, "Processing Log": "Corrupted/Unreadable Text Architecture"})
                        continue

                    # Structured Enterprise Standard Persona Prompt Block
                    prompt = f"""
                    You are working as an elite Principal Executive Recruiter. Your task is to critique the candidate's Resume Text against the target Job Description framework.
                    Deliver your complete strategic findings inside cleanly mapped Markdown containers with bold headers and clean lists. Do not use conversational preambles.
                    
                    CRITICAL CONSTRAINT: You must initiate your markdown response block with a line stating exactly: "MATCH_SCORE: [number]" (e.g., MATCH_SCORE: 78).
                    
                    Map out the following business reports:
                    1. **Executive Synergy Overview**: Core professional synopsis evaluating strategic structural fit alignment.
                    2. **Core Competency Alignments**: Enumerate explicit technical/functional matches discovered within the candidate text.
                    3. **Operational Core Skill Deficiencies**: Highlight specific target capabilities, domain experience elements, or certifications missing.
                    4. **Strategic Behavioral Interview Queries**: Generate 3 targeted, razor-sharp situational screening questions to evaluate known skill deficiencies.
                    5. **Operational Suitability Verdict**: Definitive statement summarizing final pipeline positioning recommendation.

                    Job Description Matrix:
                    {jd_text}

                    Resume Analytical Text:
                    {resume_text}
                    """
                    
                    response = client.models.generate_content(
                        model="gemini-3.5-flash",
                        contents=prompt,
                    )
                    
                    ai_output = response.text
                    score = 0
                    score_match = re.search(r"MATCH_SCORE:\s*(\d+)", ai_output)
                    if score_match:
                        score = int(score_match.group(1))
                        ai_output = re.sub(r"MATCH_SCORE:\s*\d+\n?", "", ai_output)
                    
                    results_list.append({
                        "Candidate Profile": file_name, 
                        "Fit Index (%)": score,
                        "Processing Log": "Verified Evaluation"
                    })
                    detailed_reports[file_name] = ai_output
                    
                except Exception as e:
                    results_list.append({"Candidate Profile": file_name, "Fit Index (%)": 0, "Processing Log": f"Pipeline Fault Trace: {e}"})

        st.success("✅ Talent matrix compilation completed. Visualizing core asset reports.")
        
        # 7. Real-Time Operational Analytics Dashboard Cards
        st.divider()
        df = pd.DataFrame(results_list)
        df = df.sort_values(by="Fit Index (%)", ascending=False).reset_index(drop=True)
        
        successful_evals = df[df["Processing Log"] == "Verified Evaluation"]
        
        m_col1, m_col2, m_col3 = st.columns(3)
        with m_col1:
            st.metric("Total Applicants Processed", f"{len(df)}")
        with m_col2:
            avg_score = int(successful_evals["Fit Index (%)"].mean()) if not successful_evals.empty else 0
            st.metric("Average Workspace Fit Index", f"{avg_score}%")
        with m_col3:
            high_score = int(successful_evals["Fit Index (%)"].max()) if not successful_evals.empty else 0
            st.metric("Peak Candidate Score", f"{high_score}%")

        # 8. Main Analytics Leaderboard Matrix Table
        st.header("📊 Analytical Alignment Matrix Leaderboard")
        st.dataframe(df, use_container_width=True)
        
        # 9. Individual Candidate Segment Viewports
        st.divider()
        st.header("📄 Consolidated Executive Dossier Deep-Dives")
        
        successful_candidates = successful_evals["Candidate Profile"].tolist()
        
        if successful_candidates:
            selected_candidate = st.selectbox("Select explicit candidate directory profile for core review:", successful_candidates)
            
            if selected_candidate:
                st.markdown(f"### 📋 Strategic Appraisal Ledger: {selected_candidate}")
                st.markdown(detailed_reports[selected_candidate])
                
                st.download_button(
                    label=f"📥 Download Report Dossier Ledger ({selected_candidate})",
                    data=detailed_reports[selected_candidate],
                    file_name=f"{selected_candidate}_Strategic_Evaluation.txt",
                    mime="text/plain",
                    use_container_width=True
                )

# 10. Minimal High-End Branding Architecture Footer Grid
st.markdown("""
    <div class="corporate-footer">
        <p>Deployment Node Status: Active & Secure | Engineering Infrastructure: <b>Munawir.mt</b> | Communications Portfolio: <a href="mailto:munawirmt002@gmail.com">munawirmt002@gmail.com</a></p>
    </div>
""", unsafe_allow_html=True)
