from lib.parser import command_list
from lib.AsmMaskException import AsmMaskException
from lib.AsmCommand import AsmCommand


class AsmDisassembler:
    def __init__(self):
        self.commands = []
        self.index = 0

    def __call__(self, *args, **kwargs):
        answer = ''
        i = input('ВВедите hex код: \n')
        while i != '':
            answer += i
            i = input()
        self.parse(answer)

    def parse(self, raw_string: str):
        hex_commands = []
        for row in self._get_rows(raw_string + 'kk'):
            for i in range(0, len(row), 2):
                hex_commands.append(row[i:i + 2])

        answer = []
        for part_1, part_2 in zip(hex_commands[::2], hex_commands[1::2]):
            answer.append(part_2 + part_1)
        hex_commands = answer

        flag = False
        for command_1, command_2 in zip(hex_commands, hex_commands[1:] + hex_commands[-1:]):
            if flag:
                flag = False
                continue
            elif self._fetch_mask(command_1):
                command = self._fetch_mask(command_1)
                self.commands.append(AsmCommand(hex_format=command_1,
                                                index=hex(self.index),
                                                name=command['command'],
                                                params=command['params']))
                self.index += 2
            elif self._fetch_mask(command_1 + command_2):
                command = self._fetch_mask(command_1 + command_2)
                self.commands.append(AsmCommand(hex_format=command_1 + command_2,
                                                index=hex(self.index),
                                                name=command['command'],
                                                params=command['params']))
                self.index += 4
                flag = True
            else:
                raise AsmMaskException(msg=f'{command_1} {command_2}')
        for i in self.commands:
            print(i())

    @staticmethod
    def _fetch_mask(hex_format) -> dict[str: str]:

        binary_form = ''
        for i in range(0, len(hex_format), 2):
            binary_form += f'{bin(int(hex_format[i: i+2], 16))[2:]:>08}'
        answer = {}
        max_counter = 0
        # print(hex_format)
        for command, mask in command_list.items():
            mask = mask.replace(' ', '')
            # print('=' * 10)
            # print(command, mask, binary_form)
            match_counter = 0
            params = {}
            if len(mask) != len(binary_form):
                continue
            for mask_index, tagger in enumerate(mask):
                # print(binary_form[mask_index], tagger, tagger == binary_form[mask_index])
                if tagger == binary_form[mask_index]:
                    match_counter += 1
                elif tagger not in '01':
                    if not params.get(tagger):
                        params[tagger] = ''
                    params[tagger] += binary_form[mask_index]
                else:
                    match_counter = 0
                    break
            if match_counter != 0 and match_counter > max_counter:
                max_counter = match_counter
                answer = {
                    'command': command,
                    'params': params
                }
        return answer

    @staticmethod
    def _get_rows(raw_string: str) -> list[str]:
        answer = []
        for row in raw_string.replace('\n', '').split(':'):
            answer.append(row[8:-2])
        return answer


AsmDisassembler().__call__()
