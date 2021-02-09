import subprocess
from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/git_branch')
def git_branch():
    process = subprocess.Popen(['git', 'branch'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    if stderr:
        return jsonify({"data": stderr})
    branches = stdout.decode().split('\n')
    branch = [branch.strip() for branch in branches]

    return jsonify({"data": branch})


if __name__ == "__main__":
    app.run(debug=True)
