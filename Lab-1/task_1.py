class Language:
    def __init__(self, name: str, procedural: bool, high_level: bool, object_oriented: bool, functional: bool):
        self.name = name
        self.conf = {
            'procedural': procedural, # non-procedural
            'high_level': high_level, # low level
            'object_oriented': object_oriented, # declarative
            'functional': functional #logic
        }

# Данные не являются точно корректными. Большинство языков программирования мультипарадигмальные.
# Здесь больше представлена демонстрация фасетного поиска.
languages = [
    Language("Assembler",    procedural=True, high_level=False, object_oriented=False, functional=False),
    Language("BASIC",        procedural=True, high_level=True, object_oriented=True, functional=False),
    Language("Pascal",       procedural=True, high_level=True, object_oriented=False, functional=False),
    Language("C",            procedural=True, high_level=True, object_oriented=False, functional=False),
    Language("Fortran",      procedural=True, high_level=True, object_oriented=False, functional=False),

    Language("C++",          procedural=True, high_level=True, object_oriented=True, functional=True),
    Language("Java",         procedural=True, high_level=True, object_oriented=True, functional=True),

    Language("Visual Basic", procedural=False, high_level=True, object_oriented=True, functional=False),
    Language("Delphi",       procedural=False, high_level=True, object_oriented=True, functional=False),

    Language("Prolog",       procedural=False, high_level=True, object_oriented=False, functional=False),
    Language("Lisp",         procedural=True, high_level=True, object_oriented=False, functional=True),
    Language("PHP",          procedural=True, high_level=True, object_oriented=True, functional=True),
    Language("SQL",          procedural=True, high_level=True, object_oriented=True, functional=True)
]

if __name__ == "__main__":
    conf = {
        'procedural': True,
        'high_level': True,
        'object_oriented': False,
        'functional': False
    }
    
    def handle_ans(v) -> bool:
        return v == "Да"

    for key in conf:
        if key == "procedural":
            conf[key] = handle_ans(input("Является ли язык процедурным? "))
        elif key == "high_level":
            conf[key] = handle_ans(input("Является ли язык высокоуровневым? "))
        elif key == "object_oriented":
            conf[key] = handle_ans(input("Является ли язык объектно-ориентированным? "))
        elif key == "functional":
            conf[key] = handle_ans(input("Является ли язык функциональным? "))

    selected_languages = []
    for lang in languages:
        if conf == lang.conf:
            selected_languages.append(lang.name)

    print(f"Ответ: {', '.join(selected_languages)}")