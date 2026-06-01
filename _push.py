import subprocess

repo = r"D:\@Personal Data@\@my resume_source@\_Jonathon Brunson (A.T)_\github\jonathonb21"
msg = "Fix README images: local SVG assets and HTML img tags."

subprocess.check_call(["git", "add", "-A"], cwd=repo)
subprocess.check_call(["git", "commit", "-m", msg], cwd=repo)
subprocess.check_call(["git", "push", "origin", "main"], cwd=repo)
print("Pushed.")
