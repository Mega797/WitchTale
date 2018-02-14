##############################################################################
# Варка зелий
##############################################################################
init python:
    import string
    myItem = 0
    mySet = []
    voteDecision = False
    last_stage = 'stage1'
    usedIngredients = []
    failedIngredients = []
    def show_list_stage(type) :
        global myItem, currPotion, filteredEffect
        if not type in ['stage1','stage2','stage3']:
            type = 'stage1'
        list = []
        showed = []
        if type == 'stage1':
            currPotion = defaultPotion
        for x in player.inventory:
            if type == 'stage1' and x.id not in showed and x.type == 'food' and x not in usedIngredients:
                if intoxication in x.effects:
                    list += [x]
                    showed += [x.id]
            if type == 'stage2' and x.id not in showed and x.type == 'ingredient' and x not in usedIngredients:
                if filteredEffect == '':
                    if len(currPotion.mainEffect) == 0:
                        list += [x]
                        showed += [x.id]
                    elif currPotion.hasMainEffect(x) and x not in usedIngredients:
                        list += [x]
                        showed += [x.id]
                        
                elif filteredEffect in x.effects:
                    if len(currPotion.mainEffect) == 0:
                        list += [x]
                        showed += [x.id]
                    elif currPotion.hasMainEffect(x) and x not in usedIngredients:
                        list += [x]
                        showed += [x.id]
            if type == 'stage3' and x.id not in showed and x.type == 'ingredient' and x not in usedIngredients:
                if currPotion.hasAntiSubEffect(x.effects):
                    list += [x]
                    showed += [x.id]
        if len(list) > 0 :
            if not myItem in list :
                myItem = list[0]
        else :
            myItem = 0        
        return list
        
    def brew_action(item):
        if last_stage == 'stage1':
            return [Function(initPotion, item), AddToSet(usedIngredients, item), SetVariable('last_stage','stage2'), Function(clrscr), Show('brewing')]
        if last_stage == 'stage2':
            if len(currPotion.mainEffect) == 0:
                return [Show('mainEffectSelection', None, item)]
            else:
                if player.skills['alchemy'] > rand(1,101):
                    if len(usedIngredients) < 3:
                        return [Function(updatePotion, item), AddToSet(usedIngredients, item), SetVariable('last_stage','stage2'), Function(clrscr), Show('brewing')]
                    else:
                        return [Function(updatePotion, item), AddToSet(usedIngredients, item), SetVariable('last_stage','stage3'), Function(clrscr), Show('brewing')]
                else:
                    return [Function(player.removeItem, item), AddToSet(failedIngredients, item), Jump('brewingFail')]
        if last_stage == 'stage3':
            if player.skills['alchemy'] + 50 > rand(1,100):
                return [Function(cleanPotion, item), AddToSet(usedIngredients, item), SetVariable('last_stage','stage3'), Function(clrscr), Show('brewing')]
            else:
                return [Function(player.removeItem, item), AddToSet(failedIngredients, item), Jump('brewingFail')]


