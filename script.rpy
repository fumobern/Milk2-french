define config.language = "french"

$ renpy.music.set_volume(0.6, channel="music")
    
$ renpy.music.set_volume(0.6, channel="sound")

$ renpy.music.set_volume(0.6, channel="sounds_m")

init 1 python:
    def change_cursor(type="default"):
        persistent.mouse = type
        if type == "milk":
            setattr(config, "mouse", {"default": [("images/curs.png", 0, 0)]})
        elif type == "no":
            setattr(config, "mouse", {"default": [("images/blank.png", 0, 0)]})
        elif type == "telef":
            setattr(config, "mouse", {"default": [("images/str/telef/curs.png", 0, 0)]})
        elif type == "magaz":
            setattr(config, "mouse", {"default": [("images/str/magaz/curs.png", 0, 0)]})
        elif type == "lest":
            setattr(config, "mouse", {"default": [("images/str/lest/curs.png", 0, 0)]})
        elif type == "kompol":
            setattr(config, "mouse", {"default": [("images/str/kompol/curs.png", 0, 0)]})
        elif type == "zerk":
            setattr(config, "mouse", {"default": [("images/str/zerk/curs.png", 0, 0)]})
    if not hasattr(persistent, "mouse"):
        change_cursor()
    else:
        change_cursor(persistent.mouse)

init -2 python:
    renpy.music.register_channel("sounds_m", "music", loop=False)

init -1:
    screen say(who, what, slow_effect = slow_typewriter, slow_effect_delay = 0, always_effect = None):
        style_prefix "say"

        window:
            id "window"
            if who is not None:
                window:
                    id "namebox"
                    style "namebox"
                    text who id "who"
            fancytext what id "what" slow_effect slow_effect slow_effect_delay slow_effect_delay always_effect always_effect


init -1:
    transform mmz:
        subpixel True
        truecenter
        zoom 1.0
        ease 100.0 zoom 2.5

    transform circle:
        ease 2 yoffset 2
        ease 2 xoffset 2
        ease 2 yoffset -2
        ease 2 xoffset -2
        repeat
    
    transform circlez2:
        ease 0.1 xoffset 2
        truecenter zoom 1.4
        ease 0.05 xoffset -7
        truecenter zoom 1.1
        xzoom 2
        ease 0.05 yoffset 8
        truecenter zoom 1.2
        ease 0.2 xoffset -8
        truecenter zoom 1
        repeat
    
    transform circlez:
        ease 0.05 xoffset 2
        truecenter zoom 1.4
        ease 0.05 xoffset -2
        xzoom 3
        ease 0.05 xoffset 8
        ease 0.05 xoffset -2
        xzoom 1
        truecenter zoom 0.4
        ease 0.5 xoffset 11
        yzoom 4
        xzoom 0.3
        zoom 1.1
        ease 0.05 xoffset -50
        ease 0.1 xoffset 6
        zoom 3
        ease 0.05 xoffset -22
        zoom 0.8
        repeat
        
    transform circle2:
        ease 2 xoffset -2
        ease 2 yoffset -2
        ease 2 xoffset 0
        ease 2 yoffset 0
        repeat
        
    transform prikol1:
        ease 0.1 xoffset 81
        truecenter zoom 1.4
        ease 0.3 xoffset -7
        truecenter zoom 15
        ease 0.05 yoffset 58
        truecenter zoom 9.5
        ease 0.05 yoffset -62
        truecenter zoom 1
        repeat
        
    transform prikol2:
        ease 0.05 yoffset 18
        truecenter zoom 4
        ease 0.05 xoffset -52
        truecenter zoom 1
        ease 0.05 yoffset 81
        truecenter zoom 0.5
        repeat
        
    transform prikol3:
        ease 0.1 xoffset 18
        truecenter zoom 3
        ease 0.3 xoffset -7
        truecenter zoom 9
        ease 0.05 xoffset 38
        truecenter zoom 1.9
        ease 0.05 xoffset -2
        truecenter zoom 0.4
        ease 0.5 xoffset 111
        truecenter zoom 3.1
        ease 0.05 xoffset -22
        truecenter zoom 1
        repeat
        
    transform prikol4:
        ease 0.1 xoffset 28
        truecenter zoom 1.4
        ease 0.2 xoffset -38
        truecenter zoom 5
        ease 0.05 yoffset -64
        truecenter zoom 2
        repeat
        
        
        
        

init python:
    
    
  
    # This is set to the name of the character that is speaking, or
    # None if no character is currently speaking.
    speaking = None
  
    # This returns speaking if the character is speaking, and done if the
    # character is not.
    def while_speaking(name, speak_d, done_d, st, at):
        if speaking == name:
            return speak_d, .1
        else:
            return done_d, None
  
    curried_while_speaking = renpy.curry(while_speaking)

    def WhileSpeaking(name, speaking_d, done_d=Null()):
        return DynamicDisplayable(curried_while_speaking(name, speaking_d, done_d))
  

    def speaker_callback(name, event, **kwargs):
        global speaking
        if event == "show":
            speaking = name
            renpy.music.play("audio/narr.ogg", channel="sounds_m", loop=True)
        elif event == "slow_done" or event == "end":
            speaking = None
            renpy.music.stop(channel="sounds_m", fadeout=0.3)
        elif event == "end":
            speaking = None
  

    speaker = renpy.curry(speaker_callback)

    def narr(event, **kwargs):
        if event == "show":
            renpy.music.play("audio/narr.ogg", channel="sounds_m", loop=True)
        elif event == "slow_done" or event == "end":
            speaking = None
            renpy.music.stop(channel="sounds_m", fadeout=0.3)
            
    def narrz(event, **kwargs):
        if event == "show":
            renpy.music.play("audio/narrz.ogg", channel="sounds_m", loop=True)
        elif event == "slow_done" or event == "end":
            speaking = None
            renpy.music.stop(channel="sounds_m", fadeout=0.3)
    


init:
    
    define config.image_cache_size_mb = 400

    define _confirm_quit = False

    define nice_sounds = ["audio/nice sounds/1.ogg", "audio/nice sounds/2.ogg", "audio/nice sounds/3.ogg", "audio/nice sounds/4.ogg", "audio/nice sounds/5.ogg", "audio/nice sounds/6.ogg", "audio/nice sounds/7.ogg"]
    
    image milk_hover:
        "poc/milk_hover1.png"
        .1 
        "poc/milk_hover2.png"
        .1 
        "poc/milk_hover3.png"
        .1
        repeat
        
        
    
    define config.layers = [ "master", "transient", "say", "choice", "screens", "overlay" ]
    define config.say_layer = "say"
    
    image overlay = "overlay.png"
    image overlay_invert = "overlay_invert.png"
    
    image bg = "bg.png"
    
    image n = "nvl.png"
    







    define n = Character(None, window_background=None, what_xpos=450, what_ypos=50)
    define m = Character(window_background=None, what_xpos=450, what_ypos=50, show_always_effect = always_shake(x = 2, y = 2))
    define ngg = Character(window_background=None, callback=narr, what_xpos=450, what_ypos=50)
    define ngg2 = Character(window_background=None, what_style="centered_text", window_style="centered_window", callback=narr)
    define c = Character(None, what_style="centered_text", window_style="centered_window", show_always_effect = always_shake(x = 2, y = 2))
    define c2 = Character(None, what_style="centered_text", window_style="centered_window", show_always_effect = always_shake(x = 6, y = 6))
    define c3 = Character(None, what_style="centered_text", window_style="centered_window", show_always_effect = always_shake(x = 10, y = 10))
    
    
    define gg = Character(callback=speaker("gg"))
    define ggz = Character(callback=narrz)
    
    define ddp = ImageDissolve(im.Tile("transmask2.webp"), 3, 1)
    define ddp2 = ImageDissolve(im.Tile("transmask2.webp"), 2, 1)

label splashscreen:
    # call screen lang_choice
    
    # $ renpy.pause(1, hard=True)
    
    show dsclmr
    
    $ renpy.pause(5, hard=True)
    
    hide dsclmr
    
    $ renpy.pause(2, hard=True)
    
    show controls
    
    $ renpy.pause(5, hard=True)
    
    hide controls
    
    $ renpy.pause(2, hard=True)
    
    $ renpy.movie_cutscene("intro.webm")
    
    pause 1
    
    $ change_cursor("milk")
    
    return


label start:
    
window hide

$ _game_menu_screen = None

define config.rollback_enabled = False    
$ _skipping = False

show n

$ change_cursor("no")

stop music fadeout 4

$ renpy.pause(5, hard=True)


window hide


$ renpy.pause(1, hard=True)

play sound "audio/eyes.ogg"

show mini_cg_1_1

$ renpy.pause(4, hard=True)


play music "audio/milk/milk13.mp3" fadein 3

show mini_cg_1_2 with ddp

