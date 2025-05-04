import os
import requests

RALLY_URL = "https://rally1.rallydev.com/slm/webservice/v2.0/defect"

def create_rally_ticket(filename, details):
    api_key = os.getenv("RALLY_API_KEY")
    project = os.getenv("RALLY_PROJECT")
    workspace = os.getenv("RALLY_WORKSPACE")

    headers = {
        "ZSESSIONID": api_key,
        "Content-Type": "application/json"
    }

    payload = {
        "Defect": {
            "Name": f"Auto-Detected Issue in {filename}",
            "Description": f"Issues detected in Jenkins log file:\n\n{details}",
            "Project": f"/project/{project}",
            "Workspace": f"/workspace/{workspace}",
            "Severity": "Major Problem",
            "State": "Open",
        }
    }

    try:
        response = requests.post(RALLY_URL, headers=headers, json=payload)
        if response.status_code == 201:
            ticket_ref = response.json()["OperationResult"]["Object"]["_ref"]
            return {"status": "Created", "reference": ticket_ref}
        else:
            return {"status": "Failed", "details": response.text}
    except Exception as e:
        return {"status": "Error", "details": str(e)}
