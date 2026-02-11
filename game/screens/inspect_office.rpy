# screens/inspect_office.rpy
screen inspect_office():
    tag inspect

    add "images/bg/office_evening.png"

    # Небольшая подсказка
    text "Осмотр (кликни на объекты)" xpos 0.03 ypos 0.03

    # ДВЕРЬ (условная зона слева)
    button:
        xpos 0.05 ypos 0.25 xsize 0.20 ysize 0.45
        background None
        hover_background None
        action Function(_inspect_door)

    # СТОЛ (условная зона справа)
    button:
        xpos 0.60 ypos 0.45 xsize 0.30 ysize 0.35
        background None
        hover_background None
        action Function(_inspect_desk)

    textbutton "Вернуться":
        xpos 0.85 ypos 0.92
        action Return()

init python:
    def _inspect_door():
        global clarity, inspected_door
        if not inspected_door:
            inspected_door = True
            clarity += 1
        renpy.say(None, "На двери нет таблички. Только свежая краска и след от снятого скотча.\nКак будто название здесь бывает… но не задерживается.")

    def _inspect_desk():
        global clarity, inspected_desk
        if not inspected_desk:
            inspected_desk = True
            clarity += 1
        renpy.say(None, "В ящике лежит пачка чистых листов и одна ручка.\nРучка без логотипа. Как будто её купили специально, чтобы не запоминалась.")
