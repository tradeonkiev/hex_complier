class AsmMaskException(Exception):
    def __init__(self, msg: str = ''):
        super().__init__(f'MASK ERROR\n\t{msg}')
