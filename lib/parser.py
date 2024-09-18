command_list = {'call k': '1001 010k kkkk 111k kkkk kkkk kkkk kkkk',
                'jmp k': '1001 010k kkkk 110k kkkk kkkk kkkk kkkk',
                'adc Rd,Rr': '0001 11rd dddd rrrr',
                'add Rd,Rr': '0000 11rd dddd rrrr',
                'adiw Rdl,K': '1001 0110 KKdd KKKK',
                'and Rd,Rr': '0010 00rd dddd rrrr',
                'andi Rd,K': '0111 KKKK dddd KKKK',
                'asr Rd': '1001 010d dddd 0101',
                'bclr s': '1001 0100 1sss 1000',
                'breq k': '1111 00kk kkkk k001',
                'bld Rd,b': '1111 100b bbbb 0bbb',
                # 'breq k': '1111 01kk kkkk k001',
                'brcc k': '1111 01kk kkkk k000',
                'brcs k': '1111 00kk kkkk k000',
                'brge k': '1111 01kk kkkk k100',
                'brhc k': '1111 01kk kkkk k101',
                'brhs k': '1111 00kk kkkk k101',
                'brid k': '1111 01kk kkkk k111',
                'brie k': '1111 00kk kkkk k111',
                'brlo k': '1111 00kk kkkk k000',
                'brlt k': '1111 00kk kkkk k100',
                'brmi k': '1111 00kk kkkk k010',
                'brne k': '1111 01kk kkkk k001',
                'brpl k': '1111 01kk kkkk k010',
                'brsh k': '1111 01kk kkkk k000',
                'brtc k': '1111 01kk kkkk k110',
                'brts k': '1111 00kk kkkk k110',
                'brvc k': '1111 01kk kkkk k011',
                'brvs k': '1111 00kk kkkk k011',
                'bset s': '1001 0100 0sss 1000',
                'bst Rr,b': '1111 101b bbbb 0bbb',
                'cbi P,b': '1001 1000 PPPP Pbbb',
                'cbr Rd,K': '0111 KKKK dddd KKKK',
                'clc': '1001 0100 1000 1000',
                'clh': '1001 0100 1101 1000',
                'cli': '1001 0100 1111 1000',
                'cln': '1001 0100 1010 1000',
                'eor Rd,Rr': '0010 01rd dddd rrrr',
                'clr Rd': '0010 01dd dddd dddd',
                'cls': '1001 0100 1100 1000',
                'clt': '1001 0100 1110 1000',
                'clv': '1001 0100 1011 1000',
                'clz': '1001 0100 1001 1000',
                'com Rd': '1001 010d dddd 0000',
                'cp Rd,Rr': '0001 01rd dddd rrrr',
                'cpc Rd,Rr': '0000 01rd dddd rrrr',
                'cpi Rd,K': '0011 KKKK dddd KKKK',
                'cpse Rd,Rr': '0001 00rd dddd rrrr',
                'dec Rd': '1001 010d dddd 1010',
                'icall': '1001 0101 0000 1000',
                'ijmp': '1001 0100 0000 1000',
                'in Rd,P': '1011 0PPd dddd PPPP',
                'inc Rd': '1001 010d dddd 0011',
                'ld Rd, -X': '1001 000d dddd 1110',
                'ld Rd, -Y': '1001 000d dddd 1010',
                'ld Rd, -Z': '1001 000d dddd 0010',
                'ld Rd,X': '1001 000d dddd 1100',
                'ld Rd,X+': '1001 000d dddd 1101',
                'ld Rd,Y': '1000 000d dddd 1000',
                'ld Rd,Y+': '1001 000d dddd 1001',
                'ld Rd,Z': '1000 000d dddd 0000',
                'ld Rd,Z+': '1001 000d dddd 0001',
                'ldd Rd,Y+q': '10q0 qq0d dddd 1qqq',
                'ldd Rd,Z+q': '10q0 qq0d dddd 0qqq',
                'ldi Rd,K': '1110 KKKK dddd KKKK',
                'lds Rd,k': '1001 000d dddd 0000 kkkk kkkk kkkk kkkk',
                'lpm': '1001 0101 1100 1000',
                'lpm Rd,Z': '1001 000d dddd 0100',
                'lpm Rd,Z+': '1001 000d dddd 0101',
                'lsl Rd': '0000 11dd dddd dddd',
                'lsr Rd': '1001 010d dddd 0110',
                'mov Rd,Rr': '0010 11rd dddd rrrr',
                'movw Rd,Rr': '0000 0001 dddd rrrr',
                'neg Rd': '1001 010d dddd 0001',
                'nop': '0000 0000 0000 0000',
                'or Rd,Rr': '0010 10rd dddd rrrr',
                'ori Rd,K': '0110 KKKK dddd KKKK',
                'out P,Rr': '1011 1PPr rrrr PPPP',
                'pop Rd': '1001 000d dddd 1111',
                'push Rr': '1001 001r rrrr 1111',
                'rcall k': '1101 kkkk kkkk kkkk',
                'ret': '1001 0101 0000 1000',
                'reti': '1001 0101 0001 1000',
                'rjmp k': '1100 kkkk kkkk kkkk',
                ''        '1100 1111 1111 0010'
                'rol Rd': '0001 11dd dddd dddd',
                'ror Rd': '1001 010d dddd 0111',
                'sbc Rd,Rr': '0000 10rd dddd rrrr',
                'sbci Rd,K': '0100 KKKK dddd KKKK',
                'sbi P,b': '1001 1010 PPPP Pbbb',
                'sbic P,b': '1001 1001 PPPP Pbbb',
                'sbis P,b': '1001 1011 PPPP Pbbb',
                'sbiw Rdl,K': '1001 0111 KKdd KKKK',
                'sbr Rd,K': '0110 KKKK dddd KKKK',
                'sbrc Rr,b': '1111 110r rrrr obbb',
                'sbrs Rr,b': '1111 111r rrrr obbb',
                'sec': '1001 0100 0000 1000',
                'seh': '1001 0100 0101 1000',
                'sei': '1001 0100 0111 1000',
                'sen': '1001 0100 0010 1000',
                'ser Rd': '1110 1111 dddd 1111',
                'ses': '1001 0100 0100 1000',
                'set': '1001 0100 0110 1000',
                'sev': '1001 0100 0011 1000',
                'sez': '1001 0100 0001 1000',
                'sleep': '1001 0101 1000 1000',
                'spm': '1001 0101 1110 1000',
                'st -X,Rr': '1001 001r rrrr 1110',
                'st -Y,Rr': '1001 001r rrrr 1010',
                'st -Z,Rr': '1001 001r rrrr 0010',
                'st X+,Rr': '1001 001r rrrr 1101',
                'st X,Rr': '1001 001r rrrr 1100',
                'st Y+,Rr': '1001 001r rrrr 1001',
                'st Y,Rr': '1000 001r rrrr 1000',
                'st Z+,Rr': '1001 001r rrrr 0001',
                'st Z,Rr': '1000 001r rrrr 0000',
                'std Y+q,Rr': '10q0 qq1r rrrr 1qqq',
                'std Z+q,Rr': '10q0 qq1r rrrr 0qqq',
                'sts k,Rr': '1001 001r rrrr 0000 kkkk kkkk kkkk kkkk',
                'sub Rd,Rr': '0001 10rd dddd rrrr',
                'subi Rd,K': '0101 KKKK dddd KKKK',
                'swap Rd': '1001 010d dddd 0010',
                'tst Rd': '0010 00dd dddd dddd',
                'wdr': '1001 0101 1010 1000'}

