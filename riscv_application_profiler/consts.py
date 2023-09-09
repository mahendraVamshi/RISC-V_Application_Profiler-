import yaml
default_commitlog_regex = ...
default_disass_regex = ...
default_privilege_mode_regex = ...
config_path='./sample_config/config.yaml'
with open(config_path, 'r') as config_file:
    config = yaml.safe_load(config_file)

    commitlog_regex = config['profiles']['cfg'].get('commitlog_regex', default_commitlog_regex)
    privilege_mode_regex = config['profiles']['cfg'].get('privilege_mode_regex', default_privilege_mode_regex)

ops_dict = {
    "RV32": {
        "I": {
            "loads": [
                "lb",
                "lbu",
                "lh",
                "lhu",
                "lw",
            ],
            "stores": ["sb", "sh", "sw"],
            "imm computes": [
                "addi",
                "andi",
                "ori",
                "xori",
                "slti",
                "sltiu",
                "auipc",
                "lui",
            ],
            "imm shifts": ["slli", "srli", "srai"],
            "reg computes": ["add", "sub", "slt", "sltu", "xor", "or", "and"],
            "reg shifts": ["sll", "srl", "sra"],
            "jumps": ["jal", "jalr"],
            "branches": ["bge", "bgeu", "blt", "bltu", "beq", "bne"],
            "compares":[],
            "conversions":[],
            "moves":[],
            "classifies":[],
            "csrs":[],
            "fence":["fence","fence.i"],
        },
        "M": {
            "loads": [],
            "stores": [],
            "imm computes": [],
            "imm shifts": [],
            "reg computes": [
                "div",
                "divu",
                "mul",
                "mulh",
                "mulhsu",
                "mulhu",
                "rem",
                "remu",
            ],
            "reg shifts": [],
            "jumps": [],
            "branches": [],
            "compares":[],
            "conversions":[],
            "moves":[],
            "classifies":[],
            "csrs":[],
            "fence":[],
        },
        "F": {
            "loads": ["flw","flwsp","fld","fldsp"],
            "stores": ["fsw","fswsp","fsd","fsdsp"],
            "imm computes": [],
            "imm shifts": [],
            "reg computes": [
                "fmadd.s",
                "fmsub.s",
                "fadd.s",
                "fsub.s",
                "fmul.s",
                "fdiv.s",
                "fmin.s",
                "fmax.s",
                "fsqrt.s",
                "fmadd.s",
                "fmsub.s",
                "fnmsub.s"
                "fnmadd.s"
            ],
            "reg shifts": [],
            "jumps": [],
            "compares": ["flt.s","feq.s","fle.s"],
            "conversions":[
                "fcvt.w.s",
                "fcvt.wu.s",
                "fcvt.s.w",
                "fcvt.s.wu",
                "fsgnj.s",
                "fsgnjn.s",
                "fsgnjx.s",
            ],
            "moves":["fmv.s","fmv.x.w","fmv.w.x"],
            "classifies":["fclass.s"],
            "branches": [],
            "csrs":["frcsr.s","fscsr.s","frrm","fsrm","fsrmi",],
            "fence":[],
        },
        "D": {
            "loads": ["fld","fldsp"],
            "stores": ["fsd","fsdsp"],
            "imm computes": [],
            "imm shifts": [],
            "reg computes": [
                "fmadd.d",
                "fmsub.d",
                "fadd.d",
                "fsub.d",
                "fmul.d",
                "fdiv.d",
                "fmin.d",
                "fmax.d",
                "fsqrt.d",
                "fmadd.d",
                "fmsub.d",
                "fnmsub.d"
                "fnmadd.d"
            ],
            "reg shifts": [],
            "jumps": [],
            "compares": ["flt.d","feq.d","fle.d"],
            "conversions":[
                "fcvt.w.d",
                "fcvt.wu.d",
                "fcvt.d.w",
                "fcvt.d.wu",
                "fsgnj.d",
                "fsgnjn.d",
                "fsgnjx.d",
            ],
            "moves":["fmv.x.d","fmv.d.x"],
            "classifies":["fclass.d"],
            "branches": [],
            "csrs":["frcsr","fscsr","frrm","fsrm","fsrmi",],
            "fence":[],
            
        }, 
        "C": {
            "loads": [
                "c.lwsp",
                "c.lw",
            ],
            "stores": [
                "c.swsp",
                "c.sw",
            ],
            "imm computes": [
                "c.li",
                "c.lui",
                "c.addi",
                "c.addi16sp",
                "c.addi4spn",
                "c.andi",
            ],
            "imm shifts": [
                "c.slli",
                "c.srli",
                "c.srai",
            ],
            "reg computes": [
                "c.add",
                "c.addw",
                "c.sub",
                "c.subw",
                "c.and",
                "c.or",
                "c.xor",
                "c.mv",
            ],
            "reg shifts": ["c.sll", "c.srl", "c.sra"],
            "jumps": ["c.j", "c.jal", "c.jr", "c.jalr"],
            "branches": [
                "c.beqz",
                "c.bnez",
                "c.bltz",
                "c.bgez",
                "c.bltz",
                "c.bgez",
                "c.bltzal",
                "c.bgezal",
            ],
            "compares":[],
            "conversions":[],
            "moves":[],
            "classifies":[],
            "csrs":[],
            "fence":[],
            
        },  
        "B": {
            "loads": [],
            "stores": [],
            "imm computes": ["bclri","bexti","binvi","bseti",'slli.uw',
                             "mergei","sbseti","sbinvi",],
            "imm shifts": ['rori','roli','roriw','roliw'],
            "reg computes": ["add.uw",
                             "andn",
                             "bclr",
                             "bext",
                             "binv",
                             "bset",
                             "clmul",
                             "clmulh",
                             "clmulr",
                             "clz",
                             "clzw",
                             "cpop",'cpopw',"sbset","sbclr","sbseti","sbclri",
                             "ctz",'ctzw',"pcnt",
                             'max','maxu','min','minu',
                             'orc.b','orn',
                             "pack","packh","packu","packw",
                             'rev8','rev.b',
                             'sext.b','sexr.h','sh1add','sh1add.uw','sh2add','sh2add.uw','sh3add','sh3add.uw',
                             'unzip','xnor','xprem.b','xprem.n','zip','zext.h',
                             "funnel","unfunnel","merge","gather","gatheru","gatherx","scatter","scatteru","scatterx","sbext","sbextu","sbset","sbinv",
                             "crc32.b","crc32.h","crc32.w","crc32c.b","crc32c.h","crc32c.w"],
            "reg shifts": ["sll","srl","sra","slo","sro","rol","ror",'rorw','rolw'],
            "jumps": [],
            "compares": [],
            "conversions":[],
            "moves":[],
            "classifies":[],
            "branches": [],
            "csrs":[],
            "fence":[],
        },
        "P": {
            "loads": [
                "vld",
            ],
            "stores": [
                "vst",
            ],
            "imm computes": [
                "vaddi",
                "vsubi",
                "vslli",
                "vsrli",
                "vsrai",
                "vandi",
                "vori",
                "vxori",
                "vslti",
                "vsltiu",
            ],
            "imm shifts": [
                "vsll",
                "vsrl",
                "vsra",
            ],
            "reg computes": [
                "vadd",
                "vsub",
                "vand",
                "vor",
                "vxor",
                "vslt",
                "vsltu",
                "vmin",
                "vmax",
                "vseq",
                "vsne",
                "vzext",
                "vsext",
            ],
            "reg shifts": [
                "vssrl",
                "vssra",
                "vsll",
                "vsrl",
                "vsra",
            ],
            "jumps": [],
            "branches": [],
            "compares":[],
            "conversions":[],
            "moves":[],
            "classifies":[],
            "csrs":[],
            "fence":[],
        },
        "Zicsr": {
            "loads": [],
            "stores": [],
            "imm computes": [],
            "imm shifts": [],
            "reg computes": [],
            "reg shifts": [],
            "jumps": [],
            "compares": [],
            "conversions": [],
            "moves": [],
            "classifies": [],
            "branches": [],
            "csrs": ["csrrw","csrrs","csrrc","csrrwi","csrrsi","csrrci","rdtimeh","rdtime"],
            "fence":[],
            },

    },
    "RV64": {
        "I": {
            "loads": ["ld", "lh", "lhu", "lb", "lbu", "lw", "lwu"],
            "stores": ["sb", "sh", "sw", "sd"],
            "imm computes": [
                "addi",
                "addiw",
                "andi",
                "ori",
                "xori",
                "slti",
                "sltiu",
                "auipc",
                "lui",
            ],
            "imm shifts": ["slli", "srli", "srai", "slliw", "srliw", "sraiw"],
            "reg computes": [
                "add",
                "sub",
                "slt",
                "sltu",
                "xor",
                "or",
                "and",
                "addw",
                "subw",
            ],
            "reg shifts": ["sll", "srl", "sra", "sllw", "srlw", "sraw"],
            "jumps": ["jal", "jalr"],
            "branches": ["bge", "bgeu", "blt", "bltu", "beq", "bne"],
            "compares":[],
            "conversions":[],
            "moves":[],
            "classifies":[],
            "csrs":[],
            "fence":["fence","fence.i"],
        },
        "M": {
            "loads": [],
            "stores": [],
            "imm computes": [],
            "imm shifts": [],
            "reg computes": [
                "div",
                "divu",
                "mul",
                "mulh",
                "mulhsu",
                "mulhu",
                "rem",
                "remu",
            ],
            "reg shifts": [],
            "jumps": [],
            "branches": [],
            "compares":[],
            "conversions":[],
            "moves":[],
            "classifies":[],
            "csrs":[],
            "fence":[],
        },
        "F": {
            "loads": ["flw","flwsp","fld","fldsp"],
            "stores": ["fsw","fswsp","fsd","fsdsp"],
            "imm computes": [],
            "imm shifts": [],
            "reg computes": [
                "fmadd.s",
                "fmsub.s",
                "fadd.s",
                "fsub.s",
                "fmul.s",
                "fdiv.s",
                "fmin.s",
                "fmax.s",
                "fsqrt.s",
                "fmadd.s",
                "fmsub.s",
                "fnmsub.s"
                "fnmadd.s"
            ],
            "reg shifts": [],
            "jumps": [],
            "compares": ["flt.s","feq.s","fle.s"],
            "conversions":[
                "fcvt.w.s",
                "fcvt.wu.s",
                "fcvt.s.w",
                "fcvt.s.wu",
                "fcvt.l.s",
                "fcvt.lu.s",
                "fcvt.s.l",
                "fcvt.s.lu",
                "fsgnj.s",
                "fsgnjn.s",
                "fsgnjx.s",
            ],
            "moves":["fmv.s","fmv.x.w","fmv.w.x"],
            "classifies":["fclass.s"],
            "branches": [],
            "csrs":["frcsr","fscsr","frrm","fsrm","fsrmi",],
            "fence":[],
        },
        "D": {
            "loads": ["fld","fldsp"],
            "stores": ["fsd","fsdsp"],
            "imm computes": [],
            "imm shifts": [],
            "reg computes": [
                "fmadd.d",
                "fmsub.d",
                "fadd.d",
                "fsub.d",
                "fmul.d",
                "fdiv.d",
                "fmin.d",
                "fmax.d",
                "fsqrt.d",
                "fmadd.d",
                "fmsub.d",
                "fnmsub.d"
                "fnmadd.d"
            ],
            "reg shifts": [],
            "jumps": [],
            "compares": ["flt.d","feq.d","fle.d"],
            "conversions":[
                "fcvt.w.d",
                "fcvt.wu.d",
                "fcvt.d.w",
                "fcvt.d.wu",
                "fcvt.l.d",
                "fcvt.lu.d",
                "fcvt.d.l",
                "fcvt.d.lu",
                "fsgnj.d",
                "fsgnjn.d",
                "fsgnjx.d",
            ],
            "moves":["fmv.x.d","fmv.d.x"],
            "classifies":["fclass.d"],
            "branches": [],
            "csrs":["frcsr","fscsr","frrm","fsrm","fsrmi",],
            "fence":[],
            
        },
        "C": {
            "loads": [
                "c.lwsp",
                "c.ldsp",
                "c.lw",
                "c.ld",
            ],  
            "stores": [
                "c.swsp",
                "c.sdsp",
                "c.sw",
                "c.sd",
            ],  
            "imm computes": [
                "c.addi4spn",
                "c.addi",
                "c.addiw",
                "c.li",
                "c.lui",
                "c.addi16sp",
                "c.addi4spn",
                "c.addi",
                "c.addiw",
                "c.li",
                "c.lui",
                "c.addi16sp",
            ],
            "imm shifts": ["c.slli", "c.srli", "c.srai"],
            "reg computes": [
                "c.add",
                "c.sub",
                "c.xor",
                "c.or",
                "c.and",
                "c.subw",
                "c.addw",
                "c.mv",
            ],
            "reg shifts": ["c.sll", "c.srl", "c.sra"],
            "jumps": ["c.j", "c.jal", "c.jr", "c.jalr"],
            "branches": [
                "c.beqz",
                "c.bnez",
                "c.bltz",
                "c.bgez",
                "c.bltz",
                "c.bgez",
                "c.bltzal",
                "c.bgezal",
            ],
            "compares":[],
            "conversions":[],
            "moves":[],
            "classifies":[],
            "csrs":[],
            "fence":[],
        },

        "B": {
            "loads": [],
            "stores": [],
            "imm computes": ["bclri","bexti","binvi","bseti",'slli.uw',
                             "mergei","sbseti","sbinvi",],
            "imm shifts": ['rori','roli','roriw','roliw'],
            "reg computes": ["add.uw",
                             "andn",
                             "bclr",
                             "bext",
                             "binv",
                             "bset",
                             "clmul",
                             "clmulh",
                             "clmulr",
                             "clz",
                             "clzw",
                             "cpop",'cpopw',"sbset","sbclr","sbseti","sbclri",
                             "ctz",'ctzw',"pcnt",
                             'max','maxu','min','minu',
                             'orc.b','orn',
                             "pack","packh","packu","packw",
                             'rev8','rev.b',
                             'sext.b','sexr.h','sh1add','sh1add.uw','sh2add','sh2add.uw','sh3add','sh3add.uw',
                             'unzip','xnor','xprem.b','xprem.n','zip','zext.h',
                             "funnel","unfunnel","merge","gather","gatheru","gatherx","scatter","scatteru","scatterx","sbext","sbextu","sbset","sbinv",
                             "crc32.b","crc32.h","crc32.w","crc32c.b","crc32c.h","crc32c.w","crc32c.d","crc32.d"],
            "reg shifts": ["sll","srl","sra","slo","sro","rol","ror",'rorw','rolw'],
            "jumps": [],
            "compares": [],
            "conversions":[],
            "moves":[],
            "classifies":[],
            "branches": [],
            "csrs":[],
            "fence":[],
        },
        "P": {
            "loads": [
                "vld",
            ],
            "stores": [
                "vst",
            ],
            "imm computes": [
                "vaddi",
                "vsubi",
                "vslli",
                "vsrli",
                "vsrai",
                "vandi",
                "vori",
                "vxori",
                "vslti",
                "vsltiu",
            ],
            "imm shifts": [
                "vsll",
                "vsrl",
                "vsra",
            ],
            "reg computes": [
                "vadd",
                "vsub",
                "vand",
                "vor",
                "vxor",
                "vslt",
                "vsltu",
                "vmin",
                "vmax",
                "vseq",
                "vsne",
                "vzext",
                "vsext",
            ],
            "reg shifts": [
                "vssrl",
                "vssra",
                "vsll",
                "vsrl",
                "vsra",
            ],
            "jumps": [],
            "branches": [],
            "compares":[],
            "conversions":[],
            "moves":[],
            "classifies":[],
            "csrs":[],
            "fence":[],
        },
        "Zicsr": {
            "loads": [],
            "stores": [],
            "imm computes": [],
            "imm shifts": [],
            "reg computes": [],
            "reg shifts": [],
            "jumps": [],
            "compares": [],
            "conversions": [],
            "moves": [],
            "classifies": [],
            "branches": [],
            "csrs": ["csrrw","csrrs","csrrc","csrrwi","csrrsi","csrrci","rdtimeh","rdtime"], 
            "fence":[],
            },
    },
}

