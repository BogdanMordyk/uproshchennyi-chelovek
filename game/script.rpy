# game/script.rpy (или game/script/00_init.rpy)

define d = Character("Даша")
define n = Character(None)

image bg office_evening = "images/bg/office_evening.png"
image bg office_party = "images/bg/office_party.png"
image dasha_neutral = "images/chars/dasha_neutral.png"
image dasha_party = "images/chars/dasha_party.png"
image envelope = "images/items/envelope.png"

label start:
    jump office_slice
