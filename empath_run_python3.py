import re
import subprocess
def CallPython2(input_text = ""):
    p = subprocess.Popen("python empath_run_python2.py", shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    stdout_data, stderr_data = p.communicate(input_text.encode("utf-8"), timeout=20)
    return stdout_data.decode("utf-8")

data = CallPython2()
print(data)
pattern = r'([0-9]*)'

lists = re.findall(pattern, data)
lists_real = [i for i in lists  if i != '']
if lists_real[0] == "0":
    del lists_real[0]
    print(lists_real)
else:
    print("error number is {0}".format(lists_real[0]))
