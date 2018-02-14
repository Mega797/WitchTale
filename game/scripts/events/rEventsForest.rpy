label event_loc_forest_0_1:
    show expression 'images/events/forest/r1.png' as tempPic
    player.say '{color=#fff782}Прогуливаясь по лесу, я наткнулась на баронских солдат.'
    guard1 'Так так, кто это у нас тут?'
    guard2 'Да, кто это тут у нас?'
    guard1 'Опять нарушитель! Наверняка браконьер!'
    player.say 'Да не браконьер я... Я просто тут. Гуляю я тут, вот!'
    guard2 'Да, гуляют тут, а потом зайцы пропадают, кабаны убегают, да олени разбегаются. Налог надо заплатить!'
    guard1 'Да, налог на... - мне трудно разобрать лицо под шлемом, но бьюсь об заклад, что оно выражает чрезвычайную задумчивость.'
    guard2 'Налог за помятие травы! Помяла траву - зайцу нечего есть, заяц убежал в другой лес, в казне убыток. Убытки надо возмещать!'
    guard1 'Как возмещать будем? С такой красотки можем взять натурой!'
    guard2 'Хе-хе. Натурой, да!'
    menu:
        'Просто так убежать и запудрить им головы не получится. Будь их в два раза меньше, можно было бы попробовать... А так...'
        'Плеснуть в них зельем кровотечения и убежать' if player.hasElexir(bleeding):
            $ player.removeElexir(bleeding)
            show expression 'images/events/forest/r1_1.png' as tempPic
            player.say '{color=#fff782}Якобы потянувшись за деньгами, я плескаю в лица солдат зельем из бутылочки целясь в отверстия в шлеме. Пока они пытаются вытереть немедленно закровоточившие глаза, я скрываюсь в лесу.'
        'Плеснуть в них зельем паралича и убежать' if player.hasElexir(boostCure):
            $ player.removeElexir(boostCure)
            show expression 'images/events/forest/r1_1.png' as tempPic
            player.say '{color=#fff782}Якобы потянувшись за деньгами, я плескаю в лица солдат зельем из бутылочки, и, пока они пытаются преодолеть его эффект, скрываюсь в чаще.'
        'Выпить зелье скорости и убежать' if player.hasElexir(boost):
            $ player.removeElexir(boost)
            show expression 'images/events/forest/r1_1.png' as tempPic
            player.say '{color=#fff782}Я быстро выпиваю зелье скорости и сматываюсь от опешивших солдат.'
        'Заплатить налог (10 срубо)' if player.money >= 10:
            $ player.incMoney(-5)
            player.say '{color=#fff782}Негодуя, я отдала кровно заработанное, и в награду получила шлепок по заднице и пожелания доброго пути.'
        'Угрожать' if getPar(slaves,'loy') < -50:
            player.say 'Вы, видимо слабо представляете, с кем связываетесь. Во Флюссхофе я довольно широко известная личность. Может быть вы съебётесь, подобру - поздорову, пока свои яйца выблёвывать не начали?'
            guard1 'Ну всё, сучка! Ты огребаешь!'
            player.say '{color=#fff782}Я уже приготовилась к худшему, но подлетевший к разъярённому товарищу второй стражник, начал что-то быстро нашёптывать ему на ухо.'
            guard1 'Ты, вы, это... Мы не со зла, идите пожалуйста, госпожа! Не серчайте! глупые мы люди, чего с нас взять!'
            player.say '{color=#fff782}Баронские солдаты, постоянно кланяясь, поспешили отступить в направлении ближайшей дороги. Судя по стоящему треску ломающихся кустов, отступление скорее напоминало бегство.'
        'Умолять' if getPar(slaves,'loy') > 50:
            player.say 'Я простая травница, которая ищет никому из вас не нужные травы. У меня нечего взять. Я живу тут рядом, неподалёку от Флюссхофа. Вальда, может быть слышали?'
            guard2 'А, так это ты Вальда? Такая молоденькая? А я думал ты старуха какая! Иди конечно, и это, спасибо тебе, ты племянницу моей здорово помогла!'
            guard1 'Ты чё творишь, дурень?'
            guard2 'Вот когда твоя кровинушка от хвори поганой подыхать будет, вот тогда ты поймёшь!'
            guard2 'Идите, госпожа, не слушайте этого придурка!'
            player.say '{color=#fff782}Я пошла, оставляя ругающихся стражников за спиной.'
        'Отдаться':
            player.say 'У меня нет лишних денег...'
            guard1 'Ну тогда на колени и начинай отрабатывать! Только робу свою скинь, я вижу, что ты там прячешь пару отменных титек!'
            show expression 'images/events/forest/r1_2.png' as tempPic
            player.say '{color=#fff782}Чертыхаясь, я скинула робу и уселась на колени перед двумя херами, тычущимися мне в лицо.'
            guard2 'Давай, приступай уже!'
            menu:
                'Сосать изо всех сил.':
                    $ player.incCorr(5)
                    player.say '{color=#fff782}Из всех сил я начала отсасывать то первому, то второму. Я применяла все свои умения, чтобы довести обоих до оргазма, как можно быстрее. Ни на секунду я не оставляла мокрые от моих слюней члены без стимуляции. То я нежно подрачивала их ладошкой, то смачно облизывала головки, пытаясь высосать из них сперму. Наконец мужики не выдержали ласк и вознаградили меня бурными фонатанами семени, извергнувшихся из их членов.'
                    show expression 'images/events/forest/r1.png' as tempPic
                    guard1 'Не, молодца! Все бы так усердно налог платили!'
                    guard2 'Ага! Бывай, красавица!'
                'Филонить':
                    player.say '{color=#fff782}Я откровенно лениво посасывала стоящие передо мной члены, пока солдатам это не надоело.'
                    guard1 'Не, ну ты так до вечера ковыряться будешь!'
                    guard2 'Это точно! Два члена ртом ты никак не обслужешь! Но мы тебе поможем!'
                    show expression 'images/events/forest/r1_3.png' as tempPic
                    player.say '{color=#fff782}Стражник улёгся рядом со мной и, легко подхватив на руки, начал тыкаться своим членом в мою задницу.'
                    player.say 'Э-э-э-й! Куда ты его пытаешься вставить?'
                    guard2 'В то место, которое подлежит наказанию за плохую работу!'
                    player.say 'Стой! Я всё поняла! Я буду сосать хорошо, обещаю!'
                    guard2 'Конечно будешь! Только с хером в жопе! Вот так!'
                    player.say '{color=#fff782}Член солдата с трудом протиснулся в мою задницу, причинив к тому же неслабую боль. Ощутив, что он уже внутри, мужчина немедленно задвигал бёдрами, буквально выворачивая мой анус наизнанку.'
                    show expression 'images/events/forest/r1_4.png' as tempPic
                    player.say 'А-а-а! - попыталась закричать я от боли, но мой открытый рот был немедленно заполнен петушком второго солдата. Я пыталась вырваться, но один крепко держал меня за бёдра, а второй за голову. Я чувствовала себя игрушкой в их руках.'
                    guard1 'Чёт она вообще ртом работать перестала! Совсем охерела девка! Ну ка, Карл, подвинься. Подвинься, Карл!'
                    show expression 'images/events/forest/r1_5.png' as tempPic
                    player.say '{color=#fff782}Карл со второго раза понял, чего хочет его напарник и прижал меня к своей груди. Второй стражник немедленно примостился передо мной, направляя член во влагалище.'
                    player.say 'Стой! Ты не можешь...'
                    guard1 'Ты глубоко ошибаешься, я могу!'
                    show expression 'images/events/forest/r1_6.png' as tempPic
                    player.say '{color=#fff782}Сразу два члена заполнили мои внутренности. По ощущениями это было похоже, словно меня посадили сразу на два кола и дёргают ими внутри, разрывая напополам. Не уверена забыла ли я или просто потеряла сознание в тот момент, но когда я очнулась, было уже поздно. Всё моё тело нестерпимо болело и особенно те места между ног. Я с трудом добралась до дома.'
                    $ player.incDirty(5)
                    $ player.incPrana(-15)
                    $ hour = 22
                    $ move('loc_home')
    $ move(curloc)
    
