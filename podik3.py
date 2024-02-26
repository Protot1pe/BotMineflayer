
from javascript import require, On, Once, AsyncTask, once, off 
import random
from time import sleep
import asyncio






#смэрти/при заходе на сервер сообщение
deaths = ['За что?', 'Ненавижу тебя, кожанный ублюдок!!!!', 'Кто меня убил?', 'Я даже нормально ходить не могу, а вы меня убиваете :(((']
log = ['Всем привет! help - Все доступные комманды', 
       'Салам братья! help - Все доступные комманды', 'Ветер в радость, чифир в сладость! help - Все доступные комманды',
         'вечер в хату, господа! help - Все доступные комманды']
hi = ['Приветос!', 'Приветик', 'Здарова', 'Здаровчик', 'qq']


mineflayer = require('mineflayer')

"""options = {
    'port': 12346,
    'webPath': PATH,
    'express': EXPRESS,
    'app': APP,
    'http': HTTP,
    'io': IO,
    'startOnLoad': BOOLEAN,
    'windowUpdateDebounceTime': INT
  }

inventoryViewer(bot, options)"""


displayName = 'podik'

#данные о боте и сервере
bot =  mineflayer.createBot({

    'host':'localhost',
    'port':'12346',
    'master': 'mrshopa5',
    'username':'andreev9ivan15952g@myrambler.ru',
    'password':'6aw-sBF-LH5-f65',
    'version': '1.20.1',
    'auth': 'microsoft'
})


autoeat = require('mineflayer-auto-eat').plugin

bot.loadPlugin(autoeat)
pathfinder = require('mineflayer-pathfinder')

inventoryViewer = require('mineflayer-web-inventory')
inventoryViewer(bot)


"""autototem = require('mineflayer-auto-totem').plugin
bot.loadPlugin(autototem)
autototem(bot)"""



GoalFollow = pathfinder.goals.GoalFollow

GoalBlock = pathfinder.goals.GoalBlock



isFishing = False


On(bot, 'spawn')
def handle_arg(*args):
    print('Чарончик')
    movements = pathfinder.Movements(bot)

blockFinderPlugin = require('mineflayer-blockfinder')(mineflayer)



bot.loadPlugin(pathfinder.pathfinder)



mcData = require('minecraft-data')(bot.version)
movements = pathfinder.Movements(bot, mcData)


#нахождение руды
@On(bot, 'chat')
def chat(this, user, message, *args):
    if '#алмаз' in message: 
        block = bot.findBlock({
            'matching': mcData.blocksByName.diamond_ore.id,
            'maxDistance': 128,
            
        })
        if not block:
            bot.chat('Блок не найден!')

        else:
            print(block.position) 
            bot.chat('Нашел')   
            bot.equip(bot.registry.itemsByName.netherite_pickaxe.id, 'hand')
            bot.pathfinder.setMovements(movements)
            goal1 = GoalBlock(block.position.x, block.position.y, block.position.z)
            bot.pathfinder.setGoal(goal1, True)
            sleep(40) 
            bot.chat('#алмаз') 
        
            
    elif '#железо' in message:
        block = bot.findBlock({
            'matching': mcData.blocksByName.iron_ore.id,
            'maxDistance': 128,
        })
        if not block:
            bot.chat('Блок не найден!')

        else:
            print(block.position) 
            bot.chat('Нашел')   
            bot.equip(bot.registry.itemsByName.diamond_pickaxe.id, 'hand')
            bot.pathfinder.setMovements(movements)
            goal1 = GoalBlock(block.position.x, block.position.y, block.position.z)
            bot.pathfinder.setGoal(goal1, True)
            sleep(20) 
            bot.chat('#железо') 
        
    elif '#обломок' in message:
        block = bot.findBlock({
            'matching': mcData.blocksByName.ancient_debris.id,
            'maxDistance': 128,
        })
        
        if not block:
            bot.chat('Блок не найден!')

        else:
            print(block.position) 
            bot.chat('Нашел')   
            bot.equip(bot.registry.itemsByName.diamond_pickaxe.id, 'hand')
            bot.pathfinder.setMovements(movements)
            goal1 = GoalBlock(block.position.x, block.position.y, block.position.z)
            bot.pathfinder.setGoal(goal1, True)
            sleep(40) 
            bot.chat('#обломок') 
        
                

    