hide mini_cg_1_1
$ renpy.pause(1, hard=True)



n"Я иду в свою комнату, стараясь не смотреть по сторонам."
n"Вокруг меня то и дело пляшут озорные тени; стремительными рывками перемещаются они по стенам, по потолку..." 
n"Одна из таких теней игриво проносится мимо, слегка коснувшись моего лица - я улыбаюсь и продолжаю идти, не обращая особого внимания." 
n"Порой так легко потерять самообладание и закружиться в веселом танце - счет времени теряется вовсе." 
n"А мне, между прочим, совершенно некогда - мама сказала идти спать."

hide mini_cg_1_2 with ddp

$ renpy.pause(1, hard=True)

show mini_cg_door with ddp
$ renpy.pause(1, hard=True)

n"Я иду в свою комнату мимо кухни. Даже сквозь запертую дверь оттуда веет могильным холодом. Первая же мысль - у двери, прислонившись, сидит мертвец и дует в замочную скважину, издевательски посмеиваясь." 
n"Ха-ха, ну какая же ерунда! Я точно знаю, что мертвецов на нашей кухне нет. Я точно знаю, что никаких мертвецов на нашей кухне нет и никогда не было. Я абсолютно точно уверена, что..."

hide mini_cg_door with ddp
$ renpy.pause(1, hard=True)
show mini_cg_run with ddp
$ renpy.pause(1, hard=True)

n"Сорвавшись с места, я со всех ног бегу к запертой двери. Тени тотчас принимаются плясать впятеро хаотичней; пытаются ли они меня отговорить или же успокоить, я не знаю. Сейчас это совсем не имеет значения! Вы что, не понимаете?!"
n"Я размахиваю руками на бегу - так я пытаюсь отогнать назойливых преследователей, - и внезапно понимаю, что никак не успеваю затормозить. Выбора нет - придется выбивать дверь." 
n"Если внутри кто-то есть, я точно напугаю его до полусмерти. Хотя, постойте... если напугать мертвеца до полусмерти, не значит ли это, что он станет полуживым? Нет-нет, так не пойдет! Что же мне делать?.."
n"Мысль не успела полностью подуматься, как я впечаталась плечом в дверь, отчего та распахнулась настежь."

hide mini_cg_run with ddp
$ renpy.pause(1, hard=True)

stop music
play music "audio/milk/milk10.mp3"

show eyes_fear
pause 4

n"Мертвеца внутри, как и ожидалось, нет. Зато есть купленный мной сегодня пакет молока - он стоит в самом центре стола и смотрит на меня немигающими глазами. Я смотрю на него в ответ - ничего не происходит." 
n"Впрочем, чего я вообще жду? Благодарности? Но разве я сделала что-то, чтобы заслужить ее? Не думаю, что пакету молока очень уж важно, где находиться - на полке магазина или посреди стола на маминой кухне." 
n"С другой стороны, никто не станет пить молоко прямо в магазине - выходит, я забрала пакет из самого безопасного места в пугающую для него неизвестность. Прости, молочко!"

stop music fadeout 5
hide eyes_fear with ddp
$ renpy.pause(1, hard=True)

n"Стыдливо отвернувшись, я спешу выйти из кухни. Да уж, от меня одни беды..."
n"Я иду в свою комнату по узкому коридору."

$ renpy.pause(2, hard=True)

play sound "audio/milk/heymom_fx.mp3"  

show mini_cg_mom_1 

$ renpy.pause(3, hard=True)

play music "audio/milk/milk16.mp3"

n"У дверей мне встречается знакомое бесформенное существо; вцепившись в меня, оно принимается обнюхивать каждый сантиметр моего тела, словно голодная псина." 
n"Я не сопротивляюсь - знаю ведь, что это бессмысленно. Лишь молча терплю, пока оно крепко держит, не давая пошевелиться."
hide mini_cg_mom_1 with ddp
$ renpy.pause(1, hard=True)
  
show mini_cg_momp_1 with ddp


n"Обнюхав меня с ног до головы, существо протягивает уродливые лапы, обнажая один-единственный коготь - тонкий и острый, словно лезвие." 
ngg"- Снова?.."
n"Я вопросительно смотрю прямо в бездонные глазницы чудовища."
play sound "audio/mum xd/1.ogg"
m"- НЕ ШЕВЕЛИСЬ."
n"Существо сильно сжимает мою руку, пока не проступают вены. Я же продолжаю смотреть в черные провалы глаз, игнорируя всякую боль." 
ngg"- Я ведь столько раз обещала..."
play sound "audio/mum xd/1.ogg"
m"- СТОЙ СМИРНО."

show mini_cg_momp_2

n"В тот же миг коготь вонзается мне в руку. Я почти ничего не чувствую, разве что едва ощутимое шевеление под кожей и звон натянутых сухожилий. Но затем... затем коготь впрыскивает свой яд."

show mini_cg_momp_22
hide mini_cg_momp_2
hide mini_cg_momp_1

ngg"- Больно..."
n"Перед глазами проступает белесая пелена, пальцы судорожно сжимаются и разжимаются - я начинаю терять контроль над своим телом и медленно сползаю на пол. Совсем как в прошлый раз. Однако же..."
ngg"- Почему... почему так жарко?"
n"Чувствую, как медленно закипает кровь. Сильнейшая дрожь пробегает по телу, парализуя каждую клеточку, пока мои вены и артерии раскаляются, едва выдерживая натиск." 
n"Я пытаюсь закричать, но вместо слов изрыгаю густую молочную пену; заметив это, существо в ярости бросается на меня и хватает за горло, не выпуская отравленного когтя из моей руки."
ngg"- Убей меня. Убей меня!"
n"Истерический вопль разносится по коридору; существо в порыве безумия принимается царапать мне шею."
n"Во все стороны летят яркие брызги, звонко ударяясь о стены - я стараюсь отпечатать в памяти, куда упала каждая капелька, чтобы потом собрать их все до единой." 
n"Не забыть, главное - не забыть..."
n"Новая волна боли захлестнула меня. Все вмиг погасло."

hide mini_cg_momp_22 with ddp

$ renpy.pause(1, hard=True)

play sound "audio/mum xd/1.ogg"
c"- ПОВТОРЯЙ: 'Я НИКОГДА НЕ БУДУ ПИТЬ МОЛОКО.'"
ngg2"- Я..."
play sound "audio/mum xd/1_ext1.ogg"
c2"{size=30}{cps=10}- ПОВТОРЯЙ.{/cps}{/size}"
ngg2"- Я никогда... не буду пить... молоко..."
play sound "audio/mum xd/1_ext2.ogg"
c3"{size=40}{cps=5}- ПОВТОРЯЙ.{/cps}{/size}"
ngg2"- Я никогда не буду пить молоко!"
ngg2"{size=70}- Я НИКОГДА НЕ БУДУ ПИТЬ МОЛОКО!{/size}"

stop music fadeout 5

play sound "audio/trans/1.ogg"

$ change_cursor("no")
hide 2 with ddp

$ renpy.pause(7, hard=True)

$ renpy.free_memory()

play music "audio/milk/milk9.mp3" fadein 6

$ renpy.pause(1, hard=True)

show sky1 at circle:
    truecenter zoom 1.01
show cg_mirror_gg1 at circle2:
    truecenter zoom 1.01
show cg_mirror_brush
with ddp
$ renpy.pause(1, hard=True)
show overlay with ddp2

$ change_cursor("milk")

$ _game_menu_screen = 'save'

"Я наконец-то добралась до своей комнаты. Мне так надоела вся эта суета - хорошо, что в любимой комнате я чувствую себя уютно и тепло! Даже странные звуки из-за двери ни капли меня не тревожат."
"Мама сказала мне идти спать, так что я должна совершить все необходимые приготовления. Я умылась и теперь стою у зеркала с зубной щеткой во рту."
play sound renpy.random.choice(nice_sounds)
"Смотрю на свое отражение, не изъявляющее ни малейшего желания ложиться в кровать. Да уж, понимаю тебя..."
"А ведь когда-то моим любимым временем дня были последние минуты перед сном. Момент ожидания того, как реальность неизбежно столкнется с миром сновидений, когда-то был моим любимым моментом." 
"Я просыпалась только ради этого, проживала целый день ради этого. Моей заветной мечтой было спать целый день - как было бы здорово! Однако сны медленно, но верно ускользали." 
"Словно кто-то вытаскивал их прямо из головы, один за одним, один за одним... пока не осталось совсем ничего. И вот я снова должна ложиться спать, хоть и не чувствую в этом нужды."

$ _game_menu_screen = None

$ change_cursor("no")

hide overlay
hide cg_mirror_brush
hide sky1
hide cg_mirror_gg1
with ddp

$ renpy.free_memory()

show sky2 at circle:
    truecenter zoom 1.01
show cg_pills
with ddp
$ renpy.pause(1, hard=True)
show overlay with ddp2