reg_file = {f'x{i}':'0x00000000' for i in range(32)}
reg_file['x2'] = '0x800030d0'
reg_file['x3'] = '0x800030d0'
freg_file = {f'f{i}':'0' for i in range(32)}

csr_file = {'0x000': 'ustatus',
            #Unprivileged Floating-Point CSRs
            '0x001': 'fflags',
            '0x002': 'frm',
            '0x003': 'fcsr',
            #Unprivileged Counter/Timers
            '0xc00': 'cycle',
            '0xc01': 'time',
            '0xc02': 'instret',
            '0xc03': 'hpmcounter3',
            '0xc04': 'hpmcounter4',
            '0xc05': 'hpmcounter5',
            '0xc06': 'hpmcounter6',
            '0xc07': 'hpmcounter7',
            '0xc08': 'hpmcounter8',
            '0xc09': 'hpmcounter9',
            '0xc0a': 'hpmcounter10',
            '0xc0b': 'hpmcounter11',
            '0xc0c': 'hpmcounter12',
            '0xc0d': 'hpmcounter13',
            '0xc0e': 'hpmcounter14',
            '0xc0f': 'hpmcounter15',
            '0xc10': 'hpmcounter16',
            '0xc11': 'hpmcounter17',
            '0xc12': 'hpmcounter18',
            '0xc13': 'hpmcounter19',
            '0xc14': 'hpmcounter20',
            '0xc15': 'hpmcounter21',
            '0xc16': 'hpmcounter22',
            '0xc17': 'hpmcounter23',
            '0xc18': 'hpmcounter24',
            '0xc19': 'hpmcounter25',
            '0xc1a': 'hpmcounter26',
            '0xc1b': 'hpmcounter27',
            '0xc1c': 'hpmcounter28',
            '0xc1d': 'hpmcounter29',
            '0xc1e': 'hpmcounter30',
            '0xc1f': 'hpmcounter31',
            '0xc80': 'cycleh',
            '0xc81': 'timeh',
            '0xc82': 'instreth',
            '0xc83': 'hpmcounter3h',
            '0xc84': 'hpmcounter4h',
            '0xc85': 'hpmcounter5h',
            '0xc86': 'hpmcounter6h',
            '0xc87': 'hpmcounter7h',
            '0xc88': 'hpmcounter8h',
            '0xc89': 'hpmcounter9h',
            '0xc8a': 'hpmcounter10h',
            '0xc8b': 'hpmcounter11h',
            '0xc8c': 'hpmcounter12h',
            '0xc8d': 'hpmcounter13h',
            '0xc8e': 'hpmcounter14h',
            '0xc8f': 'hpmcounter15h',
            '0xc90': 'hpmcounter16h',
            '0xc91': 'hpmcounter17h',
            '0xc92': 'hpmcounter18h',
            '0xc93': 'hpmcounter19h',
            '0xc94': 'hpmcounter20h',
            '0xc95': 'hpmcounter21h',
            '0xc96': 'hpmcounter22h', 
            '0xc97': 'hpmcounter23h',
            '0xc98': 'hpmcounter24h',
            '0xc99': 'hpmcounter25h',
            '0xc9a': 'hpmcounter26h',
            '0xc9b': 'hpmcounter27h',
            '0xc9c': 'hpmcounter28h',
            '0xc9d': 'hpmcounter29h',
            '0xc9e': 'hpmcounter30h',
            '0xc9f': 'hpmcounter31h',
            #Supervisor Trap Setup
            '0x100': 'sstatus',
            '0x102': 'sedeleg',
            '0x103': 'sideleg',
            '0x104': 'sie',
            '0x105': 'stvec',
            '0x106': 'scounteren',
            #Supervisor Configuration
            '0x10a': 'senvcfg',
            #Supervisor Trap Handling
            '0x140': 'sscratch',
            '0x141': 'sepc',
            '0x142': 'scause',
            '0x143': 'stval',
            '0x144': 'sip',
            #Supervisor Protection and Translation
            '0x180': 'satp',
            #Debug/Trace Registers
            '0x5a8': 'scontext',
            #Hypervisor Trap Setup
            '0x600': 'hstatus',
            '0x602': 'hedeleg',
            '0x603': 'hideleg',
            '0x604': 'hie',
            '0x605': 'htvec',
            '0x606': 'hcounteren',
            '0x607': 'hgeie',
            #Hypervisor Trap Handling
            '0x643': 'htval',
            '0x644': 'hip',
            '0x645': 'hvip',
            '0x64a': 'htinst',
            '0xe12': 'hgeip',
            #Hypervisor Configuration
            '0x60a': 'henvcfg',
            '0x61a': 'henvcfgh',
            #Hypervisor Protection and Translation
            '0x680': 'hgatp',
            #Debug/Trace Registers
            '0x6a8': 'hcontext',
            #Hypervisor Counter/Timer Virtualization Registers
            '0x605': 'htimedelta',
            '0x615': 'htimedeltah',
            #Virtual Supervisor Registers
            '0x200': 'vsstatus',
            '0x204': 'vsie',
            '0x205': 'vstvec',
            '0x240': 'vsscratch',
            '0x241': 'vsepc',
            '0x242': 'vscause',
            '0x243': 'vstval',
            '0x244': 'vsip',
            '0x280': 'vsatp',
            #Machine Information Registers
            '0xf11': 'mvendorid',
            '0xf12': 'marchid',
            '0xf13': 'mimpid',
            '0xf14': 'mhartid',
            '0xf15': 'mconfigptr',
            #Machine Trap Setup
            '0x300': 'mstatus',
            '0x301': 'misa',
            '0x302': 'medeleg',
            '0x303': 'mideleg',
            '0x304': 'mie',
            '0x305': 'mtvec',
            '0x306': 'mcounteren',
            '0x307': 'mtvt',
            '0x310': 'mscratch',
            #Machine Trap Handling
            '0x340': 'mscratch',
            '0x341': 'mepc',
            '0x342': 'mcause',
            '0x343': 'mtval',
            '0x344': 'mip',
            '0x34a': 'mtinst',
            '0x34b': 'mtval2',
            #Machine Configuration
            '0x30a': 'menvcfg',
            '0x31a': 'menvcfgh',
            '0x747': 'mseccfg',
            '0x757': 'mseccfgh',
            #Machine Memory Protection
            '0x3a0': 'pmpcfg0',
            '0x3a1': 'pmpcfg1',
            '0x3a2': 'pmpcfg2',
            '0x3a3': 'pmpcfg3',
            '0x3a4': 'pmpcfg4',
            '0x3a5': 'pmpcfg5',
            '0x3a6': 'pmpcfg6',
            '0x3a7': 'pmpcfg7',
            '0x3a8': 'pmpcfg8',
            '0x3a9': 'pmpcfg9',
            '0x3aa': 'pmpcfg10',
            '0x3ab': 'pmpcfg11',
            '0x3ac': 'pmpcfg12',
            '0x3ad': 'pmpcfg13',
            '0x3ae': 'pmpcfg14',
            '0x3af': 'pmpcfg15',
            '0x3b0': 'pmpaddr0',
            '0x3b1': 'pmpaddr1',
            '0x3b2': 'pmpaddr2',
            '0x3b3': 'pmpaddr3',
            '0x3b4': 'pmpaddr4',
            '0x3b5': 'pmpaddr5',
            '0x3b6': 'pmpaddr6',
            '0x3b7': 'pmpaddr7',
            '0x3b8': 'pmpaddr8',
            '0x3b9': 'pmpaddr9',
            '0x3ba': 'pmpaddr10',
            '0x3bb': 'pmpaddr11',
            '0x3bc': 'pmpaddr12',
            '0x3bd': 'pmpaddr13',
            '0x3be': 'pmpaddr14',   
            '0x3bf': 'pmpaddr15',
            '0x3c0': 'pmpaddr16',
            '0x3c1': 'pmpaddr17',
            '0x3c2': 'pmpaddr18',
            '0x3c3': 'pmpaddr19',
            '0x3c4': 'pmpaddr20',
            '0x3c5': 'pmpaddr21',
            '0x3c6': 'pmpaddr22',
            '0x3c7': 'pmpaddr23',
            '0x3c8': 'pmpaddr24',
            '0x3c9': 'pmpaddr25',
            '0x3ca': 'pmpaddr26',
            '0x3cb': 'pmpaddr27',
            '0x3cc': 'pmpaddr28',
            '0x3cd': 'pmpaddr29',
            '0x3ce': 'pmpaddr30',
            '0x3cf': 'pmpaddr31',
            '0x3d0': 'pmpaddr32',
            '0x3d1': 'pmpaddr33',
            '0x3d2': 'pmpaddr34',
            '0x3d3': 'pmpaddr35',
            '0x3d4': 'pmpaddr36',
            '0x3d5': 'pmpaddr37',
            '0x3d6': 'pmpaddr38',
            '0x3d7': 'pmpaddr39',
            '0x3d8': 'pmpaddr40',
            '0x3d9': 'pmpaddr41',
            '0x3da': 'pmpaddr42',
            '0x3db': 'pmpaddr43',
            '0x3dc': 'pmpaddr44',
            '0x3dd': 'pmpaddr45',
            '0x3de': 'pmpaddr46',
            '0x3df': 'pmpaddr47',
            '0x3e0': 'pmpaddr48',
            '0x3e1': 'pmpaddr49',
            '0x3e2': 'pmpaddr50',
            '0x3e3': 'pmpaddr51',
            '0x3e4': 'pmpaddr52',
            '0x3e5': 'pmpaddr53',
            '0x3e6': 'pmpaddr54',
            '0x3e7': 'pmpaddr55',
            '0x3e8': 'pmpaddr56',
            '0x3e9': 'pmpaddr57',
            '0x3ea': 'pmpaddr58',
            '0x3eb': 'pmpaddr59',
            '0x3ec': 'pmpaddr60',
            '0x3ed': 'pmpaddr61',
            '0x3ee': 'pmpaddr62',
            '0x3ef': 'pmpaddr63',
            #Machine Non-Maskable Interrupt Handling
            '0x740': 'mnscratch',
            '0x741': 'mnepc',
            '0x742': 'mncause',
            '0x743': 'mntval',
            '0x744': 'mnstatus',
            #Machine Counter/Timers
            '0xb00': 'mcycle',
            '0xb02': 'minstret',
            '0xb03': 'mhpmcounter3',
            '0xb04': 'mhpmcounter4',
            '0xb05': 'mhpmcounter5',
            '0xb06': 'mhpmcounter6',
            '0xb07': 'mhpmcounter7',
            '0xb08': 'mhpmcounter8',
            '0xb09': 'mhpmcounter9',
            '0xb0a': 'mhpmcounter10',
            '0xb0b': 'mhpmcounter11',
            '0xb0c': 'mhpmcounter12',
            '0xb0d': 'mhpmcounter13',
            '0xb0e': 'mhpmcounter14',
            '0xb0f': 'mhpmcounter15',
            '0xb10': 'mhpmcounter16',
            '0xb11': 'mhpmcounter17',
            '0xb12': 'mhpmcounter18',
            '0xb13': 'mhpmcounter19',
            '0xb14': 'mhpmcounter20',
            '0xb15': 'mhpmcounter21',
            '0xb16': 'mhpmcounter22',
            '0xb17': 'mhpmcounter23',
            '0xb18': 'mhpmcounter24',
            '0xb19': 'mhpmcounter25',
            '0xb1a': 'mhpmcounter26',
            '0xb1b': 'mhpmcounter27',
            '0xb1c': 'mhpmcounter28',
            '0xb1d': 'mhpmcounter29',
            '0xb1e': 'mhpmcounter30',
            '0xb1f': 'mhpmcounter31',
            '0xb80': 'mcycleh',
            '0xb82': 'minstreth',
            '0xb83': 'mhpmcounter3h',
            '0xb84': 'mhpmcounter4h',
            '0xb85': 'mhpmcounter5h',
            '0xb86': 'mhpmcounter6h',
            '0xb87': 'mhpmcounter7h',
            '0xb88': 'mhpmcounter8h',
            '0xb89': 'mhpmcounter9h',
            '0xb8a': 'mhpmcounter10h',
            '0xb8b': 'mhpmcounter11h',
            '0xb8c': 'mhpmcounter12h',
            '0xb8d': 'mhpmcounter13h',
            '0xb8e': 'mhpmcounter14h',
            '0xb8f': 'mhpmcounter15h',
            '0xb90': 'mhpmcounter16h',
            '0xb91': 'mhpmcounter17h',
            '0xb92': 'mhpmcounter18h',
            '0xb93': 'mhpmcounter19h',
            '0xb94': 'mhpmcounter20h',
            '0xb95': 'mhpmcounter21h',
            '0xb96': 'mhpmcounter22h',
            '0xb97': 'mhpmcounter23h',
            '0xb98': 'mhpmcounter24h',
            '0xb99': 'mhpmcounter25h',
            '0xb9a': 'mhpmcounter26h',
            '0xb9b': 'mhpmcounter27h',
            '0xb9c': 'mhpmcounter28h',
            '0xb9d': 'mhpmcounter29h',
            '0xb9e': 'mhpmcounter30h',
            '0xb9f': 'mhpmcounter31h',
            #Machine Counter Setup
            '0x320': 'mcountinhibit',
            '0x323': 'mhpmevent3',
            '0x324': 'mhpmevent4',
            '0x325': 'mhpmevent5',
            '0x326': 'mhpmevent6',
            '0x327': 'mhpmevent7',
            '0x328': 'mhpmevent8',
            '0x329': 'mhpmevent9',
            '0x32a': 'mhpmevent10',
            '0x32b': 'mhpmevent11',
            '0x32c': 'mhpmevent12',
            '0x32d': 'mhpmevent13',
            '0x32e': 'mhpmevent14',
            '0x32f': 'mhpmevent15',
            '0x330': 'mhpmevent16',
            '0x331': 'mhpmevent17',
            '0x332': 'mhpmevent18',
            '0x333': 'mhpmevent19',
            '0x334': 'mhpmevent20',
            '0x335': 'mhpmevent21',
            '0x336': 'mhpmevent22',
            '0x337': 'mhpmevent23',
            '0x338': 'mhpmevent24',
            '0x339': 'mhpmevent25',
            '0x33a': 'mhpmevent26',
            '0x33b': 'mhpmevent27',
            '0x33c': 'mhpmevent28',
            '0x33d': 'mhpmevent29',
            '0x33e': 'mhpmevent30',
            '0x33f': 'mhpmevent31',
            #Debug/Trace Registers (shared with Debug Mode)
            '0x7a0': 'tselect',
            '0x7a1': 'tdata1',
            '0x7a2': 'tdata2',
            '0x7a3': 'tdata3',
            '0x7a8': 'mcontext',
            #Debug Mode Registers
            '0x7b0': 'dcsr',
            '0x7b1': 'dpc',
            '0x7b2': 'dscratch',
            '0x7b3': 'dscratch1',

            '0x345': 'mnxti',
            '0x347': 'mintthresh',
            '0x346': 'mintstatus',
            '0x348': 'mscratchcsw',
            '0x349': 'mscratchcswl',
            }