#следовать за игроком/перестать следовать за игроком
@On(bot, 'spawn')
def spawn(*args):
    mcData = require('minecraft-data')(bot.version)
    movements = pathfinder.Movements(bot, mcData)

    @On(bot, 'chat')
    def sled(this, user, message, *args):
        if user != displayName:
            if '#следуй за мной' in message:
                bot.chat('Хорошо, следую за вами!')
                

                player = bot.players[user]
                target = player.entity

                bot.pathfinder.setMovements(movements)
                goal = GoalFollow(target, 1)
                bot.pathfinder.setGoal(goal, True)
                
            elif '#хватит преследовать' in message:
                bot.chat('Вот мы и прибыли')
                player = bot.players[user]
                target = player.entity

                bot.pathfinder.setMovements(movements)
                goal = GoalFollow(target, 1)
                bot.pathfinder.setGoal(goal, False) 
            


#прийти домой
@On(bot, 'chat')
def chat(this, user, message, *args):
    if user and (user != displayName):
        if message == '#дом':
            x = -431 # переделать потом на координаты
            y = 150 # переделать потом на координаты
            z = -6023 # переделать потом на координаты
            bot.pathfinder.setGoal(pathfinder.goals.GoalNear(x, y, z))






@On(bot, 'chat')
def chat(this, user, message, slot, *args):
    if user and (user != displayName):
        if message == '#сундук':
           
            block = bot.findBlock({
            'matching': mcData.blocksByName.chest.id, # переделать потом на координаты
            'maxDistance': 128
            })
        
            print(block.position)

            pos0 = block.position

            if not block:
                bot.chat('Блок не найден!')

            else:
                bot.chat('Иду к сундуку!')
                bot.lookAt(pos0)
            
                bot.pathfinder.setMovements(movements)
                
                goal3 = GoalBlock(pos0.x, pos0.y, pos0.z)
            

                bot.pathfinder.setGoal(goal3, True)
                bot.lookAt(pos0)

                sleep(1)
                bot.openContainer(block)
                
                
                   
               
                   

            


                
@On(bot, 'chat')
def chat(this, user, message, block, *args):
   if user != displayName:
      if message == '#закрой':
          bot.chat('Ок')
          sleep(1)
          x = -443 # переделать потом на координаты
          y = 141# переделать потом на координаты
          z = -5998 # переделать потом на координаты
          bot.pathfinder.setGoal(pathfinder.goals.GoalNear(x, y, z)) #сделать так что бы он оходил на то место когда он был при написании комманды
          



#сменить слоты поочерёдно
@On(bot, 'chat')
def chat(this, user, message, slot, *args):
    if user and (user != displayName):
        if message == '#слот':
            
            bot.activateItem(False)
            bot.setQuickBarSlot(0)
            bot.chat('Вот первый слот')
            sleep(2)
            bot.setQuickBarSlot(1)
            bot.chat('Вот второй слот')
            sleep(2)
            bot.setQuickBarSlot(2)
            bot.chat('Вот третий слот')
            sleep(2)
            bot.setQuickBarSlot(3)
            bot.chat('Вот четвёртый слот')
            sleep(2)
            bot.setQuickBarSlot(4)
            bot.chat('Вот пятый слот')
            sleep(2)
            bot.setQuickBarSlot(5)
            bot.chat('Вот шестой слот')
            sleep(2)
            bot.setQuickBarSlot(6)
            bot.chat('Вот седьмой слот')
            sleep(2)
            bot.setQuickBarSlot(7)
            bot.chat('Вот восьмой слот')
            sleep(2)
            bot.setQuickBarSlot(8)
            bot.chat('Вот и девятый слот')
            
            
'''@On(bot, 'chat')           
def tossNext(this, user, message, slot, *args):
    if user and (user != displayName):            
        if message == '11':
            
            bot.setQuickBarSlot(0)
            bot.chat('Вот твой предмет')
            item = bot.inventory.items()[0]
            bot.tossStack(item, tossNext)'''
            


