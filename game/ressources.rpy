
# bg images
image bgmain = "images/bg_main.jpg"
image bg = "images/bgb.jpg"

# others
image blossoms1 = SnowBlossom("sakura/sakura.png",count=5,start=1)
image blossoms2 = SnowBlossom("sakura/sakura2.png",count=5,start=2)
image blossoms3 = SnowBlossom("sakura/sakura3.png",count=7,start=3)

# characters
define outlineWidth = 2

define povSilent  = Character(None,show_two_window=True, ctc="ctc", ctc_position="fixed",window_background=Frame("layout/narratordialoguebox.png",35,35))
define comment = Character(None, window_background=Frame("layout/narratordialoguebox.png",35,35))
define povSpeaks = DynamicCharacter("povName", who_outlines=[(outlineWidth, "#9d6e30")], show_two_window=True,ctc="ctc", ctc_position="fixed")

define bastion = Character('BASTION', who_outlines=[(outlineWidth, "#7a9767")], show_two_window=True,ctc="ctc", ctc_position="fixed")
define dva = Character('D.VA', who_outlines=[(outlineWidth, "#feabe6")], show_two_window=True,ctc="ctc", ctc_position="fixed")
define genji = Character('GENJI', who_outlines=[(outlineWidth, "#b6ef13")], show_two_window=True,ctc="ctc", ctc_position="fixed")
define hanzo = Character('HANZO', who_outlines=[(outlineWidth, "#345286")], show_two_window=True,ctc="ctc", ctc_position="fixed")
define junkrat = Character('JUNKRAT', who_outlines=[(outlineWidth, "#ffdc44")], show_two_window=True,ctc="ctc", ctc_position="fixed")
define lucio = Character('LUCIO', who_outlines=[(outlineWidth, "#80cc2e")], show_two_window=True,ctc="ctc", ctc_position="fixed")
define mcCree = Character('MCCREE', who_outlines=[(outlineWidth, "#c23f46")], show_two_window=True,ctc="ctc", ctc_position="fixed")
define mei = Character('MEI', who_outlines=[(outlineWidth, "#87d7f6")], show_two_window=True,ctc="ctc", ctc_position="fixed")
define mercy = Character('MERCY', who_outlines=[(outlineWidth, "#ffffa3")], show_two_window=True,ctc="ctc", ctc_position="fixed")
define pharah = Character('PHARAH', who_outlines=[(outlineWidth, "#3461a4")], show_two_window=True,ctc="ctc", ctc_position="fixed")
define reaper = Character('REAPER', who_outlines=[(outlineWidth, "#33333")], show_two_window=True,ctc="ctc", ctc_position="fixed")
define reinhardt = Character('REINHARDT', who_outlines=[(outlineWidth, "#b9b5ad")], show_two_window=True,ctc="ctc", ctc_position="fixed")
define roadhog = Character('ROADHOG', who_outlines=[(outlineWidth, "#c7712a")], show_two_window=True,ctc="ctc", ctc_position="fixed")
define soldier76 = Character('SOLDIER: 76', who_outlines=[(outlineWidth, "#525d9b")], show_two_window=True,ctc="ctc", ctc_position="fixed")
define symmetra = Character('SYMMETRA', who_outlines=[(outlineWidth, "#3cffff")], show_two_window=True,ctc="ctc", ctc_position="fixed")
define torbjorn = Character('TORBJÖRN', who_outlines=[(outlineWidth, "#b04a33")], show_two_window=True,ctc="ctc", ctc_position="fixed")
define tracer = Character('TRACER', who_outlines=[(outlineWidth, "#ffcf35")], show_two_window=True,ctc="ctc", ctc_position="fixed")
define widowmaker = Character('WIDOWMAKER', who_outlines=[(outlineWidth, "#af5e92")], show_two_window=True,ctc="ctc", ctc_position="fixed")
define winston = Character('WINSTON', who_outlines=[(outlineWidth, "#595959")], show_two_window=True,ctc="ctc", ctc_position="fixed")
define zarya = Character('ZARYA', who_outlines=[(outlineWidth, "#ff73c1")], show_two_window=True,ctc="ctc", ctc_position="fixed")
define zenyatta = Character('ZENYATTA', who_outlines=[(outlineWidth, "#e1c931")], show_two_window=True,ctc="ctc", ctc_position="fixed")

# affinity flags
define affinityBastion = 0
define affinityDVa = 0
define affinityGenji = 0
define affinityHanzo = 0
define affinityJunkrat = 0
define affinityLucio = 0
define affinityMcCree = 0
define affinityMei = 0
define affinityMercy = 0
define affinityPharah = 0
define affinityReaper = 0
define affinityReinhardt = 0
define affinityRoadhog = 0
define affinitySoldier76 = 0
define affinitySymmetra = 0
define affinityTorbjorn = 0
define affinityTracer = 0
define affinitySymmetra = 0
define affinityWidowmaker = 0
define affinityWinston = 0
define affinityZarya = 0
define affinityZenyatta = 0

# ui layout
define slowDissolve = Dissolve(1.0)
image ctc:
       anim.Blink("layout/logob.png")
       xpos 0.925 ypos 0.93
       xanchor 1.0 yanchor 1.0