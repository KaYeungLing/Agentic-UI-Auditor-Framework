import json
from datetime import datetime

class ReportGenerator:
    @staticmethod
    def generate_json_report(state: dict, output_file: str = "data/reports/audit_report.json"):
        report = {
            "audit_date": datetime.now().isoformat(),
            "target_url": state.get("url"),
            "goal": state.get("goal"),
            "total_steps_taken": state.get("current_step"),
            "critical_issues_found": len(state.get("issues_found", [])),
            "detailed_findings": state.get("issues_found", []),
            "artifacts_generated": state.get("screenshots", [])
        }
        
        with open(output_file, 'w') as f:
            json.dump(report, f, indent=4)
            
        print(f"Enterprise Audit Report generated at: {output_file}")