#дропнуть ВСЕ предметы из определённого слота
@On(bot, 'chat')
def tossNext1(this, user, message, slot, *args):
    if user and (user != displayName):
        """a = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10' , '11', '12', '13', 
             '14', '15', '16', '17', '37']"""
        b = [str(a) for a in range(0, 36)]
        a = b.copy()
        if message in a:
            if bot.inventory.items()[int(message) - 1] == None:
                bot.chat('Пусто')
                return
            else:
                 friend = bot.nearestEntity()
                 bot.lookAt(friend.position)
                 pos = friend.position
            
                 bot.pathfinder.setMovements(movements)
                 bot.pathfinder.setGoal(pathfinder.goals.GoalNear(pos.x, pos.y, pos.z))
                 bot.chat("Держи")
                 print(bot.inventory.items()[int(message) - 1])
                 
                 item = bot.inventory.items()[int(message) - 1]
                 bot.tossStack(item, tossNext1)
            if not friend:
                bot.chat("Братишка, ты где?")
                return
            
        
           
            
        
          
    




#узнать координаты бота/свои
@On(bot, 'chat')
def say_position(this, username, message, *args):
    if message == '#где ты':
        p = bot.entity.position
        bot.chat(f"Мои кординаты: {p.toString ()}")
    if message == '#где я':
        if username in bot.players:
            p = bot.players[username].entity.position
            bot.chat(f"Твои кординаты: {p.toString ()}")


            

#когда заходит бот/игрок
"""@On(bot, "playerJoined")
def playerJoined(this, player):
    print("joined", player)
    if player["username"] != bot.username:
        bot.chat(random.choice(hi)) # добавить ники"""
        




#кушать и узнать колво еды бота            
@On(bot, 'chat')
def eda(this, user,message, *args):
    if user != displayName:
        if '#еда' in message:
            
            bot.chat(f'Моя еда - {bot.food}')



#{bot.food}


#файт бота с игроками
@On(bot, "chat")
def attack(this, user, message, entity, *args):
    mcData = require('minecraft-data')(bot.version)
    movements = pathfinder.Movements(bot, mcData)
    if user != displayName:
        if '#сражайся со мной' in message:
            bot.chat('Тебе конец, щегол')
            bot.equip(bot.registry.itemsByName.netherite_sword.id, 'hand')
            player = bot.players[user]
            target = player.entity
            
            
            player = bot.players[user] #еслу указать никнейм то он будет бить того игрока с тем никнеймом
            
            goal = GoalFollow(target, 1)
            bot.pathfinder.setGoal(goal, True)
            

            for i in range(75):
                sleep(0.001)
                bot.setControlState('jump', True)
                sleep(0.1)
                bot.setControlState('jump', False)
                bot.attack(target)
                    
                
                bot.equip(bot.registry.itemsByName.netherite_sword.id, 'hand')
                
                '''if bot.health < 4:
                    
                    bot.equip(bot.registry.itemsByName.golden_apple.id, 'hand')
                    bot.activateItem()'''
                    
                    
@On(bot, "chat")
def attack(this, user, message, entity, *args):
    mcData = require('minecraft-data')(bot.version)
    movements = pathfinder.Movements(bot, mcData)
    if user != displayName:
        if '#турель' in message:
            bot.chat('Turrel')
            bot.equip(bot.registry.itemsByName.netherite_sword.id, 'hand')
            player = bot.players[user]
            target = player.entity
            
            
            player = bot.players[user] #еслу указать никнейм то он будет бить того игрока с тем никнеймом
            
           
            

            for i in range(80):
                sleep(0.01)
                bot.setControlState('jump', True)
                sleep(0.1)
                bot.setControlState('jump', False)
                bot.attack(target)
                    
                
                bot.equip(bot.registry.itemsByName.netherite_sword.id, 'hand')
                
                if bot.health < 6:
                    
                    bot.equip(bot.registry.itemsByName.golden_apple.id, 'hand')
                    bot.activateItem()                    
                    



            

            
        if message == "#хватит":
                target = bot.nearestEntity()
                bot.pathfinder.setMovements(movements)
                goal = GoalFollow(target, 1)
                bot.chat('ок :(')                 
                bot.pathfinder.setGoal(goal, False)
                            
                        
