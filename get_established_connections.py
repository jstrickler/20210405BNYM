from subprocess import run, PIPE, CalledProcessError
import shlex

RAW_CMD = "netstat -a"
CMD_WORDS = shlex.split(RAW_CMD)
try:
    proc = run(CMD_WORDS, stdout=PIPE)
except CalledProcessError as err:
    print(err)
    print("External program stopped with status code", proc.returncode)
else:
    raw_output = proc.stdout.decode()
    output_lines = raw_output.splitlines()
    connections = [line for line in output_lines if 'ESTAB' in line]
    for connection in connections:
        proto, local, remote, status = connection.split()
        local_ip, local_port = local.split(':')
        remote_ip, remote_port = remote.split(':')
        print(proto, local_ip, remote_ip)