label event_loc_forest_0_2:
    show expression 'images/events/forest/r2.png' as tempPic
    player.say '{color=#fff782}Издалека я услышала голоса и хохот. Подкравшись поближе, я заметила трёх мужчин явно бандитского вида, которые докапывались до странно выглядевшей женщины.'
    player.say 'Да, бедная девушка. Будет удивительно, если она доберёться сегодня до дома живой.'
    player.say '{color=#fff782}Я ничем не могу помочь ей, и оставаться тут дольше опасно. Поспешно собравшись, я пошла в противоположную от инцедента сторону.'
    $ move(curloc)
    
label event_loc_forest_0_3:
    show expression 'images/events/forest/r3.png' as tempPic
    player.say '{color=#fff782}Гуляя по лесу, я слегка заблудилась. Да к тому же опустился страшный туман. Мне стоило больших трудов вновь выйти на знакомую местность. К сожалению, я потеряла много времени на это.'
    $advancetime(1)
    $ move(curloc)
    
label event_loc_forest_0_4:
    show expression 'images/events/forest/r4_1.png' as tempPic
    player.say '{color=#fff782}Я наткнулась на палатку то ли охотницы, то ли друидки. У неё были весьма странные черты лица и олени её совсем не боялись. К счастью, она меня не заметила, продолжая заниматься своими "друидскими" делами между ног. Интересно, стоит ли мне здесь задержаться, и проверить её палатку, или просто уйти?'
    menu:
        'Осмотреть палатку':
            if rand(1,5) == 1:
                player.say '{color=#fff782}Я нашла немного ингредиентов!'
                python:
                    for x in range(1,5):
                        player.addItem(choice(ingHunter))
            else:
                player.say '{color=#fff782}Я впустую потратила время, перерывая вещи женщины. К счастью, она была слишком занята, чтобы заметить меня.'
            $changetime(60)
        'Подсматривать':
            $ changetime(60)
            $ player.incCorr(1)
            show expression 'images/events/forest/r4_2.png' as tempPic
            player.say '{color=#fff782}Женщина использовала то ли какую-то кость, то ли бивень животного, водя им по намокшим губам своей щели. Вы ожидали услышать какие то вздохи или стоны, но до вас доносился только какой-то речитатив. Учитывая, что олень рядом даже и не думал убегать, возможно женщина как то его гипнотизировала? Я решила не рисковать быть обнаруженной или загипнотизированной этой странной дамой, и поспешила удалиться.'
            $ changetime(20)
        'Уйти':
            player.say '{color=#fff782}И чего я там не видела? - подумалось мне, и, не теряя времени, я ушла.'
    $ move(curloc)
    
