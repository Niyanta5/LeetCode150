import os
import requests
import datetime
from github import Github

# Load environment variables
LEETCODE_USERNAME = os.getenv("LEETCODE_USERNAME")
LEETCODE_TOKEN = os.getenv("LEETCODE_TOKEN")
LEETCODE_REPO = os.getenv("LEETCODE_REPO")
BRANCH_NAME = os.getenv("BRANCH_NAME", "main")  # Default to 'main' if not set
leetcode_url = f"https://leetcode.com/api/submissions/{LEETCODE_USERNAME}/"

# GitHub Authentication
g = Github(LEETCODE_TOKEN)
repo = g.get_user().get_repo(LEETCODE_REPO)
branch = 'dev'

# Fetch LeetCode submissions
def fetch_submissions():
    response = requests.get(leetcode_url)
    if response.status_code == 200:
        return response.json().get("submissions_dump", [])
    else:
        raise Exception(f"Failed to fetch submissions: {response.status_code}")

# Save and push submission to GitHub
def push_to_github(submission):
    problem_name = submission['title_slug']
    language = submission['lang']
    date = datetime.datetime.fromtimestamp(submission['timestamp']).strftime('%Y-%m-%d')
    code = submission['code']
    
    # Define file path for GitHub
    file_path = f"{date}/{problem_name}/{problem_name}_{language}.py"
    
    # Check if file exists and push to the specific branch
    try:
        # Try to get the file contents from the specific branch
        file_content = repo.get_contents(file_path, ref=BRANCH_NAME)
        # Update the file
        repo.update_file(file_content.path, f"Update {problem_name}", code, file_content.sha, branch=BRANCH_NAME)
    except:
        # If the file doesn't exist, create it on the specified branch
        repo.create_file(file_path, f"Add solution for {problem_name}", code, branch=BRANCH_NAME)

# Main function
def main():
    submissions = fetch_submissions()
    for submission in submissions:
        try:
            push_to_github(submission)
            print(f"Synced solution for {submission['title_slug']}")
        except Exception as e:
            print(f"Failed to sync solution for {submission['title_slug']}: {e}")

if __name__ == "__main__":
    main()

