# script/office_slice.rpy

label office_slice:

    scene bg office_evening

    play ambience "audio/ambience/office_hum.ogg" fadein 1.0

    n "Офис… странно спрятан. Не центр, но и не окраина."
    n "Новые дома вокруг, пустые окна, мокрый бетон."
    n "Я пришёл слишком рано — или слишком поздно."

    show dasha_neutral

    d "Ты уже тут. Быстро ты."

    if clarity >= 1:
        n "Она сказала это так, будто знала."
    else:
        n "Видимо, меня уже ждали."

    menu:
        "Привет. Тут всегда так тихо?":
            $ clarity += 1
        "Привет. Да, решил не опаздывать.":
            $ bond += 1
        "Тут… точно офис?":
            $ clarity += 2
            $ bond -= 1

    if bond < 0:
        d "Да. Просто мы не любим лишнего шума."
    else:
        d "Пока да. Людей мало. Большинство позже."

    d "Я покажу, где ты будешь сидеть."

    # Осмотр
    call screen inspect_office

    d "Слушай… ты, наверное, удивишься. У нас зарплата… не как в госке."

    menu:
        "В смысле?":
            $ clarity += 1
        "Окей.":
            $ clarity -= 1
            $ bond += 1
        "Это незаконно.":
            $ clarity += 2
            $ bond -= 2

    d "Это просто удобнее. Не усложняй. Вот твой аванс."

    # Предмет: конверт
    show envelope at truecenter

    menu:
        "Взять конверт":
            $ envelope = True
            if clarity <= 0:
                $ clarity -= 1
        "Не брать":
            $ envelope = False
            $ clarity += 1
            $ bond -= 1

    hide envelope

    if envelope:
        n "Бумага плотная. Тёплая от её рук."
        n "Я почему-то не хочу считать сразу."
    else:
        n "Я оставил его на столе."
        n "Надо подумать, что делать с этой информацией."

    d "Ты быстро тут освоишься."
    pause 0.6
    d "…обычно так и происходит."

    stop ambience fadeout 1.0

    scene black
    n "Конец демо."
    return
