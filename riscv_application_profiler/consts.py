commitlog_regex="^core\s+\d+:\s+\d*\s+(0x[0-9a-fA-F]+)\s+\((0x[0-9a-fA-F]+)\)\s*(x[0-9]*)?(c[0-9]+[_a-z]*)?(mem)?\s*(0x[0-9a-fA-F]*)?\s*(x[0-9]*)?(c[0-9]+[_a-z]*)?(mem)?\s*(0x[0-9a-fA-F]*)?\s*(x[0-9]*)?(c[0-9]+[_a-z]*)?(mem)?\s*(0x[0-9a-fA-F]*)?"
disass_regex = "^\s*([0-9a-f]+):\s+([0-9a-f]+)\s+([a-z][a-z\.0-9]*)"


# branch_lists = [bge, bgeu, blt, bltu, beq, bne, jalr, jal]