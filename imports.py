from typing import Generator
import re

from AI_DIRECTIVES.Instructions import CAPTAIN_INSTRUCTIONS
from INTELLIGENCE.REACTION.LINGUISTICS import groq
from SPEECH_MODULES.SPEECH_SYNTHESIS.text_to_speech import speak

captain_text = [
  '\033[0;94mC\033[0m',
  '\033[1;94m.A\033[0m',
  '\033[1;96m.P\033[0m',
  '\033[0;94m.T\033[0m',
  '\033[1;94m.A\033[0m',
  '\033[1;96m.I\033[0m',
  '\033[0;94m.N\033[0m'
]
