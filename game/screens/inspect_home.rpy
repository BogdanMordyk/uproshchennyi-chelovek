screen inspect_home():
    tag inspect

    add "images/bg/home_tv.png"

    text "Осмотр (кликни на объекты)" xpos 0.03 ypos 0.03

    # ТЕЛЕВИЗОР (центр-право)
    button:
        xpos 0.47
        ypos 0.18
        xsize 0.46
        ysize 0.40
        background None
        hover_background None
        action Function(_inspect_tv)

    # ВИНО (справа на столике)
    button:
        xpos 0.70
        ypos 0.52
        xsize 0.26
        ysize 0.34
        background None
        hover_background None
        action Function(_inspect_wine)

    textbutton "Вернуться":
        xpos 0.85 ypos 0.92
        action Return()

init python:
    def _inspect_tv():
        global clarity, inspected_tv
        if not inspected_tv:
            inspected_tv = True
            clarity += 1

        # Текст зависит от clarity ПОСЛЕ увеличения (это ок — так даже сильнее)
        if clarity <= 6:
            renpy.say(None,
                "По телевизору — снег. Белый шум, как дыхание стены.\n"
                "Почему там ничего нет? И как давно это продолжается?"
            )
        else:
            renpy.say(None,
                "Снег на экране словно шевелится не случайно.\n"
                "Меня гипнотизируют. Меня держат здесь этим шумом."
            )

    def _inspect_wine():
        global clarity, inspected_wine
        if not inspected_wine:
            inspected_wine = True
            clarity += 1

        if clarity < 6:
            renpy.say(None,
                "Вино тёмное, липкое. Пахнет сладко, слишком сладко.\n"
                "Хватит пить эту дрянь. Надо собраться."
            )
        else:
            renpy.say(None,
                "Это вообще не похоже на вино. Слишком вязкое.\n"
                "Откуда оно тут взялось? И почему я не помню, как наливал?"
            )
