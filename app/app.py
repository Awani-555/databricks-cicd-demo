import os

import gradio as gr


def build_status_message() -> str:
    app_env = os.getenv("APP_ENV", "local")
    lines = [f"Running in environment: {app_env}"]

    if app_env.lower() == "staging":
        pr_number = os.getenv("PR_NUMBER", "N/A")
        lines.append(f"PR number: {pr_number}")

    return "\n".join(lines)


with gr.Blocks(title="Databricks CI/CD Demo App") as demo:
    gr.Markdown("# Databricks CI/CD Demo App")
    gr.Markdown(build_status_message())
    gr.Markdown("## Loan Repayment Data")
    gr.Dataframe(
        headers=["Customer ID", "EMI Amount", "Status"],
        value=[
            ["CUST-1001", 1250, "Paid"],
            ["CUST-1002", 980, "Pending"],
            ["CUST-1003", 1575, "Overdue"],
        ],
        interactive=False,
    )


if __name__ == "__main__":
    demo.launch(
        server_name="0.0.0.0",
        server_port=8000
    )