label event_loc_forest_0_5:
    show expression 'images/events/forest/r5.png' as tempPic
    player.say '{color=#fff782}Гуляя по лесу, я наткнулась на древнюю плиту в прудике, от которой буквально фонило Изнанкой. Взяв себя в руки, я разделась и устроилась на плите поудобней. Несмотря на тёплую погоду и воду, моё тело покрылось мурашками от пронзающего меня потока силы. Собрав волю в кулак я продолжала сидеть, впитывая эманации другой стороны, пока не почувствовала, что полна.'
    player.say 'Надо собираться, - сказала я себе, поспешно подплывая к берегу и одеваясь. Странно, но через 5 минут, как я ушла, я совершенно забыла как вернуться в это место снова. Может мне повезёт ещё раз наткнуться на это святилище?'
    $ player.incMana(100)
    $ changetime(60)
    $ move(curloc)
    
label event_loc_forest_0_6:
    show expression 'images/events/forest/r6.png' as tempPic
    player.say '{color=#fff782}Я встретила лису на полянке. Удивительно, но это хитрое животное не замечало меня.'
    menu:
        'Попробовать эмпатию':
            if player.getSkill('empathy') > rand(0,100):
                $ player.incSkill('empathy')
                player.say '{color=#fff782}У меня ничего не вышло... Но зато навык слегка увеличился.'
            else:
                show expression 'images/events/forest/r6_2.png' as tempPic
                player.say '{color=#fff782}Мне удалось подойти к лисице, усыпив её бдительность своим умением. Правда мне пришлось встать на четвереньки, чтобы не было ассоциации с человеком. Немного попрыгав вокруг меня, зверёк убежал охотиться на зайцев, лизнув меня на прощание в нос.'
            $ changetime(60)
        'Уйти':
            player.say '{color=#fff782}Не желая терять времени, я просто развернулась и ушла'
    $ move(curloc)
    