@On(bot, 'eat')
def eat(this, eat):
    if bot.eat < 17:
                    
        bot.equip(bot.registry.itemsByName.golden_apple.id, 'hand')
        bot.activateItem()



@On(bot, 'chat')
def time(this, user, message, *args):
    print(message)
    if message == "#время" or message == "#Время":
        bot.chat(f"Игровое время: " + str(bot.time.timeOfDay))

@On(bot, 'death')
def death(this):
    bot.chat(random.choice(deaths))




@On(bot, 'login')
def login(this):
    bot.chat('/login 123321')



@On(bot, 'chat')
def chat(this, user, message, *args):
    print(message)
    if message == "#Привет":
        bot.chat('Привет!')



@On(bot, "rain")
def rain(this):
    if bot.isRaining:
        bot.chat("Дождь пошел кажись")
    else:
        bot.chat('О, а вот уже и дождь закончился!')


@On(bot._client, 'sound_effect')
def sound_handler(this, packet, *args):
    global isFishing
    if isFishing == True:
        soundId = packet
        if soundId['soundId'] > 1500:
            bot.activateItem()
            isFishing = False
 
 
 
'''@On(bot, 'chat')
def msgHandler(this, user, message, *args):
    print(message)
    if message == 'fish':
        bot.equip(bot.registry.itemsByName.fishing_rod.id, 'hand')
        @AsyncTask(start=True)
        def fishing(task):
            global isFishing
            while True:
                if isFishing == False:
                    sleep(1)
                    bot.activateItem()
                    isFishing = True'''


@On(bot, 'chat')
def chat(this, user, message, *args):
    print(message)
    if message == '#quit':
        bot.quit()

@On(bot, 'chat')
def chat(this, user, message, *args):
    if message == '#тотем':
        
        bot.equip(bot.registry.itemsByName.totem_of_undying.id, 'off-hand')

@On(bot, 'chat')
def chat(this, user, message, *args):
    if message == '#скинь':
        item = bot.registry.itemsByName[bot.registry.itemsByName.totem_of_undying.id]
        if (item) in (bot.inventory.items()): 
            bot.chat('Ща сек')
            player = bot.players[user]
            target = player.entity
            bot.pathfinder.setMovements(movements)
            goal = GoalFollow(target, 1)
            bot.pathfinder.setGoal(goal, True)
        else:
            bot.chat("Такого предмета у меня нет")
                   

# @On(bot, "autototem")
# def physicsTick(this, totem):
#bot.autototem.equip(bot.registry.itemsByName.totem_of_undying.id, 'off-hand')



@On(bot, 'chat')
def chat(this, user, message, *args):
    if user and (user != displayName):
        if message == '#ферма':
            
            for i in range(1):
                x = -434 # переделать потом на координаты
                y = 150 # переделать потом на координаты
                z = -6011 # переделать потом на координаты
                bot.pathfinder.setGoal(pathfinder.goals.GoalNear(x, y, z))
                sleep(5)
                x = -435 # переделать потом на координаты
                y = 150 # переделать потом на координаты
                z = -6011
                bot.pathfinder.setGoal(pathfinder.goals.GoalNear(x, y, z))
                sleep(5)
                x = -433 # переделать потом на координаты
                y = 143 # переделать потом на координаты
                z = -6011
                bot.pathfinder.setGoal(pathfinder.goals.GoalNear(x, y, z))
                sleep(9)


@On(bot, 'chat')
def chat(this, user, message, *args):
    if user and (user != displayName):
        if '#иди на' in message:
            message = message[8:]
            message = message.split(' ')
            a = []
            for i in message:
                a.append(int(i))
            x, y, z = a
            
            bot.pathfinder.setGoal(pathfinder.goals.GoalNear(x, y, z))

@On(bot, 'chat')
def chat(this, user, message, *args):
    if user and (user != displayName):    
        if message == '#git':
            bot.chat("https://github.com/MrShopa5/BotMineflayer")      
            

while True:
    pass