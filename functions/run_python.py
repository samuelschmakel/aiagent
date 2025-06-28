import os
import subprocess
from google.genai import types

def run_python_file(working_directory, file_path, args=None):
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    if not abs_file_path.startswith(abs_working_dir):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(abs_file_path):
        return f'Error: File "{file_path}" not found.'
    if not file_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'
    try:
        cmds = ["python3", abs_file_path]
        if args:
            cmds.extend(args)
        result = subprocess.run(
        cmds,
        cwd=abs_working_dir,
        capture_output=True,
        text=True, # treates stdout and stderr as strings instead of bytes
        timeout=30 # timeout after 30 seconds
        )
        output = ""
        if result.stdout:
            output += f"STDOUT:\n{result.stdout}"
        if result.stderr :
            output += f"STDERR:\n{result.stderr}"
        if result.returncode != 0:
            output += f"\nProcess exited with code {result.returncode}"
        if result.stdout == "" and result.stderr == "":
            return "No output produced"
        return output if output else "No output produced"
    except Exception as e:
        return f"Error: executing Python file: {e}"
    
schema_run_python_file = types.FunctionDeclaration(
        name="run_python_file",
        description="Runs the given Python file. Constrained to the working directory.",
        parameters=types.Schema(
            type=types.Type.OBJECT,
            properties={
                "file_path": types.Schema(
                    type=types.Type.STRING,
                    description="The file path to list files from, relative to the working directory. If not provided, information from files in the working directory itself is output.",
                ),
            },
        ),
    )
    