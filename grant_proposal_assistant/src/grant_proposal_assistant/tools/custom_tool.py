from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field

class WordLimitChecker:
    def check(self, text, limit):
        words = text.split()
        count = len(words)

        return {
            "word_count": count,
            "within_limit": count <= limit,
            "words_to_cut": max(0, count - limit)
        }
