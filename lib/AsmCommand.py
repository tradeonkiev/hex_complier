from lib.AsmParameterInstruction import AsmParameterInstruction


class AsmCommand:
    def __init__(self, hex_format, index, name, params):
        hex_format = [f'{hex_format[i + 2: i + 4]} {hex_format[i: i + 2]}' for i in range(0, len(hex_format), 4)]
        self.hex_format = ' '.join(hex_format)
        self.row_index = index
        self.name = name
        self.params = params
        self.get_command()

    def get_command(self):
        def parameter_treatment(special, mask_value, constraints, param):
            def get_invert_number(number):
                invert_number = ''
                for i in number:
                    if i == '1':
                        invert_number += '0'
                    else:
                        invert_number += '1'
                return invert_number

            sign_mark = ''
            if special == 'address':
                mask_value += '0'
                altered_value = int(mask_value, 2)
            elif special == 'signed':
                sign_mark = '-' if mask_value[0] == '1' else '+'
                answer = 0
                if mask_value[0] == '1':
                    mask_value = get_invert_number(mask_value)
                    answer += 1
                answer += int(mask_value, 2)
                altered_value = answer * 2
            else:
                altered_value = int(mask_value, 2)

            if constraints and '<' in constraints:
                altered_value += int(constraints.split('<')[0])

            if special == 'r':
                return f'r{altered_value}'
            elif sign_mark:
                return f'{sign_mark}{altered_value}'
            elif altered_value > 9:
                return hex(altered_value)
            else:
                return altered_value

        self.params: dict
        try:
            parameter_value = AsmParameterInstruction()[self.name]
        except:
            return
        parameter_value: dict
        for argument, value in self.params.items():
            for parameter, info_dict in parameter_value['parameters'].items():
                if argument in info_dict['mask_bits']:
                    value = str(parameter_treatment(
                        special=info_dict['options'],
                        mask_value=value,
                        constraints=info_dict['constraints'],
                        param=info_dict['mask_bits']))
                    self.name = f"{self.name.split(' ')[0]} {self.name.split(' ')[-1].replace(parameter, value)}"

    def __call__(self, *args, **kwargs):
        return f'{self.row_index[2:]:0>2}: {self.hex_format: >12} \t{self.name}'