label event_loc_forest_0_7:
    show expression 'images/events/forest/r7.png' as tempPic
    player.say '{color=#fff782}Я увидела нескольких волков, только что заваливших оленя и выяснявших отношения между собой.'
    menu:
        'Подождать, пока они уйдут и собрать остатки':
            player.say '{color=#fff782}Я решила подождать, пока волки насытятся и собрать полезные ингредиенты после их трапезы. Время текло так медленно, как никогда в жизни. Близость к опасным хищникам заставляло моё сердце биться всё быстрее и быстрее, благо что хоть ветер дул в мою сторону, скрывая мой запах.'
            player.say '{color=#fff782}Спустя продолжительное время волки наконец насытились и ушли, позволив мне собрать всё, что осталось. Я правда, не уверена, что это стоило потраченного времени.'
            python:
                for x in range(1,15):
                    player.addItem(choice(ingHunter))
                advancetime(1)
        'Уйти':
            player.say '{color=#fff782}Не желая рисковать, я поспешно скрылась в ближайших кустах, стараясь не потревожить ни одну веточку, чтобы не привлечь хищников.'
    $ move(curloc)
    
label event_loc_forest_0_8:
    $ s1 = getChar()
    show expression 'images/events/forest/r8.png' as tempPic
    player.say '{color=#fff782}Мне страшно приспичило сходить в туалет... Ненормально сильно, видимо недавно съеденная курятина была не первой свежести... Надо либо выпить что-то от поноса, либо сходить под деревце.'
    menu:
        'Выпить зелье' if player.hasElexir(diareaCure):
            $ player.removeElexir(diareaCure)
            player.say '{color=#fff782}Быстро вынув пробку, я опустошила бутылочку одним глотком. Мне сразу полегчало и я продолжила свой путь.'
        'Сходить в кусты':
            $ changetime(30)
            show expression 'images/events/forest/r8_1.png' as tempPic
            player.say '{color=#fff782}Оставив робу на ближайшей ветке, я пристроилась под берёзой и с наслаждением опорожнила свой кишечник. По лесу начала разноситься нездоровая вонь.'
            show expression 'images/events/forest/r8_2.png' as tempPic
            player.say '{color=#fff782}Вытерев задницу лопушком, что рос неподалёку, я уже собиралась вставать, как вдруг...'
            show expression 'images/events/forest/r8_3.png' as tempPic
            guard1 'Так так, кто это у нас тут загрязняет своим дерьмом баронские леса? Такая вонища стоит, что дерево явно подохнет от твоих испражнений, рыжая!'
            player.say '{color=#fff782}Шокированная внезапным появлением стражника в этой глуши, я прикрыла срамные места руками, молясь, чтобы он наконец отстал от меня.'
            guard1 'Ну что молчишь то, рыжая? Платить за ущерб будем, или нет? Портить деревья в баронском лесу никому не дозволяется!'
            menu:
                'Заплатить налог (5 срубо)' if player.money >= 5:
                    $ player.incMoney(-5)
                    player.say '{color=#fff782}Негодуя, я отдала кровно заработанное, и в награду получила шлепок по заднице и пожелания доброго пути.'
                'Угрожать' if getPar(slaves,'loy') < -50:
                    $ s1.incLoy(-10)
                    player.say 'Как меня заебал и ваш барон, и его тугоумные выродки. Может ты, блядь, не в курсе, но я - Вальда Сибель, и при упоминании этого имени в соседней деревни срутся даже нищие, которые не жрали последние 5 дней. Причём делают это обильно и не снимая портков! И если ты не хочешь пополнить и без того многочисленные ряды прокажённых, стоящих у входа в вашу сраную церковь, будь добр, подай мне робу, и постарайся забыть нахуй, как я без неё выгляжу, понял?'
                    player.say '{color=#fff782}Мне не было видно лицо этого остолопа, но судя по тому, как затряслись его руки, потянувшиеся, чтобы подать мне робу, имя моё он слышал... Приятно всё таки иметь хоть какую-то репутацию. Пусть даже и не самую хорошую.'
                'Умолять' if getPar(slaves,'loy') > 50:
                    $ s1.incLoy(10)
                    player.say 'Не хотела я вредить лесу, честное слово! Да и не повредила я никак. На этом месте и травы гуще расти будут, и насекомым пища, а раз насекомых больше, то и птицы прилетят. Так что я ещё хорошо лесу сделала! Я ведь простая травница, Вальда, может слышали?'
                    guard1 'Так, рыжая, живёт в хижине, травница. Да, слышал. Многие хорошо о тебе отзывались. Ладно, что же я изверг какой? Но есть у  меня одна проблемка, слушай.'
                    player.say '{color=#fff782}Я выслушала банальную проблему любого стареющего мужчины, посоветовала ему пару травок и спокойно отправилась дальше.'
                'Отдаться':
                    $ player.incCorr(3)
                    player.say 'Я не могу себе позволить заплатить такие деньги...'
                    'Вальда потупила взор, ожидая решения стража. Ну не убьёт же он её в самом деле.'
                    guard1 'Так, ну раз нет денег, возьму натурой. Задницей твоей засранной я сегодня побрезгую, но ртом поработать придётся! И смотри, не укуси! А быстро клинком рёбра пересчитаю!'
                    show expression 'images/events/forest/r8_4.png' as tempPic
                    'Без лишних слов, стражник скинул с себя доспехи, и засунул свой небольшой член во влажный рот Вальды, едва доставая до глотки.'
                    guard1 'Давай, рыжая сучка, поработай язычком, ублажи папочку!'
                    player.say 'Тфы мфе ме пфапфа! - яростно промычала Вальда с забитым ртом.'
                    guard1 'Да, детка, разговаривай побольше! Твой язычок делает волшебные вещи! Тебе стоит обратится в местную таверну и зарабатывать им!'
                    player.say 'Фукин фын!'
                    guard1 'Вот так, крошка, не останавливайся, сейчас я дам тебе сладенького молочка!'
                    player.say '{color=#fff782}Его член напрягся у меня во рту, бёдра подались вперёд, и густой поток полился в мою глотку и желудок. Задыхаясь, я начала отталкивать его, но его руки только сильнее схватили меня за волосы, заталкивая хер всё глубже.'
                    show expression 'images/events/forest/r8_5.png' as tempPic
                    'В конце концов, пытка закончилась, и удовлетворённый стражник быстро набросил свои доспехи и скрылся в лесу, оставив Вальду с заляпанным спермой лицом и телом.'
                    $ player.incDirty(5)
    $ move(curloc)
    
