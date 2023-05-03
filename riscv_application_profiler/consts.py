commitlog_regex="^core\s+\d+:\s+\d*\s+(0x[0-9a-fA-F]+)\s+\((0x[0-9a-fA-F]+)\)\s*(x[0-9]*)?(c[0-9]+[_a-z]*)?(mem)?\s*(0x[0-9a-fA-F]*)?\s*(x[0-9]*)?(c[0-9]+[_a-z]*)?(mem)?\s*(0x[0-9a-fA-F]*)?\s*(x[0-9]*)?(c[0-9]+[_a-z]*)?(mem)?\s*(0x[0-9a-fA-F]*)?"
disass_regex = "^\s*([0-9a-f]+):\s+([0-9a-f]+)\s+([a-z][a-z\.0-9]*)"

ops_dict = {
    'RV32' : {
    'I' : {
    'loads' : ['lb', 'lbu', 'lh', 'lhu','lw',],
    'stores' : ['sb', 'sh', 'sw'],
    'imm computes' : ['addi', 'andi', 'ori', 'xori', 'slti', 'sltiu', 'auipc', 'lui'],
    'imm shifts' : ['slli', 'srli', 'srai'], 
    'reg computes' : ['add', 'sub', 'slt', 'sltu', 'xor', 'or', 'and'],
    'reg shifts' : ['sll', 'srl', 'sra'],
    'jumps' : ['jal', 'jalr'],
    'branches' : ['bge', 'bgeu', 'blt', 'bltu', 'beq', 'bne'], 
    #'nop' : ['nop'],

    },
    'M' : {
    'loads' :[],
    'stores':[],
    'imm computes' :[],
    'imm shifts' :[],
    'reg computes' :['div', 'divu', 'mul', 'mulh', 'mulhsu', 'mulhu', 'rem','remu'],
    'reg shifts' :[],
    'jumps' :[],
    'branches' :[],
    #'nop' : [],

    },
    'C' : {
    'loads' :['c.lwsp', 'c.lw', ], 
    'stores':['c.swsp', 'c.sw', ], 
    'imm computes' : ['c.li', 'c.lui', 'c.addi', 'c.addi16sp', 'c.addi4spn', 'c.andi',],
    'imm shifts' : ['c.slli', 'c.srli', 'c.srai', ],
    'reg computes' : ['c.add', 'c.addw', 'c.sub', 'c.subw', 'c.and', 'c.or', 'c.xor', 'c.mv', ],
    'reg shifts' : ['c.sll', 'c.srl', 'c.sra'],
    'jumps' : ['c.j', 'c.jal', 'c.jr', 'c.jalr'],
    'branches' : ['c.beqz', 'c.bnez', 'c.bltz', 'c.bgez', 'c.bltz', 'c.bgez', 'c.bltzal', 'c.bgezal'],
    #'nop' : ['c.nop'],
    },#c.nop, c.ebreak, c.mv,
    },

    'RV64' : {
    'I' : {
    'loads' : ['ld', 'lh', 'lhu', 'lb', 'lbu', 'lw','lwu'],
    'stores' : ['sb', 'sh', 'sw', 'sd'],
    'imm computes' : ['addi', 'addiw', 'andi', 'ori', 'xori', 'slti', 'sltiu', 'auipc', 'lui'],
    'imm shifts' : ['slli', 'srli', 'srai', 'slliw', 'srliw', 'sraiw'],
    'reg computes' : ['add', 'sub','slt', 'sltu', 'xor', 'or', 'and', 'addw', 'subw'],
    'reg shifts' : ['sll', 'srl', 'sra', 'sllw', 'srlw', 'sraw'],
    'jumps' : ['jal', 'jalr'],
    'branches' : ['bge', 'bgeu', 'blt', 'bltu', 'beq', 'bne'],
    #'nop' : ['nop'],

    },
    'M' : {
    'loads' :[],
    'stores':[],
    'imm computes' :[],
    'imm shifts' :[],
    'reg computes' :['div', 'divu', 'mul', 'mulh', 'mulhsu', 'mulhu', 'rem','remu'],
    'reg shifts' :[],
    'jumps' :[],
    'branches' :[],
    #'nop' : [],

    },
    'C' : {
    'loads' : ['c.lwsp', 'c.ldsp', 'c.lw', 'c.ld', ], # c.lq, c.lqsp, c.flwsp, c.fldsp, c.fld, c.flw
    'stores' : ['c.swsp', 'c.sdsp', 'c.sw', 'c.sd',], #c.sq,  c.sqsp, c.fswsp, c.fsdsp, c.fsd, c.fsw
    'imm computes' : ['c.addi4spn', 'c.addi', 'c.addiw', 'c.li', 'c.lui', 'c.addi16sp', 'c.addi4spn', 'c.addi', 'c.addiw', 'c.li', 'c.lui', 'c.addi16sp'],
    'imm shifts' : ['c.slli', 'c.srli', 'c.srai'],
    'reg computes' : ['c.add', 'c.sub', 'c.xor', 'c.or', 'c.and', 'c.subw', 'c.addw', 'c.mv'],
    'reg shifts' : ['c.sll', 'c.srl', 'c.sra'],
    'jumps' : ['c.j', 'c.jal', 'c.jr', 'c.jalr'],
    'branches' : ['c.beqz', 'c.bnez', 'c.bltz', 'c.bgez', 'c.bltz', 'c.bgez', 'c.bltzal', 'c.bgezal'],
    #'nop' : ['c.nop'],
    }
}
}