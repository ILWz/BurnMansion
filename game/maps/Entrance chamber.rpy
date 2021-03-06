﻿# image bird_move:
#     "maps/office/office_bird.png"
#     xpos 800 yalign .2
#     linear 4 xpos renpy.random.randint(240,315) yalign .2
#     pause 2
#     xpos 800 yalign .2
#     linear 4 xpos renpy.random.randint(260,353) yalign .3
#     pause 2
#     repeat



image entrance_chamber_fire:
    "chamber_fire1"
    .15
    "chamber_fire2"
    .15
    "chamber_fire3" 
    .15
    "chamber_fire4"
    .15
    "chamber_fire5" 
    .15
    "chamber_fire6"
    .15
    repeat

image entrance_chamber_fire_left:
    "chamber_fire1_left"
    .15
    "chamber_fire2_left"
    .15
    "chamber_fire3_left" 
    .15
    "chamber_fire4_left"
    .15
    "chamber_fire5_left" 
    .15
    "chamber_fire6_left"
    .15
    repeat

default chamber_entrance_door_loc = place("Locked Door", (602, 192), Jump('chamber_entrance_door'), "location/chamber entrance/chamber entrance door.png")
default chamber_entrance_exit_loc = place("Exit entrance", (755, 1047), [Play("music", "audio/mansion_draft1.mp3"), Jump('office')], "location/chamber entrance/chamber exit.png")

# default office_fire_loc = place("fire", (0, 0), None, "office_fire")

default chamber_entrance_map = maps(
    "Chamber gate",
    [
    #    "chamber insert",
        # "office_sky",
        # "bird_move",
        # "office_sky_wood",
        "entrance_chamber_fire_left",
        "entrance_chamber_fire",
        chamber_entrance_door_loc,
        "chamber insert",
        chamber_entrance_exit_loc,


    ]
    )


label chamber_entrance:
    scene chamber entrance bg
    show screen map(chamber_entrance_map)
    pause
    jump chamber_entrance



label chamber_entrance_door:

    if check_door == False and chamber_diamond_collected == False:
        burn "Oh, I remember this. This is one of my many genius creation."
        burn "I wanted something unique and unusual kind of secret chamber with a locked door"
        burn "The password or simple lock is super boring and lame, so I came up with this genius idea"
        burn "That was to, implement a triangle shape and you require to . . . . ."
        burn "Wait"
        burn "Why don't I remember this???!!?"
        burn "I have to ask Weylon about this, it has been ages since I last came here. "
        $ check_door = True
        jump chamber_entrance

    # if chamber_diamond_collected == False:
    #     # $ chamber_entrance_map.rem("chamber insert")
    #     # $ chamber_entrance_map.discover("chamber diamond")
    #     burn "Hm... missing something here"
    #     # $ chamber_diamond_collected = True
    #     jump chamber_entrance

    if chamber_diamond_collected == True:
        jump chamber

    if chamber_diamond_collected == False and player.bags[0].exist(blue_gem, 1) and player.bags[0].exist(green_gem, 1) and player.bags[0].exist(red_gem, 1):
        burn "Got all the parts needed, about time I place it where It belongs "
        $ chamber_entrance_map.rem("chamber insert")
        $ chamber_entrance_map.discover("chamber diamond")
        burn "There we go, I should be able to open it now"
        $ player.drop(blue_gem, 1), player.drop(red_gem, 1), player.drop(green_gem, 1)
        $ check_door = False
        $ chamber_diamond_collected = True
        jump chamber_entrance

    else:
        burn "Hm.. missing something here"
        jump chamber_entrance

# label office_football:
#     burn "Ahh HA, a signed football"
#     burn "This will definitly sell me some good price !"
#     $ office_map.rem(office_football_loc)
#     jump office
