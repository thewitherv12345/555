import subprocess
from datetime import datetime


def save_build_info():
    try:
        commit_hash = subprocess.check_output(['git', 'rev-parse', 'HEAD']).decode().strip()
    except:
        commit_hash = "commit не найден"

    try:
        commit_date = subprocess.check_output(['git', 'log', '-1', '--format=%cd']).decode().strip()
    except:
        commit_date = "Дата коммита не найдена"

    build_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("build_info.txt", "w", encoding="utf-8") as file:
        file.write(f"Commit hash: {commit_hash}\n")
        file.write(f"Commit date: {commit_date}\n")
        file.write(f"Build time: {build_time}\n")
        file.write("Студент №8\n")


if __name__ == "__main__":
    save_build_info()
