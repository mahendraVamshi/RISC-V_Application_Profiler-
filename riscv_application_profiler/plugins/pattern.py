from riscv_isac.log import *
from riscv_application_profiler.consts import *
import re

def group_by_pattern(master_inst_list: list, ops_dict: dict, extension_used: list):
    '''
    Groups instructions based on the operation.

    Args:
        - master_inst_list: A list of InstructionEntry objects.

    Returns:
        - A 
    '''
    # Log the start of the process for getting the pattern.
    logger.info("Getting Pattern.")

    # Initialize dictionaries to hold address counts, patterns, names, and cycle information.
    count_dict = {}
    pattern_dict = {}
    address_name_dict = {}
    address_pc_dict = {}
    address_cycle_dict = {}
    prev = None

    # Loop through each entry in the master_inst_list.
    for entry in master_inst_list:
        # Check if the instruction address is not in the count_dict.
        if hex(entry.instr_addr) not in count_dict:
            count_dict[hex(entry.instr_addr)] = 0
            address_name_dict[hex(entry.instr_addr)] = entry.instr_name
            address_pc_dict[hex(entry.instr_addr)] = str(hex(entry.instr_addr))
            address_cycle_dict[hex(entry.instr_addr)] = 1
        count_dict[hex(entry.instr_addr)] += 1

    # Group instructions based on their occurrence count.
    for entry in count_dict:
        if count_dict[entry] not in pattern_dict:
            pattern_dict[count_dict[entry]] = list()
        pattern_dict[count_dict[entry]].append(entry)

    # Sort the patterns by occurrence count in descending order.
    sort_count_list = sorted(pattern_dict.items(), key=lambda x: x[0], reverse=True)

    # Remove single instructions or patterns with count 1.
    sort_count_list = [entry for entry in sort_count_list if len(entry[1]) > 1 and entry[0] != 1]

    # Initialize a dictionary to store sorted pattern information.
    s_dict = {'count': [], 'instr': [], 'PC': [], 'cycles': [], 'cycles_reduced': []}

    # Process sorted patterns.
    for entry in sort_count_list:
        adj_inst = [address_name_dict[entry[1][0]]]
        adj_pc = [address_pc_dict[entry[1][0]]]
        adj_cycles = [address_cycle_dict[entry[1][0]]]
        prev = entry[1][0]
        for i in entry[1][1:]:
            # Check if the difference between addresses is 4 or 2.
            if (int(i, 16) - int(prev, 16)) == 4 or (int(i, 16) - int(prev, 16)) == 2:
                adj_inst.append(address_name_dict[i])
                adj_pc.append(address_pc_dict[i])
                adj_cycles.append(address_cycle_dict[i])
            else:
                # Store the current pattern information.
                # if adj_cycles in s_dict['cycles']:
                #     continue
                s_dict['instr'].append(adj_inst)
                s_dict['PC'].append(adj_pc)
                s_dict['cycles'].append(adj_cycles)
                s_dict['count'].append(entry[0])
                adj_inst = [address_name_dict[i]]
                adj_pc = [address_cycle_dict[i]]
                adj_cycles = [address_cycle_dict[i]]
            prev = i
        if len(adj_inst) > 1:
            s_dict['count'].append(entry[0])
            s_dict['cycles'].append(adj_cycles)
            s_dict['instr'].append(adj_inst)
            s_dict['PC'].append(adj_pc)

    # Calculate improved performance for each pattern.
    for i in range(len(s_dict['count'])):
        imp_performance = s_dict['count'][i] * (sum(s_dict['cycles'][i]) - 1)
        s_dict['cycles_reduced'].append(imp_performance)

    # Log the completion of pattern computation.
    logger.info("Pattern computed.")
    # Return the computed pattern information.
    return s_dict