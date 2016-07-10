# You can place the script of your game in this file.

# The game starts here.
label start:
    
    scene black

    if not persistent.nameWasSaved:
        comment "{cps=30}{i}WELCOME TO THIS SHORT LOVERWATCH DEMO!{/i}{/cps}"
        comment "{cps=30}{i}FIRST OF ALL, I'LL NEED YOU TO TELL ME YOUR NAME{/i}{/cps}"
        $ povName = renpy.input(_("{i}{size=15}PLEASE, ENTER YOUR NAME :{/size}{/i}"),length=15).upper() or _("ROBIN")
        $ gender = renpy.input(_("{i}{size=15}WHAT ARE YOUR PRONOUNS?(EX. HE, SHE, THEY) :{/size}{/i}"), length=15).upper() or _("THEY")
        $ persistent.nameWasSaved = True
        $ persistent.savedName = povName
        $ persistent.genderWasSaved = True
        $ persistent.savedGender = gender
        comment "{cps=30}{i}OK [povName], TIME TO WAKE UP! {/i}{/cps}"
    else :
        $ povName = persistent.savedName
        $ gender = persistent.savedGender
        comment "{cps=30}{i}OH! HELLO BACK [povName]! {/i}{/cps}"
        comment "{cps=30}{i}You said your pronoun was [gender], right? Sorry if I get it wrong!{/i}{/cps}"
        comment "{cps=30}{i}I HOPE YOU'RE ENJOYING YOUR DEMO. {/i}{/cps}"
        
    pause 0.5
    
    povSilent "{cps=30}{b}...{/b}{/cps}"
    povSilent "{cps=30}{b}IS IT MORNING ALREADY?{/b}{/cps}"
    povSilent "{cps=30}{b}OUCH, MY HEAD HURTS...{/b}{/cps}"
    povSilent "{cps=30}{b}WHAT HAPPENED LAST NIGHT?{/b}{/cps}"
    povSilent "{cps=30}{b}WHAT HAPPENED LAST NIGHT? {fast} OH...{/b}{/cps}"
    povSilent "{cps=30}{b}...{/b}{/cps}"
    povSilent "{cps=30}{b}I CAN'T BELIEVE I TOLD HIM HOW I FEEL.{/b}{/cps}"
    pause 0.5
    povSilent "{cps=30}{b}HOW EMBARRASSING.{/b}{/cps}"

    scene bg
    with slowDissolve
    
    show blossoms1
    show blossoms2
    show blossoms3
    
    povSilent "{cps=30}{b}THE SUN IS ALREADY SO HIGH.{/b}{/cps}"
    povSilent "{cps=30}{b}AH!{/b}{/cps}"
    
    show soldVisorOn at Position(xpos = 0.5, xanchor=0.5, ypos=0.5, yanchor=0.5)
    with slowDissolve
    
    povSilent "{cps=30}{b}THERE HE IS!{/b}{/cps}"
    
    menu:

        povSilent "{b}THERE HE IS!{/b}"
        "{b}TALK TO HIM{/b}":
            jump talkToHim

        "{b}LEAVE HIM BE{/b}":
            povSilent "{cps=30}{b}BETTER GIVE HIM SOME SPACE FOR THE MOMENT.{/b}{/cps}"
            jump end


label talkToHim :
    
    povSpeaks "{cps=30}{b}GOOD MORNING, JACK.{/b}{/cps}"
    soldier76 "{cps=30}{b}MHH... ? {/b}{/cps}"
    soldier76 "{cps=30}{b}MHH... ? {fast} OH, IT'S YOU [povName]. GOOD MORNING.{/b}{/cps}"
    soldier76 "{cps=30}{b}DID YOU SLEEP WELL ?{/b}{/cps}"
    povSpeaks "{cps=30}{b}WELL...{/b}{/cps}"
    povSpeaks "{cps=30}{b}WELL... {fast} NOT REALLY TO BE HONEST...{/b}{/cps}"
    soldier76 "{cps=30}{b}I SEE...{/b}{/cps}"
    
    soldier76 "{cps=30}{b}LISTEN...{/b}{/cps}"
    
    hide soldVisorOn
    show soldVisorOff at Position(xpos = 0.5, xanchor=0.5, ypos=0.5, yanchor=0.5)
    soldier76 "{cps=30}{b}ABOUT YESTERDAY,{/b}{/cps}"
    soldier76 "{cps=30}{b}ABOUT YESTERDAY, {fast} I DON'T KNOW WHAT YOU WERE HOPING WHEN YOU CONFESSED TO ME.{/b}{/cps}"
    soldier76 "{cps=30}{b}I... {/b}{/cps}"
    soldier76 "{cps=30}{b}I... {fast} I WAS FLATTERED BUT STILL...{/b}{/cps}"
    soldier76 "{cps=30}{b}YOU'RE TOO YOUNG FOR THIS OLD MAN ...{/b}{/cps}"
    hide soldVisorOff

    show soldVisorOn at Position(xpos = 0.5, xanchor=0.5, ypos=0.5, yanchor=0.5)
    #with slowDissolve
    soldier76 "{cps=30}{b}YOU'D BE BETTER OFF WITH SOMEONE ELSE ...{/b}{/cps}"
    
    menu:

        soldier76 "{b}YOU'D BE BETTER OFF WITH SOMEONE ELSE ...{/b}"
        "{b}I DON\'T WANT ANYONE ELSE!{/b}":
            povSpeaks "{cps=30}{b}I DON'T WANT ANYONE ELSE, JACK!{/b}{/cps}"
            $affinitySoldier76 +=2
            jump wantYou

        "{b}DO YOU REALLY THINK THAT?{/b}":
            povSpeaks "{cps=30}{b}DO... DO YOU REALLY THINK THAT?{/b}{/cps}"
            $affinitySoldier76 +=1
            jump whatYouThink
            
label wantYou:
    
label whatYouThink:
    
    if affinitySoldier76 > 1 :
        soldier76 "{cps=30}{b}PLEASE, TRY TO UNDERSTAND...{/b}{/cps}"
    else :
        soldier76 "{b}...{/b}"
        
    hide soldVisorOn
    with slowDissolve
    povSpeaks "{cps=30}{b}WAIT !{/b}{/cps}"
    povSilent "{cps=30}{b}DID HE JUST...{/b}{/cps}"
    povSilent "{cps=30}{b}DID HE JUST...{fast} RUN AWAY?{/b}{/cps}"
 
label end:
    
    hide blossoms1
    hide blossoms2
    hide blossoms3
    scene black
    with dissolve
    
    povSilent "..."
    povSilent "{cps=30}{b}BE PREPARED \"OLD MAN\",{/b}{/cps}"
    povSilent "{cps=30}{b}BE PREPARED \"OLD MAN\",{fast} I'M NOT GIVING UP SO EASILY !{/b}{/cps}"
    
    comment "{cps=30}{i}TO BE CONTINUED ...{/i}{/cps}"
    
    return
