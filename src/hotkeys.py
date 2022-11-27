from typing import Tuple
from monkey_enum import MonkeyEnum
from action_enum import ActionEnum

def get_monkey_key(monkey:MonkeyEnum) -> Tuple[str]:
    if(monkey == MonkeyEnum.DART_MONKEY): return ('q',)
    if(monkey == MonkeyEnum.BOOMERANG_MONKEY): return ('w',)
    if(monkey == MonkeyEnum.BOMB_SHOOTER): return ('e',)
    if(monkey == MonkeyEnum.TACK_SHOOTER): return ('r',)
    if(monkey == MonkeyEnum.ICE_MONKEY): return ('t',)
    if(monkey == MonkeyEnum.GLUE_GUNNER): return ('y',)
    if(monkey == MonkeyEnum.SNIPER_MONKEY): return ('z',)
    if(monkey == MonkeyEnum.MONKEY_SUB): return ('x',)
    if(monkey == MonkeyEnum.MONKEY_BUCANEER): return ('c',)
    if(monkey == MonkeyEnum.MONKEY_ACE): return ('v',)
    if(monkey == MonkeyEnum.HELI_PILOT): return ('b',)
    if(monkey == MonkeyEnum.MORTAR_MONKEY): return ('n',)
    if(monkey == MonkeyEnum.DARTLING_GUNNER): return ('m',)
    if(monkey == MonkeyEnum.WIZARD_MONKEY): return ('a',)
    if(monkey == MonkeyEnum.SUPER_MONKEY): return ('s',)
    if(monkey == MonkeyEnum.NINJA_MONKEY): return ('d',)
    if(monkey == MonkeyEnum.ALCHEMIST): return ('f',)
    if(monkey == MonkeyEnum.DRUID): return ('g',)
    if(monkey == MonkeyEnum.BANANA_FARM): return ('h',)
    if(monkey == MonkeyEnum.ENGINEER_MONKEY): return ('l',)
    if(monkey == MonkeyEnum.SPIKE_FACTORY): return ('j',)
    if(monkey == MonkeyEnum.MONKEY_VILLAGE): return ('k',)
    if(monkey == MonkeyEnum.HEROES): return ('u',)

def get_action_key(action:ActionEnum)->Tuple[str, ...]:
    if(action == ActionEnum.UPGRADE_PATH_1): return (',',)
    if(action == ActionEnum.UPGRADE_PATH_2): return ('.',)
    if(action == ActionEnum.UPGRADE_PATH_3): return ('/',)
    if(action == ActionEnum.CHANGING_TARGETING): return ('tab',)
    if(action == ActionEnum.REVERSE_CHANGING_TARGETING): return ('ctrl', 'tab')
    if(action == ActionEnum.MONKEY_SPECIAL): return ('pgdown',)
    if(action == ActionEnum.SELL): return ('backspace',)
    if(action == ActionEnum.PLAY_OR_FAST_FORWARD): return ('space',)
    if(action == ActionEnum.SEND_NEXT_ROUND): return ('shift', 'space')
    if(action == ActionEnum.PAUSE): return ('`',)
    if(action == ActionEnum.ACTIVIATED_ABILITY_1): return ('1',)
    if(action == ActionEnum.ACTIVIATED_ABILITY_2): return ('2',)
    if(action == ActionEnum.ACTIVIATED_ABILITY_3): return ('3',)
    if(action == ActionEnum.ACTIVIATED_ABILITY_4): return ('4',)
    if(action == ActionEnum.ACTIVIATED_ABILITY_5): return ('5',)
    if(action == ActionEnum.ACTIVIATED_ABILITY_6): return ('6',)
    if(action == ActionEnum.ACTIVIATED_ABILITY_7): return ('7',)
    if(action == ActionEnum.ACTIVIATED_ABILITY_8): return ('8',)
    if(action == ActionEnum.ACTIVIATED_ABILITY_9): return ('9',)
    if(action == ActionEnum.ACTIVIATED_ABILITY_10): return ('0',)
    if(action == ActionEnum.ACTIVIATED_ABILITY_11): return ('-',)
    if(action == ActionEnum.ACTIVIATED_ABILITY_12): return ('=',)
    if(action == ActionEnum.ROAD_SPIKES): return ('shift', '1')
    if(action == ActionEnum.MOAB_MINES): return ('shift', '2')
    if(action == ActionEnum.GLUE_TRAP): return ('shift', '3')
    if(action == ActionEnum.CAMO_TRAP): return ('shift', '4')
    if(action == ActionEnum.BANANA_FARMER): return ('shift', '5')
    if(action == ActionEnum.TECH_BOT): return ('shift', '6')
    if(action == ActionEnum.ENERGIZING_TOTEM): return ('shift', '7')
    if(action == ActionEnum.PONTOON): return ('shift', '8')
    if(action == ActionEnum.PORTABLE_LAKE): return ('shift', '9')
    if(action == ActionEnum.SUPER_MONKEY_STORM): return ('shift', '0')
    if(action == ActionEnum.MONKEY_BOOST): return ('shift', '-')
    if(action == ActionEnum.THRIVE): return ('shift', '=')
    if(action == ActionEnum.TIME_STOP): return ('shift', '[')
    if(action == ActionEnum.CASH_DROP): return ('shift', ']')
    if(action == ActionEnum.SEND_RED_BLOON): return ('ctrl', '1')
    if(action == ActionEnum.SEND_BLUE_BLOON): return ('ctrl', '2')
    if(action == ActionEnum.SEND_GREEN_BLOON): return ('ctrl', '3')
    if(action == ActionEnum.SEND_YELLOW_BLOON): return ('ctrl', '4')
    if(action == ActionEnum.SEND_PINK_BLOON): return ('ctrl', '5')
    if(action == ActionEnum.SEND_BLACK_BLOON): return ('ctrl', '6')
    if(action == ActionEnum.SEND_PURPLE_BLOON): return ('ctrl', '7')
    if(action == ActionEnum.SEND_WHITE_BLOON): return ('ctrl', '8')
    if(action == ActionEnum.SEND_LEAD_BLOON): return ('ctrl', '9')
    if(action == ActionEnum.SEND_ZEBRA_BLOON): return ('ctrl', '0')
    if(action == ActionEnum.SEND_RAINBOW_BLOON): return ('ctrl', '-')
    if(action == ActionEnum.SEND_CERAMIC_BLOON): return ('ctrl', '=')
    if(action == ActionEnum.SEND_MOAB_BLOON): return ('ctrl', 'o')
    if(action == ActionEnum.SEND_BFB_BLOON): return ('ctrl', 'p')
    if(action == ActionEnum.SEND_ZOMG_BLOON): return ('ctrl', '[')
    if(action == ActionEnum.SEND_DDT_BLOON): return ('ctrl', ']')
    if(action == ActionEnum.SEND_BAD_BLOON): return ('ctrl', '\\')
    if(action == ActionEnum.SEND_TEST_BLOON): return ('ctrl', '`')