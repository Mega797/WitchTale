label event_loc_tavern_0_1:
    $ player.incLust(5)
    $ s1 = whore
    show expression 'images/events/tavern/r1.png' as tempPic
    player.say '{color=#fff782}Местная шлюха, за пару звонких срубо, подрачивала член заезжему наёмнику прямо в углу общего зала. Он радостно хрюкал каждый раз, когда маленькая ладошка оттягивала крайнюю плоть с его члена, обнажая розовую головку.'
    if trigger[29] == 0:
        $ trigger[29] = 1
        merc 'Слышь, подруга, а может быть рот возьмёшь, вон он у меня как стоит и тебя хочет!'
        s1.say 'За две монеты можешь сам у себя в рот взять! Вот когда разбогатеешь - обращайся. Я вообще не понимаю, зачем ты меня попросил себе подрочить, у самого что ли рук нет?'
        merc 'Не верещи, малая! Мои руки под молот заточены, а не под хуй! С такими мозолями мне до него дотрагиваться то страшно, не то что дрочить!'
        s1.say 'Бедненький, как же ты по ветру то ходишь? - с показной заботой спросила Хуре, ни на секунду не прерывая движения своей ручки на здоровенном хере, - Небось все портки обоссаны?'
        merc 'Ой, заткнись уже, я тебе не за разговоры плачу! - его голова откинулась, глаза прикрылись и он начал слегка подрагивать, когда ладошка девушки касалась его головки.'
    konrad.say 'Слышь, Хуре, подойди ка сюда, как закончишь! - крикнул трактирщик из за своей стойки.'
    $ move(curloc)
    
label event_loc_tavern_0_2:
    if trigger[29] != 4:
        $ skipEvent()
    $ s1 = whore
    $ s2 = getChar('male','young')
    show expression 'images/events/tavern/ask.png' as tempPic
    player.say '{color=#fff782}У входа стояла Хуре и договаривалась с очередным клиентом.'
    s2.say 'Плачу 5 срубо, но я кончаю тебе в рот!'
    s1.say 'За 5 срубо, можешь сам себе в рот накончать, извращенец чёртов! Ещё раз заикнёшься, чёрных позову, они мигом тебя вразумят, греховное создание!'
    s2.say 'Ну ахереть, вот уж не думал встретить саму мать Терезу в образе шлюхи в деревенском трактире! Пошли уже!'
    s1.say 'А хер с тобой, всё равно других клиентов нет! - она схватила парня за руку, и повела в свою комнату, крикнув Конраду по дороге, - Я на 20 минут!'
    menu:
        'Пойти за ними':
            if math.fabs(getPar(slaves, 'loy')) < 30:
                show expression 'images/events/tavern/seeKonrad.png' as tempPic
                konrad.say 'Эй, куда это ты направилась, чертовка? Комната уже снята! Но, если ты хочешь посмотреть... В соседней комнате есть небольшое отверстие. И я готов сдать тебе эту комнату за 5 срубо на 5 минут!'
                menu:
                    'Заплатить' if player.money >= 5:
                        $ player.incMoney(-5)
                        player.say '{color=#fff782}Кинув на прилавок 5 монет, я отправилась в соседнюю комнату.'
                    'Уйти':
                        player.say 'Платить за то, чтобы посмотреть? Ищи дурака!'
                        $ move(curloc)
                $ player.incLust(15)
                show expression 'images/events/tavern/r2.png' as tempPic
                player.say '{color=#fff782}Широко расставив ноги и прикусив губу, Хуре смотрела на трахающего её крестьянина. В тишине комнаты раздавалось лишь пыхтение мужика и громкое хлюпанье поглощающей член вагины.'
                s2.say 'Что, нравится? - не прекращая пыхтеть, спросил [s2].'
                s1.say 'Что для тебя удовольствие, для меня - работа! - бросила Хуре, но по предательски прикушенная губа, капельки пота покрывавшее тело и раскрасневшаяся шея выдавали её враньё. Она получала откровенное удовольствие от таранящего её влагалище члена.'
                s2.say 'Ну так работай лучше, давай, подвигай задницей! - [s1] звонко шлёпнул по правой ягодице шлюхи.'
                player.say '{color=#fff782}Хуре подчинилась, и когда член начал входить в неё под разными углами, не сдержала громкого стона.'
                s2.say 'Вот так то! Давай! Нравится теперь тебе? - крестьянин начал увеличивать темп, то почти полностью вытаскивая своей елдак, то загоняя его обратно на полную длину.'
                s1.say 'Блядь, да! Еби меня! Твой хуй самый охуеннный! О боже, как хорошо! - женщина извивалась в наслаждении под мускулистым телом селянина.'
                s2.say 'Вот так, получай! - член мужика глубоко погрузился во влажные недра шлюхи, и выдал первую порцию спермы, - Ты стоишь каждого срубо, потраченного на тебя!'
                player.say '{color=#fff782}В этот момент в дверь постучался Конрад, возвещая о том, что время просмотра вышло.'
        'Остаться':
            pass
    $ move(curloc)
    