$ change_cursor("milk")

$ _game_menu_screen = 'save'

"Закончив водные процедуры, я привычно протягиваю руку к своим лекарствам. Забавно, но я понятия не имею, как они действуют по отдельности - я всегда проглатывала их сразу, не задумываясь." 
"Сейчас же мне захотелось рассмотреть их поближе, повертеть в пальцах, попробовать на зуб..." 
"Что угодно, лишь бы подольше потянуть время."
"На меня смотрит гладкая и вытянутая капсула красного цвета. Снаружи она покрыта мутной полупрозрачной пленкой, но кое-как рассмотреть ее содержимое все же возможно." 
"Итак, что же у тебя внутри?"
"Слегка надавив на капсулу с обеих сторон, я с удивлением обнаруживаю, что она очень мягкая и податливая. Сдавливаю еще - капсула лопается; наружу вытекает липкая ярко-красная жидкость... Мерзость, мерзость!"
"Таблетка отправляется прямиком в мусорный бак; я же принимаюсь тщательно отмывать руки. Нет уж, пить ЭТО я наотрез отказываюсь! "
"Следующая на очереди - плоская таблетка такого же кроваво-красного цвета. На ней, к тому же, отпечатаны какие-то буквы... Ага, я поняла!" 
"Это тот самый препарат, от которого жутко клонит в сон. Но это не тот сон, совсем не тот. Ненастоящий, фальшивый! Нет, нет, нет! Даже видеть не желаю!" 
"Вслед за первой эта таблетка отправляется в мусор." 
"Следующие полчаса проходят примерно так: я рассматриваю таблетки со всех сторон и для каждой нахожу причину ни в коем случае ее не пить." 
"Вместо этого я придумываю свои собственные лекарства и с удовольствием принимаю их одно за одним, всецело отдаваясь их целительным эффектам." 
"...вот и горло больше не болит."
"...вот и рука больше не болит."
"...вот и голова больше не болит."
"...вот и сердце больше не болит."
"...вот и живот больше не болит."
"...вот и глаза больше не болят."
"И как я раньше не додумалась? Это же так просто! Надо срочно кому-нибудь похвастаться!"
"...но только не маме, она будет ругаться." 
"К тому же она уверена, что я уже сплю - не буду лишний раз тревожить ее. Придумаю что-нибудь сама!"
"И вообще, мне просто хочется поболтать... Ах, кто же будет моим собеседником?"

stop music fadeout 4

$ _game_menu_screen = None

$ change_cursor("no")

hide overlay
hide cg_pills
hide sky2
with ddp

$ renpy.free_memory()

$ renpy.pause(1, hard=True)

$ change_cursor("milk")

$ _game_menu_screen = 'save'

play sound "audio/fx3.mp3"

call screen ok

label ok:

$ _game_menu_screen = None
        
$ change_cursor("no")
        
$ renpy.pause(2, hard=True)
        
play music "audio/milk/milk5.mp3" fadein 6
        
show sky3 at circle:
    truecenter zoom 1.01
show cg_mirror_gg2 at circle2:
    truecenter zoom 1.01
show bg
with ddp
show overlay onlayer say with ddp2
show gg_smile_1 with ddp2
        
$ change_cursor("milk")
        
$ _game_menu_screen = 'save'
        
gg"- Привет! Давно не виделись!"

menu:
    "(И часа не прошло, глупая...)":
        hide gg_smile_1
        show gg_sad_1
        gg"- Ну вот, снова обижаешь..."
        jump choice1
    "(Ты ведь в курсе, что нам запрещено видеться чаще одного раза в сутки?)":
        show gg_mad_2_oa
        hide gg_smile_1
        gg"- Ну что за угрюмая интонация?.."

hide gg_mad_2_oa
show gg_zout_2
"Разумеется, я читала инструкцию. Судя по картинкам, побочные эффекты при передозировке стандартные - головная боль, тошнота, усталость..." 
"В общем, ничего такого, с чем я бы не справилась своими силами. Ведь теперь-то я знаю, как это сделать!" 

menu:
    "(Ты не ответила...)":
        hide gg_zout_2
        show gg_sad_2_ad

label choice1:
hide gg_sad_1
show gg_sad_2_ad
gg"- Неужели ты даже капельку не рад? Даже совсем чуть-чуть?"

menu:
    "(Нет.)":
        hide gg_sad_2_ad
        show gg_mad_3
        gg"- Ну, значит, и я не рада!"
    "(Я порядком вымотался за сегодня. Впрочем, как и ты...)":
        hide gg_sad_2_ad
        show gg_conf_3
        gg "- Неправда!"
menu:
    "(Тебе нужно ложиться спать.)":
        hide gg_mad_3
        hide gg_conf_3
        show gg_mad_1
        gg"- Нет уж! Ты сегодня достаточно мной командовал, теперь моя очередь! Значит так..."

menu:
    "(Я просто буду молчать, пока не закончится действие лекарства. Как тебе такое?)":
        show gg_sad_1_ad
        hide gg_mad_1
        gg"- Эй, но... но так ведь нельзя! Ты должен делать все для того, чтоб я чувствовала себя лучше!"

menu:
    "(Именно это я и делаю.)":
        hide gg_sad_1_ad
        show gg_zout_2
        "До чего же противный..." 
        "А, впрочем, чего это я переживаю?"
        
show gg_smile_2_oa
hide gg_zout_2

gg"- На самом деле... ты мне вовсе не нужен! Совсем!"

menu:
    "(Хм-м-м?)":
        show gg_smile_1 
        hide gg_smile_2_oa
        gg"- Я полна сил и чувствую себя прекрасно - значит, мне все нипочем. А ты... ты можешь только смотреть и кусать локти от своей бесполезности!"
        show gg_smile_2
        hide gg_smile_1
        gg"- Хи-хи, могу представить, как ты сейчас злишься."
menu:
    "(Да уж, я прямо вне себя.)":
        menu:
            "(И кстати, бесполезная здесь только ты.)":
                menu:
                    "(И жалкая вдобавок.)":
                        pass
    "(С чего вдруг такое хорошее настроение?)":
        hide gg_smile_2
        show gg_smile_3_ad
        gg"- А чего грустить?"
        menu:
            "(Вспомни себя пару часов назад.)":
                show gg_mad_3
                hide gg_smile_3_ad
                gg"- Не понимаю, о чем ты."
                menu:
                    "(Не ври.)":
                        show gg_smile_1_oa
                        hide gg_mad_3
                        gg"- Не-а. Все равно не понимаю."
                        menu:
                            "(Ну и ладно. Зато я еще долго не забуду эту жалкую, сопливую девчонку.)":
                                menu:
                                    "(Которая только и делает, что постоянно ноет.)":
                                        hide gg_smile_1_oa
                    "(Не ври.)":
                        show gg_smile_1_oa
                        hide gg_mad_3
                        gg"- Не-а. Все равно не понимаю."
                        menu:
                            "(Ну и ладно. Зато я еще долго не забуду эту жалкую, сопливую девчонку.)":
                                menu:
                                    "(Которая только и делает, что постоянно ноет.)":
                                        hide gg_smile_1_oa
                    "(Не ври.)":
                        show gg_smile_1_oa
                        hide gg_mad_3
                        gg"- Не-а. Все равно не понимаю."
                        menu:
                            "(Ну и ладно. Зато я еще долго не забуду эту жалкую, сопливую девчонку.)":
                                menu:
                                    "(Которая только и делает, что постоянно ноет.)":
                                        hide gg_smile_1_oa
hide gg_smile_2
show gg_nerv_1_ad
gg"- Даже не пытайся испортить мне настроение! Пока мы вместе, я хочу веселиться, ясно?"
play sound renpy.random.choice(nice_sounds)
menu:
    "(Значит, теперь ты диктуешь условия?)":
        show gg_mad_3
        hide gg_nerv_1_ad
        gg"- Да!"

menu:
    "(Что ж, посмотрим, надолго ли тебя хватит.)":
        show gg_mad_2_ad
        hide gg_mad_3
        gg"- Вот и посмотрим!"
        show gg_nerv_2_oa
        hide gg_mad_2_ad
        gg"- ..."
        show gg_sad_3
        hide gg_nerv_2_oa
        gg"- Я..."
        show gg_sad_2
        hide gg_sad_3
        gg"- Я и правда настолько жалкая?"
menu:
    "(...)":
        show gg_sad_1_ad
        hide gg_sad_2
        gg"- Не молчи..."
        hide gg_sad_1_ad
        show gg_zout_2

"Я чувствую, как слезы стекают по щекам, задерживаются на подбородке, а затем... Затем падают на мою одежду, прожигая в ней дыры."

