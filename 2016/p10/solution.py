import re
from collections import defaultdict


def process_instructions(ip_str, targets_a=None, output_bins_b=None):
    bots = defaultdict(list)
    outputs = defaultdict(list)
    bot_instructions = {}

    def _transfer_chip(recipient_type, recipient_num, chip):
        if recipient_type == 'bot':
            bots[recipient_num].append(chip)
        elif recipient_type == 'output':
            outputs[recipient_num].append(chip)

    for ip_line in ip_str.split('\n'):
        matches = re.search(r"value (?P<chip>\w+) goes to bot (?P<bot>\w+)", ip_line)
        if matches:
            chip, bot = matches.group('chip'), matches.group('bot')
            bots[bot].append(chip)
        else:
            matches = re.search(
                r"bot (?P<bot>\w+) gives low to (?P<lower_recipient_type>\w+) (?P<lower_recipient_num>\w+) "
                r"and high to (?P<higher_recipient_type>\w+) (?P<higher_recipient_num>\w+)",
                ip_line)
            if matches:
                bot, lower_recipient_type, \
                lower_recipient_num, higher_recipient_type, higher_recipient_num \
                    = matches.group('bot'), matches.group('lower_recipient_type'), \
                      matches.group('lower_recipient_num'), matches.group('higher_recipient_type'), \
                      matches.group('higher_recipient_num')
                bot_instructions[bot] = {
                    'lower_recipient_type': lower_recipient_type,
                    'lower_recipient_num': lower_recipient_num,
                    'higher_recipient_type': higher_recipient_type,
                    'higher_recipient_num': higher_recipient_num
                }

    while True:
        active_bots = dict(filter(lambda (x, y): len(y) == 2 and x in bot_instructions, bots.items())).keys()
        if not active_bots:
            break
        for active_bot in active_bots:
            current_instruction = bot_instructions.pop(active_bot)
            if all(target_chip in bots[active_bot] for target_chip in targets_a):
                print active_bot
            sorted_list = sorted(bots.pop(active_bot), key=int)
            lower_chip, higher_chip = sorted_list[0], sorted_list[1]
            _transfer_chip(current_instruction['lower_recipient_type'],
                           current_instruction['lower_recipient_num'],
                           lower_chip)
            _transfer_chip(current_instruction['higher_recipient_type'],
                           current_instruction['higher_recipient_num'],
                           higher_chip)

    print reduce(lambda x, y: x * y, [int(outputs[i][0]) for i in output_bins_b])


ip_str = open('input.txt', 'r').read()
process_instructions(ip_str, targets_a=['61', '17'], output_bins_b=['0', '1', '2'])