label event_loc_tavern_0_3:
    if trigger[29] != 4:
        $ skipEvent()
    
    $ s1 = whore
    $ s2 = getChar('male','old')
    show expression 'images/locations/tavern.png' as tempPic
    player.say '{color=#fff782}Из комнаты Хуре слышались громкие голоса и звуки скандала.'
    show expression 'images/events/tavern/r3.png' as tempPic
    s1.say 'То есть ты хочешь сказать, что трахал меня три часа в долг, только потому, что все деньги потратил на свою чудодейственную настойку, старый пердун? Получай! - ножка Хуре взлетела и впечаталась в сморщенную физиономию старика.'
    player.say 'Хм. Похоже от обильных совокуплений у кого то появилась неплохая растяжка... - тихо пробормотала я, глядя на хнычущего старика на полу.'
    $ move(curloc)
    
label event_loc_tavern_0_4:
    if trigger[29] != 4:
        $ skipEvent()
    $ s1 = whore
    $ s2 = getChar('male')
    show expression 'images/locations/tavern.png' as tempPic
    player.say '{color=#fff782}Хуре не было в зале, как обычно.'
    menu:
        'Проверить её комнату':
            if math.fabs(getPar(slaves, 'loy')) < 30:
                show expression 'images/events/tavern/seeKonrad.png' as tempPic
                konrad.say 'Эй, куда это ты направилась, чертовка? Комната уже снята! Но, если ты хочешь посмотреть... В соседней комнате есть небольшое отверстие. И я готов сдать тебе эту комнату за 5 срубо на 5 минут!'
                menu:
                    'Заплатить' if player.money >= 5:
                        $ player.incMoney(-5)
                        player.say '{color=#fff782}Кинув на прилавок 5 монет, я отправилась в соседнюю комнату.'
                    'Уйти':
                        player.say 'Платить за то, чтобы посмотреть? Ищи дурака!'
                        $ move(curloc)
                $ player.incLust(15)
                show expression 'images/events/tavern/r4.png' as tempPic
                s1.say 'Серьёзно, ты хочешь чтобы я ударила тебя по яйцам ногой? - недоверчиво спрашивала Хуре'
                perv 'Да, если это тебя не затруднит, моя госпожа! - заискивающим тоном проговорил извращенец.'
                s1.say 'Госпожа... Меня так никто не называл. Даже как то неудобно, ну да ладно, желание клиента - закон! - звонко сказала она и с размаху вмазала по яйцам мужика.'
                show expression 'images/events/tavern/r4_1.png' as tempPic
                perv 'Оу! Ах! Да! - яйца мужика смешно сплющились, но потом вернулись в прежнее состояние. Возбуждённый член подрагивал, глядя в потолок.'
                show expression 'images/events/tavern/r4.png' as tempPic
                s1.say 'Ещё? - с улыбкой спросила Хуре, водя ножкой по возбужденному стволу.'
                perv 'Да, если это вас не затруднит!'
                show expression 'images/events/tavern/r4_1.png' as tempPic
                'БАЦ!'
                perv 'А-а-а-а! Да! Ещё!'
                'БАЦ!'
                perv 'ЕЩЁ!'
                'БАЦ!'
                perv 'ДА!!!'
                show expression 'images/events/tavern/r4_2.png' as tempPic
                player.say '{color=#fff782}После очередного удара, член мужика задёргался, разбрызгивая вокруг белые капли.'
                s1.say 'Фу! Ну ты и даешь! - сказала Хуре, но её глаза расширились, когда первые струи начали покрывать её, наносящие удары, ножку.'
                player.say '{color=#fff782}В этот момент в дверь постучался Конрад, возвещая о том, что время просмотра вышло.'
        'Подождать':
            pass
    $ move(curloc)
    