menu:
    "(Недолго ты продержалась. Что ж, ожидаемо.)":
        hide gg_zout_2
        show gg_sad_2_oa
        gg"- Эй, я хотя бы попыталась!.."
        menu:
            "(Сходи ка-ты умойся. Потом решим, что с тобой делать.)":
                
                stop music fadeout 4
                $ change_cursor("no")
                
                $ _game_menu_screen = None
                
                hide gg_sad_2_oa
                hide overlay onlayer say
                hide cg_mirror_gg2
                hide bg
                hide sky3
                with ddp
                
                $ renpy.free_memory()
                
                $ renpy.pause(1, hard=True)
                
                play music "audio/milk/milk4.mp3" fadein 6
                
                show sky1 at circle:
                    truecenter zoom 1.01
                show cg_mirror_gg4 at circle2:
                    truecenter zoom 1.01
                show cg_mirror_idle
                with ddp
                $ renpy.pause(1, hard=True)
                show overlay with ddp2
                $ renpy.pause(1, hard=True)
                $ change_cursor("milk")
                
                $ _game_menu_screen = 'save'
                
                "И вновь я у зеркала. Неотрывно смотрю на саму себя, пытаясь не отвлекаться на насмешливые взгляды стен, не вслушиваться в их мерзкое хихиканье. Но вот и мое собственное отражение криво улыбается, скалит на меня зубы..." 

"Я зажмуриваюсь, но это не помогает. Даже провались я под землю, не помогло бы."
"Я принимаюсь считать в уме числа. Два в квадрате, дважды два в квадрате, квадрат в квадрате, квадратный квадрат в пирамиде, пирамидальная структура в кубе, пирамидальная структура в гиперкубе..."
"Помогло."
play sound renpy.random.choice(nice_sounds)
"Правда, голова теперь раскалывается."

menu:
    "(Как ты себя чувствуешь?)":
        gg"- Издеваешься, да?.."
        menu:
            "(Я обязан спрашивать тебя об этом хотя бы пару раз за сеанс.)": 
                gg"- Сеанс, значит..."
                menu:
                    "(Не нравится слово?)":
                        gg"- Все в порядке."
                        menu:
                            "(Нет уж, не в порядке.)":
                                gg"- Я..."
            "(Если тебе так угодно.)":
                gg"- ..."
                menu:
                    "(Что же случилось?)":
                        gg"- Ничего, просто..."
                    "(Я волнуюсь за тебя.)":
                        gg"- Я это знаю!"
                        gg"- Я повела себя странно, да?"
                        gg"- Понимаешь, я..."
    "(Прости, что нагрубил.)":
        gg"- Ты не виноват."
        gg"- Ты никогда ни в чем не виноват."
        menu:
            "(Хорошо, можешь винить себя. Но не переусердствуй.)":
                gg"- Я..."
            

gg"- Почему-то я подумала, что смогу все взять в свои руки. Я была почти готова!.."
gg"- Была уверена, что смогу изменить хоть что-нибудь. Ведь получилось же купить молоко, понимаешь?"
gg"- Ты ведь знал, каким это было испытанием."

$ _game_menu_screen = None

$ change_cursor("no")
hide sky1
hide overlay
hide cg_mirror_gg4
hide cg_mirror_idle
with ddp

$ renpy.free_memory()

$ renpy.pause(1, hard=True)

show sky4 at circle:
    truecenter zoom 1.01
show cg_pills
with ddp
$ renpy.pause(1, hard=True)
show overlay with ddp2
$ renpy.pause(1, hard=True)
$ change_cursor("milk")

$ _game_menu_screen = 'save'

menu:
    "(И поэтому ты выбросила лекарства?)":
        gg"- Глупое решение, да?"

menu:
    "(Несомненно.)": 
        menu:
            "(Однако, есть и хорошая сторона.)":
                gg"- Какая?"
                menu:
                    "(Разве это не значит, что ты выздоравливаешь?)":
                        gg"- Ерунда. Лекарства надо принимать, а не выбрасывать." 
                        gg"- Глупо, так глупо..."
            "(Более того, это опасно.)":
                gg"- Я знаю..."
                gg"- А ты давишь на меня!"
    "(Это твое решение, каким бы оно ни было.)":
        gg"- Разве это имеет значение?"
        menu:
            "(Да.)":
                gg"- Почему-то мне совсем в это не верится."
            "(Нет.)":
                gg"- Я так и думала."
            "(А как ты считаешь?)":
                gg"- Я совсем ни в чем не уверена. Да и ты все равно не воспринимаешь меня всерьез."

menu:
    "(Тогда почему ты это сделала?)":
        gg"- Мне казалось, что я справлюсь своими силами."

"Действительно, в тот момент боль ненадолго отступила... Однако сейчас я чувствую ее с утроенной силой."
gg"- Мне так больно..."

menu:
    "(Выпей уже лекарства, наконец. Иначе я не буду с тобой разговаривать.)": 
        gg"- Нет, только не бросай меня!.."
        menu:
            "(...)":
                gg"- ..."
    "(Ты знаешь, как нужно поступить.)":
        pass
        

"Я с обреченным видом протягиваю руку к полке с лекарствами. Глотаю таблетки одну за другой, отгоняя неприятные образы, то и дело всплывающие в памяти."
"И все же... перед глазами стоит жуткая картина: комки густой крови в прозрачной оболочке спускаются вниз по пищеводу, царапая его нежные стенки, оставляя борозды..." 
"Я с силой встряхиваю головой - пусть кружится, пусть болит - лишь бы не думать об этой мерзости!.."

menu:
    "(И все-таки ты осталась при своем.)":
        gg"- Что ты имеешь в виду?"
        menu:
            "(Ты боишься остаться одна и это беспокоит тебя гораздо больше, чем боль.)":
                gg"- Да, наверное..."

"Я подбрасываю последнюю таблетку в воздух и ловлю ее ртом."

stop music fadeout 4
$ change_cursor("no")

$ _game_menu_screen = None

hide sky4
hide overlay
hide cg_pills
with ddp

$ renpy.free_memory()

$ renpy.pause(1, hard=True)

play music "audio/milk/milk14.mp3" fadein 6

show sky1 at circle:
    truecenter zoom 1.01
show cg_floor
with ddp
$ renpy.pause(6, hard=True)
show overlay with ddp2
$ renpy.pause(1, hard=True) 
$ change_cursor("milk")

$ _game_menu_screen = 'save'

"Я ложусь на пол. Смотрю в потолок. Оттуда, сверху, отчетливо слышен бег воды по металлическим трубам. Слышен треск бетонных плит, что когда-нибудь обрушатся мне на голову." 
"Однако я совсем этого не боюсь; сложно представить, что смерть поджидает меня наверху. Скорее, она тянет когтистые лапы откуда-то снизу, дожидаясь, пока я потеряю бдительность..."
play sound renpy.random.choice(nice_sounds)
$ change_cursor("no")
window hide
hide overlay with ddp2
$ renpy.pause(6, hard=True)
$ change_cursor("milk")
menu:
    "(Хочешь поговорить об этом?)":
        show overlay onlayer say with ddp2
        window show
        gg"- Нет уж, хватит с меня болтовни."
        $ change_cursor("no")
        window hide
        hide overlay onlayer say with ddp2
        $ renpy.pause(6, hard=True)
        $ change_cursor("milk")
        menu:
            "(Тогда чего ты хочешь?)":
                show overlay onlayer say with ddp2
                window show
                gg"- Просто... просто немного полежать."            
$ change_cursor("no")
window hide
hide overlay onlayer say with ddp2
$ renpy.pause(6, hard=True)
$ change_cursor("milk")
menu:
    "(Если потолок и обрушится, то это произойдет не сегодня.)":
        show overlay onlayer say with ddp2
        window show
        gg"- Прошу, помолчи."
        gg"- Мне нужно привести мысли в порядок."
    "(...)":
        pass

$ _game_menu_screen = None

$ change_cursor("no")
window hide
hide sky1
hide overlay onlayer say
hide cg_floor
with ddp

$ renpy.free_memory()

$ renpy.pause(1, hard=True)

show sky3 at circle:
    truecenter zoom 1.01
show cg_ceiling
with ddp
$ renpy.pause(1, hard=True)
show overlay with ddp2
$ renpy.pause(1, hard=True) 
$ change_cursor("milk")

$ _game_menu_screen = 'save'

"Я аккуратно извлекаю несформировавшиеся мысли из головы и располагаю ровными рядами на потолке - теперь он выполняет роль пробковой доски."
"В надежде собрать цельную картину я переставляю их местами, складываю в стопки, беспорядочно раскидываю... В конечном итоге я раздраженно смахиваю их прочь движением руки и начинаю заново."
gg"- Не выходит..."

menu:
    "(Знаешь выражение ‘тараканы в голове’? Вот и представь, будто твои мысли - это тараканы.)":
        gg"- Фу, ненавижу тараканов! Можно это будут светлячки?"