screen brewing:
    zorder 1
    modal True
    fixed :
        add 'images/events/brewing/bg.png'
        add 'images/bg.png'
    $ adj = ui.adjustment()
    fixed xpos 0.01 ypos 0.01:
        hbox :
            key "game_menu" action Function(move, curloc)
            textbutton _('Назад'):
                action [SetVariable('currPotion', defaultPotion),  SetVariable('last_stage','stage1'), Function(move, curloc)]
            textbutton _('Основа'):
                action [SensitiveIf(last_stage == 'stage1'), SetVariable('last_stage','stage1'), Function(clrscr), Show('brewing')]
            textbutton _('Варка'):
                action [SensitiveIf(currPotion != defaultPotion and len(usedIngredients) < 4), SetVariable('last_stage','stage2'), Function(clrscr), Show('brewing')]
            textbutton _('Дистилляция'):
                action [SensitiveIf(len(currPotion.mainEffect) > 0), SetVariable('last_stage','stage3'), Function(clrscr), Show('brewing')]
    python:
        tab_i = show_list_stage(last_stage)
        tab_cols = 7.0
        tab_rows = round(float(len(tab_i))/float(tab_cols) +0.45)
        tab_n = (tab_rows*tab_cols) - len(tab_i)
    side "c r":
        area (250, 90, 640, 650)
        frame xminimum 650 yminimum 650 xpos -10 ypos -10:
            null
        viewport:
            yadjustment adj
            mousewheel True
            grid tab_cols tab_rows:   
                xfill True
                spacing 10
                for x in tab_i:
                    imagebutton:
                        idle im.MatrixColor(im.FactorScale(x.picto,0.4), im.matrix.opacity(0.7))
                        hover im.MatrixColor(im.FactorScale(x.picto,0.4), im.matrix.opacity(1.0))
                        hovered [SetVariable('myItem', x)]
                        action brew_action (x)
                for i in range(int(tab_n)):
                    vbox:
                        null
        # bar adjustment adj style "vscrollbar"
        
    vbox xalign 0.88 yalign 0.15 xanchor 0.5 yanchor 0:
        text (currPotion.name)
        null height 10
        text('Потрачено ингредиентов: ' + str(len(usedIngredients)))
        null height 10
        text _('Усиление эффектов: ' + str(currPotion.mult)) 
        null height 10
        text _('Основной эффект:')
        # text _('DictSize ' + str(len(currPotion.mainEffect)))
        for x in currPotion.mainEffect:
            text ('- ' + x.name + ':' + str(currPotion.mainEffect.get(x))) style style.my_text
        if len(currPotion.mainEffect) == 0:
            text '- Нет' style style.my_text
        null height 10
        text _('Побочные эффекты:')
        for x in currPotion.subEffects:
            text ('- ' + x.name + ':' + str(currPotion.subEffects.get(x))) style style.my_text
        if len(currPotion.subEffects) == 0:
            text '- Нет' style style.my_text
        null height 10
        if len(currPotion.mainEffect) > 0 and len(currPotion.subEffects) == 0:
            textbutton _('Забрать'):
                action[Function(getPotion, currPotion), Function(move, curloc)]
            if checkAmount(5):
                textbutton _('Забрать x5'):
                    action[Function(getPotions, currPotion, 5), Function(move, curloc)]
            if checkAmount(10):
                textbutton _('Забрать x10'):
                    action[Function(getPotions, currPotion, 10), Function(move, curloc)]
            if checkAmount(25):
                textbutton _('Забрать x25'):
                    action[Function(getPotions, currPotion, 25), Function(move, curloc)]
            if checkAmount(100):
                textbutton _('Забрать x100'):
                    action[Function(getPotions, currPotion, 100), Function(move, curloc)]
                    
    if last_stage == 'stage2':
        vbox xalign 0.73 yalign 0.50 yanchor 0.5:
            $ displayedEffects = []
            textbutton 'Сбросить фильтр':
                action [SetVariable('filteredEffect',''), Function(clrscr), Show('brewing')]
                xminimum 200
            for item in player.inventory:
                if item.type == 'ingredient':
                    for effect in item.effects:
                        if effect.id not in displayedEffects:
                            textbutton effect.name:
                                action [If(filteredEffect != effect, true = SetVariable('filteredEffect',effect), false = SetVariable('filteredEffect','')), SelectedIf(filteredEffect == effect), Function(clrscr), Show('brewing')]
                                xminimum 200
                            $ displayedEffects.append(effect.id)
    use showItem

screen mainEffectSelection(item):
    zorder 2
    modal True
    add 'images/bg.png'
    frame xpos 0.5 ypos 0.5 xanchor 0.5 yanchor 0.5:
        vbox:
            text _('Выберите основной эффект зелья')
            for x in item.effects:
                textbutton (x.name + ':' + str(min(100,item.effects.get(x)))):
                    action [Function(setMainEffectPotion, x), AddToSet(usedIngredients, item), Function(updatePotion, item), Function(clrscr), Show('brewing')]
                    xpos 0.5
                    xanchor 0.5
                    
screen brewingFail:
    zorder 2
    modal False
    frame xpos 0.3 ypos 0.8 xanchor 0.5 yanchor 0.5:
        vbox:
            text('Я испортила ингредиент, пытаясь добавить его.')
            if showIncSkill == 1:
                $ temp = player.getSkill('alchemy')
                text('Но я учла свою ошибку и увеличила навык зельеварения до [temp]!')
    # Тут пауза!
    # on "show" action Hide("brewingFail")
                
    
label brewingFail:
    $ showIncSkill = 0
    show screen brewing
    if rand(0, player.getSkill('alchemy')) < 10:
        $ temp = player.getSkill('alchemy')
        $ player.incSkill('alchemy')
        $ showIncSkill = 1
        
    show screen brewingFail
    pause 3.0
    hide screen brewingFail
    call screen brewing
    
        