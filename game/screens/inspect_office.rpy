# screens/inspect_office.rpy
screen inspect_office():
    tag inspect

    add "images/bg/office_evening.png"

    text "Осмотр (кликни на объекты)" xpos 0.03 ypos 0.03

    # ОКНО (большая зона по центру-право, верхняя половина)
    button:
        xpos 0.28
        ypos 0.10
        xsize 0.69
        ysize 0.56
        background None
        hover_background None
        action Function(_inspect_window)

    # СТОЛ (нижняя центральная зона)
    button:
        xpos 0.18
        ypos 0.56
        xsize 0.66
        ysize 0.34
        background None
        hover_background None
        action Function(_inspect_desk)

    textbutton "Вернуться":
        xpos 0.85 ypos 0.92
        action Return()

init python:
    def _inspect_window():
        global clarity, inspected_window
        if not inspected_window:
            inspected_window = True
            clarity += 1
        renpy.say(None,
            "За окном — стройка. Башенные краны стоят, как молчаливые скобки, удерживающие серое небо.\n"
            "Огоньки в недостроенных этажах горят слишком ровно — будто кто-то проверяет, жив ли город."
        )

    def _inspect_desk():
        global clarity, inspected_desk
        if not inspected_desk:
            inspected_desk = True
            clarity += 1
        renpy.say(None,
            "На столе — ноутбук, пара листов и чей-то телефон.\n"
            "Всё разложено так аккуратно, что кажется: здесь не работают — здесь подготавливают картинку работы."
        )