menu:
    "(Как хочешь...)":
        
        stop music fadeout 1
        
        hide overlay with ddp2
        
        play music "audio/milk/milk25.mp3" fadein 2
        
        show fireflies_anim with ddp
        
        $ renpy.pause(3, hard=True)
        
        show overlay onlayer say with ddp2
        
        "Не успеваю я моргнуть и глазом, как мысли (а теперь - светлячки) принимаются кружить по потолку самостоятельно, складываясь в причудливые узоры." 
        "Мне остается лишь наблюдать за этим и ловить подходящий момент."
"..."
"..."
"..."
"Только вот... он все никак не наступает."
"..."
"..."
"..."
"Слушая издевательский шелест маленьких крыльев под потолком, я начинаю терять терпение."
"..."
"..."
"..."

gg"- С меня хватит! Ненавижу вас!"

$ _game_menu_screen = None

stop music fadeout 4
$ change_cursor("no")
hide sky3
hide overlay onlayer say
hide cg_ceiling
hide fireflies_anim
with ddp

$ renpy.free_memory()

$ renpy.pause(1, hard=True)

play music "audio/milk/milk5.mp3" fadein 6

show sky2 at circle:
    truecenter zoom 1.01
show cg_mirror_gg2 at circle2:
    truecenter zoom 1.01
show bg
with ddp
show overlay onlayer say with ddp2
$ change_cursor("milk")

$ _game_menu_screen = 'save'

"Вскочив на ноги, я кричу что есть силы - светлячки в страхе разлетаются кто куда."
menu:    
    "(Молодец. А теперь начинай заново.)":
        show gg_mad_3 with ddp2
        gg"- Еще чего!"

menu:
    "(Неуравновешенность тебя совсем не красит.)":
        hide gg_mad_3
        show gg_mad_3_ad
        gg"- Да плевать я хотела!"

menu:
    "(И тебя это не тревожит?)":
        hide gg_mad_3_ad
        show gg_sad_2
        gg"- А должно?"

menu:
    "(Нет.)":
        menu:
            "(Многие люди так себя ведут.)":
                hide gg_sad_2
                show gg_sad_1
                gg"- ..."
                hide gg_sad_1
                show gg_sad_2
                gg"- Правда?"
                menu:
                    "(Нет ничего постыдного в том, чтобы сорваться на кого-нибудь. Если на то есть причина.)":
                        menu:
                            "(У тебя ведь была причина?)":
                                hide gg_sad_2
                                show gg_nerv_2_oa
                                gg"- ..."
                                menu:
                                    "(Ты обязательно выздоровеешь, поверь мне.)":
                                        menu:
                                            "(А теперь начинай заново.)":
                                                pass
    "(Да.)":
        hide gg_sad_2
        show gg_mad_1
        gg"- И что прикажешь делать?"
        menu:
            "(Не знаю. Тебе решать.)":
                pass
hide gg_mad_1
hide gg_nerv_2_oa
show gg_sad_3
gg"- ..."
hide gg_sad_3
show gg_smile_3
gg"- Хи-хи..."
gg"- Ты опять за старое..."

menu:
    "(О чем ты?)":
        hide gg_smile_3
        show gg_smile_2_ad
        gg"- Неважно!"
hide gg_smile_2_ad
show gg_sad_1
gg"- И вообще, я передумала. Пожалуйста, больше не молчи так долго."
hide gg_sad_1
show gg_sad_2
gg"- Мне не обойтись без твоей помощи."
menu:
    "(...)":
        menu:
            "(Хорошо.)":
                hide gg_sad_2
                show gg_sad_3
                "Я вновь поднимаю глаза к потолку - к сожалению, все мои светлячки куда-то спрятались."

hide gg_sad_3
show gg_sad_2_oa
gg"- Их надо найти..."

menu:
    "(Забудь о них и ложись спать.)":
        hide gg_sad_2_oa
        show gg_nerv_1_ad
        gg"- Нет, ты не понимаешь. Если я уже о чем-то задумалась, мне нужно обязательно додумать эту мысль до конца, иначе..."
    "(...)":
        pass
hide gg_sad_2_oa
hide gg_nerv_1_ad
show gg_nerv_2
play sound renpy.random.choice(nice_sounds)
"Я бегло оглядываю комнату - слишком много мест, где может спрятаться такое маленькое существо, как светлячок."
hide gg_nerv_2
show gg_sad_1 
gg"- Они могут быть где угодно..."
hide gg_sad_1
show gg_sad_3

play sound "audio/clock.ogg"

"Внезапно раздается оглушающий грохот - часы показали полночь. Уже так поздно... но я не могу сейчас пойти спать!"
hide gg_sad_3
show gg_sad_1_oa
gg"- Ты ведь поможешь мне? Пожалуйста, скажи, что поможешь!"

menu:
    "(...)":
        hide gg_sad_1_oa
        show gg_nerv_2_ad
        gg"- Ну-у, не издевайся! Ты ведь обещал со мной говорить!"

menu:
    "(О чем ты думала тогда, на полу?)":
        hide gg_nerv_2_ad
        show gg_mad_1
        gg"- Что ты имеешь в виду? Ты как никто другой должен это знать."

menu:
    "(...)":
        gg"- Вместо того, чтоб спрашивать всякую ерунду, лучше бы помог мне найти светлячков!"
        jump dnow
    "(В том и дело, что я понятия не имею. Это... странно.)":
        hide gg_mad_1
        show gg_sad_2
        gg "- ..."
menu:
    "(...)":
        menu:
            "(Ты расскажешь мне?)":
                hide gg_sad_2
                show gg_sad_1
                gg"- Я..."
                hide gg_sad_1
                hide bg
                hide sky
                hide cg_mirror_gg

stop music fadeout 0.5

$ _game_menu_screen = None

$ change_cursor("no")

hide sky2
hide cg_mirror_gg2
hide overlay onlayer say
window hide

$ renpy.free_memory()

$ renpy.movie_cutscene("eyez.mkv")

play music "audio/milk/milk2.mp3"
scene sky2 at circle:
    truecenter zoom 1.01
$ renpy.pause(5, hard=True)
show overlay onlayer say with ddp

$ change_cursor("milk")

"Я закатываю рукава и принимаюсь неистово тереть глаза. Они чешутся..."

menu:
    "(????????????????????Почему ты плачешь????????????????????)":
        ggz"{cps=14}- Глаза чешутся...{/cps}"
    "(????????????????????Почему ты плачешь????????????????????)":
        ggz"{cps=14}- Глаза чешутся...{/cps}"

menu:
    "(????????????????????Ты выпила молоко????????????????????)": 
        ggz"{cps=14}- Интересно, а если оторвать все ресницы одну за другой, глаза перестанут чесаться?..{/cps}" 
        ggz"{cps=14}- Интересно, а если оторвать все ресницы одну за другой, все ресницы одну за другой, они... а если оторвать все ресницы одну за другой...{/cps}"
    "(????????????????????Он принес молоко????????????????????)":
        ggz"{cps=14}- Интересно, а если оторвать все ресницы одну за другой, глаза перестанут чесаться?..{/cps}" 
        ggz"{cps=14}- Интересно, а если оторвать все ресницы одну за другой, все ресницы одну за другой, они... а если оторвать все ресницы одну за другой...{/cps}"

menu:
    "(????????????????????Что ты наделала????????????????????)":
        ggz"{cps=14}- Мне надо собрать стекло, а потом... Потом мне надо принять ванну, а потом...{/cps}"
menu:
    "(Вот, выпей немного молока.)":
        
        play sound "audio/no.ogg"
        
        play audio "audio/narrz2.ogg"
        
        scene skyseizure
        
        "{size=60}- НЕ-Е-Е-Е-Е-Е-Е-Е-Е-Е-Е-Е-Е-Е-Е-Е{nw}{/size}"
        stop music
        play music "audio/milk/milk5.mp3"

hide sky3

$ renpy.free_memory()

show sky2 at circle:
    truecenter zoom 1.01
show cg_mirror_gg2 at circle2:
    truecenter zoom 1.01
show bg

$ achievement.grant("Achievement01_first_death1")
init:
    $ achievement.register("Achievement01_first_death1")
    $ achievement.sync()

$ achievement.sync()

$ _game_menu_screen = 'save'

$ second_death = True

"Я стою посреди комнаты, раскрыв рот и тяжело дыша. Кажется, я только что испытала смерть... Как еще объяснить произошедшее, я не знаю." 
"Да уж, вот так новости!"

menu:
    "(Так ты расскажешь мне или нет?)":
        show gg_smile_2_ad with ddp2
        gg"- О чем?"
        hide gg_smile_2_ad
        show gg_conf_1
        gg"- Давай лучше искать светлячков!"