label event_loc_tavern_0_5:
    if trigger[29] != 4:
        $ skipEvent()
    $ s1 = whore
    $ s2 = getChar('male','young')
    $ player.incLust(10)
    show expression 'images/events/tavern/r5.png' as tempPic
    player.say '{color=#fff782}Посреди общего зала разворачивалось необычное событие, обнажённая Хуре лежала на столе, а пьяный крестьянин готовился её трахнуть у всех на глазах.'
    s1.say 'Серьёзно, тут? Может быть всё таки пойдём в комнату? - пыталась вразумить шлюха пьяного мужика.'
    s2.say 'Я заплатил вперёд! Я сделаю это так, как хочу! Пусть все видят, что я мужик!'
    s1.say 'Да никто не сомневается, может быть пойдём? - сделала ещё одну попытку Хуре.'
    konrad.say 'Так, что за херня тут происходит? - Конрад вернулся из подвальчика и увидел происходящее.'
    s2.say 'Я заплатил 50 срубо и буду ебать её где захочу! - продолжать гнуть своё [s2]'
    konrad.say 'Он действительно заплатил столько? - обратился трактирщик к шлюхе. Та сокрушённо помотала головой.'
    konrad.say 'Да за такую цену можешь её хоть у меня на стойке выебать! - отрезал все пути к отступлению Конрад и, облокотившись на стойку, приготовился наслаждаться представлением. Многие посетители тоже отвернулись от своих столов, чтобы краем глаза взглянуть, как [s2] будет доказывать свою мужественность.'
    show expression 'images/events/tavern/r5_1.png' as tempPic
    player.say '{color=#fff782}[s2] не теряя больше времени, приставил свой член к влагалищу шлюхи, резко подался вперёд и полностью вошёл. Хуре послушно завела ноги на его спину, и нежно обняла. Вдруг она начала нестерпимо ржать, как лошадь.'
    s1.say 'Серьёзно? Ты уже кончил, "мужик"? Ах-ха-ха-ха! Ну как, всем всё доказал?'
    player.say '{color=#fff782}Из её киски действительно начала стекать выплёскиваемая членом сперма. [s2] густо покраснел, и попытался отстраниться.'
    s2.say 'Я требую свои деньги назад! - начал он было возмущаться, но Конрад резко осадил его сквозь хохот зала.'
    konrad.say 'Ты получил всё, что заказывал. Хуре трахнута, трахнута тобой, трахнута посреди зала. А теперь... - он сплюнул сквозь дыру меж передних зубов, - Съебал отсюда.'
    show expression 'images/locations/tavern.png' as tempPic
    player.say '{color=#fff782}Посрамлённый селянин поспешил скрыться с глаз долой.'
    $ move(curloc)
    
label event_loc_tavern_0_6:
    $ player.incLust(5)
    $ s1 = whore
    $ s2 = getChar('male', 'young')
    show expression 'images/events/tavern/r6.png' as tempPic
    ' Эротично двигаясь в своём зелёном платье, Хуре завлекала случайных клиентов. Один из которых, судя по всему уже был почти готов спустить в штаны, глядя на её изгибающееся в танце тело.\n
    - Эй! В моей таверне бесплатно дрочить запрещено! - гневно окликнул Конрад зазевавшегося крестьянина.\n
    - Что? Да ты не кипишуй, Конрад, просто хер зачесался! - невинно развёл руками селянин.\n
    - Знаю я вас, начешетесь херов, а потом на ровном месте поскальзываешься! Ты либо снимай её, либо иди нахер со своими почесушками!\n
    - Всё всё! Оставлю жене на сладкое! - холоп покорно спрятал руки за спину.'
    $ move(curloc)