"""
CP1404 - Prac 06 languages
Estimate - 15mins 10:37
Actual -
"""
from prac_06.programming_language import ProgrammingLanguage


def main():
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    print(python, ruby, visual_basic, sep="\n")

    programming_languages = [python, ruby, visual_basic]
    print("The dynamically typed languages are:")
    print("\n".join(language.name for language in programming_languages if language.is_dynamic()))

    # for language in programming_languages:
    #     if language.is_dynamic():
    #         print(language.name)


main()