menu:
    "(Ты какая-то странная.)":
        hide gg_conf_1
        show gg_mad_1_oa
        gg"- Лучше помогай мне, а не болтай. И так многовато приключений перед сном..."
        hide gg_mad_1_oa
        show gg_sad_2_oa
        gg "- Надо поскорее собрать свои мысли в кучу и лечь спать."
        hide gg_sad_2_oa
        show gg_smile_1
        gg "- А мысли-то спрятались, хи-хи!"
        $ magaz = True

label dnow:
menu:
    "(Честно говоря, я понятия не имею, где их искать.)":
        hide gg_mad_1 
        hide gg_nerv_2_ad
        hide gg_smile_1
        show gg_neutral_3_ad
        gg"- Я тоже..."

menu:
    "(Значит, придется перевернуть все вверх дном и...)":
        hide gg_neutral_3_ad
        show gg_mad_1
        gg"- Нет, нет и еще раз нет! Если я устрою хотя бы небольшой беспорядок, мне будет очень плохо."
        hide gg_mad_1
        show gg_mad_4_oa
        gg"- Все вещи должны оставаться на своих местах и никак иначе!"

menu:
    "(Почему?)":
        hide gg_mad_4_oa
        show gg_nerv_1_ad
        gg"- ..."
        hide gg_nerv_1_ad
        show gg_nerv_2_ad
        gg"- ..."

menu:
    "(Ты что, пытаешься придумать причину прямо сейчас?)":
        hide gg_nerv_2_ad
        show gg_sad_1_oa
        gg"- Я?.. Н-нет, ничего подобного!"
        menu:
            "(Кажется, ты забыла поставить свой мыслеблок - тебя всю насквозь видно.)":
                hide gg_sad_1_oa
                show gg_mad_3
                gg"- Нахал!"
    "(Не хочешь - не говори...)":
        gg"- Не хочу и не скажу!"

menu:
    "(Что ж, ладно. Выходит, нам надо найти крохотных насекомых среди кучи хлама, при этом не сдвинув ничего даже на сантиметр?)":
        hide gg_mad_3
        hide gg_nerv_2_ad
        show gg_conf_1
        gg"- Да!"

menu:
    "(Ну и ну.)":
        hide gg_conf_1
        show gg_mad_2
        gg"- ..."

hide gg_mad_2
show gg_smile_1
gg"- У меня есть идея!.."
gg"- В прошлый раз я была персонажем визуальной новеллы, и это помогло мне справиться с задачей. Теперь я хочу быть персонажем квеста!"
hide gg_smile_1
show gg_smile_2
gg"- Знаешь... Там бывают эпизоды, когда ты просто смотришь на разные предметы и что-то обязательно происходит!"
hide gg_smile_2
show gg_smile_1_oa
gg"- Здорово же!"

menu:
    "(А как же те вещи, которыми ты пользуешься регулярно? Их ты тоже отказываешь трогать?)":
        hide gg_smile_1_oa
        show gg_conf_3
        gg"- Так даже интересней!"

menu:
    "(Это так по-детски...)":
        hide gg_conf_3
        show gg_smile_2_oa
        gg"- А знаешь, что самое классное?"
        hide gg_smile_2_oa
        show gg_smile_1
        gg"- Что этим займешься ты!"

menu:
    "(Ну уж нет.)":
        pass
hide gg_smile_1
show gg_smile_3
gg"- А вот и да!"
hide gg_smile_3
show gg_mad_1
gg"- У меня начинается паника, когда нужно выбрать что-то одно из множества вариантов."
hide gg_mad_1
show gg_mad_2_ad
gg"- Я буду без конца топтаться на месте и в конечном итоге расплачусь и убегу. Ты этого хочешь?"

menu:
    "(До чего капризная...)": 
        menu:
            "(Ты ведь уже доказала, что способна на самостоятельные решения. Почему бы не продолжить в том же духе?)":
                hide gg_mad_2_ad
                hide gg_sad_1
                show gg_sad_2
                gg"- Ну же, не будь таким скучным!"
            "(Делай, что хочешь.)":
                jump pncok

menu:
    "(Я ведь просто дразнюсь.)":
        menu:
            "(Не нужно все взваливать на себя. Просить помощи - это вполне здравое решение.)":
                hide gg_sad_2
                show gg_smile_1_oa
                gg"- Давай уже приступать!"

label pncok:
hide gg_mad_2_ad    
hide gg_smile_1_oa
show gg_smile_3
"Я выхожу в центр комнаты и оглядываюсь по сторонам. Куда бы я спряталась, будь я маленьким светлячком? Ах, до чего же интересно!"
"От предвкушения на сердце ощутимо теплеет."

menu:
    "(Эй.)":
        hide gg_smile_3
        show gg_mad_1
        gg"- Что?"

menu:
    "(Посмотри вниз.)":
        hide gg_mad_1
        show gg_mad_3
        "Я опускаю глаза; спустя секунду из-под моей кофты выползает маленький комочек тепла и света." 
        hide gg_mad_3
        show gg_smile_2
        gg"- Ух ты!"

menu:
    "(Ух ты!)":
        pass
    "(У тебя одежда дымится.)":
        hide gg_smile_2
        show gg_smile_3_ad
        gg"- Хи-хи, да и пусть!"

$ _game_menu_screen = None

$ change_cursor("no")
window hide
hide gg_smile_2
hide gg_smile_3_ad
hide overlay onlayer say
show n
hide cg_mirror_gg2
hide cg_eyelash
hide bg
hide sky2
with ddp

$ renpy.free_memory()
                
$ renpy.pause(1, hard=True)

show sky1 at circle:
    truecenter zoom 1.01
show cg_firefly
with ddp
$ renpy.pause(1, hard=True)
show overlay onlayer say with ddp2
$ renpy.pause(1, hard=True)
$ change_cursor("milk")

$ _game_menu_screen = 'save'

"Я аккуратно подхватываю светлячка - он приятно обжигает пальцы - и кладу на плечо."
gg"- Прости меня, малыш. Пора домой!"
"Словно по команде, светлячок неспешно поднимается в воздух, кружит над головой какое-то время, а затем пулей залетает прямо мне в ухо."
gg"- Хи-хи, щекотно!"
menu:
    "(Что ж, один есть. Давай искать остальных!)":
        gg"- Давай!"

$ _game_menu_screen = None

stop music fadeout 4
$ change_cursor("no")
hide overlay onlayer say
hide cg_firefly
hide sky1
with ddp
window hide

$ renpy.free_memory()

show sky3 at circle:
    truecenter zoom 1.01
show cg_mirror_gg1 at circle2:
    truecenter zoom 1.01
show bg
with ddp
$ renpy.pause(1, hard=True)
$ change_cursor("milk")    

$ _game_menu_screen = 'save'

label pnc_label:
    call screen pnc
    
label newscene_check:
    if X == 5:
        jump newscene_1
    elif X <=4:
        pass

label vse:
hide gg_nerv_2 with ddp2
if zerk:
    pass
else:
    show overlay onlayer say with ddp2

stop sound fadeout 2

play music "audio/milk/milk5.mp3"

"Мысли вроде бы собрались в кучу, но что-то все равно тревожит меня. С другой стороны, я ведь и не должна радоваться..."
menu:
    "(Почему так?)":
        show gg_sad_2_oa with ddp2
        gg"- Если я что-то потеряла, а потом нашла - это просто возврат к началу. Никаких изменений. Ноль - ни плюс, ни минус."
        hide gg_sad_2_oa
        show gg_sad_3_ad
        gg"- А радость - это всегда плюс, понимаешь?"
menu:
    "(Тебе вредно слишком много думать, знаешь ли.)":
        hide gg_sad_3_ad
        show gg_zout_1
        gg"- Спать хочется..."
menu:
    "(Может, проветришься перед сном?)":
        hide gg_zout_1
        show gg_sad_2
        gg"- То есть?"
menu:
    "(Ну, выйдешь на балкон, воздухом подышишь.)":
        hide gg_sad_2
        show gg_zout_2
        "Почему-то эти слова вызвали у меня приступ паники. Я неосознанно делаю шаг назад от балкона." 
        hide gg_zout_2
        show gg_mad_1
        gg"- Не думаю, что это хорошая идея..."
menu:
    "(Почему?)":
        hide gg_mad_1
        show gg_mad_2
        gg"- Это может прозвучать глупо, но..."
        hide gg_mad_2
        show gg_sad_1_oa
        gg"- Мне кажется, кто-то смотрит на меня."
menu:
    "(Хорошо, давай останемся здесь.)":
        hide gg_sad_1_oa
        show gg_sad_2_oa
        gg"- Ага."
        $ lest = True
        jump room
        
    "(Да кому ты нужна!)":
        hide gg_sad_1_oa
        show gg_sad_2_oa
        gg"- ..."
        hide gg_sad_2_oa
        show gg_sad_1_oa
        gg"- Всего на пару минут, ладно?"
        
        stop music fadeout 6
        
        jump balcony
        
label balcony:
show n
$ change_cursor("no")

$ _game_menu_screen = None

