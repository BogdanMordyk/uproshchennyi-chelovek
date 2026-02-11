# game/script.rpy (или game/script/00_init.rpy)

define d = Character("Даша")
define n = Character(None)

image bg office_evening = "images/bg/office_evening.png"
image dasha_neutral = "images/chars/dasha_neutral.png"
image envelope = "images/items/envelope.png"

label start:
    jump office_slice
