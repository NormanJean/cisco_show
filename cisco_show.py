from netmiko import ConnectHandler

print('*'*37)
print('*',f'{"":^33}','*')
print('*',f'{"CISCO":^33}','*')
print('*',f'{"SHOW":^33}','*')
print('*',f'{"":^33}','*')
print('*'*37)
print()

user = input('login: ')
password_ = input('password: ')
secret = input('privelege password: ')

with open('switches', 'r') as switches_file:
    switches = switches_file.readlines()
    for ip in switches:
        switch = ip

        cisco = {
            "device_type": "cisco_ios_telnet",
            "host": switch,
            "username": user,
            "password": password_,
            "secret": secret,
        }

        try:
            with ConnectHandler(**cisco) as net_connect:
                net_connect.enable()
                print(switch)
                with open('commands', 'r') as commands_file:
                    commands = commands_file.readlines()
                    for sh in commands:
                        command = sh
                        output = net_connect.send_command(command)
                        print(command)
                        result = open('result/' + switch[:-1] + '.txt', 'a',
                              encoding='utf-8')
                        result.write(output)
        except Exception as ex:
            print(switch)
            print(ex)
            with open('errors/' + switch[:-1] + '.txt', 'w',
                      encoding='utf-8') as error:
                error.write(str(ex))