hide overlay onlayer say
hide gg_sad_1_oa
hide bg
hide sky3
hide cg_mirror_gg1
with ddp

$ renpy.free_memory()

$ renpy.pause(2, hard=True)
play music "audio/milk/milk18.mp3"
$ renpy.pause(2, hard=True)


show cg_balcony at Move((0.5, -1.5), (0.5, -0.1), 75,
                  xanchor=0.5, yanchor=0)
with ddp

$ renpy.pause(2, hard=True)

show overlay onlayer say with ddp

$ change_cursor("milk")

$ _game_menu_screen = 'save'

"Мой дом похож на бездонный котел. Вместо копоти на его стенках - сотни бетонных и железных коробок." 
"В окнах горит свет, звучат неразборчивые голоса. Оглушающе воет ветер, закручиваясь спиралями и разделяясь на сотни отдельных потоков - по всей видимости, для того, чтобы быть услышанным каждым жителем дома." 
"До чего же, должно быть, тоскливо постоянно жить в тишине..."
menu:
    "(Странный у тебя дом, не находишь?)":
        gg"- Раньше из окна был вид на горизонт, а дом уходил вправо и влево на многие сотни метров. Наверно, в какой-то момент он замкнулся в кольцо."
        gg"- По-моему, ничего странного."
menu:
    "(...)":
        menu:
            "(Как ты себя чувствуешь?)":
                gg"- Я определенно себя чувствую. Иногда большего и не надо."
menu:
    "(И все же, тебе тревожно. Я прав?)": 
        gg"- Разумеется. Более того - я в абсолютном ужасе. Но разве это так заметно?"
menu:
    "(Ты смотришь куда угодно, но не вверх.)":
        gg"- Ах, это..."
        gg"- Я ведь тебе рассказывала, верно?"
menu:
    "(О чем?)": 
        gg"- Да так, пустяки."
menu:
    "(Разве могут пустяки вызывать ужас?)":
        gg"- Это... сложно описать."
"Я взбираюсь на металлические перила и свешиваю ноги вниз." 
"Один за другим бросаю в бездну короткие взгляды - та отвечает мне рассерженным ледяным дыханием." 
"Так мы и общаемся. Будто старинные друзья."
gg"- Иногда мне кажется, что весь мир притворяется ненормальным."
gg"- Он будто бы хочет убедить меня в чем-то, чего на самом деле нет."
menu:
    "(Странно, не находишь?)":
        gg"- Да, но..."
        gg"- В то же время... Я даже немного рада этому."
        gg"- Все вокруг создано лишь для меня. Создано обманывать, запутывать, сбивать с толку..."
        gg"- Если это правда, выходит, не такая уж я и сумасшедшая?"
menu:
    "(Считать это правдой и есть сумасшествие.)":
        gg"- Наверное."
"..."
"Очередной ураган проносится по стенкам котла, разбивая в пыль стекла и сметая бетонный налет. Меня он лишь нежно гладит, взъерошивая волосы."

if kompik:
    jump fall
else:
    jump nofall

label fall:
gg"- Я так и не придумала кодовое слово..."
menu:
    "(Ты ведь и сама вспомнила о своем обещании. Значит, кодовое слово уже не нужно.)":
        gg"- Не люблю, когда так происходит. Хочу вспоминать о некоторых вещах только тогда, когда хочется."
menu:
    "(Тем не менее, ты обещала.)":
        gg"- Я сдержу обещание. Просто имей в виду, что с этой секунды каждое слово будет приносить мне боль."
"Я наклоняюсь вниз и мысленно падаю в пропасть. Ровно две минуты до того, как я разобьюсь."

stop music fadeout 4

$ _game_menu_screen = None

$ change_cursor("no")
hide cg_balcony
hide overlay onlayer say
with ddp

$ renpy.free_memory()

$ renpy.pause(1, hard=True)


play music "audio/milk/milk20.mp3"

show sky1 at circle:
    truecenter zoom 1.01
show cg_fall_far
with ddp

$ renpy.pause(5, hard=True)

hide cg_fall_far
hide sky1
with ddp

$ renpy.pause(1, hard=True)

show sky4 at circle:
    truecenter zoom 1.01
show cg_fall_close 
with ddp

show overlay onlayer say with ddp
$ change_cursor("milk")

$ _game_menu_screen = 'save'

gg"- У меня был друг в сети. Лучший друг! Даже несмотря на то, что его набор букв вместо имени был не самым клевым."
gg"- Да и набор пикселей вместо фотографии был скучным и непривлекательным..."
gg"- Это ведь странно и неправильно - нарушать правила нахождения в сети. Зачем он это делал?" 
gg"- Может, в его коде не хватало нескольких строк?"
menu:
    "(Я не совсем понимаю, о чем ты.)":
        gg"- Я бы могла рассказать тебе об этих правилах."
        gg"- Их невозможно нигде отыскать, но я-то умная и сама во всем разобралась!"
        gg"- Однако же..."
        gg"- Я не уверена, стоит ли их озвучивать."
menu:
    "(Почему?)":
        gg"- Когда я пытаюсь произнести вслух то, что на уме - запросто могу где-то ошибиться." 
        gg"- Одна ошибка - и все сказанное дальше полностью противоречит моим мыслям."
        gg"- И в итоге я сама себя разубеждаю."
        gg"- А я этого не хочу!"
menu:
    "(По твоей логике лучше вообще никогда рта не открывать.)":
        gg"- Конечно! Это моя мечта!"
        gg"- Не открывать рта, не вставать с кровати, ничего не видеть и не слышать..."
        gg"- Лишь сны, сны... ах, ну почему все так ужасно?"
menu:
    "(Не отвлекайся. Так что же твой друг?)":
        gg"- Друг?"
        gg"- Ах, да..."
        gg"- Он... и хватило же наглости!.."
menu:
    "(Ну же, собери мысли в кучу.)":
        gg"- Он каким-то образом заставил меня поверить, будто он настоящий."
        gg"- Расписывал мне чью-то жизнь в мельчайших подробностях, выдавая за свою."
        gg"- И, разумеется, ждал того же и от меня."
        gg"- Ну я и рассказала ему все-все о себе. Ничего не утаила."
        "Я крепко стискиваю зубы. Ветер нещадно хлещет по лицу, разрезает кожу на неровные полосы, словно тонкую ткань."
        gg"- Он знал обо мне больше, чем кто-либо в мире."
        gg"- И знаешь, что он сделал?"
menu:
    "(Да.)":
        gg"- Ха-ха..."
        gg"- Натравить на меня сотни ботов, должно быть, очень весело."
        gg"- А главное, все от этого только выигрывают."
        gg"- Они появляются тут и там. Довольно простой код, не требующих особых усилий для выполнения - неудивительно, что алгоритм присуждает эту модель поведения с большей вероятностью, чем прочие из списка."
        gg"- Генераторы текстов и видеороликов тут же принимаются за работу. Мое имя всплывает в сети все чаще и чаще."
        gg"- Это невыносимо."
        gg"- Невыносимо."
        gg"- Из-за каждого угла, с балконов, крыш, подвалов, стен, потолков я всегда ощущаю пристальные взгляды множества глаз."
        gg"- А теперь - и с экранов."
        gg"- Но я положу этому конец. Я давно решила."
        gg"- Хотя... Возможно, я решила сделать это только..."
        $ kompol = True

hide sky4
hide cg_fall_close
show sky1

play sound "audio/milk/boom.ogg"
stop music fadeout 2
"Мое тело наконец обрушивается на землю, разлетаясь, словно фарфор, на миллионы мелких частиц." 
if second_death:
    
    $ achievement.grant("Achievement01_second_death1")
    init:
        $ achievement.register("Achievement01_second_death1")
        $ achievement.sync()

    $ achievement.sync()
    
    "Уже вторая смерть за сегодня."
else:
    pass
label nofall:
gg"- Мне холодно, пойдем внутрь."

stop music fadeout 4

$ _game_menu_screen = None

$ change_cursor("no")
hide overlay onlayer say
hide cg_balcony
hide sky1
with ddp

$ renpy.free_memory()


show sky2 at circle:
    truecenter zoom 1.01
show cg_mirror_gg2 at circle2:
    truecenter zoom 1.01
show bg
with ddp
$ renpy.pause(1, hard=True)
show overlay onlayer say with ddp
$ change_cursor("milk")

$ _game_menu_screen = 'save'

"Я вернулась в комнату. К счастью, она совсем не изменилась за те минуты, что я была за её пределами."
if kompol:
    "Ни секунды не думая, я подхожу к ноутбуку и с силой выдергиваю кабель из розетки."
    
    show gg_sad_2 with ddp2
    
    gg"- Вот и все."
    "Вот и все."
    menu:
        "(Вот и все.)":
            pass
else:
    jump room

