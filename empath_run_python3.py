import subprocess
def inputToPython2(input_text):
    p = subprocess.Popen("python empath_run_python2.py", shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    stdout_data, stderr_data = p.communicate(input_text.encode("utf-8"), timeout=20)
    return stdout_data.decode("utf-8")

print(inputToPython2("aaa"))

