# clocks.py
from interactions import Extension, slash_command, SlashContext, slash_option, OptionType
import datetime as dt

class Clocks(Extension):
    def __init__(self):
        super().__init__()

    