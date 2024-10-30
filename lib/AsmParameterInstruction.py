class AsmParameterInstruction:
    instruction = {
        "add Rd,Rr": {
            "parameters": {
                "Rd": {"constraints": "0< <32", "options": 'r', "mask_bits": "dddd"},
                "Rr": {"constraints": "0< <32", "options": 'r', "mask_bits": "rrrr"}
            }
        },
        "sub Rd, Rr": {
            "parameters": {
                "Rd": {"constraints": "0< <32", "options": 'r', "mask_bits": "dddd"},
                "Rr": {"constraints": "0< <32", "options": 'r', "mask_bits": "rrrr"}
            }
        },
        "sbci Rd,K": {
            "parameters": {
                "Rd": {"constraints": "0< <31", "options": 'r', "mask_bits": "dddd"},
                "K": {"constraints": "0< <255", "options": None, "mask_bits": "KKKK KKKK"}
            }
        },
        "sbic P,b": {
            "parameters": {
                "P": {"constraints": None, "options": None, "mask_bits": "PPPP"},
                "b": {"constraints": None, "options": None, "mask_bits": "bbb"}
            }
        },
        "cbi P,b": {
            "parameters": {
                "P": {"constraints": "0<= <=31", "options": None, "mask_bits": "PPPP"},
                "b": {"constraints": "0<= <=7", "options": None, "mask_bits": "bbb"}
            }
        },
        "sbi P,b": {
            "parameters": {
                "P": {"constraints": '0< <31', "options": None, "mask_bits": "PPPP"},
                "b": {"constraints": '0< <7', "options": None, "mask_bits": "bbb"}
            }
        },
        "ldi Rd,K": {
            "parameters": {
                "Rd": {"constraints": "16< <32", "options": 'r', "mask_bits": "dddd"},
                "K": {"constraints": "0<= <=255", "options": None, "mask_bits": "KKKK KKKK"}
            }
        },
        "subi Rd,K": {
            "parameters": {
                "Rd": {"constraints": "16< <32", "options": 'r', "mask_bits": "dddd"},
                "K": {"constraints": "0<= <=255", "options": None, "mask_bits": "KKKK KKKK"}
            }
        },
        'ser Rd':{
                "parameters": {
                    "Rd": {"constraints": "16< <31", "options": 'r', "mask_bits": "dddd"},
                }
            },
        "jmp k": {
            "parameters": {
                "k": {"constraints": None, "options": "address", "mask_bits": "kkkk kkkkk kkkkk kkkkk kkkkk"}
            }
        },
        "call k": {
            "parameters": {
                "k": {"constraints": None, "options": "address", "mask_bits": "kkkk kkkkk kkkkk kkkkk kkkkk"}
            }
        },
        "brne k": {
            "parameters": {
                "k": {"constraints": None, "options": "signed", "mask_bits": "kkkk kkkk k001"}
            }
        },
        "breq k": {
            "parameters": {
                "k": {"constraints": None, "options": "signed", "mask_bits": "kkkk kkkk k001"}
            }
        },
        "mov Rd,Rr": {
            "parameters": {
                "Rd": {"constraints": "0< <32", "options": 'r', "mask_bits": "dddd"},
                "Rr": {"constraints": "0< <32", "options": 'r', "mask_bits": "rrrr"}
            }
        },
        "out P,Rr": {
            "parameters": {
                "P": {"constraints": "0<= <=63", "options": None, "mask_bits": "PPPP"},
                "Rr": {"constraints": "0< <32", "options": 'r', "mask_bits": "rrrr"}
            }
        },
        "in Rd,P": {
            "parameters": {
                "Rd": {"constraints": "0< <32", "options": 'r', "mask_bits": "rrrr"},
                "P": {"constraints": "0<= <=63", "options": None, "mask_bits": "PPPP"}
            }
        },
        "rjmp k": {
            "parameters": {
                "k": {"constraints": None, "options": "signed", "mask_bits": "kkkk kkkkk kkkkk kkkkk"}
            }
        },
        "sbc Rd,Rr": {
            "parameters": {
                "Rd": {"constraints": "0< <32", "options": 'r', "mask_bits": "dddd"},
                "Rr": {"constraints": "0< <32", "options": 'r', "mask_bits": "rrrr"}
            }
        },
        "adc Rd,Rr": {
            "parameters": {
                "Rd": {"constraints": "0< <32", "options": 'r', "mask_bits": "dddd"},
                "Rr": {"constraints": "0< <32", "options": 'r', "mask_bits": "rrrr"}
            }
        },
        "lsr Rd": {
            "parameters": {
                "Rd": {"constraints": "0< <32", "options": 'r', "mask_bits": "dddd"}
            }
        },
        "ror Rd": {
            "parameters": {
                "Rd": {"constraints": "0< <32", "options": 'r', "mask_bits": "dddd"}
            }
        },
        "asr Rd": {
            "parameters": {
                "Rd": {"constraints": "0< <32", "options": 'r', "mask_bits": "dddd"}
            }
        },
        "com Rd": {
            "parameters": {
                "Rd": {"constraints": "0< <32", "options": 'r', "mask_bits": "dddd"}
            }
        },
        "neg Rd": {
            "parameters": {
                "Rd": {"constraints": "0< <32", "options": 'r', "mask_bits": "dddd"}
            }
        },
        "swap Rd": {
            "parameters": {
                "Rd": {"constraints": "0< <32", "options": 'r', "mask_bits": "dddd"}
            }
        },
        "dec Rd": {
            "parameters": {
                "Rd": {"constraints": "0< <32", "options": 'r', "mask_bits": "dddd"}
            }
        },
        "inc Rd": {
            "parameters": {
                "Rd": {"constraints": "0< <32", "options": 'r', "mask_bits": "dddd"}
            }
        },
        "cpi Rd,K": {
            "parameters": {
                "Rd": {"constraints": "16< <32", "options": 'r', "mask_bits": "dddd"},
                "K": {"constraints": "0<= <=255", "options": None, "mask_bits": "KKKK KKKK"}
            }
        },
        "cp Rd,Rr": {
            "parameters": {
                "Rd": {"constraints": "0< <32", "options": 'r', "mask_bits": "dddd"},
                "Rr": {"constraints": "0< <32", "options": 'r', "mask_bits": "rrrr"}
            }
        },
        "and Rd,Rr": {
            "parameters": {
                "Rd": {"constraints": "0< <32", "options": 'r', "mask_bits": "dddd"},
                "Rr": {"constraints": "0< <32", "options": 'r', "mask_bits": "rrrr"}
            }
        },
        "or Rd,Rr": {
            "parameters": {
                "Rd": {"constraints": "0< <32", "options": 'r', "mask_bits": "dddd"},
                "Rr": {"constraints": "0< <32", "options": 'r', "mask_bits": "rrrr"}
            }
        },
        "eor Rd,Rr": {
            "parameters": {
                "Rd": {"constraints": "0< <32", "options": 'r', "mask_bits": "dddd"},
                "Rr": {"constraints": "0< <32", "options": 'r', "mask_bits": "rrrr"}
            }
        },
        "mul Rd,Rr": {
            "parameters": {
                "Rd": {"constraints": "0<= <32", "options": 'r', "mask_bits": "dddd"},
                "Rr": {"constraints": "0<= <32", "options": 'r', "mask_bits": "rrrr"}
            }
        },
        "muls Rd,Rr": {
            "parameters": {
                "Rd": {"constraints": "16<= <32", "options": 'r', "mask_bits": "dddd"},
                "Rr": {"constraints": "16<= <32", "options": 'r', "mask_bits": "rrrr"}
            }
        },
        "lsl Rd": {
            "parameters": {
                "Rd": {"constraints": "0<= <32", "options": 'r', "mask_bits": "dddd"}
            }
        },
        "push Rd": {
            "parameters": {
                "Rd": {"constraints": "0<= <32", "options": 'r', "mask_bits": "dddd"}
            }
        },
        "pop Rd": {
            "parameters": {
                "Rd": {"constraints": "0<= <32", "options": 'r', "mask_bits": "dddd"}
            }
        },
        "clr Rd": {
            "parameters": {
                "Rd": {"constraints": "0< <31", "options": 'r', "mask_bits": "dddd"}
            }
        },
        "break": {
            "parameters": {}
        },
        "sleep": {
            "parameters": {}
        },
        "wdr": {
            "parameters": {}
        }
    }

    def __getitem__(self, item):
        return self.instruction[item]
