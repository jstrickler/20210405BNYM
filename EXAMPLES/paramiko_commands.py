#!/usr/bin/env python

import paramiko

with paramiko.SSHClient() as ssh:  # <1>

    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # <2>

    ssh.connect('localhost', username='python', password='l0lz')  # <3>

    stdin, stdout, stderr = ssh.exec_command('netstat -an')  # <4>
    raw_output = stdout.read().decode()
    lines = raw_output.splitlines()
    connections = [line for line in lines if 'ESTAB' in line]
    for connection in connections:
        proto, local, remote, status = connection.split()
        local_ip, local_port = local.split(':')
        remote_ip, remote_port = remote.split(':')
        print(proto, local_ip, remote_ip)
    print('-' * 60)

    stdin, stdout, stderr = ssh.exec_command('ls -l')  # <4>
    print(stdout.read().decode())  # <5>
    print('-' * 60)

    stdin, stdout, stderr = ssh.exec_command('ls -l /etc/passwd /etc/horcrux')  # <4>
    print("STDOUT:")
    print(stdout.read().decode())  # <5>
    print("STDERR:")
    print(stderr.read().decode())  # <6>
    print('-' * 60)
