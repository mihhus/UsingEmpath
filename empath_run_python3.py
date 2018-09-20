def inputToPython2(input_text):
    p = subprocess.Pone("empath_run_python2.py", shell=True, stdin=subprocess.PIPE, stdout=subprocess.PINE, stderr=subprocess.PINE)

    stdout_data, stderr_data = p.communicate(input_text.encode("utf-8"), timeout=20)
    return stdout_data.decode("utf-8")

inputToPython2("aaa")
