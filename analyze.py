import os
import subprocess

def run_radon(repo_path):
    result = subprocess.run(['radon', 'cc', '-a', repo_path], capture_output=True, text=True)
    print("Radon Cyclomatic Complexity Analysis:\n", result.stdout)

def run_pylint(repo_path):
    result = subprocess.run(['pylint', repo_path], capture_output=True, text=True)
    print("Pylint Analysis:\n", result.stdout)

def analyze_repo(repo_path):
    run_radon(repo_path)
    run_pylint(repo_path)

if __name__ == "__main__":
    repo_path = input("Enter the path to the Python repository: ")
    analyze_repo(repo_path)