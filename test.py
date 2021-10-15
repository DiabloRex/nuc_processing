import subprocess


args = ["ls", "-l"]
args1 = ["head", "-4"]

a = subprocess.Popen(args, stdout=subprocess.PIPE)
b = subprocess.Popen(args1, stdin=subprocess.PIPE)



#std_out, std_err = a.communicate()
b.stdin.write(a.communicate()[0])

b.communicate()


