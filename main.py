import ctypes
import sys
import subprocess
import time
import webbrowser
from diagnostic_config import tools
from utils import generate_html_report, run_tool  # Ensure both functions are defined in utils.py


import streamlit as st

st.title("Diagnostic App")
st.write("Welcome to the Diagnostic Tool!")

def is_admin():
    """Check if script is running with admin rights."""
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except Exception:
        return False

def main():
    # Relaunch with admin if not already
    if not is_admin():
        print("🛑 Administrator privileges required. Requesting now...")
        ctypes.windll.shell32.ShellExecuteW(
            None, "runas", sys.executable, " ".join(sys.argv), None, 1
        )
        sys.exit()

    print("✅ Script is running with administrator privileges.")
    print("\n🔧 Running all diagnostic tools...\n")

    results = []

    for tool in tools:
        print(f"→ Running: {tool['name']}")
        status, message = run_tool(tool)

        results.append({
            "name": tool["name"],
            "status": status,   # Will be 'PASS' or 'FAIL'
            "message": message
        })

        if status == "PASS":
            print(f"   ✅ Test successful: {tool['name']}")
        else:
            print(f"   ❌ Test failed: {tool['name']}")

        print(f"   Result: {status} - {message}\n")

    # Generate HTML report
    report_path = generate_html_report(results)
    if report_path:
        print(f"\n📄 Opening report: {report_path}")
        webbrowser.open(report_path)
    else:
        print("❌ Failed to generate report.")

if __name__ == "__main__":
    main()
