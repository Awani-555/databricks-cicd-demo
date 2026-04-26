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


if __name__ == "__main__":
    demo.launch()
