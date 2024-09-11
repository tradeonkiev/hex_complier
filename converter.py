from parser import command_list
import requests
from pprint import pprint
from bs4 import BeautifulSoup
from function_command import function_command


def command_convert(command_cod):
    answer = []
    for command, mask in zip(command_list, command_list.values()):
        control = {'command': command,
                   'kargs': 0,
                   'args': 0,
                   'args_dict': {}}
        red_flag = False
        if mask.__len__() == command_cod.__len__():
            for x, y in zip(mask, command_cod):
                if x in '01':
                    if x == y:
                        control['args'] += 1
                        continue
                    red_flag = True
                    break
                elif x == ' ':
                    continue
                else:
                    control['kargs'] += 1
                    if not control['args_dict'].get(x):
                        control['args_dict'][x] = ''
                    control['args_dict'][x] += y
            if not red_flag:
                answer.append(control)
    if not answer:
        return 'ERROR'
    max_command = answer[0]
    for i in answer:
        if i['args'] > max_command['args']:
            max_command = i
        elif i['args'] == max_command['args'] and i['kargs'] > max_command['kargs']:
            max_command = i
    return max_command


def parser():
    input_data = []
    while i := input().replace(':', ''):
        input_data.append(i)

    def convert_to_modify(raw_string):
        commands = [''.join(list(j)) for j in zip(raw_string[8::2], raw_string[9::2])]
        commands = [f'{y}{x}'
                    for x, y in zip(commands[::2], commands[1::2])]
        answer = []
        commands += ['']
        flag = False
        for x, y in zip(commands, commands[1:]):
            if flag:
                flag = False
                continue
            else:
                answer.append(x)
        return answer

    modified_commands = []
    for i in input_data:
        modified_commands += convert_to_modify(i)
    answer_ = []
    for command in modified_commands:
        command = [f'{bin(int(x + y, 16))[2:]:>08}' for x, y in zip(command[::2], command[1::2])]
        answer = ''
        for i in command:
            answer += f'{i[:4]} {i[4:]} '
        answer_.append(answer.strip())
    modified_commands = answer_
    c = 0
    flag = False
    for j in range(len(modified_commands)):
        if flag:
            flag = False
            continue
        i = modified_commands[j]
        if j + 1 < len(modified_commands):
            k = modified_commands[j + 1]
        else:
            k = 0
        if command_convert(i) != 'ERROR':
            pass
        elif command_convert((i := f'{i} {k}')) != 'ERROR':
            flag = True
        command = command_convert(i)
        # print('=' * 100)
        hex_format = []
        for j in range(len(k := hex(int(i.replace(' ', ''), 2))[2:].upper()) // 2):
            hex_format.append(k[j * 2: j * 2 + 2])
        answer = ''
        for x, y in zip(hex_format[0::2], hex_format[1::2]):
            answer += f'{y} {x} '
        if not answer:
            answer = '00 00 '
        command = command_convert(i)
        name_command = command['command']
        commands = ''
        for x, y in zip(command['args_dict'].keys(), command['args_dict'].values()):
            if x in function_command[name_command]:
                commands += f'{function_command[name_command][x](y)} '
        print(f'{hex(c)[2:]:>3}: {answer:>12} {name_command.split()[0].replace('*', ''):>6} '
              f'{commands.strip().replace(' ', ', ')}')
        # url = f"http://2www.gaw.ru/html.cgi/txt/doc/micros/avr/asm/{name_command}.htm"
        # response = requests.get(url)
        # soup = BeautifulSoup(response.text, 'html.parser')
        # flag_ = False
        # for j in soup.find_all('p', attrs={'class': 'bl'}):
        #     j = j.get_text().split('\n')
        #     if flag_:
        #         break
        #     for k in j:
        #         if 'Циклов' in k:
        #             # print(k)
        #             flag_ = True
        c += i.split(' ').__len__() // 2


parser()