play sound renpy.random.choice(nice_sounds)
label room:
    
    if lest:
        pass
    else:
        play music "audio/milk/milk5.mp3" fadein 5

    menu:
        "(Что будешь делать?)":        
            if kompol:
                hide gg_sad_2
                show gg_mad_3
            elif lest:
                hide gg_sad_2_oa
                hide gg_sad_2
                show gg_mad_3
            else:
                hide gg_sad_2_oa
                hide gg_sad_2
                show gg_mad_3 with ddp2
                
            gg"- Что за глупый вопрос?"
            gg"- Спать, конечно же."
            hide gg_mad_3
            show gg_mad_1_oa
            gg"- Надеяться, что завтра наступит через год или десять."
            hide gg_mad_1_oa
            show gg_sad_2
            gg"- Представлять, будто я где-то вне своей оболочки, и при этом я - это все еще я. Немыслимо, как молоко вне пакета. И все же..."
menu:
    "(И все же?..)":
        hide gg_sad_2
        show gg_nerv_1_ad
        gg"- Необязательно говорить вслух, чтобы я понимала, что ты переживаешь за меня."
        gg"- Ведь я и так это знаю."
        hide gg_nerv_1_ad
        show gg_mad_3_oa
        gg"- Также я знаю, что у нас осталось совсем немного времени."
menu:
    "(Ты не станешь пить еще одну таблетку.)":
        hide gg_mad_3_oa
        show gg_mad_3
        gg"- Разумеется. Более того, я не стану пить ее и завтра."
        hide gg_mad_3
        show gg_mad_1
        gg"- И послезавтра."
        hide gg_mad_1
        show gg_mad_2
        gg"- И вообще никогда."
menu:
    "(Прощаемся, выходит?)":
        hide gg_mad_2
        show gg_sad_1
        gg"- ..."
        hide gg_sad_1
        show gg_sad_2_ad
        gg"- Нет..."
        gg"- У меня будет еще одна просьба... совсем крохотная."
menu:
    "(Какая же?)":
        hide gg_sad_2_ad
        show gg_zout_1
        gg"- Я сегодня слишком много наговорила. Многое хотелось бы навсегда забыть."
        hide gg_zout_1
        show gg_sad_2_oa
        gg"- Я не виню тебя, просто... Было ли это так необходимо?"
menu:
    "(Вот завтра и узнаешь.)":
        hide gg_sad_2_oa
        show gg_mad_2_ad
        gg"- Нет, я так не усну."
menu:
    "(Хорошо, так что за просьба?)":
        hide gg_mad_2_ad
        show gg_neutral_3_oa
        gg"- Я... м-м..."
        hide gg_neutral_3_oa
        show gg_nerv_2
        "Я нервно чешу запястья и прикусываю губу."
menu:
    "(Постой, ты что... боишься мне сказать?)":
        hide gg_nerv_2
        show gg_sad_1_oa
        gg"- Да!"
        hide gg_sad_1_oa
        show gg_sad_2_oa
        gg"- А еще я боюсь, что произойдет что-то очень плохое, если я скажу!"
        hide gg_sad_2_oa
        show gg_sad_3_ad
        gg"- А еще я боюсь, что из-за того, что произойдет что-то плохое, произойдет что-то гораздо, гораздо хуже!" 
menu:
    "(Да понял я!)":
        menu:
            "(И все же не отстану, пока не скажешь.)":
                
                hide gg_sad_3_ad
                show gg_mad_3
                
                gg"- Зануда..."
menu:
    "(Нет, ты!)":
        
        stop music fadeout 4
        
        $ _game_menu_screen = None
        
        $ change_cursor("no")
        show n
        hide gg_mad_3
        hide overlay onlayer say
        hide cg_mirror_gg1
        hide cg_mirror_gg2
        hide cg_mirror_gg3
        hide cg_mirror_gg4
        hide bg
        hide sky1
        hide sky2
        hide sky3
        hide sky4
        with ddp
        
        $ renpy.free_memory()
        
        $ renpy.pause(1, hard=True)
        
        play music "audio/milk/milk21.mp3" fadein 4
        
        show sky3 at circle:
            truecenter zoom 1.01
        show cg_dream
        with ddp
        show overlay onlayer say with ddp
        $ renpy.pause(1, hard=True)
        $ change_cursor("milk")
        
        $ _game_menu_screen = 'save'
        
"Я неуклюже забираюсь в спальный мешок. Внизу комнаты очень прохладно; и пусть электрический обогреватель работает изо всех сил, я, тем не менее, спешу скорей укутаться."
hide cg_dream
show cg_dream_s
gg"- Мне грустно из-за того, что сны больше не приходят."
gg"- Ни за что не поверишь, как я поначалу справлялась с этим."
menu:
    "(Конечно, поверю.)": 
        gg"- Я знаю. Это была шутка."
gg"- Так вот - я умывалась, чистила зубы, ложилась и начинала воображать, будто я вижу сон. При этом я, конечно же, совсем не спала и поутру вечно клевала носом."
gg"- После недели бессонных ночей я стала себя странно чувствовать и начала видеть всякое..."
gg"- Парящие в воздухе буквы, странные силуэты, появляющиеся в самых неожиданных местах. Выпученные глаза с дрожащими бледными зрачками... Страшно, знаешь ли!"
gg"- Однажды я чуть не умерла. Просто упала посреди комнаты и какое-то время не могла пошевелиться. А силуэты, буквы и глаза нависли надо мной и осуждающе шипели."
gg"- Это было ужасно."
gg"- И... заслуженно, что ли?"
gg"- Я будто была поймана на самой большой в мире лжи. Да, должно быть, так и было."
gg"- После этого я прекратила."
gg"- А силуэты, буквы и глаза остались жить тут - понравилось, видимо!"
gg"- Вечно ходят за мной по пятам, подглядывают... А я их побаиваюсь и не могу даже слова поперек сказать."
gg"- Но сегодня..."
gg"- Сегодня..."
menu:
    "(Ну?)":
        gg"- Я..."
menu:
    "(Ты все еще боишься мне сказать?)":
        gg"- Конечно, они же слушают!"
menu:
    "(Объясни на пальцах.)":
        gg"- Ладно!"
hide cg_dream_s
show cg_dream
"Я принимаюсь беспорядочно, но оттого не менее воодушевленно вертеть пальцами, выстраивая сложные фигуры."
menu:
    "(Ты хочешь, чтобы я... рассказал тебе историю перед сном?)":
        gg"- Тш-ш-ш-ш!"
        hide cg_dream
        show cg_dream_s
        gg"- Я что, зря тут стараюсь? Тебя ведь услышат!"
menu:
    "(Расслабься, никто тебя не слышит.)":
        gg"- ..."

gg"- Ну так что?"
menu:
    "(Я бы с радостью, но я совсем не знаю, как их рассказывать.)":
        gg"- Ой, да это очень просто!"
        gg"- Просто говори о чем угодно без остановки."
menu:
    "(Звучит нелепо.)":
        gg"- И вовсе нет!"
menu:
    "(А еще бессмысленно.)":
        gg"- Да что ты вообще понимаешь?"
menu:
    "(Достаточно, чтобы понять, что мы лишь впустую потратим время.)":
        menu:
            "(Давай сосредоточимся на чем-нибудь действительно важном.)":
                gg"- Скукотища..."
menu:
    "(...)":
        gg"- Ладно..."
menu:
    "(Закрывай глаза.)":
        
        stop music fadeout 5
        
        $ change_cursor("no")
        
        $ _game_menu_screen = None
        
        show b
        hide bg
        hide sky3
        hide cg_dream_s
        hide overlay onlayer say
        hide n
        
        $ renpy.free_memory()
        
        $ renpy.pause(3, hard=True)

if magaz:
    jump magaz
elif telef:
    jump telef
elif zerk:
    jump zerk
elif kompol:
    jump kompol
elif lest:
    jump lest
else:
    jump magaz

label newscene_1:
    
    stop sound fadeout 2
    
    show gg_smile_1 with ddp2
    show overlay onlayer  say with ddp2
    gg"- Ты нашел всех светлячков! Здорово!"
    hide gg_smile_1
    show gg_nerv_2
    gg"- Вроде бы..."
    $ zerk = True
    jump vse
    
label arxe:
    
    hide n
    
    $ change_cursor("no")
    
    $ renpy.movie_cutscene("end.mkv")
    
    pause 2
    
    $ achievement.grant("Achievement01_end1")
    init:
        $ achievement.register("Achievement01_end1")
        $ achievement.sync()

    $ achievement.sync()
    
    play music "audio/milk/milk41.mp3" fadein 25
    
    show nk
    
    $ renpy.pause(6, hard=True)
    
    hide nk
    
    show creditroll at Move((0.5, 0.0), (0.5, -9.2), 90,
                  xanchor=0.5, yanchor=0)
    $ renpy.pause(91, hard=True)
    
    
    
    $ change_cursor("milk")
    
    return


