label event_loc_forest_0_9:
    if trigger[24] == 0:
        $ trigger[24] = 1
        show expression 'images/events/forest/r9.png' as tempPic
        player.say '{color=#fff782}Я наткнулась на двух стражников. Точнее на стражника и стражницу. Последняя была одета весьма фривольно для своей должности. Я бы сказала, что если бы не шлем, я бы не смогла отличить её от портовой шлюхи.'
        guard1 'Так как ты говоришь, ты получила это место работы?'
        guard3 'А тебе всё скажи, Карл... Сам то как думаешь, приятно день деньской стирать чьи то портки и нянчить орущих детей? Или может быть приятней расставлять ноги перед всяким отребьем, чтобы было чем набить брюхо на ночь? Я поступила умнее...'
        guard1 'Раздвинула ноги перед начальником стражи?'
        guard3 'Ах, было бы там перед чем раздвигать! Но в целом да, я считаю, что это более удачная судьба, чем у большинства деревенских баб.'
        guard1 'Ну хоть драться то ты умеешь, Кристина?'
        guard3 'Да нахера мне, Карл? Ты то у меня на что такой большой... И сильный...'
        'Рука стражницы осторожно опустилась на гульфик кольчужных доспехов...'
        player.say '{color=#fff782}Так, я знаю к чему это ведёт, нужно сваливать, пока меня не заметили и не назначили какой нить дебильный штраф за порчу травы.'
    elif trigger[24] == 1:
        $ trigger[24] = 2
        show expression 'images/events/forest/r9_1.png' as tempPic
        $ player.incLust(10)
        guard3 'Да, Карл, еби меня! Еби свою сучку, как в последний раз! Спаси меня своим хером от одиночества, да!!!'
        player.say '{color=#fff782}Издалека услышав сладострастные крики, я направилась к месту их происхождения, с небольшим удивлением обнаружив там знакомых мне стражников Карла и Кристину, которые яростно совокуплялись прямо на земле под берёзой. Член Карла неистово долбил узкую щёлку Кристины, от чего та верещала на весь лес.'
        guard3 'Да! Да! Это ты должен стать капитаном стражи, а не тот дряхлый импотент! Трахай меня, мой капитан, не останавливайся!'
        guard1 'Да, сучка! Я покажу тебе кто тут главный! Твоя щель запомнит мой хер надолго, и другого не захочется! Я, блядь сам стану капитаном и выебу этого Кая вместо тебя!'
        guard3 'Да! Мы выебем его вместе! Сегодня! Но сначала отрежем голову этому старому импотенту!'
        player.say '{color=#fff782}Мда, это выглядит ещё отвратительней, чем я думаю...'
    elif trigger[24] == 2:
        $ trigger[24] = 3
        show expression 'images/events/forest/r9_2.png' as tempPic
        player.say '{color=#fff782}Мда. Видимо "дряхлый импотент" оказался куда круче и умнее этих двоих...'
        'Вальда стояла перед телами двух стражников, проткнутых их же мечами. Приподняв шлем женщины, она убедилась, что перед ней Кристина, возлюбленная Карла. Похоже, что взятие поста капитана стражи пошло явно не так, как задумывалось этими двумя. Ну да единый им судья. Порывшись в куче одежды рядом, Вальда смогла обнаружить небольшую горстку монет и бутылку вина.'
        $ player.addItem(wine)
        $ player.incMoney(15)
        $ changetime(30)
    else:
        $ skipEvent()
    $ move(curloc)
    
