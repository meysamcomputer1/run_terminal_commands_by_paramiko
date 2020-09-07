import paramiko, time, getpass

username = input("Please enter your linux username: ")
password = getpass.getpass('Please enter your linux password: ')

commands = ['uname -a', 'echo hi']

connection = paramiko.SSHClient()
connection.set_missing_host_key_policy(paramiko.AutoAddPolicy())
try:
    connection.connect('localhost', username=username, password=password,
    look_for_keys=False, allow_agent=False)

    for command in commands:
        stdin, stdout, stderr = connection.exec_command(command)
        print(stdout.readlines())

except:
    print('sth is in problem')