import streamlit as st
import pandas as pd
from diagnostic_config import tools
from utils import run_tool, generate_html_report

def main():
    st.title("Diagnostic App")
    st.write("Welcome to the Diagnostic Tool!")
    
    if st.button("Run Diagnostics"):
        results = []
        progress_bar = st.progress(0)
        
        for index, tool in enumerate(tools):
            st.write(f"Running: {tool['name']}")
            status, message = run_tool(tool)
            
            results.append({
                "name": tool["name"],
                "status": status,
                "message": message
            })
            
            if status == "PASS":
                st.success(f"✅ {tool['name']}: {message}")
            else:
                st.error(f"❌ {tool['name']}: {message}")
                
            progress_bar.progress((index + 1) / len(tools))
        
        # Display results in a table
        df = pd.DataFrame(results)
        st.table(df)

if __name__ == "__main__":
    main()