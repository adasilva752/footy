import git
from flask import Flask, render_template, url_for, flash, redirect, request

@app.route("/update_server", methods=['POST'])
def webhook():
    if request.method == 'POST':
        repo = git.Repo('/home/CHANGE_TO_PYTHON_ANYWHERE_USERNAME/CHANGE_TO_GITHUB_REPO_NAME')
        origin = repo.remotes.origin
        origin.pull()
        return 'Updated PythonAnywhere successfully', 200
    else:
        return 'Wrong event type', 400