label event_loc_forest_0_10:
    show expression 'images/events/forest/r10.png' as tempPic
    player.say '{color=#fff782}Я наткнулась на мёртвого волка, придавленного упавшим деревом. Возможно он был слишком стар, а может быть не слишком везуч, раз закончил свою жизнь подобным образом. Не желая упускать момент, я вырезала у него глаза и положила в свою суму. '
    python:
        for x in range(1,2):
            player.addItem(wolfEye)
    $ changetime(30)
    $ move(curloc)
    
label event_loc_forest_0_11:
    show expression 'images/events/forest/r11.png' as tempPic
    player.say '{color=#fff782}Я нашла под берёзой тело то ли солдата, то ли мародёра, умершего от потери крови. Две стрелы пробили его фактически насквозь, не оставляя шансов пережить подобное ранение.'
    menu:
        'Можно вырезать ему сердце, которое является ценным продуктом в алхимии, но если тело найдут, у меня могут быть проблемы...'
        'Вырезать сердце':
            if rand(1,3) == 1:
                $ getChar().incLoy(-100)
            $ player.addItem(heartHuman)
            $ player.incDirty(2)
            'Склонившись над несчастным с ножом, я взрезала ему живот под рёбрами, и, тихо матерясь, вытащила сердце.'
            $ changetime(30)
        'Не трогать':
            'Решив не трогать без нужды останки безвременно усопшего, я отошла и продолжила свой путь.'
    $ move(curloc)
    
