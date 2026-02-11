# systems/fx.rpy

# Шумовой оверлей (чуть двигается, чтобы "жил")
image ui_noise = "images/ui/noise.png"

transform noise_wiggle:
    alpha 0.0
    pause 0.05
    alpha 0.04
    pause 0.05
    alpha 0.02
    pause 0.05
    alpha 0.05
    pause 0.05
    alpha 0.03
    pause 0.05
    repeat

# Лёгкое "дыхание" кадра (почти незаметный zoom)
transform slow_breath:
    zoom 1.0
    linear 3.0 zoom 1.01
    linear 3.0 zoom 1.0
    repeat

# Экран эффектов: включается при clarity > 6
screen clarity_fx():
    zorder 200  # поверх всего

    if clarity > 6:
        # чуть "дышит" вся сцена
        add Solid("#0000") at slow_breath

        # шум поверх картинки
        add "ui_noise" at noise_wiggle

        # лёгкая виньетка (без отдельной картинки — просто затемняем края чуть-чуть)
        # (простая имитация: полупрозрачная черная подложка)
        add Solid("#000000") alpha 0.06
