def analyze_log(lines):
    error_keywords = ["ERROR", "Exception", "FAILURE"]
    issue_lines = [line for line in lines if any(k in line for k in error_keywords)]

    if issue_lines:
        details = "\n".join(issue_lines[:10])  # Include first 10 issue lines
        return True, details
    return False, ""
