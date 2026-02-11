screen inspect_party():
    tag inspect

    add "images/bg/office_party.png"

    text "Осмотр (кликни на объекты)" xpos 0.03 ypos 0.03

    # ЁЛКА (справа)
    button:
        xpos 0.78
        ypos 0.22
        xsize 0.20
        ysize 0.56
        background None
        hover_background None
        action Function(_inspect_tree)

    # АЛКОГОЛЬ НА СТОЛЕ (центр-лево)
    button:
        xpos 0.30
        ypos 0.48
        xsize 0.34
        ysize 0.30
        background None
        hover_background None
        action Function(_inspect_alcohol)

    textbutton "Вернуться":
        xpos 0.85 ypos 0.92
        action Return()

init python:
    def _inspect_tree():
        global clarity, inspected_tree
        if not inspected_tree:
            inspected_tree = True
            clarity += 1
        renpy.say(None,
            "Ёлка выглядит не офисно. Слишком домашняя — даже не домашняя, а будто из гаража.\n"
            "Игрушки разные, старые, чужие. Как будто их не покупали — их принесли."
        )

    def _inspect_alcohol():
        global clarity, inspected_alcohol
        if not inspected_alcohol:
            inspected_alcohol = True
            clarity += 1
        renpy.say(None,
            "Алкоголь странный и бедный. Лейблы такие, будто их печатали на принтере.\n"
            "Для корпоратива — как-то слишком скромно. И почему-то слишком… уверенно выставлено на стол."
        )
