﻿transform girl_pos:
    xalign 0.8
    ypos 0.3
transform girl_pos1:
    xalign 0.86
    ypos 0.65


style scene_text is text:
    color 'fe4911'
    font 'fonts/gadugib.ttf'
    outlines [(4, "#000000", 0, 0)] # this value is not final, just trying to see some results





label story_1:
    hide screen map
    scene burn_lookdown
    pause
    scene burn_lookup with dissolve
    burn "...and so gentleman, so does my time as owner and operator of the Springfield Nuclear Power Plant finally come to a close."
    pause
    scene burn_yesmen4 with dissolve
    yes_men4 "But sir, wasn't that Canary M. Burns the legal owner of the plant?"
    scene burn_yesmen2 with dissolve
    yes_men2 "Yes, but then it got released and that idiot Simpson was granted power, correct?"
    scene burn_yesmen3 with dissolve
    yes_men3 "No because then he decided to relinquish power back to"
    yes_men3 "Mr. Burns because he learned a valuable lesson about family and spending time with"
    scene burn_yell_t with dissolve
    burn "That was seasons ago you squabbling ninnies!"
    scene burn_anger_t2 with dissolve
    burn "Nobody cares to remember that!"
    burn "Charles Montgomery Burns is the one"
    scene burn_hmm_left_t with dissolve
    burn "and only owner of this plant ever worth remembering or noting!"
    scene burn_yesmen1 with dissolve
    yes_men1 "So... it's really the end of the line, sir?"
    scene burn_yesmen3
    yes_men3 "The Burns dynasty has reached its final destination"
    scene burn_yesmen2
    yes_men2 "The plant isn't going to close, is it?"
    scene burn_hmml_t with dissolve
    burn "{i}Oh-ho!{/i} Please, please, gentleman! There's no such need for such dramatics!"
    scene burn_normal_t with dissolve
    burn "No, no, the plant will surpass me for hopefully many more years. I plan to make sure of that."
    burn "The transition of power will be a smooth and painless one!"
    burn "And I know that the person I pick will be the best man for the job!"
    scene burn_yesmen4 with dissolve
    yes_men4 "But sir, how can you be certain that they'll be up to the challenge?"
    scene burn_hmm_left_t with dissolve
    burn "Oh, quite simple, my good brown noser! By the simple virtue of knowing that my replacement..."
    scene burn_anger_t2 with dissolve
    burn "...won't be {u}any{/u} of you incompetent fools who drove my business into the ground in the first place!"
    scene yesmen_t with dissolve
    yes_men "...s-sir?"
    scene yesman_redbutton with dissolve
    burn "*Pushes the button*"
    scene fall_yesmen with dissolve
    pause
    yes_men "{i}AAAAAAAAGHHHH!!!!{/i}"
    scene fall_yesmen1 with dissolve
    pause
    burn "Oh hoho ho ho, {i}ah heh ahh hah hehh!!{/i}"
    scene fall_yesmen2 with dissolve
    $ burns_face = "normal"
    $ burns_hands = "3"
    scene office blur with dissolve   
    show burn_base at left with dissolve
  #  show weylon_base at right with dissolve
    pause
    $ burns_face = "smirkleft"
    pause
    $ burns_face = "hmm"
    burn "Oh ho... {i}hohhh{/i}, goodness..."
    burn "that was sweeter than a fourty year-old piece of Abba-Zabba"
    $ burns_face = "normal_t"
    burn "Oh yes, that really lifted my spirits"
    burn "Thank goodness I had Smithers hire that finance..."
    burn "...{i}hmmm?{/i}"
    burn "Smithers? Where are you?"
    $ burns_face = "angry"
    pause
    show weylon_base at right with dissolve
    pause
    $ weylon_face = "normal_t"
    weylon "Right here, Mr. Burns.{p}Pardon my absence, there was a situation I was attending to"
    $ weylon_face = "normal"
    $ burns_face = "normal_t"
    burn "{i}Ahhh{/i}, good, good... when you've the opportunity, do inform that delightful advisor you hired..."
    $ burns_face = "normal"
    burn "{i}Ehhrmmm{/i}..."
    $ weylon_face = "normal_t"
    $ burns_face = "normal"     
    weylon "Miss Hastings, sir?" 
    $ weylon_face = "normal"
    $ burns_face = "hmm"    
    burn "Yes, Hastings! Do tell Miss Hastings that I absolutely relished her suggestion to terminate all those higher up baffoons.."
    burn "If it's really true what she's said about the plant's future, then"
    $ burns_face = "normal_t"    
    burn "I'll glady part with those pompous tie clip wearing miscreants that fowled things up for me."
  #  $ weylon_face = "normal_t"
    $ burns_face = "normal"    
    pause
    $ weylon_face = "hmm"
    pause
    $ weylon_face = "hmm_t"
    weylon "Very good sir, a clean slate with your higher maintenance"
    weylon "was exactly what Miss Hastings had in mind."
    $ weylon_face = "normal_t"
    weylon "...Can't say I know whether she'd have been so on the nose with the trap door element"
    weylon "but I thought it was a marvelous touch"
    $ weylon_face = "normal"
    $ burns_face = "normal_t" 
    $ burns_hands = "2"
    burn "Oh well, you know"
    burn "I figured the air tube would prove fruitless considering the number of suit wearing rubes I had to deal with"
    $ burns_hands = "3"
    $ weylon_face = "normal_t"
    $ burns_face = "normal" 
    weylon "A very astute point sir, I don't think I could have said it any better myse"
    $ weylon_face = "normal"
    $ burns_face = "angry_t" 
    burn "Smithers! Enough jibber jabber! I think I've just proven my point that I don't need yes men to come in and kiss my pruney posterior!"
    $ weylon_face = "normal_t"
    $ burns_face = "angry" 
    weylon "Yes sir, of course"
    $ weylon_face = "normal"
    $ burns_face = "normal_t" 
    burn "No, what I need right now is people of action! Real bold initiative types! Someone who knows how to run a company as well oiled as I have!"
    $ weylon_face = "normal_t"
    $ burns_face = "normal" 
    weylon "Somebody who won't let his upper level staff make poor decisions with"
    weylon "his resources and borderline bankrupt his company, sir?"
    $ weylon_face = "normal"
    $ burns_face = "normal" 
    burn "..."
    $ burns_face = "normal_t" 
    burn "...as cheeky as you may be behaving right now, and"
    burn "as tempted I am to have you release the hounds on yourself, Smithers..."
    burn "I am aware the situation is dire."
    $ burns_face = "hmm"
    burn "And that's why I'm going to put in the work to make things profitable again"
    burn "...by making you and Miss Hastings figure out how to make things profitable again"
    $ weylon_face = "normal_t"
    $ burns_face = "normal" 
    weylon "Of course, sir, I'm sure when Miss Hastings arrives today, she'll have a few more ideas to-"


    pause



    # scene yesman_new1 with dissolve
    # pause
    # scene yesman_burn_lookup with dissolve
    # pause
    # scene yesman_burn_talk with dissolve
    # burn "isn’t that who I’m supposed to be?"
    # scene yes_man_all_talk with dissolve
    # yes_men "yes sir, absolutely, no mistake about it."
    # scene yesman_burn_talk2 with dissolve
    # burn "then tell me this. Why on earth has my business, the perfume business, has been dropping market wise? That’s not all! The business is about to FAIL! FAIL! Of all things! So tell me, how could this happen? Did I make a wrong move?"
    # scene yes_man_oneguy with dissolve  
    # yes_men "no sir, definitely not. You made all the right moves sir. Yes sir."  
    # scene yesman_burn_lookup with dissolve
    # burn ". . ."
    # scene yesman_burn_talk3 with dissolve
    # burn "you bunch of imbeciles. Fine! No matter"
    # burn "I had been in this hellhole before. If I have to begin from the start, I will do so"
    # burn "That’s right, this will be as easy as taking candies from drunk old man sitting in the front porch of his retirement house"
    # burn "After all, I still have my mansion. Yes, I know just what to do"
    # scene yesman_burn_talk2 with dissolve
    # burn "But first... there is this sweet red button I was waiting to touch"
    # scene yesman_redbutton with dissolve
    # burn "*About time... BEEN SO LONG*"
    # scene black with dissolve
    # pause
    # scene yes_men_middle_gone with dissolve
    # burn "*HAHAHAHAHAAAAAAAAAAAA*"
    # pause
    # scene yes_men_middle_gone1 with dissolve
    # pause
    # scene yesman_lastgetout with dissolve
    # burn "Now then, GET OUT OF THE OFFICE NOW"
    # scene yesman_alone with dissolve
    # burn "........"
    # scene yesman_alone_talk with dissolve
    # burn "That should let them know who not to MESS with."
    # scene yesman_alone with dissolve
    # pause
    # scene office blur with dissolve
    # show burn_base at left

    # $ burns_face = "normal"
    # $ burns_hands = "3"
   #  show mindy_base at right with dissolve
   #  show allison_base at girl_pos1 with dissolve
   #  show ashley_base at center with dissolve
   #  $ burns_face = "normal_t"
   #  burn "From today on, you will work in this mansion until the day your contract expires."
   #  burn "As per the contract, you will work 24/7 during workdays, weekends, and holidays"
   #  burn "You will also work within questionable safety precautions with no insurance and receive salary below the minimum wages. Any questions?”"
   #  $ burns_face = "normal"
   #  $ mindy_face = "normalt"
   #  mindy "What about Christmas ?"
   #  $ burns_face = "normal_t"
   #  $ mindy_face = "normal"
   #  burn "You will help with getting the Christmas tree and then decorating it"
   #  $ burns_face = "normal"
   # # show ashley angry at center with dissolve
   #  $ ashley_face = "angry"
   #  pause
   #  $ ashley_face = "angryt"
   #  ashley "this is bullshit! How can we possibly just accept all of this!?"
   #  $ burns_face = "normal_t"
   #  $ ashley_face = "angry"
   #  burn "oh, then I guess you would rather go back to the fast food restaurant where you came from?"   
   #  $ burns_face = "normal"
   #  $ ashley_face = "normal"
   # # show ashley normal at center with dissolve
   #  pause
   #  $ ashley_face = "normalt"
   #  ashley "……on second thought, it’s basically the same thing"
   #  $ ashley_face = "normal"
   #  $ burns_face = "normal_t"
   #  burn "Well then"
   #  burn "Since you are now the employees of this house, you shall call me ‘the honorable mr burns"
   #  pause 2.0

   #  burn "Wait wait, no, lord Montgomery burns"
   #  $ burns_face = "laugh"
   #  burn "Yes! That’s it! Brilliant! Alright, enough talking"
   #  $ burns_face = "hmm"
   #  # show burn rage with dissolve
   #  burn "Now get to it, chop-chop!”"
   #  $ burns_face = "angry"
   #  $ allison_face = "normalt"
   #  allison "oh, I forgot to ask"
   #  $ burns_face = "normal_t"
   #  $ allison_face = "normal"
   #  burn "yes ?"
   #  $ allison_face = "normalt"
   #  allison "When will our contract end ?"
   #  $ allison_face = "normal"
   #  burn "they don't."
   #  $ burns_face = "smirkleft"
   #  $ mindy_face = "sad"
   #  $ ashley_face = "sad"
   #  $ allison_face = "sad"
   #  hide burn with dissolve
   #  hide mindy with dissolve
   #  hide ashley with dissolve
   #  hide allison with dissolve
   #  scene black with dissolve

 #    pause
 #    "Weylon shows up"
 #    $ burns_face = "normal"
 #    show weylon_base at right with dissolve
 #    pause
 #    $ burns_face = "normal_t"
 #    burn "Now then Weylon"
 #    burn "Tell me again about my brilliant plan to plan to fulfil a successful business"
 #    $ burns_face = "smirkleft"
 #    $ weylon_face = "normal_t"
 #    weylon "Certainly sir"
 #    $ burns_face = "normal"
 #    # show weylon talk_calm with dissolve
 #    weylon "You remember one of the subject model that was specifically made to persuade a certain gender ?"
 #    $ burns_face = "normal_t"
 #    burn "What about it ?"
 #    $ burns_face = "normal"
 #    $ weylon_face = "normal_t"
 #    weylon "Well, the department for it is still active and it is producing those products"
 #    $ weylon_face = "hmm_t"
 #    weylon "You realize you can use this product on any women? It’s like an Aphrodite effect"
 #    weylon "With this perfume in your hands, You will be able proceed to claim their wealth through coercion, blackmail, assassination, or any other means necessary. Afterwards, after you gain their money, properties, and probably their souls, you will reclaim everything one by one until you once again become the de facto king of America because who needs the president when you have capitalism. God bless America"
 #    $ weylon_face = "hmm"
 #    $ burns_face = "smirkleft"
 #    pause
 #    $ burns_face = "normal_t"
 #    burn "Hmm, I like this"
 #    $ burns_face = "laugh"
 #    burn "(Very evil hahaaaaaaaaaaaaHAHAH)"
 #    $ burns_face = "hmm"
 #    burn "and this will strike up the perfume business ?"
 #    $ burns_face = "normal"
 #    $ weylon_face = "normal_t"    
 #    weylon "Yes"
 #    $ burns_face = "normal_t"
 #    $ weylon_face = "normal"
 #    burn "Perfect! Now all we have to do is. . . where is the perfume? "
 #    $ burns_face = "normal"
 #    $ weylon_face = "normal_t"
 #    weylon "I have it, but one more thing I have to inform you sir"
 #    $ burns_face = "hmm"
 #    $ weylon_face = "normal"
 #    burn "What? There's is more? What now"
 #    $ burns_face = "normal"
 #    $ weylon_face = "normal_t"
 #    weylon "There is someone who will assist you"
 #    $ weylon_face = "hmm_t"
 #    weylon "I have hired the best financial advisor that you can possibly get"
 #    weylon "She will be your best asset and the biggest key to achieving your plan, sir"
 #   # $ burns_face = ""
 #    $ weylon_face = "hmm"
 #    burn "(What? A advisor ? Female? Gorgeous ? hot? What is this, Weylon)"
 #    weylon ". . ."
 #   # $ burns_face = "normal"
 #    $ weylon_face = "normal_t"
 #    weylon "Yes she is sir, you won't be dissapointed by her perfection figure"
 # #   $ burns_face = "normal"
 #    $ weylon_face = "normal"
 #    burn "(Wait ? I didn't even say anything)"
 #    $ burns_face = "normal_t"
 #    burn "*ahem* You.. better be right about that, Weylon"
 #    burn "ANYWAYS!"
 #    burn "Where is she? I shall meet this financial advisor"
 #    $ burns_face = "normal"
 #    $ weylon_face = "normal_t"
 #    weylon "Right away sir"
 #    $ burns_face = "normal_t"
 #    $ weylon_face = "normal"
 #    burn "Good. Now then, it’s only a matter of time before I finally return to the billionaire club. But for now"
 #    $ burns_face = "normal"
 #    $ weylon_face = "normal_t"
 #    weylon "Oh, sir, in case you’re feeling stuck or if you’re unsure of what to do next, you know, in those rare instances where you kinda forgot what you should be doing, you can talk to me and I might be able to provide some hints."
 #    $ burns_face = "hmm"
 #    $ weylon_face = "normal"   
 #    burn "Are you suggesting that I have inadequate capacity to remember my plans?"
 #    $ burns_face = "normal"
 #    $ weylon_face = "normal_t"
 #    weylon "No sir"
 #    $ burns_face = "hmm"
 #    $ weylon_face = "normal" 
 #    burn "Are you implying that I'm going senile?"
 #    $ burns_face = "normal"
 #    $ weylon_face = "normal_t" 
 #    weylon "Definitly not sir"
 #    $ burns_face = "angry_t"
 #    $ weylon_face = "normal" 
 #    burn "Good, because I'm not !"
 #    $ burns_face = "angry"
 #    $ weylon_face = "normal" 
 #    weylon ". . ."
 #    burn ". . ."
 #    weylon ". . ."
 #    $ burns_face = "normal_t"
 #    $ weylon_face = "normal" 
 #    burn "Weylon, do you happen to remember what I plan to do this afternoon ?"
 #    $ burns_face = "normal"
 #    $ weylon_face = "normal_t" 
 #    weylon "You were about to meet with the financial advisor, sir"
 #    $ burns_face = "normal_t"
 #    $ weylon_face = "normal" 
 #    burn "Right ! "
 #    $ burns_face = "normal"
 #    $ weylon_face = "normal_t" 
 #    weylon "I will call her in, sir"
 #    weylon "Also, I forgot to mention. Please bare with her and don’t lose your cool. You MUST have her by your side at all cost"
 #    $ burns_face = "normal_t"
 #    $ weylon_face = "normal"  
 #    burn "Right"
 #    $ burns_face = "normal"
 #    $ weylon_face = "normal_t" 
 #    weylon "And I shall pardon myself, sir"
 #    $ weylon_face = "normal"
 #    hide weylon_base with dissolve

 #    show grace_base at right with dissolve
 #    pause
 #    $ grace_face = "talk"
 #    grace "Hello, Mr. Burn"
 #    grace "It's a pleasure to finally meet you in person"
 #    $ grace_face = "normal"
 #    $ burns_face = "hmm"
 #    burn "Ah, yes."
 #    $ grace_face = "talk"
 #    $ burns_face = "normal"   
 #    grace "Yes"
 #    $ grace_face = "talk_close"
 #    grace "After all that never ending training & periodic intern test at your company, I finally made it at last"
 #    $ grace_face = "normal"
 #    burn "(Training ? A test? At my company? Good. But I don't know what she is talking about)"
 #    burn "(But... what is that on her hand? A vintage cigarette?)"
 #    $ grace_face = "normal"
 #    $ burns_face = "hmm"  
 #    burn "*Ahem*"
 #    $ burns_face = "normal_t"  
 #    burn "Hello. . Miss .. ?"
 #    $ grace_face = "talk"
 #    $ burns_face = "normal"
 #    grace "Grace, it is Grace"
 #    $ grace_face = "normal"
 #    $ burns_face = "normal_t"
 #    burn "Ah yes, Miss Grace"
 #    burn "You do possess a wonderful figu. ."
 #    burn "I mean, a wonder dress *Ahem*"
 #    $ grace_face = "talk_close"
 #    $ burns_face = "normal"
 #    grace "Thank you"
 #    $ grace_face = "talk"
 #    $ burns_face = "normal"
 #    grace "Back to business, if you did not know. I'm here as your financial advisor"
 #    grace "I will be responsible in managing your cash, and you will have to inform whenever you need cash"
 #    $ grace_face = "normal"
 #    $ burns_face = "angry_t"
 #    burn "WHAT?! This is preposterous !"
 #    burn "You think I'm just going to LET YOU. . . ."
 #    $ burns_face = "hmm"
 #    burn "Wait"
 #    $ burns_face = "angry"
 #    burn "(God dammit, Weylon. I... this mere human as my so called assistant. FINE)"
 #    $ burns_face = "hmm"
 #    burn "*ahem*"
 #    $ burns_face = "normal"
 #    $ grace_face = "talk"
 #    grace "Don’t worry sir, you can trust me and I know you very well deeply. Those test were quite useful."
 #    $ grace_face = "normal"
 #    grace "But, I will not hold back on your anger either. So refrain from losing your cool sir."
 #    $ grace_face = "talk_angry"
 #    grace "And, please do call me Grace from now on. Not Miss Grace"
 #    $ grace_face = "angry close"
 #    burn "(I’m going to fucking destroy this woman whole career once I get my)"
 #    $ grace_face = "talk_angry"
 #    grace "I'm not liking your face, Mr Burn"
 #    $ grace_face = "normal"
 #    $ burns_face = "normal_t"
 #    burn "Of course Grace, I will call you Grace"
 #    $ grace_face = "talk"
 #    $ burns_face = "normal"
 #    grace "Good"
 #    grace "Now, Weylon has left me this perfurm to pass it to you"
 #    grace "Here is your black perfume"
 #    $ grace_face = "talk_close"
 #    grace "Don't know what your purpose is behind the perfume, but have fun with it"
 #    $ grace_face = "normal"
 #   # $ burns_face = "normal"
 #    burn ". . ."
 #    burn "(I swear, I will have you . . )"
 #    burn "(Wait, I can test this product on someone)"
 #    burn "(Where can I.. . AHH yes, the park. I shall visit the park)"
 #  #  $ grace_face = "talk"
 #    $ burns_face = "hmm"
 #    burn "Miss. Grace, I’m in a hurry now. Is there anything you else you need to say?"
 #    $ grace_face = "angry_angry"
 #    $ burns_face = "normal"
 #    grace "It's GRACE, Mr Burn !"
 #    $ grace_face = "angry close"
 #    $ burns_face = "normal_t"
 #    burn "haha yes, Grace. Sorry about that (NOT SORRY)"
 #    burn "Now, is there anything else?"
 #    $ grace_face = "talk"
 #    $ burns_face = "normal_t"
 #    grace "No, there isn't but"
 #    grace "I will be here by the office, if you need anything from me"
 #    $ grace_face = "normal"
 #    $ burns_face = "normal_t"
 #    burn "Okay, I will see you later (WAIT AND SEE, MISS GRACE. But damn, I wonder what is under her vibrant bod)"
 #    hide burn with dissolve
 #    hide grace_base with dissolve
 #    $ burns_face = "normal"
 #    pause
    centered "{=scene_text}Off to pester now.{/=scene_text}" with dissolve
    play music "audio/mansion_draft1.mp3"

    jump office

