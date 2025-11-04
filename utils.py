import os
import time
import subprocess
import pyautogui
from typing import Dict, Tuple, List
from jinja2 import Environment, FileSystemLoader

def run_tool(tool: Dict[str, str | bool]) -> Tuple[str, str]:
    try:
        if not os.path.isfile(tool["path"]):
            return "FAIL", f"Executable not found: {tool['path']}"

        process = subprocess.Popen(tool["path"])
        
        if tool.get("gui", False):
            time.sleep(3)  # Let GUI open
            pyautogui.press("f5")  # Example action for GUI tools
            print(f"Sent F5 to {tool['name']}")

        while process.poll() is None:
            time.sleep(1)

        return "PASS", "Test completed manually."
    
    except Exception as e:
        return "FAIL", str(e)

def generate_html_report(results: List[Dict[str, str]]) -> str:
    template_dir = "templates"
    output_dir = "reports"
    report_path = os.path.join(output_dir, "diagnostics_report.html")

    os.makedirs(output_dir, exist_ok=True)

    try:
        env = Environment(loader=FileSystemLoader(template_dir))
        template = env.get_template("report_template.html")
        output = template.render(results=results)

        with open(report_path, "w", encoding="utf-8") as report_file:
            report_file.write(output)

        print(f"Report generated at: {report_path}")
        return report_path

    except Exception as e:
        print(f"Failed to generate report: {e}")
        return ""
