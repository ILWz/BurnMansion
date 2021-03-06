﻿init -97 python:
    try:
        mmm.add(
            gui0_menu(
                _("Save"),
                ShowMenu("save"),
                True, False, True
                ),
            )
        mmm.add(
            gui0_menu(
                _("Load"),
                ShowMenu("load"),
                False, False, True
                ),
            )
    except:
        pass

init offset = -1
define config.thumbnail_width = 384
define config.thumbnail_height = 216
## Load and Save screens #######################################################

screen save():
    tag menu
    add "0GUI/save/frame_save.jpg"
    use file_slots(_("Save"))

screen load():
    tag menu
    add "0GUI/save/frame_load.jpg"
    use file_slots(_("Load"))
    
screen file_slots(title):
    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))
    style_prefix "sav"
    use game_menu(title):
        vbox:
            yoffset 80
            grid 3 2:
                for i in range(6):
                    $ slot = i + 1
                    button:
                        at btn
                        background Frame("0GUI/save/save_slot.png", 20,20)
                        action FileAction(slot)
                        has vbox
                        add FileScreenshot(slot)
                        text FileTime(slot, format=_("{#file_time}%a, %H:%M - %b %d  %Y, "), empty=_("empty slot")) text_align .5
                        if FileSaveName(slot):
                            text FileSaveName(slot)
                        key "save_delete" action FileDelete(slot)

        hbox:
            yoffset -300
            button:
                background None
                add "0GUI/save/left_arrow_th.png"
                action FilePagePrevious() at btn
            button:
                background Frame("0GUI/save/mdle_th.png", 10,10)
                ysize 82
                at btn
                key_events True
                action page_name_value.Toggle()
                input:
                    value page_name_value
            button:
                background None
                add "0GUI/save/right_arrow_th.png"
                action FilePageNext() at btn
