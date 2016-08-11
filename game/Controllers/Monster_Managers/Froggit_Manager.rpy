

init -9 python:

    class Froggit(Monster):
        def __init__(self):
            Monster.__init__(self)
            self.name = "Froggit"
            self.default_event = Event("froggit_default_dialogue",True,self)





#this is floweys default scene
label froggit_default_dialogue(owner):
    call show_buttons
    show froggit normal

    $ renpy.pause()

    if not owner.visited:
        froggit "Oh, hello!"
        froggit "Try to watch out where you walk."
        froggit "Some of my friends are very tiny, so it is easy to not see them." 
        froggit "Wait, where are they...actually..."
        $ owner.visited = True
    
    elif not owner.dialogue_toggle:
        froggit "Is this the first time for you to talk to a Froggit?"
        froggit "Sometimes people forget about us so it feels nice..."
        hide froggit
        show froggit happy
        froggit "I am glad we don't have to fight!"
        froggit "Hum?"
        hide froggit
        show froggit happy
        froggit "Oh yes, monsters used to fight humans..."
        froggit "But that is in the past, we mostly talk now!"
        $ owner.dialogue_toggle = True

    else:
        froggit "You know, even if it is sometimes tempting, it is quite rude to skip what someone is saying you know."
        froggit "But hey, if you want to, you just have to click!"
        $ owner.dialogue_toggle = False
    
    return
