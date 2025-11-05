import os
import time
import subprocess
from typing import Dict, Tuple, List
from jinja2 import Environment, FileSystemLoader

def run_tool(tool: Dict) -> Tuple[str, str]:
    """
    Run a diagnostic tool and return its status
    """
    try:
        # Simulate tool running for demo
        time.sleep(1)
        return "PASS", f"Successfully ran {tool['name']}"
    except Exception as e:
        return "FAIL", str(e)

def generate_html_report(results: List[Dict]) -> str:
    """
    Generate HTML report from diagnostic results
    """
    try:
        env = Environment(loader=FileSystemLoader('templates'))
        template = env.get_template('report_template.html')
        
        report_content = template.render(results=results)
        
        # Save report
        report_path = os.path.join('reports', 'diagnostic_report.html')
        os.makedirs('reports', exist_ok=True)
        
        with open(report_path, 'w') as f:
            f.write(report_content)
            
        return report_path
    except Exception as e:
        print(f"Error generating report: {e}")
        return None