label event_loc_forest_0_12:
    show forest as tempPic
    $ s1 = getChar('female','young')
    $ alignment = getAlignment(s1).lower()
    menu:
        'Вдалеке я услышала женские крики и волчий лай.'
        'Пойти посмотреть':
            show expression 'images/events/forest/r12.png' as tempPic
            player.say '{color=#fff782}Выглядывая из ближайших кустов, я увидела, как [s1.fname] отбивается от пары волков с помощью небольшого кинжала. Я вспомнила, что она [alignment].'
            menu:
                'Попытаться заворожить волков':
                    $ s1.incLoy(50)
                    $ player.incMoney(rand(5,15))
                    $ changetime(30)
                    if player.getSkill('empathy') < rand(0,100):
                        $ player.incSkill('empathy')
                        $ player.applyEffects({bleeding:25})
                        show expression 'images/events/forest/r12_1.png' as tempPic
                        player.say '{color=#fff782}Мне не удалось заворожить лесных бестий, и вожак повалил меня на землю. Благо, отбиваясь, я умудрилась попасть ему по яйцам, так что храбрый волчара заскулив, убежал в лес, уводя за собой свою свору. [s1.fname] сердечно поблагодарила меня, и дала все срубо, что у неё были с собой за своё спасение. К сожалению, волк успел один раз куснуть меня, и моя роба начала медленно пропитываться кровью.'
                    else:
                        show forest as tempPic
                        player.say '{color=#fff782}Волки успешно поддались моему искусству эмпатии, и, мгновенно успокоившись, ушли глубже в лес. [s1.fname] сердечно поблагодарила меня, и дала все срубо, что у неё были с собой за своё спасение.'
                    $ player.money += rand(15,50)
                'Ждать':
                    $ changetime(30)
                    $ s1.incLoy(-100)
                    $ slaves.remove(s1)
                    show expression 'images/events/forest/r12_2.png' as tempPic
                    player.say '{color=#fff782}С содроганием я смотрела, как волки повалили девушку и перегрызли ей горло, разорвав попутно всю одежду. Вся трава была покрыта ярко алой кровью, толчками вырывавшейся из порванной аорты. Как только последняя судорога пробежала по телу несчастной, волки потеряли всякий интерес, и скрылись в лесу. Я подошла поближе.'
                    $ player.incMoney(rand(5,15))
                    menu:
                        'Обыскать и уйти':
                            'Отыскав в кровавой траве кошель девушки, Вальда забрала его и быстро покинула полянку.'
                        'Вырезать сердце':
                            $ player.addItem(heartHuman)
                            $ changetime(30)
                            show expression 'images/events/forest/r12_3.png' as tempPic
                            'Взрезав живот в районе желудка, Вальда, засучив рукав, просунула руку внутрь в поисках сердца.'
                            player.say 'Фу, дрянь какая!'
                            player.say '{color=#fff782}Спустя некоторое время мне удалось освободить молодое сердце от прежнего его обиталища и поместить в свою суму. Наверное, стоит побыстрее покинуть это место.'
        'Постараться оказаться подальше от шума':
            if rand(1,3) == 1:
                $ slaves.remove(s1)
            player.say '{color=#fff782}Я решила не рисковать, и пошла подальше от тревожного шума.'
    $ move(curloc)