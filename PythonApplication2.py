import telebot
import webbrowser
from telebot import types
import random
from random import choice

rand = ['Яичница','Манная каша','Английский завтрак','Яблочный пирог','Овсяноблин','Запеченые котлеты','Плов','Запеченые овощи','Паста с соусом песто','Драники из картошки с сыром','Оливье','Крабовый','Цезарь','С мятой и лаймом','С фетой и свеклой','Яичные блинчики','Шампиньоны','Сырные палочки','Мини-слойки','Рулетики из бекона','Чизкейк','Яблочный штрудель','Коржики молочные','Желе молочно-кофейное']

bot = telebot.TeleBot('7089392266:AAHIo7teieRgO0NPhaFkxjdzsS1mxkasf0I')

@bot.message_handler(commands=['start'])
def main(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    b1 = types.KeyboardButton('Рецепты')
    b6 = types.KeyboardButton('Рассчет')
    markup.add(b1,b6)
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}! Я бот по поиску рецептов🧑‍🍳\n\nПросто выбери категорию блюда, которое хочешь приготовить, и я помогу тебе найти подходящий рецепт.\n\nДавай готовить вместе!🥰\n\n\nЧТО УМЕЕТ БОТ❓\n\nБот может отправлять рецепты, а так же рассчитывать суточную норму калорий и ИМТ(индекс массы тела). Для того, чтобы получить рецепт нажмите "Рецепты", для получения рассчетов нажмите "Рассчет"\n\nСПИСОК КОМАНД:\n\n/start - Перезапустить бота\n/breakfast - Завтраки\n/main_dishes - Основные блюда \n/salads -салаты \n/snacks - Закуски \n/deserts - Десерты\n/random - Случайный рецепт\n/kkal - Рассчитать КБЖУ\n/imt - Рассчитать ИМТ\n/main_menu - Главное меню\n/menu - Меню с рецептами', reply_markup = markup)

def after_text(message):
    if len(message.text.split()) == 3:
        ves = "".join(message.text.split()[0])
        rost = "".join(message.text.split()[1])
        age = "".join(message.text.split()[2])
        if ves.isdigit() == True and rost.isdigit() == True and float(rost) != 0 and age.isdigit() == True:
            global itog
            itog = round(655.1 + 9.563 * int(ves) + 1.85 * int(rost) - 4.676 * int(age))
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)    
            b1 = types.KeyboardButton('1,2')
            b2 = types.KeyboardButton('1,375')
            b3 = types.KeyboardButton('1,55')
            b4 = types.KeyboardButton('1,7')
            b5 = types.KeyboardButton('1,9')
            b6 = types.KeyboardButton('Вернуться к выбору пола')
            markup.add(b1,b2,b3,b4,b5,b6)
            msg = bot.send_message(message.from_user.id, 'Выберите коэффициент физической активности, где:\n1,2 – минимальный (сидячая работа, отсутствие физических нагрузок);\n1,375 – низкий (тренировки не менее 20 мин 1-3 раза в неделю);\n1,55 – умеренный (тренировки 30-60 мин 3-4 раза в неделю);\n1,7 – высокий (тренировки 30-60 мин 5-7 раза в неделю; тяжелая физическая работа);\n1,9 – экстремальный (несколько интенсивных тренировок в день 6-7 раз в неделю; очень трудоемкая работа)', reply_markup = markup)
        else:
            bot.send_message(message.from_user.id, 'Некорректно введенные данные. Вернитесь на шаг назад!')
    else:
        bot.send_message(message.from_user.id, 'Введите три числа! Вернитесь на шаг назад и попробуйте снова.')

def after_text2(message):
    if len(message.text.split()) == 3:
        ves = "".join(message.text.split()[0])
        rost = "".join(message.text.split()[1])
        age = "".join(message.text.split()[2])
        if ves.isdigit() == True and rost.isdigit() == True and float(rost) != 0 and age.isdigit() == True:
            global itog
            itog = round(66.5 + 13.75 * int(ves) + 5.003 * int(rost) - 6.775 * int(age))
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)    
            b1 = types.KeyboardButton('1,2')
            b2 = types.KeyboardButton('1,375')
            b3 = types.KeyboardButton('1,55')
            b4 = types.KeyboardButton('1,7')
            b5 = types.KeyboardButton('1,9')
            b6 = types.KeyboardButton('Вернуться к выбору пола')
            markup.add(b1,b2,b3,b4,b5,b6)
            msg = bot.send_message(message.from_user.id, 'Выберите коэффициент физической активности, где:\n1,2 – минимальный (сидячая работа, отсутствие физических нагрузок);\n1,375 – низкий (тренировки не менее 20 мин 1-3 раза в неделю);\n1,55 – умеренный (тренировки 30-60 мин 3-4 раза в неделю);\n1,7 – высокий (тренировки 30-60 мин 5-7 раза в неделю; тяжелая физическая работа);\n1,9 – экстремальный (несколько интенсивных тренировок в день 6-7 раз в неделю; очень трудоемкая работа)', reply_markup = markup)
        else:
            bot.send_message(message.from_user.id, 'Некорректно введенные данные. Вернитесь на шаг назад!')
    else:
        bot.send_message(message.from_user.id, 'Введите три числа! Вернитесь на шаг назад и попробуйте снова.')
        
def after_text3(message):
        if len(message.text.split()) == 2:
            ves = "".join(message.text.split()[1])
            rost = "".join(message.text.split()[0])
            if ves.isdigit() == True and rost.isdigit() == True and float(rost) != 0:
                imt = float(ves)/(float(rost)*float(rost))
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)    
                b1 = types.KeyboardButton('К выбору рассчета')
                markup.add(b1)
                if imt <= 16:
                    bot.send_message(message.from_user.id, 'Выраженный дефицит массы тела')
                elif imt>16 and imt<=18.5:
                    bot.send_message(message.from_user.id,'Недостаточная (дефицит) масса тела', reply_markup = markup)
                elif imt>18.5 and imt<=25:
                    bot.send_message(message.from_user.id,'Норма', reply_markup = markup)
                elif imt>25 and imt<=30:
                    bot.send_message(message.from_user.id,'Избыточная масса тела (предожирение)', reply_markup = markup)
                elif imt>30 and imt<=35:
                    bot.send_message(message.from_user.id,'Ожирение первой степени', reply_markup = markup)
                elif imt>35 and imt<=40:
                    bot.send_message(message.from_user.id,'Ожирение второй степени  ', reply_markup = markup)
                elif imt>40:
                    bot.send_message(message.from_user.id,'Ожирение третьей степени (морбидное)', reply_markup = markup)
            else:
                bot.send_message(message.from_user.id, 'Некорректно введенные данные. Попробуйте еще раз.')
        else:
            bot.send_message(message.from_user.id, 'Введите два числа!')

@bot.message_handler(content_types=['photo'])
def photo(message):
    bot.reply_to(message, 'Вау😍Какое красивое фото! Вы молодец <3')

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == 'Рассчет' or message.text == 'К выбору рассчета':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)    
        b1 = types.KeyboardButton('КБЖУ')
        b2 = types.KeyboardButton('ИМТ')
        b3 = types.KeyboardButton('В главное меню')
        markup.add(b1,b2,b3)
        bot.send_message(message.from_user.id, 'Выберите интересующий вас рассчет', reply_markup = markup)

    elif message.text == 'В меню рецептов' or message.text == 'Рецепты' or message.text == '/menu':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        b1 = types.KeyboardButton('Завтраки')
        b2 = types.KeyboardButton('Основные блюда')
        b3 = types.KeyboardButton('Салаты')
        b4 = types.KeyboardButton('Закуски')
        b5 = types.KeyboardButton('Десерты')
        b6 = types.KeyboardButton('👀 Случайный рецепт')
        b7 = types.KeyboardButton('В главное меню')
        markup.add(b1,b2,b3,b4,b5,b6,b7)
        bot.send_message(message.from_user.id, 'Выберите интересующую вас категорию', reply_markup = markup)

    elif message.text == '👀 Случайный рецепт' or message.text == '/random':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        b3 = types.KeyboardButton(random.choice(rand))
        b4 = types.KeyboardButton('В меню рецептов')
        markup.add(b3, b4)
        bot.send_message(message.from_user.id, 'Ваш рецепт:', reply_markup = markup)

    elif message.text == 'КБЖУ' or message.text == 'Вернуться к выбору пола' or message.text == '/kkal':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)    
        b1 = types.KeyboardButton('Мужчина')
        b2 = types.KeyboardButton('Женщина')
        b3 = types.KeyboardButton('К выбору рассчета')
        markup.add(b1,b2,b3)
        bot.send_message(message.from_user.id, 'Выберите свой пол', reply_markup = markup)

    elif message.text == 'Женщина':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)    
        msg = bot.send_message(message.from_user.id, 'Введите через пробел три значения: свой вес в кг, свой рост в см и свой возраст (Пример: 65 170 21)', reply_markup = markup)
        bot.register_next_step_handler(msg, after_text)
    elif message.text == 'Мужчина':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)    
        msg = bot.send_message(message.from_user.id, 'Введите через пробел три значения: свой вес в кг, свой рост в см и свой возраст (Пример: 65 170 21)', reply_markup = markup)
        bot.register_next_step_handler(msg, after_text2)

    elif message.text == '1,2':   
        bot.send_message(message.from_user.id, 'Ваша суточкая норма калорий: '+str(round(1.2*itog))+'\n\nБЕЛКИ,ЖИРЫ И УГЛЕВОДЫ:\nДля похудения: 30-35% белки, 30-35% жиры, 30-40% углеводы;\nДля поддержания веса: 25-35% белки, 25-35% жиры, 40-50% углеводы;\nДля набора массы: 35-40% белки, 15-25% жиры, 40-60% углеводы.')
    elif message.text == '1,375':   
        bot.send_message(message.from_user.id, 'Ваша суточкая норма калорий: '+str(round(1.375*itog))+'\n\nБЕЛКИ,ЖИРЫ И УГЛЕВОДЫ:\nДля похудения: 30-35% белки, 30-35% жиры, 30-40% углеводы;\nДля поддержания веса: 25-35% белки, 25-35% жиры, 40-50% углеводы;\nДля набора массы: 35-40% белки, 15-25% жиры, 40-60% углеводы.')
    elif message.text == '1,55':   
        bot.send_message(message.from_user.id, 'Ваша суточкая норма калорий: '+str(round(1.55*itog))+'\n\nБЕЛКИ,ЖИРЫ И УГЛЕВОДЫ:\nДля похудения: 30-35% белки, 30-35% жиры, 30-40% углеводы;\nДля поддержания веса: 25-35% белки, 25-35% жиры, 40-50% углеводы;\nДля набора массы: 35-40% белки, 15-25% жиры, 40-60% углеводы.')
    elif message.text == '1,7':   
        bot.send_message(message.from_user.id, 'Ваша суточкая норма калорий: '+str(round(1.7*itog))+'\n\nБЕЛКИ,ЖИРЫ И УГЛЕВОДЫ:\nДля похудения: 30-35% белки, 30-35% жиры, 30-40% углеводы;\nДля поддержания веса: 25-35% белки, 25-35% жиры, 40-50% углеводы;\nДля набора массы: 35-40% белки, 15-25% жиры, 40-60% углеводы.')
    elif message.text == '1,9':   
        bot.send_message(message.from_user.id, 'Ваша суточкая норма калорий: '+str(round(1.9*itog))+'\n\nБЕЛКИ,ЖИРЫ И УГЛЕВОДЫ:\nДля похудения: 30-35% белки, 30-35% жиры, 30-40% углеводы;\nДля поддержания веса: 25-35% белки, 25-35% жиры, 40-50% углеводы;\nДля набора массы: 35-40% белки, 15-25% жиры, 40-60% углеводы.')
      
    elif message.text == 'ИМТ' or message.text == '/imt':
        msg = bot.send_message(message.from_user.id, 'Введите через пробел свой рост в метрах и вес в кг\n(Пример: 1.75 67)')
        bot.register_next_step_handler(msg, after_text3)

    elif message.text == 'В главное меню' or message.text == '/main_menu':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        b1 = types.KeyboardButton('Рецепты')
        b6 = types.KeyboardButton('Рассчет')
        markup.add(b1,b6)
        bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}! Я бот по поиску рецептов🧑‍🍳\n\nПросто выбери категорию блюда, которое хочешь приготовить, и я помогу тебе найти подходящий рецепт.\n\nДавай готовить вместе!🥰\n\n\nЧТО УМЕЕТ БОТ❓\n\nБот может отправлять рецепты, а так же рассчитывать суточную норму калорий и ИМТ(индекс массы тела). Для того, чтобы получить рецепт нажмите "Рецепты", для получения рассчетов нажмите "Рассчет"\n\nСПИСОК КОМАНД:\n\n/start - Перезапустить бота\n/breakfast - завтраки\n/main_dishes - основные блюда \n/salads -салаты \n/snacks - закуски \n/deserts - десерты\n/random - Случайный рецепт\n/kkal - Рассчитать КБЖУ\n/imt - Рассчитать ИМТ\n/main_menu - Главное меню\n/menu - Меню с рецептами', reply_markup = markup)


    #ЗАВТРАКИ
    if message.text == 'Завтраки' or message.text == '/breakfast':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)    
        b1 = types.KeyboardButton('Яичница')
        b2 = types.KeyboardButton('Манная каша')
        b3 = types.KeyboardButton('Английский завтрак')
        b4 = types.KeyboardButton('Яблочный пирог')
        b5 = types.KeyboardButton('Овсяноблин')
        b6 = types.KeyboardButton('В меню рецептов')
        photo = open(r'C:\Users\Юля\source\repos\PythonApplication2\фото/завтрак0.jpg', 'rb')
        markup.add(b1,b2,b3,b4,b5,b6)
        bot.send_photo(message.chat.id, photo=photo, caption = '«Как день начнешь, так его и проведешь» — это не только народная мудрость, но и настоятельный совет диетологов. Завтрак — едва ли не самый важный прием пищи. Он должен давать мгновенную энергию, длительную сытость и как минимум повышать настроение.\nПодборка рецептов завтраков на каждый день из простых продуктов с пошаговыми фото и инструкциями поможет сделать ваше утро особенным.\nВыберите рецепт и наслаждайтесь готовкой!', reply_markup = markup)

    elif message.text == 'Яичница':
        photo1 = open(r'C:\Users\Юля\source\repos\PythonApplication2\фото/яичница.jpg', 'rb')
        photo2 = open(r'C:\Users\Юля\source\repos\PythonApplication2\фото/яичница1.jpg', 'rb')
        photo3 = open(r'C:\Users\Юля\source\repos\PythonApplication2\фото/яичница5.jpg', 'rb')
        photo4 = open(r'C:\Users\Юля\source\repos\PythonApplication2\фото/яичница2.jpg', 'rb')
        photo5 = open(r'C:\Users\Юля\source\repos\PythonApplication2\фото/яичница3.jpg', 'rb')
        photo6 = open(r'C:\Users\Юля\source\repos\PythonApplication2\фото/яичница4.jpg', 'rb')
        bot.send_photo(message.chat.id, photo=photo1, caption = 'ЯИЧНИЦА С ВЕТЧИНОЙ И ГРЕНКАМИ\n\nВеликолепное в своей простоте блюдо для завтрака - вкусная яичница, дополненная обжаренными кубиками ветчины и белого хлеба.\n\nПРОДУКТЫ:\n\nЯйца куриные - 2 шт.\nХлеб тостовый - 50 г\nВетчина - 100 г\nМасло растительное - для обжаривания\nСоль - по вкусу\nСмесь молотых перцев - по вкусу')
        bot.send_photo(message.chat.id, photo=photo2, caption = 'Подготовить продукты для яичницы с ветчиной и гренками. Вместо ветчины можно использовать колбасу. Тостовый хлеб можно заменить обычным.')
        bot.send_photo(message.chat.id, photo=photo3, caption = 'С хлеба срезать корочки и нарезать небольшими кубиками. Ветчину тоже нарезать кубиками.')
        bot.send_photo(message.chat.id, photo=photo4, caption = 'В сковороде разогреть немного растительного масла и выложить нарезанный хлеб. Постоянно помешивая (или встряхивая сковороду), обжарить гренки до лёгкого золотистого цвета. Выложить к гренкам ветчину и обжарить вместе, чтобы ветчина тоже подрумянилась.')
        bot.send_photo(message.chat.id, photo=photo5, caption = 'Затем вбить яйца, стараясь не повредить желтки. Добавить соль и смесь молотых перцев. Жарить яичницу до желаемой готовности.')
        bot.send_photo(message.chat.id, photo=photo6, caption = 'Переложить готовую яичницу с гренками и ветчиной на тарелку и сразу же подавать к столу, пока не остыла. Приятного аппетита!')
        bot.send_message(message.chat.id, 'Как приготовите, пришлите мне фото готового блюда. Буду очень рад!🥰')

    elif message.text == 'Манная каша':
        photo1 = open(r'C:\Users\Юля\source\repos\PythonApplication2\фото/манка.jpg', 'rb')
        photo2 = open(r'C:\Users\Юля\source\repos\PythonApplication2\фото/манка1.jpg', 'rb')
        photo3 = open(r'C:\Users\Юля\source\repos\PythonApplication2\фото/манка2.jpg', 'rb')
        photo4 = open(r'C:\Users\Юля\source\repos\PythonApplication2\фото/манка3.jpg', 'rb')
        photo5 = open(r'C:\Users\Юля\source\repos\PythonApplication2\фото/манка4.jpg', 'rb')
        photo6 = open(r'C:\Users\Юля\source\repos\PythonApplication2\фото/манка5.jpg', 'rb')
        photo7 = open(r'C:\Users\Юля\source\repos\PythonApplication2\фото/манка6.jpg', 'rb')
        bot.send_photo(message.chat.id, photo=photo1, caption = 'БАНАНОВАЯ МАННАЯ КАША НА МОЛОКЕ\n\nКлассическая молочная манная каша без комочков - завтрак, любимый многими за свою питательность, нежность и воздушность. Благодаря маленькой хитрости манную кашу очень просто сварить без единого комочка, а добавление бананового пюре внесёт приятное разнообразие в привычный рецепт молочной каши и обогатит её вкус. Манная каша на молоке приобретает приятный фруктовый аромат и ярко выраженный вкус банана. Попробуйте и вы банановую манную кашу!\n\nПРОДУКТЫ\n\nМолоко - 250 мл\nБанан - 1 шт. (с кожурой - 230 г, вес мякоти - 150 г)\nКрупа манная - 50 г\nСахар - 40 г\nМасло сливочное - 20 г\nСоль - щепотка')
        bot.send_photo(message.chat.id, photo=photo2, caption = 'Подготовьте необходимые ингредиенты. Банан лучше всего брать спелый - он и слаще, и пюре из него получится более нежным и однородным. Количество сахара можно варьировать в зависимости от предпочтений. Также сахар и вовсе можно заменить мёдом или любым другим подсластителем по вкусу.')
        bot.send_photo(message.chat.id, photo=photo3, caption = 'В кастрюльку или сотейник пересыпьте манную крупу и добавьте кусочек сливочного масла. Поставьте на минимальный нагрев и, помешивая, прогрейте до того момента, пока масло не растопится, а манная крупа не станет похожа на мокрый песок. Всыпьте сахар и щепотку соли. Перемешайте.\nПомешивая, прогрейте смесь ещё минуту.')
        bot.send_photo(message.chat.id, photo=photo4, caption = 'Банан очистите от кожуры. Мякоть банана нарежьте кружочками или кубиками и переложите в миску.\nРазомните мякоть банана в пюре с помощью вилки.')
        bot.send_photo(message.chat.id, photo=photo5, caption = 'Получившееся банановое пюре переложите в сотейник. Тщательно перемешайте.')
        bot.send_photo(message.chat.id, photo=photo6, caption = 'Влейте молоко. Перемешайте.\nУвеличьте нагрев плиты до максимального и доведите смесь до кипения. Затем убавьте огонь до минимума и, помешивая, варите банановую манную кашу примерно 5 минут, до загустения.')
        bot.send_photo(message.chat.id, photo=photo7, caption = 'Банановая манная каша на молоке готова. Разложите её по тарелкам и подавайте к столу, по желанию украсив ломтиками банана, ягодами, кусочками фруктов или сухофруктов.\nПриятного аппетита!')
        bot.send_message(message.chat.id, 'Как приготовите, пришлите мне фото готового блюда. Буду очень рад!🥰')

    elif message.text == 'Английский завтрак':
        photo1 = open(r'C:\Users\Юля\source\repos\PythonApplication2\фото/англ5.jpg', 'rb')
        photo2 = open(r'C:\Users\Юля\source\repos\PythonApplication2\фото/англ2.jpg', 'rb')
        photo3 = open(r'C:\Users\Юля\source\repos\PythonApplication2\фото/англ3.jpg', 'rb')
        photo4 = open(r'C:\Users\Юля\source\repos\PythonApplication2\фото/англ4.jpg', 'rb')
        photo5 = open(r'C:\Users\Юля\source\repos\PythonApplication2\фото/англ1.jpg', 'rb')
        bot.send_photo(message.chat.id, photo=photo1, caption = 'КЛАССИЧЕСКИЙ АНГЛИЙСКИЙ ЗАВТРАК\n\nВ любом отеле подадут английский завтрак, который включает в себя обязательный набор: яйца, тост, сосиски, бекон и фасоль. Он считается самым вкусным и самым полезным. Чтобы на минуту почувствовать себя на отдыхе, не обязательно далеко ехать. Английский завтрак можно запросто сделать дома, потратив на это буквально 20 минут. Он включает в себя сытные и питательные продукты, благодаря которым насыщение не пройдет до самого обеда.\n\nПРОДУКТЫ:\n\nТостовый хлеб - 1 шт\nКуриное яйцо - 2 шт\nСосиски - 2 шт\nКонсервированная белая фасоль - 4 ст.л.\nСырокопченый бекон - 2 шт\nМасло подсолнечное - 1 ст.л.')
        bot.send_photo(message.chat.id, photo=photo2, caption = 'Необходимое количество продуктов достаньте из упаковок и разложите на столе так, чтобы все было под рукой.')
        bot.send_photo(message.chat.id, photo=photo3, caption = 'Обжарьте ингредиенты. Тост обжарьте на сухой сковороде или в тостере. Фасоль с небольшим количеством соуса прогрейте на среднем огне, помешивая, чтобы не пригорела. Отдельно обжарьте бекон до золотистого цвета. Сосиски опустите в кипящую воду на 2-3 минуты.')
        bot.send_photo(message.chat.id, photo=photo4, caption = 'Пожарьте яичницу. Глазунью жарьте на подсолнечном масле последней, так как яйца очень быстро остывают. Переложите ее на тарелку. Выложите рядом фасоль, сосиски, бекон и кусочек обжаренного тоста.')
        bot.send_photo(message.chat.id, photo=photo5, caption = 'Зерна кофе измельчите в кофемолке. Залейте в турке водой и сварите. Подайте свежесваренный кофе сразу после приготовления вместе с английским завтраком.')
        bot.send_message(message.chat.id, 'Как приготовите, пришлите мне фото готового блюда. Буду очень рад!🥰')

    elif message.text == 'Яблочный пирог':
        photo1 = open(r'C:\Users\Юля\source\repos\PythonApplication2\фото/пирог.jpg', 'rb')
        photo2 = open(r'C:\Users\Юля\source\repos\PythonApplication2\фото/пирог1.jpg', 'rb')
        photo3 = open(r'C:\Users\Юля\source\repos\PythonApplication2\фото/пирог2.jpg', 'rb')
        photo4 = open(r'C:\Users\Юля\source\repos\PythonApplication2\фото/пирог3.jpg', 'rb')
        photo5 = open(r'C:\Users\Юля\source\repos\PythonApplication2\фото/пирог4.jpg', 'rb')
        photo6 = open(r'C:\Users\Юля\source\repos\PythonApplication2\фото/пирог5.jpg', 'rb')
        bot.send_photo(message.chat.id, photo=photo1, caption = 'ЯБЛОЧНЫЙ ПИРОГ С ГЕРКУЛЕСОМ\n\nЯблочный пирог с геркулесом получается немного влажным, в меру сладким, ароматным и вкусным. Его можно назвать запеченной овсянкой, ведь за основу теста берутся геркулесовые хлопья. Добавьте изюм, любые другие сухофрукты, ягоды и специи, чтобы разнообразить текстуру и вкус. Сверху посыпьте пирог измельченными грецкими орехами или фундуком. Кстати, он получится вкусным даже в холодном виде, правда тогда он будет больше похож на печенье.\n\nПРОДУКТЫ:\n\nЯблоки - 500 г\nКокосовое масло - 2 ст.л.\nКуриное яйцо - 2 шт\nИзюм - 25 г\nФундук - 30 г\nОвсяные хлопья - 2 стакана\nСпеции - по вкусу')
        bot.send_photo(message.chat.id, photo=photo2, caption = 'Помойте яблоки и куриные яйца. Залейте изюм горячей водой на 10 минут. Затем слейте воду и обсушите изюм на бумажных полотенцах. Застелите форму для запекания пергаментом. Подготовьте блендер с чашей.')
        bot.send_photo(message.chat.id, photo=photo3, caption = 'Положите геркулес в чашу блендера. Измельчите его в мелкую крошку. Очистите яблоки от кожуры, нарежьте их на дольки, а также удалите сердцевину. После этого натрите яблоки на крупной терке.')
        bot.send_photo(message.chat.id, photo=photo4, caption = 'Смешайте в глубокой миске геркулес с куриными яйцами, яблоком, кокосовым маслом, солью, корицей и разрыхлителем.')
        bot.send_photo(message.chat.id, photo=photo5, caption = 'Добавьте в тесто изюм, хорошо перемешайте. Выложите тесто в форму для запекания ровным слоем. Разогрейте духовку до 180°С. Мелко покрошите фундук. Посыпьте пирог измельченными орехами и отправьте в разогретую духовку на 45 минут.')
        bot.send_photo(message.chat.id, photo=photo6, caption = 'Разрежьте пирог на порции. Перед подачей полейте десерт медом.')
        bot.send_message(message.chat.id, 'Как приготовите, пришлите мне фото готового блюда. Буду очень рад!🥰')

    elif message.text == 'Овсяноблин':
        photo1 = open(r'C:\Users\Юля\source\repos\PythonApplication2\фото/блин.jpg', 'rb')
        photo2 = open(r'C:\Users\Юля\source\repos\PythonApplication2\фото/блин1.jpg', 'rb')
        photo3 = open(r'C:\Users\Юля\source\repos\PythonApplication2\фото/блин2.jpg', 'rb')
        photo4 = open(r'C:\Users\Юля\source\repos\PythonApplication2\фото/блин3.jpg', 'rb')
        photo5 = open(r'C:\Users\Юля\source\repos\PythonApplication2\фото/блин4.jpg', 'rb')
        photo6 = open(r'C:\Users\Юля\source\repos\PythonApplication2\фото/блин5.jpg', 'rb')
        bot.send_photo(message.chat.id, photo=photo1, caption = 'ОВСЯНОБЛИН\n\nОвсяноблин не просто так рекомендуют готовить тем, кто придерживается правильного питания. Благодаря сложным углеводам в составе он надолго дает чувство сытости. Еще он богат белком, нужным для построения новых клеток организма, и клетчаткой, так необходимой для нормального пищеварения. Всего за 10 минут, проведенных у плиты, можно получить полезное блюдо. А еще оно очень вкусное.\n\nПРОДУКТЫ:\n\nКуриное яйцо - 2 шт\nОвсяные хлопья - 3 ст.л.\nМолоко - 1 ст.л.\nСыр - 30 г\nРастительное масло - 1 ст.л.\nСпеции - по вкусу')
        bot.send_photo(message.chat.id, photo=photo2, caption = 'Помойте куриные яйца. Отмерьте нужное количество всех ингредиентов.')
        bot.send_photo(message.chat.id, photo=photo3, caption = 'В миске взбейте куриные яйца с молоком, солью и перцем. Добавьте овсяные хлопья, перемешайте.')
        bot.send_photo(message.chat.id, photo=photo4, caption = 'Разогрейте на сковороде растительное масло. Влейте в сковороду яично-овсяную массу. Жарьте на среднем огне две минуты под крышкой.')
        bot.send_photo(message.chat.id, photo=photo5, caption = 'Нарежьте сыр тонкими ломтиками. Переверните овсяноблин на другую сторону. Положите на него ломтики сыра. Жарьте блюдо еще 2 минуты под крышкой.')
        bot.send_photo(message.chat.id, photo=photo6, caption = 'Смажьте овсяноблин творожным сыром. Положите на него кружочки помидоров и сложите пополам.')
        bot.send_message(message.chat.id, 'Как приготовите, пришлите мне фото готового блюда. Буду очень рад!🥰')

    #ОСНОВНЫЕ БЛЮДА
    elif message.text == 'Основные блюда' or message.text == '/main_dishes':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)    
        b1 = types.KeyboardButton('Запеченые котлеты')
        b2 = types.KeyboardButton('Плов')
        b3 = types.KeyboardButton('Запеченые овощи')
        b4 = types.KeyboardButton('Паста с соусом песто')
        b5 = types.KeyboardButton('Драники из картошки с сыром')
        b6 = types.KeyboardButton('В меню рецептов')
        markup.add(b1,b2,b3,b4,b5,b6)
        photo = open(r'C:\Users\Юля\source\repos\PythonApplication2\фото/осн.jpg', 'rb')
        bot.send_photo(message.chat.id, photo=photo, caption = 'Раздел "Основные блюда" предлагает широкий выбор рецептов для горячих блюд, которые удовлетворят ваши вкусовые предпочтения. Здесь вы найдете рецепты мясных и рыбных блюд, пасты, овощей и других вкусных комбинаций. Каждый рецепт сопровождается пошаговыми инструкциями, чтобы приготовление блюда было легким и приятным процессом.\nНасладитесь разнообразием вкусов и текстур, готовя основные блюда из этого раздела!', reply_markup = markup)

    elif message.text == 'Запеченые котлеты':
        photo1 = open(r'C:\Users\Юля\source\repos\PythonApplication2\фото/котлеты.jpg', 'rb')
        photo2 = open(r'C:\Users\Юля\source\repos\PythonApplication2\фото/котлеты1.jpg', 'rb')
        photo3 = open(r'C:\Users\Юля\source\repos\PythonApplication2\фото/котлеты2.jpg', 'rb')
        photo4 = open(r'C:\Users\Юля\source\repos\PythonApplication2\фото/котлеты3.jpg', 'rb')
        photo5 = open(r'C:\Users\Юля\source\repos\PythonApplication2\фото/котлеты5.jpg', 'rb')
        photo6 = open(r'C:\Users\Юля\source\repos\PythonApplication2\фото/котлеты4.jpg', 'rb')
        photo7 = open(r'C:\Users\Юля\source\repos\PythonApplication2\фото/котлеты6.jpg', 'rb')
        bot.send_photo(message.chat.id, photo=photo1, caption = 'ЗАПЕЧЕННЫЕ КОТЛЕТЫ В СМЕТАННОМ СОУСЕ\n\nУ котлет, запеченных в духовке, есть несколько преимуществ перед жареными. Без обжаривания в масле они будут более легкими для желудка, при этом не надо стоять у плиты и их переворачивать. А сметанный соус готовится сразу вместе с котлетами, пропитывая их и делая намного вкуснее. В качестве гарнира подойдет рис, гречка или овощной салат.\n\nПРОДУКТЫ:\n\nФарш из свинины и говядины - 400 г\nМолоко 2,5% жирности - 2 ст. л.\nБелый хлеб - 1 ломтик\nКуриное яйцо - 1 шт.\nЧеснок - 1 зубчик\nУкроп - 2 веточки\nЧерный перец молотый - 0.25 ч. л.\nСоль - 0.33 ч. л.\nРастительное масло - 1 ч. л. = 5 г')
        bot.send_photo(message.chat.id, photo=photo2, caption = 'Помойте и почистите чеснок. Вымойте яйцо и укроп, промокните их бумажными полотенцами. Подготовьте миски и глубокую форму для запекания. Смажьте форму растительным маслом.')
        bot.send_photo(message.chat.id, photo=photo3, caption = 'Отрежьте корку с хлеба, поломайте мякиш на кусочки в миску. Залейте мякиш молоком и дайте хлебу набухнуть 5-7 минут. Пропустите чеснок через пресс или мелко его натрите. Порубите укроп. Соедините в миске чеснок, укроп и мясной фарш. Посолите и поперчите фарш, разбейте в него яйцо. Отожмите кусочки хлеба от молока, выложите их в фарш. Тщательно вымесите фарш до однородной гладкой консистенции.')
        bot.send_photo(message.chat.id, photo=photo4, caption = 'Смочите руки прохладной водой, слепите из фарша котлеты. Уложите котлеты в форму для запекания на расстоянии друг от друга.')
        bot.send_photo(message.chat.id, photo=photo5, caption = 'Налейте воду комнатной температуры в миску, всыпьте в нее крахмал и хорошо перемешайте, разбивая все комочки. Выложите сметану в воду с крахмалом, размешайте. Включите духовку разогреваться до 180°C. Всыпьте в соус соль и перец, еще раз как следует размешайте.')
        bot.send_photo(message.chat.id, photo=photo6, caption = 'Залейте соусом котлеты в форме для запекания. Поставьте форму в духовку и запекайте котлеты в течение 40-45 минут, пока верх котлет не подрумянится, а соус не загустеет. Достаньте котлеты из духовки и подавайте горячими к столу.')
        bot.send_photo(message.chat.id, photo=photo7, caption = 'Подайте котлеты в сметанном соусе с гарниром из риса. Украсьте блюдо ломтиками свежего огурца, помидорами черри и укропом.')
        bot.send_message(message.chat.id, 'Как приготовите, пришлите мне фото готового блюда. Буду очень рад!🥰')

    elif message.text == 'Плов':
        photo1 = open(r'C:\Users\Юля\source\repos\PythonApplication2\фото/плов.jpg', 'rb')
        photo2 = open(r'C:\Users\Юля\source\repos\PythonApplication2\фото/плов1.jpg', 'rb')
        photo3 = open(r'C:\Users\Юля\source\repos\PythonApplication2\фото/плов2.jpg', 'rb')
        photo4 = open(r'C:\Users\Юля\source\repos\PythonApplication2\фото/плов3.jpg', 'rb')
        photo5 = open(r'C:\Users\Юля\source\repos\PythonApplication2\фото/плов4.jpg', 'rb')
        photo6 = open(r'C:\Users\Юля\source\repos\PythonApplication2\фото/плов5.jpg', 'rb')
        photo7 = open(r'C:\Users\Юля\source\repos\PythonApplication2\фото/плов6.jpg', 'rb')
        bot.send_photo(message.chat.id, photo=photo1, caption = 'ПЛОВ С МАШЕМ И ГОВЯЖЬИМИ РЕБРАМИ\n\nЛучше всего для плова подходит, конечно, казан. Но не у всех он есть. Заменить его могут глубокая сковорода с толстым дном или мультиварка. Начните готовить с мяса, а затем постепенно добавьте к нему остальные ингредиенты. Маш нужно заранее замочить в воде, чтобы он набух и размяк. Лучше всего залить маш водой на ночь, но и 4-5 часов будет достаточно\n\nПРОДУКТЫ:\n\nРис длиннозерный - 180 г\nРепчатый лук - 1 шт. = 80 г\nМорковь - 1 шт. = 90 г\nЧеснок - 4 зубчик = 20 г\nРастительное масло - 3 ст. л. = 51 г\nГовяжьи ребрышки - 500 г\nСоль - 1 ч. л. = 10 г\nСпеции для плова - 1 ч. л.')
        bot.send_photo(message.chat.id, photo=photo2, caption = 'Разморозьте, помойте и протрите говяжьи ребра. Промойте под проточной водой рис и маш. Замочите маш в воде на 3-4 часа или даже на ночь. Помойте и почистите морковь, лук и чеснок. Подготовьте глубокую сковороду.')
        bot.send_photo(message.chat.id, photo=photo3, caption = 'Разрежьте ребра между костями на части. Разогрейте в сковороде растительное масло. Обжарьте ребра на сильном огне в течение 5 минут, периодически переворачивая их. Нарежьте лук тонкими полукольцами, добавьте его к мясу и хорошо перемешайте. Уменьшите нагрев до среднего. Готовьте говядину еще 5 минут.')
        bot.send_photo(message.chat.id, photo=photo4, caption = 'Нарежьте морковь соломкой. Выложите в сковороду. Жарьте еще 5 минут, регулярно перемешивая.Влейте 1 стакан воды. Тушите мясо в течение 20 минут под крышкой на медленном огне.')
        bot.send_photo(message.chat.id, photo=photo5, caption = 'Всыпьте в сковороду маш. Хорошенько перемешайте. Посолите, приправьте специями, добавьте чеснок. Готовьте все вместе еще 20 минут.')
        bot.send_photo(message.chat.id, photo=photo6, caption = 'Добавьте рис. Перемешайте и разровняйте поверхность. Влейте кипяток так, чтобы он превышал уровень продуктов на 1 см. Накройте крышкой, готовьте еще 20 минут.')
        bot.send_photo(message.chat.id, photo=photo7, caption = 'Украсьте подачу помидорами черри и зеленью.')
        bot.send_message(message.chat.id, 'Как приготовите, пришлите мне фото готового блюда. Буду очень рад!🥰')

    elif message.text == 'Запеченые овощи':
        photo1 = open(r'C:\Users\Юля\source\repos\PythonApplication2\фото/овощи.jpg', 'rb')
        photo2 = open(r'C:\Users\Юля\source\repos\PythonApplication2\фото/овощи1.jpg', 'rb')
        photo3 = open(r'C:\Users\Юля\source\repos\PythonApplication2\фото/овощи2.jpg', 'rb')
        photo4 = open(r'C:\Users\Юля\source\repos\PythonApplication2\фото/овощи3.jpg', 'rb')
        photo5 = open(r'C:\Users\Юля\source\repos\PythonApplication2\фото/овощи4.jpg', 'rb')
        photo6 = open(r'C:\Users\Юля\source\repos\PythonApplication2\фото/овощи5.jpg', 'rb')
        photo7 = open(r'C:\Users\Юля\source\repos\PythonApplication2\фото/овощи6.jpg', 'rb')
        bot.send_photo(message.chat.id, photo=photo1, caption = 'ЗАПЕЧЕННЫЕ ОВОЩИ С ЯЙЦОМ\n\nЕсть запеченные брокколи и морковь очень полезно, а с яйцом и сыром еще и вкусно. Положите в запеканку немного кукурузы для аппетитного вида. Сбалансированный по всем параметрам завтрак или ужин хорошо насытит и не оставит чувства тяжести. Для большей пикантности добавьте немного чеснока, красный лук или пряные травы.\n\nПРОДУКТЫ:\n\nКуриное яйцо - 2 шт. = 120 г\nБрокколи - 100 г\nКонсервированная кукуруза - 20 г\nМорковь - 50 г\nПолутвердый сыр - 35 г\nЧерный перец молотый - 0.3 г\nСоль - 1.5 г\nПодсолнечное масло рафинированное - 1 ч. л.')
        bot.send_photo(message.chat.id, photo=photo2, caption = 'Помойте яйца и брокколи, промокните их бумажными салфетками. Вымойте и почистите морковь. Подготовьте терку, миску и глубокую стеклянную форму для запекания. Смажьте форму растительным маслом.')
        bot.send_photo(message.chat.id, photo=photo3, caption = 'Разберите брокколи на маленькие соцветия. Крупно натрите сыр и морковь.')
        bot.send_photo(message.chat.id, photo=photo4, caption = 'Разбейте яйца в миску, взбейте их венчиком.')
        bot.send_photo(message.chat.id, photo=photo5, caption = 'Выложите в миску к яйцам брокколи, морковь, кукурузу, тертый сыр. Всыпьте соль и перец, все перемешайте.')
        bot.send_photo(message.chat.id, photo=photo6, caption = 'Дайте духовке разогреться до 180°C. Перелейте яично-овощную смесь в форму для запекания и поставьте ее в духовку. Готовьте яйца с овощами в течение 20 минут.')
        bot.send_photo(message.chat.id, photo=photo7, caption = 'Подайте к запеченным овощам с яйцом сметанный соус и стакан сока или морса.')
        bot.send_message(message.chat.id, 'Как приготовите, пришлите мне фото готового блюда. Буду очень рад!🥰')

    elif message.text == 'Паста с соусом песто':
        photo1 = open(r'C:\Users\Юля\source\repos\PythonApplication2\фото/паста.jpg', 'rb')
        photo2 = open(r'C:\Users\Юля\source\repos\PythonApplication2\фото/паста1.jpg', 'rb')
        photo3 = open(r'C:\Users\Юля\source\repos\PythonApplication2\фото/паста2.jpg', 'rb')
        photo4 = open(r'C:\Users\Юля\source\repos\PythonApplication2\фото/паста3.jpg', 'rb')
        photo5 = open(r'C:\Users\Юля\source\repos\PythonApplication2\фото/паста4.jpg', 'rb')
        photo6 = open(r'C:\Users\Юля\source\repos\PythonApplication2\фото/паста5.jpg', 'rb')
        photo7 = open(r'C:\Users\Юля\source\repos\PythonApplication2\фото/паста6.jpg', 'rb')
        bot.send_photo(message.chat.id, photo=photo1, caption = 'ПАСТА С СОУСОМ ПЕСТО\n\nЧто может быть более итальянским, чем паста с соусом песто? Для приготовления этого наивкуснейшего блюда вы можете использовать классический песто зеленого цвета под названием «Дженовезе». Этот соус готовится на основе базилика, чеснока, сыра и оливкового масла. Либо же вы можете выбрать оригинальные вариации этого соуса, например, песто с томатами.\n\nПРОДУКТЫ:\n\nМакароны - 160 г\nВода - 1.6 л\nОливковое масло - 1 ст. л.\nЧеснок - 1 зубчик\nМолоко - 80 мл\nСоус песто - 60 г\nПармезан - 2 ст. л. = 36 г\nЧерный перец молотый - по вкусу\nСоль - по вкусу')
        bot.send_photo(message.chat.id, photo=photo2, caption = 'Подготовьте все ингредиенты. В качестве макаронных изделий можете выбрать любой вид пасты. Сегодня в магазинах можно найти множество видов макарон разной формы и размеров. Например: фарфалле, физулли, лингвини, пенне, конкильони, челлентани, тальятелле и другие. Соус песто можете выбрать совершенно любой, но опять же продукт должен быть качественным, приготовленным исключительно из натуральных продуктов. Еще для приготовления блюда понадобятся коровье молоко любой жирности, пармезан, чеснок, оливковое масло, перец и соль.')
        bot.send_photo(message.chat.id, photo=photo3, caption = 'Возьмите глубокую большую кастрюлю, поскольку для варки пасты необходим большой объем воды. В выбранную кастрюлю влейте воду и поставьте ее на огонь, доведите до кипения, слегка подсолите воду и всыпьте макаронные изделия. Варите пасту до состояния аль денте, не закрывая кастрюлю крышкой.')
        bot.send_photo(message.chat.id, photo=photo4, caption = 'Пока варится паста, займитесь приготовлением соуса с песто. В сковороду влейте оливковой масло и поставьте на огонь. Когда масло будет разогрето, выложите в сковороду очищенный и раздавленный зубчик чеснока. Обжарьте его на среднем огне до появления вкусного чесночного аромата, после чего извлеките чеснок из сковороды. В ароматное чесночное масло сначала введите коровье молоко, а затем добавьте соус песто и хорошенько перемешайте все ингредиенты на сковороде до однородного состояния.')
        bot.send_photo(message.chat.id, photo=photo5, caption = 'Готовую пасту откиньте на дуршлаг и дайте немного времени, чтобы вся лишняя вода стекла. Отварные макаронные изделия перекиньте в сковороду с приготовленным соусом, поперчите по вкусу и перемешайте так, чтобы весь соус равномерно распределился по пасте.')
        bot.send_photo(message.chat.id, photo=photo6, caption = 'Для окончательного штриха понадобится пармезан. Его легче купить уже в натертом виде. Если же вы приобрели цельный кусочек пармезана, то вы можете натереть его на мелкой терке, предварительно охладив его, что облегчит вам работу. А можете перетереть пармезан с помощью блендера, использую диск с мелким решетом.')
        bot.send_photo(message.chat.id, photo=photo7, caption = 'Готовую пасту разложите по тарелкам, сверху посыпьте натертым пармезаном и в горячем виде подайте на стол. Для красоты украсьте блюдо веточкой базилика и помидорами черри.')
        bot.send_message(message.chat.id, 'Как приготовите, пришлите мне фото готового блюда. Буду очень рад!🥰')

    elif message.text == 'Драники из картошки с сыром':
        photo1 = open(r'C:\Users\Юля\source\repos\PythonApplication2\фото/драники.jpg', 'rb')
        photo2 = open(r'C:\Users\Юля\source\repos\PythonApplication2\фото/драники1.jpg', 'rb')
        photo3 = open(r'C:\Users\Юля\source\repos\PythonApplication2\фото/драники2.jpg', 'rb')
        photo4 = open(r'C:\Users\Юля\source\repos\PythonApplication2\фото/драники3.jpg', 'rb')
        photo5 = open(r'C:\Users\Юля\source\repos\PythonApplication2\фото/драники4.jpg', 'rb')
        photo6 = open(r'C:\Users\Юля\source\repos\PythonApplication2\фото/драники5.jpg', 'rb')
        bot.send_photo(message.chat.id, photo=photo1, caption = 'ДРАНИКИ ИЗ КАРТОШКИ С СЫРОМ\n\nДраники из картошки с сыром можно подать в качестве гарнира к любому мясному блюду или соединить на одной тарелке с салатом из свежих овощей. От того, какой сыр вы выберете, будет зависеть и вкус драников. Можно даже на одном противне приготовить сразу несколько разных вариантов. Любителям острых блюд рекомендуем добавить в картофельное тесто немного измельченного перца халапеньо или молотого красного перца.\n\nПРОДУКТЫ:\n\nКартошка - 4 шт. = 480 г\nРепчатый лук - 1 шт.\nЧеснок - 1 зубчик\nПшеничная мука хлебопекарная - 1.5 ст. л. = 37.5 г\nМолоко 2,5% жирности - 50 мл \nТвердый сыр - 100 г\nСоль - 1 ч. л.\nЧерный перец молотый - 0.5 ч. л.\nРастительное масло - 0.25 стакан\nУкроп - 0.5 пучок\nМайонез - 1 ст. л.')
        bot.send_photo(message.chat.id, photo=photo2, caption = 'Помойте и почистите картошку, репчатый лук и чеснок. Ополосните укроп. Разогрейте духовку до 180°C. Застелите противень пергаментом.')
        bot.send_photo(message.chat.id, photo=photo3, caption = 'Натрите картошку на мелкой терке. Отожмите лишнюю жидкость. Покрошите репчатый лук и укроп как можно мельче. Смешайте в одной миске картофель, лук, молоко, муку, зелень, соль и черный молотый перец.')
        bot.send_photo(message.chat.id, photo=photo4, caption = 'Разогрейте в сковороде немного растительного масла. Выкладывайте ложкой тесто и жарьте драники с двух сторон по 3-4 минуты на среднем огне. По мере необходимости подливайте масло.')
        bot.send_photo(message.chat.id, photo=photo5, caption = 'Натрите сыр. Пропустите чеснок через пресс. Смешайте в небольшой миске сыр, чеснок и майонез. Переложите драники на противень. На каждый выложите немного сырной массы. Отправьте противень в духовку на 10 минут.')
        bot.send_photo(message.chat.id, photo=photo6, caption = 'Подавайте драники, полив их любимым соусом, например, сырным, сливочным или сметанным.')
        bot.send_message(message.chat.id, 'Как приготовите, пришлите мне фото готового блюда. Буду очень рад!🥰')

        #Салаты
    elif message.text == 'Салаты' or message.text == '/salads':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)    
        b1 = types.KeyboardButton('Оливье')
        b2 = types.KeyboardButton('Крабовый')
        b3 = types.KeyboardButton('Цезарь')
        b4 = types.KeyboardButton('С мятой и лаймом')
        b5 = types.KeyboardButton('С фетой и свеклой')
        b6 = types.KeyboardButton('В меню рецептов')
        markup.add(b1,b2,b3,b4,b5,b6)
        photo = open(r'C:\Users\Юля\source\repos\PythonApplication2\фото/салаты.jpg', 'rb')
        bot.send_photo(message.chat.id, photo=photo, caption = 'Раздел "Салаты" предлагает разнообразные рецепты для тех, кто ценит легкие и освежающие блюда. Здесь вы найдете рецепты классических овощных салатов, фруктовых салатов, салатов с добавлением морепродуктов или мяса, а также оригинальные варианты с использованием различных видов зелени и заправок. Независимо от ваших предпочтений, здесь есть салаты на любой вкус и под любое настроение. Каждый рецепт сопровождается подробными инструкциями, чтобы вы могли легко приготовить свой идеальный салат.', reply_markup = markup)

    elif message.text == 'Оливье':
        photo1 = open(r'C:\Users\Юля\source\repos\PythonApplication2\фото/оливье.jpg', 'rb')
        photo2 = open(r'C:\Users\Юля\source\repos\PythonApplication2\фото/оливье1.jpg', 'rb')
        photo3 = open(r'C:\Users\Юля\source\repos\PythonApplication2\фото/оливье2.jpg', 'rb')
        photo4 = open(r'C:\Users\Юля\source\repos\PythonApplication2\фото/оливье3.jpg', 'rb')
        photo5 = open(r'C:\Users\Юля\source\repos\PythonApplication2\фото/оливье4.jpg', 'rb')
        bot.send_photo(message.chat.id, photo=photo1, caption = 'САЛАТ ОЛИВЬЕ\n\nПРОДУКТЫ (на 8 порций):\n\nКартофель - 4 шт.\nЯйца куриные - 7 шт.\nКолбаса "Докторская" - 300 г\nОгурцы соленые - 3 шт.\nМорковь - 2-3 шт.\nЗеленый горошек консервированный - 1 баночка\nЛук зеленый (по желанию) - 1 пучок\nЗелень - по вкусу\nМайонез - по вкусу\nСоль - по вкусу\nПерец - по вкусу')
        bot.send_photo(message.chat.id, photo=photo2, caption = 'Ингредиенты для салата Оливье с колбасой перед Вами. Как приготовить салат Оливье с колбасой: Хорошо вымыть и отварить до готовности картофель и морковь. Остудить. Очистить.')
        bot.send_photo(message.chat.id, photo=photo3, caption = 'Залить яйца холодной водой. Посолить и отварить вкрутую. Охладить и очистить. Морковь, колбасу, картофель, яйца, огурцы нарезать кубиками. Зеленый горошек открыть и откинуть на дуршлаг, чтобы стекла жидкость. Зелень и зеленый лук вымыть и нарезать. (Лук в оливье чаще не добавляют, но если используется, то лучше зеленый.)')
        bot.send_photo(message.chat.id, photo=photo4, caption = 'Все ингредиенты соединить в миске, посолить, поперчить и заправить майонезом по вкусу. Хорошо перемешать.')
        bot.send_photo(message.chat.id, photo=photo5, caption = 'Салат Оливье с колбасой готов. Приятного аппетита!')
        bot.send_message(message.chat.id, 'Как приготовите, пришлите мне фото готового блюда. Буду очень рад!🥰')

    elif message.text == 'Крабовый':
        photo1 = open(r'C:\Users\Юля\source\repos\PythonApplication2\фото/краб.jpg', 'rb')
        photo2 = open(r'C:\Users\Юля\source\repos\PythonApplication2\фото/краб1.jpg', 'rb')
        photo3 = open(r'C:\Users\Юля\source\repos\PythonApplication2\фото/краб2.jpg', 'rb')
        photo4 = open(r'C:\Users\Юля\source\repos\PythonApplication2\фото/краб3.jpg', 'rb')
        photo5 = open(r'C:\Users\Юля\source\repos\PythonApplication2\фото/краб4.jpg', 'rb')
        bot.send_photo(message.chat.id, photo=photo1, caption = 'КРАБОВЫЙ САЛАТ\n\nСалат с пeкинскoй капустoй, крабoвыми палoчками и кукурузoй – один из самых пoпулярных, простых и бюджeтных рeцeптoв. Салат пoлучаeтся свeжим, лeгким и oбъeмным.\n\nПРОДУКТЫ:\n\nКапуста пекинская – 1/3 стандартнoгo кoчана\nКрабoвыe палoчки (или крабовое мясо) – 1 упакoвка (200 г)\nКукуруза консервированная – 1/2 стандартнoй банки\nЯйца – 2 шт.\nОгурeц средний – 1 шт.\nМайoнeз – 4 ст. лoжки с гoркoй\nСoль - пo вкусу')
        bot.send_photo(message.chat.id, photo=photo2, caption = 'Как приготовить крабовый салат с пекинской капустой: Нарезаем пекинскую капусту. Огурцы нарезаем брусочками. Крабовые палочки нарезаем кружочками. Отварные яйца нарезаем кубиками.')
        bot.send_photo(message.chat.id, photo=photo3, caption = 'Собираем салат. В миску перекладываем порезанную пекинскую капусту, огурцы, крабовые палочки, яйца. Выкладываeм в салатник с нарублeнными прoдуктами кукурузу, предварительно слив с неё жидкость.')
        bot.send_photo(message.chat.id, photo=photo4, caption = 'Добавляем немного соли и майонез.')
        bot.send_photo(message.chat.id, photo=photo5, caption = 'Всё хорошо перемешиваем и подаём к столу. Приятного аппетита!')
        bot.send_message(message.chat.id, 'Как приготовите, пришлите мне фото готового блюда. Буду очень рад!🥰')

    elif message.text == 'Цезарь':
        photo1 = open(r'C:\Users\Юля\source\repos\PythonApplication2\фото/цезарь.jpg', 'rb')
        photo2 = open(r'C:\Users\Юля\source\repos\PythonApplication2\фото/цезарь1.jpg', 'rb')
        photo3 = open(r'C:\Users\Юля\source\repos\PythonApplication2\фото/цезарь2.jpg', 'rb')
        photo4 = open(r'C:\Users\Юля\source\repos\PythonApplication2\фото/цезарь3.jpg', 'rb')
        photo5 = open(r'C:\Users\Юля\source\repos\PythonApplication2\фото/цезарь4.jpg', 'rb')
        photo6 = open(r'C:\Users\Юля\source\repos\PythonApplication2\фото/цезарь5.jpg', 'rb')
        photo7 = open(r'C:\Users\Юля\source\repos\PythonApplication2\фото/цезарь6.jpg', 'rb')
        bot.send_photo(message.chat.id, photo=photo1, caption = 'ЦЕЗАРЬ КЛАССИЧЕСКИЙ\n\nCалат "Цезарь" – это очень популярный салат. Вкусный и легкий салат с сухариками (крутонами) подается к столу сразу после приготовления. За долгие годы существования этого салата появилось много различных его вариантов. Мы хотим предложить вам классическую версию салата "Цезарь". И рассказать, как приготовить соус к салату "Цезарь".\n\nПРОДУКТЫ:\n\nКрутоны (сухарики) - 200 г\nСалат листовой (желательно салат ромэн) - 400 г\nЧеснок - 2 зубка\nАнчоусы (филе) - 3 шт.\nЖелтки - 2 шт.\nЛимон (для сока) - 1 шт.\nМасло оливковое - 150 г\nСыр пармезан - 70 г\nСоль - 0,25 ч. ложки\nПерец черный молотый - 0,25 ч. ложки')
        bot.send_photo(message.chat.id, photo=photo2, caption = 'Подготавливаем продукты для салата "Цезарь".')
        bot.send_photo(message.chat.id, photo=photo3, caption = 'Приготовим соус. Отделяем белки двух яиц от желтков. (Белки убираем в холодильник – они нам в этом рецепте не понадобятся.) Желтки, все время перемешивая, нагреваем на водяной бане до температуры 57-60 градусов и оставляем остывать.')
        bot.send_photo(message.chat.id, photo=photo4, caption = 'Измельчаем три филе анчоусов, добавляем в желтки. Туда же добавляем сок одного лимона, перемешиваем. Добавляем 1/4 чайной ложки соли, 1/4 чайной ложки черного молотого перца, перемешиваем. Добавляем 2 измельчённых зубчика чеснока, перемешиваем.')
        bot.send_photo(message.chat.id, photo=photo5, caption = 'Все время взбивая полученную смесь венчиком, вливаем тонкой струйкой 150 граммов оливкового или другого растительного масла. Взбиваем до получения гладкого и нежного соуса. Соус для салата "Цезарь" готов.')
        bot.send_photo(message.chat.id, photo=photo6, caption = '400 граммов листьев салата (желательно салата ромэн) моем, обсушиваем и рвем на кусочки в миску. Добавляем 70 граммов натертого сыра пармезан, 150 граммов из подготовленных 200 граммов крутонов, аккуратно перемешиваем. Добавляем в салат "Цезарь" приготовленный соус. Еще раз аккуратно перемешиваем.')
        bot.send_photo(message.chat.id, photo=photo7, caption = 'Салат с сухариками (крутонами) сразу выкладываем в салатник, украшаем оставшимися крутонами и подаем к столу. Салат "Цезарь" чаще всего подают к блюдам из курицы, но также можно подать к блюдам из морепродуктов и к мясным блюдам.')
        bot.send_message(message.chat.id, 'Как приготовите, пришлите мне фото готового блюда. Буду очень рад!🥰')

    elif message.text == 'С мятой и лаймом':
        photo1 = open(r'C:\Users\Юля\source\repos\PythonApplication2\фото/мята.jpg', 'rb')
        photo2 = open(r'C:\Users\Юля\source\repos\PythonApplication2\фото/мята1.jpg', 'rb')
        photo3 = open(r'C:\Users\Юля\source\repos\PythonApplication2\фото/мята2.jpg', 'rb')
        photo4 = open(r'C:\Users\Юля\source\repos\PythonApplication2\фото/мята3.jpg', 'rb')
        photo5 = open(r'C:\Users\Юля\source\repos\PythonApplication2\фото/мята4.jpg', 'rb')
        photo6 = open(r'C:\Users\Юля\source\repos\PythonApplication2\фото/мята5.jpg', 'rb')
        bot.send_photo(message.chat.id, photo=photo1, caption = 'САЛАТ С МЯТОЙ И ЛАЙМОМ\n\nНи один вид зелени не даст такого освежающего эффекта, как мята. Положите ее вместо петрушки или базилика в классический микс помидоров и огурцов и получите совершенно новый вкус привычного салата. Чтобы подчеркнуть вкус ментола и привнести в блюдо кислинку, добавьте сок и цедру лайма. Для заправки такого салата лучше всего подойдет оливковое масло первого холодного отжима.\n\nПРОДУКТЫ:\n\nСалатные листья - 100 г\nОгурец - 1 шт. = 100 г\nПомидор - 2 шт. = 160 г\nМята - 3 веточка = 3 г\nЛайм - 0.5 шт. = 30 г\nЧерный перец молотый - 1 щепотка = 1 г\nСоль - 0.25 ч. л. = 2.5 г\nОливковое масло - 1 ст. л. = 17 г')
        bot.send_photo(message.chat.id, photo=photo2, caption = 'Помойте мяту, лайм, помидоры, огурец и салатные листья. Разложите все на бумажных полотенцах обсыхать. Достаньте терку, миску, разделочную доску и салатник.')
        bot.send_photo(message.chat.id, photo=photo3, caption = 'Снимите с половины лайма цедру мелкой теркой. Из мякоти половины выжмите сок. Мелко нарежьте мяту, соедините ее в миске с соком и цедрой лайма. Посолите и поперчите мятно-лаймовую смесь, хорошо размешайте.')
        bot.send_photo(message.chat.id, photo=photo4, caption = 'Нарвите листья салата руками, нарежьте помидоры и огурец кубиками со стороной около 1,5 см. Выложите овощи в салатник.')
        bot.send_photo(message.chat.id, photo=photo5, caption = 'Положите к овощам мятно-лаймовую смесь, полейте оливковым маслом. Перемешайте салат и подайте к столу.')
        bot.send_photo(message.chat.id, photo=photo6, caption = 'Украсьте салат ломтиками лайма и веточкой мяты.')
        bot.send_message(message.chat.id, 'Как приготовите, пришлите мне фото готового блюда. Буду очень рад!🥰')

    elif message.text == 'С фетой и свеклой':
        photo1 = open(r'C:\Users\Юля\source\repos\PythonApplication2\фото/свекла.jpg', 'rb')
        photo2 = open(r'C:\Users\Юля\source\repos\PythonApplication2\фото/свекла1.jpg', 'rb')
        photo3 = open(r'C:\Users\Юля\source\repos\PythonApplication2\фото/свекла2.jpg', 'rb')
        photo4 = open(r'C:\Users\Юля\source\repos\PythonApplication2\фото/свекла3.jpg', 'rb')
        photo5 = open(r'C:\Users\Юля\source\repos\PythonApplication2\фото/свекла4.jpg', 'rb')
        photo6 = open(r'C:\Users\Юля\source\repos\PythonApplication2\фото/свекла5.jpg', 'rb')
        bot.send_photo(message.chat.id, photo=photo1, caption = 'САЛАТ С ФЕТОЙ И СВЕКЛОЙ\n\nРазноцветные продукты не только создают яркий и красивый вид салата, но и придают ему очень интересный вкус с солоновато-кислыми, сладкими, пикантными и пряными нотками. Медово-горчичная заправка с лимонным соком помогает связать вкусы салата и сделать его очень необычным и вкусным.\n\nПРОДУКТЫ:\n\nДля основного блюда\n\nСвекла - 1 шт. = 130 г\nСыр фета - 80 г\nГрецкие орехи - 60 г\nЛимонный сок - 2 ст. л. = 36 г\nАпельсин - 0.5 шт. = 62.5 г\nРукола - 50 г\nКрасный лук - 0.5 шт. = 37.5 г\nДля заправки\n\nЛимонный сок - 1 ст. л. = 18 г\nЦветочный мед - 1 ст. л. = 28 г\nЗернистая горчица - 2 ч. л. = 16 г\nОливковое масло Extra Virgin - 1 ст.л.')
        bot.send_photo(message.chat.id, photo=photo2, caption = 'Помойте свеклу и апельсин. Очистите апельсин от кожуры. Вымойте и почистите лук. Ополосните руколу, выложите ее на бумажное полотенце обсохнуть. Подготовьте кастрюлю, миски, разделочную доску и салатник.')
        bot.send_photo(message.chat.id, photo=photo3, caption = 'Положите свеклу в кастрюлю, залейте ее водой и поставьте на плиту. Доведите воду до кипения на сильном огне. Уменьшите огонь до среднего и отварите свеклу до мягкости 50-60 минут. Дайте свекле остыть и очистите ее от кожуры. Нарежьте лук полукольцами, выложите его в миску и полейте 2 ст.л. лимонного сока. Помаринуйте лук 15 минут, затем слейте жидкость. Нарежьте свеклу произвольными кусочками. Примерно такими же кусочками нарежьте апельсин ,а сыр фета кубиком. Порубите орехи на кусочки.')
        bot.send_photo(message.chat.id, photo=photo4, caption = 'Налейте в чистую миску 1 ст.л. лимонного сока. Положите к нему мед и горчицу, добавьте оливковое масло. Все перемешайте.')
        bot.send_photo(message.chat.id, photo=photo5, caption = 'Соедините в миске свеклу, апельсин, сыр, орехи, руколу и лук. Полейте все лимонно-горчичной заправкой и аккуратно размешайте.')
        bot.send_photo(message.chat.id, photo=photo6, caption = 'Украсьте салат целыми ядрами грецких орехов.')
        bot.send_message(message.chat.id, 'Как приготовите, пришлите мне фото готового блюда. Буду очень рад!🥰')
        
        #Закуски
    elif message.text == 'Закуски' or message.text == '/snacks':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)    
        b1 = types.KeyboardButton('Яичные блинчики')
        b2 = types.KeyboardButton('Шампиньоны')
        b3 = types.KeyboardButton('Мини-слойки')
        b4 = types.KeyboardButton('Сырные палочки')
        b5 = types.KeyboardButton('Рулетики из бекона')
        b6 = types.KeyboardButton('В меню рецептов')
        markup.add(b1,b2,b3,b4,b5,b6)
        photo = open(r'C:\Users\Юля\source\repos\PythonApplication2\фото/закуски.jpg', 'rb')
        bot.send_photo(message.chat.id, photo=photo, caption = 'В разделе "Закуски" вы найдете множество рецептов для приготовления вкусных и разнообразных закусок. Здесь можно найти идеи как для повседневного ужина, так и для праздничного стола. От легких овощных закусок до изысканных мясных и рыбных блюд — выбор за вами. Приготовьте что-то особенное и порадуйте себя и близких вкусными угощениями.', reply_markup = markup)

    elif message.text == 'Яичные блинчики':
        photo1 = open(r'C:\Users\Юля\source\repos\PythonApplication2\фото/блинчики.jpg', 'rb')
        photo2 = open(r'C:\Users\Юля\source\repos\PythonApplication2\фото/блинчики1.jpg', 'rb')
        photo3 = open(r'C:\Users\Юля\source\repos\PythonApplication2\фото/блинчики2.jpg', 'rb')
        photo4 = open(r'C:\Users\Юля\source\repos\PythonApplication2\фото/блинчики3.jpg', 'rb')
        photo5 = open(r'C:\Users\Юля\source\repos\PythonApplication2\фото/блинчики4.jpg', 'rb')
        photo6 = open(r'C:\Users\Юля\source\repos\PythonApplication2\фото/блинчики5.jpg', 'rb')
        photo7 = open(r'C:\Users\Юля\source\repos\PythonApplication2\фото/блинчики6.jpg', 'rb')
        bot.send_photo(message.chat.id, photo=photo1, caption = 'ЯИЧНЫЕ БЛИНЧИКИ С КРАБОВЫМИ ПАЛОЧКАМИ И СЫРОМ\n\nПростая и лёгкая закуска - рулетики из яичных блинчиков с крабовыми палочками и сыром. Нежные яичные блинчики с начинкой из крабовых палочек и сыра выглядят очень нарядно и вполне способны стать угощением даже на праздничном столе.\n\nПРОДУКТЫ:\n\nЯйца - 3 шт.\nКрабовые палочки - 3 шт.\nСыр твёрдый - 100 г\nМайонез - 2 ст. ложки\nУкроп свежий - 4-5 веточек (10 г)\nСоль - по вкусу\nМасло растительное (для жарки) - 1 ст. ложка')
        bot.send_photo(message.chat.id, photo=photo2, caption = 'Подготовьте продукты по списку. Крабовые палочки полностью разморозьте на нижней полке холодильника.')
        bot.send_photo(message.chat.id, photo=photo3, caption = 'Одно из яиц разбейте в мисочку, посолите и взболтайте вилкой до однородности.')
        bot.send_photo(message.chat.id, photo=photo4, caption = 'Сковороду смажьте растительным маслом и разогрейте на среднем огне. Вылейте яичную массу, разровняйте, наклоняя сковороду в стороны. Поджарьте получившийся блинчик примерно по 1-2 минуты с каждой стороны. Таким же образом из оставшихся яиц испеките ещё 2 блинчика.')
        bot.send_photo(message.chat.id, photo=photo5, caption = 'Крабовые палочки очистите от заводской оболочки. Одну палочку аккуратно, стараясь не порвать, разверните и выложите сверху на один из яичных блинчиков. Точно таким же образом поступите с оставшимися 2 яичными блинчиками и крабовыми палочками.')
        bot.send_photo(message.chat.id, photo=photo6, caption = 'Сыр натрите на средней тёрке и разделите на 3 равные части. Распределите сыр на каждый блинчик сверху крабовой палочки. Полейте сыр сверху майонезом. Это очень удобно сделать из кондитерского корнетика или при помощи обычного пакета. Укроп промойте, обсушите, мелко нарежьте и разделите на 3 части. Посыпьте укропом начинку каждого блинчика.')
        bot.send_photo(message.chat.id, photo=photo7, caption = 'Сверните каждый блинчик с начинкой в плотный рулетик. Разрежьте каждый рулетик поперёк на 3-4 части. Выложите яичные блинчики с крабовыми палочками и сыром на сервировочное блюдо и подавайте к столу. Приятного аппетита!')
        bot.send_message(message.chat.id, 'Как приготовите, пришлите мне фото готового блюда. Буду очень рад!🥰')

    elif message.text == 'Шампиньоны':
        photo1 = open(r'C:\Users\Юля\source\repos\PythonApplication2\фото/грибы.jpg', 'rb')
        photo2 = open(r'C:\Users\Юля\source\repos\PythonApplication2\фото/грибы1.jpg', 'rb')
        photo3 = open(r'C:\Users\Юля\source\repos\PythonApplication2\фото/грибы2.jpg', 'rb')
        photo4 = open(r'C:\Users\Юля\source\repos\PythonApplication2\фото/грибы3.jpg', 'rb')
        bot.send_photo(message.chat.id, photo=photo1, caption = 'ШАМПИНЬОНЫ ЖАРЕНЫЕ\n\nВкуснейшая закуска за 5 минут. Я не люблю сложные рецепты, на которые уходит несколько часов. И уже стала замечать, что чем проще - тем вкуснее. Эти сочные, ароматные, вкуснейшие жареные грибочки я готовлю очень часто. И просто на ужин, и на праздничный стол, и на закуску, если вдруг неожиданно гости...\n\nПРОДУКТЫ:\n\nШампиньоны\nСоль\nМука\nМасло подсолнечное (дла жарки)')
        bot.send_photo(message.chat.id, photo=photo2, caption = 'Все очень просто! Шампиньоны режу, солю.')
        bot.send_photo(message.chat.id, photo=photo3, caption = 'Обваливаю нарезанные шампиньоны в муке и жарю их на подсолнечном масле.')
        bot.send_photo(message.chat.id, photo=photo4, caption = 'Подаю жареные грибы со сметанным соусом. Шампиньоны "Хочу еще!" - это очень вкусно!')
        bot.send_message(message.chat.id, 'Как приготовите, пришлите мне фото готового блюда. Буду очень рад!🥰')

    elif message.text == 'Мини-слойки':
        photo1 = open(r'C:\Users\Юля\source\repos\PythonApplication2\фото/слойки.jpg', 'rb')
        photo2 = open(r'C:\Users\Юля\source\repos\PythonApplication2\фото/слойки1.jpg', 'rb')
        photo3 = open(r'C:\Users\Юля\source\repos\PythonApplication2\фото/слойки2.jpg', 'rb')
        photo4 = open(r'C:\Users\Юля\source\repos\PythonApplication2\фото/слойки3.jpg', 'rb')
        photo5 = open(r'C:\Users\Юля\source\repos\PythonApplication2\фото/слойки4.jpg', 'rb')
        photo6 = open(r'C:\Users\Юля\source\repos\PythonApplication2\фото/слойки6.jpg', 'rb')
        bot.send_photo(message.chat.id, photo=photo1, caption = 'МИНИ-СЛОЙКИ С СЫРОМ И ВЕТЧИНОЙ\n\nЕсли в морозильной камере "на всякий случай" лежит слоёное тесто, а в холодильнике – ветчина и сыр, приготовьте закусочные слойки. Получается аппетитно, вкусно и празднично!\n\nПРОДУКТЫ:\n\nТесто слоёное - 330 г\nСыр твёрдый - 100 г (8 ломтиков)\nВетчина - 100 г (8 ломтиков)\nЯйцо - 1 шт.\nКунжут чёрный (семена) - 10 г')
        bot.send_photo(message.chat.id, photo=photo2, caption = 'Подготовьте продукты. Слоёное тесто предварительно разморозьте. Ветчину и твёрдый сыр лучше брать уже нарезанные слайсами. Кунжут можно заменить семенами тмина или семечками. Включите духовку разогреваться до 180 градусов.')
        bot.send_photo(message.chat.id, photo=photo3, caption = 'Слоёное тесто разложите на пергаменте. На одну половину теста выложите тонко нарезанные ломтики сыра. На одну половину теста выложите тонко нарезанные ломтики сыра.')
        bot.send_photo(message.chat.id, photo=photo4, caption = 'Накройте сыр и ветчину второй половиной теста. Острым ножом или круглым ножом для пиццы разрежьте получившийся прямоугольник на 4 полоски, равные по ширине. Затем каждую полоску разрежьте на 4-5 частей. Получаются квадраты со стороной около 3-4 см.')
        bot.send_photo(message.chat.id, photo=photo5, caption = 'Яйцо вбейте в глубокую тарелку. Вилкой перемешайте белок и желток. Кисточкой смажьте поверхность теста взбитым яйцом - это придаст готовым слойкам аппетитный блеск. Сверху слоёные квадратики присыпьте семенами кунжута.')
        bot.send_photo(message.chat.id, photo=photo6, caption = 'Выпекайте закусочные слойки в разогретой до 180 градусов духовке 25-30 минут, до румяности (зависит от особенностей вашей духовки). Аккуратно отделите горячие закусочные слойки с сыром и ветчиной одну от другой и выложите на тарелку. Приятного аппетита!')
        bot.send_message(message.chat.id, 'Как приготовите, пришлите мне фото готового блюда. Буду очень рад!🥰')

    elif message.text == 'Сырные палочки':
        photo1 = open(r'C:\Users\Юля\source\repos\PythonApplication2\фото/сыр.jpg', 'rb')
        photo2 = open(r'C:\Users\Юля\source\repos\PythonApplication2\фото/сыр1.jpg', 'rb')
        photo3 = open(r'C:\Users\Юля\source\repos\PythonApplication2\фото/сыр2.jpg', 'rb')
        photo4 = open(r'C:\Users\Юля\source\repos\PythonApplication2\фото/сыр.jpg', 'rb')
        bot.send_photo(message.chat.id, photo=photo1, caption = 'СЫРНЫЕ ПАЛОЧКИ\n\nСырные палочки — идеальная закуска на любой случай, которую легко сделать в домашних условиях. Готовить это легкое блюдо можно во фритюре или на сковороде. Приготовьте палочки с сыром в панировке по классическому рецепту. Приготовление займет мало времени, справится даже новичок. Делать палочки лучше из твердого сыра высокого качества. Если хотите, чтобы вкус жареных сырных палочек имел пикантный вкус и легкий аромат, возьмите за основу сыр моцарелла.\n\nПРОДУКТЫ:\n\nТвердый сыр - 200 г\nКуриное яйцо - 2 шт. = 120 г\nПанировочные сухари - 200 г')
        bot.send_photo(message.chat.id, photo=photo2, caption = 'Подготовьте все необходимые ингредиенты, 2 отдельные емкости (для панировочных сухарей и для яичной смеси), венчик.')
        bot.send_photo(message.chat.id, photo=photo3, caption = 'Нарежьте сыр ломтиками 1-1,5 см. Вбейте яйца в миску. Хорошенько взбейте их венчиком. В отдельную миску насыпьте панировочные сухари.Обмакивайте кусочки сыра в яичную смесь, а затем в панировочные сухари. Обжаривайте палочки на раскаленной сковороде с растительным маслом по 3 минуты с каждой стороны.')
        bot.send_photo(message.chat.id, photo=photo4, caption = 'Подавайте сырные палочки с соусом барбекю. Закуска одинаково хороша и в горячем, и в холодном виде.')
        bot.send_message(message.chat.id, 'Как приготовите, пришлите мне фото готового блюда. Буду очень рад!🥰')

    elif message.text == 'Рулетики из бекона':
        photo1 = open(r'C:\Users\Юля\source\repos\PythonApplication2\фото/рулетики.jpg', 'rb')
        photo2 = open(r'C:\Users\Юля\source\repos\PythonApplication2\фото/рулетики1.jpg', 'rb')
        photo3 = open(r'C:\Users\Юля\source\repos\PythonApplication2\фото/рулетики2.jpg', 'rb')
        photo4 = open(r'C:\Users\Юля\source\repos\PythonApplication2\фото/рулетики3.jpg', 'rb')
        photo5 = open(r'C:\Users\Юля\source\repos\PythonApplication2\фото/рулетики4.jpg', 'rb')
        photo6 = open(r'C:\Users\Юля\source\repos\PythonApplication2\фото/рулетики5.jpg', 'rb')
        photo7 = open(r'C:\Users\Юля\source\repos\PythonApplication2\фото/рулетики6.jpg', 'rb')
        bot.send_photo(message.chat.id, photo=photo1, caption = 'РУЛЕТИКИ ИЗ БЕКОНА С СЫРОМ И ЯЙЦАМИ\n\nНетривиальная закуска, которая идеально подойдёт на праздничный и повседневный стол. Из полосок бекона делаем рулетики и отправляем их в духовку. А из сыра и яиц готовим аппетитную начинку, в которую для скрепления и вкуса добавляем майонез, зелень и чеснок. Затем всё соединяем. Получается очень вкусная и питательная закуска.\n\nПРОДУКТЫ:\n\nБекон - 250 г (8 полосок)\nСыр твёрдый - 180 г\nЯйца - 4 шт.\nМайонез - 80 г\nУкроп свежий - 5 г (1-2 веточки)\nЧеснок - 2 зубчика\nСоль - щепотка (по вкусу)\nПерец свежемолотый (смесь перцев) - на кончике ножа')
        bot.send_photo(message.chat.id, photo=photo2, caption = 'Подготовить продукты по списку.')
        bot.send_photo(message.chat.id, photo=photo3, caption = 'В кастрюлю отправить 3 яйца, залить водой и поставить на огонь. Отварить яйца вкрутую (8-10 минут с момента закипания). Затем залить холодной водой, остудить. Параллельно включить духовку для разогрева до 180 градусов. Из фольги сделать 8 трубочек (по количеству полосок бекона) длиной примерно 10 см и диаметром 2-2,5 см.')
        bot.send_photo(message.chat.id, photo=photo4, caption = 'Каждую трубочку из фольги обернуть беконом. Выложить все заготовки швом вниз на противень, выстеленный пергаментом. Оставшееся яйцо разбить, отделить белок от желтка (белок не понадобится). Смазать заготовки бекона сверху желтком. Запекать бекон в разогретой до 180 градусов духовке 10-15 минут, чтобы трубочки скрепились и подрумянились (ориентируйтесь на особенности своей духовки). Затем бекон остудить, не снимая с фольги.')
        bot.send_photo(message.chat.id, photo=photo5, caption = 'Остывшие яйца очистить, натереть на мелкой тёрке и выложить в глубокую миску. Твёрдый сыр натереть на мелкой тёрке и добавить к яйцам. Зелень укропа промыть и обсушить, измельчить и отправить к сыру и яйцам. Заправить всё майонезом, добавить очищенный и пропущенный через пресс чеснок, соль и перец по вкусу. Тщательно всё перемешать. ')
        bot.send_photo(message.chat.id, photo=photo6, caption = 'Наполнить рулетики из бекона сырно-яичной массой.')
        bot.send_photo(message.chat.id, photo=photo7, caption = 'Рулетики из бекона с сыром и яйцами готовы. Украсить рулетики зеленью и подавать к столу. Приятного аппетита!')
        bot.send_message(message.chat.id, 'Как приготовите, пришлите мне фото готового блюда. Буду очень рад!🥰')
        
        #Десерты
    elif message.text == 'Десерты' or message.text == '/deserts':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)    
        b1 = types.KeyboardButton('Коржики молочные')
        b2 = types.KeyboardButton('Яблочный штрудель')
        b3 = types.KeyboardButton('Чизкейк')
        b4 = types.KeyboardButton('Желе молочно-кофейное')
        b6 = types.KeyboardButton('В меню рецептов')
        markup.add(b1,b2,b3,b4,b6)
        photo = open(r'C:\Users\Юля\source\repos\PythonApplication2\фото/десерты.jpg', 'rb')
        bot.send_photo(message.chat.id, photo=photo, caption = 'В разделе "Десерты" вы найдете множество восхитительных рецептов для сладких угощений. Здесь можно найти рецепты тортов, пирогов, пудингов, муссов, панакот и многих других десертов. От классических шоколадных брауни до изысканных фруктовых десертов — выбор огромен. Приготовьте что-то особенное, чтобы завершить прием пищи вкусным и незабываемым десертом.', reply_markup = markup)

    elif message.text == 'Коржики молочные':
        photo1 = open(r'C:\Users\Юля\source\repos\PythonApplication2\фото/корж.jpg', 'rb')
        photo2 = open(r'C:\Users\Юля\source\repos\PythonApplication2\фото/корж1.jpg', 'rb')
        photo3 = open(r'C:\Users\Юля\source\repos\PythonApplication2\фото/корж2.jpg', 'rb')
        photo4 = open(r'C:\Users\Юля\source\repos\PythonApplication2\фото/корж3.jpg', 'rb')
        photo5 = open(r'C:\Users\Юля\source\repos\PythonApplication2\фото/корж4.jpg', 'rb')
        photo6 = open(r'C:\Users\Юля\source\repos\PythonApplication2\фото/корж5.jpg', 'rb')
        bot.send_photo(message.chat.id, photo=photo1, caption = 'МОЛОЧНЫЕ КОРЖИКИ\n\nПредлагаю приготовить знакомые с детства молочные коржики. Приготовление не займет много времени, и здесь можно обойтись даже без миксера.\n\nПРОДУКТЫ:\n\nМасло сливочное размягчённое (или маргарин) – 100 г\nСахар – 150 г\nЯйцо – 1 шт.\nМолоко – 80 мл\nМука – 350 г\nРазрыхлитель – 10 г')
        bot.send_photo(message.chat.id, photo=photo2, caption = 'Мягкое сливочное масло растираем с сахаром. Добавляем яйцо и молоко, перемешиваем до однородности с помощью венчика. Молоко лучше подогреть до комнатной температуры, чтобы оно хорошо соединилось с остальными ингредиентами.')
        bot.send_photo(message.chat.id, photo=photo3, caption = 'Муку (350 г = 2 стакана объёмом 250 мл + 1 ст. ложка с горкой) объединяем с разрыхлителем и частями вводим к основной массе, замешивая тесто. Замешивать можно, для удобства, сначала ложкой, потом руками.')
        bot.send_photo(message.chat.id, photo=photo4, caption = 'Тесто получается мягкое, эластичное и совсем не липнет к рукам. Включаем духовку и разогреваем до 180 градусов. Раскатываем тесто в пласт 0,5 см толщиной и с помощью вырубки формируем коржики.')
        bot.send_photo(message.chat.id, photo=photo5, caption = 'Выкладываем заготовки на противень, застеленный пергаментной бумагой, на небольшом расстоянии друг от друга. Выпекаем при 180 градусах около 15 минут.')
        bot.send_photo(message.chat.id, photo=photo6, caption = 'Молочные коржики как в детстве готовы!')
        bot.send_message(message.chat.id, 'Как приготовите, пришлите мне фото готового блюда. Буду очень рад!🥰')


    elif message.text == 'Яблочный штрудель':
        photo1 = open(r'C:\Users\Юля\source\repos\PythonApplication2\фото/штрудель.jpg', 'rb')
        photo2 = open(r'C:\Users\Юля\source\repos\PythonApplication2\фото/штрудель1.jpg', 'rb')
        photo3 = open(r'C:\Users\Юля\source\repos\PythonApplication2\фото/штрудель2.jpg', 'rb')
        photo4 = open(r'C:\Users\Юля\source\repos\PythonApplication2\фото/штрудель3.jpg', 'rb')
        photo5 = open(r'C:\Users\Юля\source\repos\PythonApplication2\фото/штрудель4.jpg', 'rb')
        photo6 = open(r'C:\Users\Юля\source\repos\PythonApplication2\фото/штрудель5.jpg', 'rb')
        photo7 = open(r'C:\Users\Юля\source\repos\PythonApplication2\фото/штрудель6.jpg', 'rb')
        bot.send_photo(message.chat.id, photo=photo1, caption = 'ЯБЛОЧНЫЙ ШТРУДЕЛЬ\n\nКлассический яблочный штрудель - это тонкое вытяжное тесто, хрустящая корочка и ароматная сочная начинка! Настоящий яблочный штрудель - просто объедение! Легко и просто!\n\nПРОДУКТЫ:\n\nДля теста:\nМука пшеничная - 250 г + для работы с тестом\nСоль - 0,5 ч. ложки\nЯйцо - 1 шт.\nВода тёплая - 100 мл\nМасло растительное - 20 мл (чуть больше столовой ложки) + для смазывания теста\nМасло сливочное растопленное - 100 г\n*\nДля начинки:\nЯблоки кисло-сладкие - 800 г (6 шт.)\nСухари сдобные молотые - 70 г\nИзюм - 180 г\nСахар - 3 ст. ложки (по вкусу)\nКорица молотая - 7 г\n*\nДля украшения:\nСахарная пудра - по вкусу')
        bot.send_photo(message.chat.id, photo=photo2, caption = 'Готовим вытяжное тесто. Муку просеиваем. Добавляем соль. Перемешиваем. В муке делаем небольшое углубление, добавляем яйцо, растительное масло и тёплую воду. Ложкой собираем тесто в комок.')
        bot.send_photo(message.chat.id, photo=photo3, caption = 'Руками замешиваем эластичное тесто. Чтобы тесто перестало липнуть к рукам, месить нужно минут 10-15. При необходимости присыпаем стол мукой. Тесто смазываем растительным маслом, оборачиваем пищевой плёнкой и оставляем на 30 минут при комнатной температуре.')
        bot.send_photo(message.chat.id, photo=photo4, caption = 'Готовим начинку. Изюм промываем и заливаем горячей водой минут на 10. Затем воду сливаем, изюм обсушиваем бумажным полотенцем. Яблоки очищаем от кожуры и сердцевины и нарезаем небольшими кусочками. К яблокам добавляем изюм, сухари, сахар и корицу. Хорошо перемешиваем начинку.')
        bot.send_photo(message.chat.id, photo=photo5, caption = 'Включаем духовку для разогрева до 190 градусов. Противень застилаем бумагой для выпечки. Рабочую поверхность и тесто присыпаем мукой. Скалкой раскатываем тесто от центра к краям. Посыпаем тыльную сторону рук мукой. Подкладываем руки (полусогнутые кулачки) под тесто и аккуратно растягиваем его во всех направлениях. Тесто эластичное и хорошо вытягивается.')
        bot.send_photo(message.chat.id, photo=photo6, caption = 'Пласт теста перекладываем на салфетку. Если края толстые, то лучше их срезать. Немного отступая от края, выкладываем начинку горкой по всей длине. Прижимаем начинку. Сворачиваем тесто с начинкой в рулет, помогая салфеткой.')
        bot.send_photo(message.chat.id, photo=photo7, caption = 'Выпекаем яблочный штрудель в разогретой духовке минут 30, до золотистого цвета. Подаём яблочный штрудель с шариком сливочного мороженого или со взбитыми сливками. Приготовьте и порадуйте себя и своих близких вкусным десертом! Приятного Вам аппетита!')
        bot.send_message(message.chat.id, 'Как приготовите, пришлите мне фото готового блюда. Буду очень рад!🥰')

    elif message.text == 'Чизкейк': 
        photo1 = open(r'C:\Users\Юля\source\repos\PythonApplication2\фото/чизкейк.jpg', 'rb')
        photo2 = open(r'C:\Users\Юля\source\repos\PythonApplication2\фото/чизкейк1.jpg', 'rb')
        photo3 = open(r'C:\Users\Юля\source\repos\PythonApplication2\фото/чизкейк2.jpg', 'rb')
        photo4 = open(r'C:\Users\Юля\source\repos\PythonApplication2\фото/чизкейк3.jpg', 'rb')
        photo5 = open(r'C:\Users\Юля\source\repos\PythonApplication2\фото/чизкейк4.jpg', 'rb')
        photo6 = open(r'C:\Users\Юля\source\repos\PythonApplication2\фото/чизкейк5.jpg', 'rb')
        photo7 = open(r'C:\Users\Юля\source\repos\PythonApplication2\фото/чизкейк6.jpg', 'rb')
        bot.send_photo(message.chat.id, photo=photo1, caption = 'ЧИЗКЕЙК\n\nЕсли вы ищете хороший рецепт чизкейка, то вы его нашли. Чизкейк "Нью-Йорк" с нежной шелковистой текстурой и легкими нотками лимона. Чизкейк очень простой в приготовлении и сам процесс занимает немало времени, но, поверьте, результат того стоит!\n\nПРОДУКТЫ:\n\nДля основы:\nПеченье песочное или несоленые крекеры - 350 г\nМасло сливочное - 200 г + для смазывания формы\nСахар - 2 ст. л.\n*\nДля начинки:\nСыр сливочный (филадельфия) - 1 кг\nСахар - 250 г\nКрахмал кукурузный - 3 ст. л.\nСок лимонный - 2 ст. л.\nЦедра лимонная - 2 ч. л.\nЯйца - 5 шт.\nВанильный экстракт - 2 ч. л.\nСметана 20% - 100 г\n*\nДля покрытия:\nСметана 20% - 150 г\nСахарная пудра - 2 ст. л.\nСок лимонный - 2 ч. л.')
        bot.send_photo(message.chat.id, photo=photo2, caption = 'Готовим основу для чизкейка. В блендере измельчаем печенье в мелкую крошку. Вливаем в крошку из печенья растопленное сливочное масло, добавляем сахар и хорошо перемешиваем.')
        bot.send_photo(message.chat.id, photo=photo3, caption = 'Дно формы диаметром 22 см застилаем бумагой для выпечки, края смазываем сливочным маслом. Выкладываем крошку в форму, утрамбовываем дно, по желанию формируем стенки. Выпекаем основу для чизкейка при 175°С 10 минут, затем полностью остужаем.')
        bot.send_photo(message.chat.id, photo=photo4, caption = 'Перемешиваем сливочный сыр до тех пор, пока он не станет мягким и гладким (если используете миксер, старайтесь взбивать на очень низких оборотах миксера). Добавляем сахар маленькими порциями и продолжаем перемешивать миксером.\nСтарайтесь не слишком сильно взбивать. Если масса будет перенасыщена пузырьками воздуха, при выпечке чизкейк может вздуться и потрескаться. Поэтому перемешиваем очень аккуратно, можно использовать венчик вместо миксера. Добавляем кукурузный крахмал, лимонный сок, лимонную цедру, ванильную эссенцию и взбиваем буквально 15-20 секунд.\nЗатем добавляем сметану и опять взбиваем на низкой скорости миксера 15-20 секунд.Добавляем по одному яйцу, каждый раз хорошо перемешиваем, после каждого добавления.')
        bot.send_photo(message.chat.id, photo=photo5, caption = 'Выливаем сырную начинку на основу из печенья и хорошо разравниваем поверхность. ВАЖНО! Выпекать чизкейк четко по инструкции, тогда он не потрескается и не пересушится.\n*\nВыпекаем чизкейк первые 10 минут при температуре 200°С, затем уменьшаем температуру до 120°С и выпекаем еще 60-90 минут. После выпечки выключаем духовку и оставляем чизкейк с закрытой дверцей на 30 минут. Потом дверцу духовки приоткрываем и оставляем еще на 30 минут. Время выпекания может варьироваться в зависимости от вашей духовки, поэтому края чизкейка должны схватиться, только центр будет немного жидковатый и шаткий.')
        bot.send_photo(message.chat.id, photo=photo6, caption = 'Пока чизкейк выпекается, приготовим сметанный слой. Перемешиваем сметану с сахарной пудрой и лимонным соком.\nВынимаем чизкейк из духовки и еще горячим смазываем сметанным кремом по всей поверхности. Затем оставляем чизкейк остывать при комнатной температуре.\nПосле полного остывания отправляем чизкейк в холодильник минимум на 6-8 часов до нарезки и подачи на стол.')
        bot.send_photo(message.chat.id, photo=photo7, caption = 'Аккуратно освобождаем от формы, в которой выпекался чизкейк. Перекладываем его на блюдо для торта и по желанию украшаем чизкейк свежими фруктами и ягодами. Чизкейк "Нью-Йорк" готов.\nПриятного аппетита и удачной вам выпечки!')
        bot.send_message(message.chat.id, 'Как приготовите, пришлите мне фото готового блюда. Буду очень рад!🥰')

    elif message.text == 'Желе молочно-кофейное':
        photo1 = open(r'C:\Users\Юля\source\repos\PythonApplication2\фото/желе.jpg', 'rb')
        photo2 = open(r'C:\Users\Юля\source\repos\PythonApplication2\фото/желе1.jpg', 'rb')
        photo3 = open(r'C:\Users\Юля\source\repos\PythonApplication2\фото/желе2.jpg', 'rb')
        photo4 = open(r'C:\Users\Юля\source\repos\PythonApplication2\фото/желе3.jpg', 'rb')
        photo5 = open(r'C:\Users\Юля\source\repos\PythonApplication2\фото/желе4.jpg', 'rb')
        bot.send_photo(message.chat.id, photo=photo1, caption = 'МОЛОЧНО-КОФЕЙНОЕ ЖЕЛЕ\n\nМолочно-кофейное желе - очень красивый и оригинальный десерт для любителей кофе. Контрастное сочетание кофейного и молочного слоёв выглядит очень эффектно, поэтому такой десерт вполне можно подать гостям в качестве альтернативы торту. Ну а технология приготовления такого лакомства очень проста, так что можно смело приступать к готовке!\n\nПРОДУКТЫ:\n\nМолоко - 500 мл\nКофе растворимый - 4 ч. ложки\nСахар - 150 г\nЖелатин - 30 г')
        bot.send_photo(message.chat.id, photo=photo2, caption = 'Желатин залить 200 мл холодной кипяченой воды и оставить набухать. Приготовить кофе. Растворимый кофе залить 500 мл воды, добавить 80 г сахара. В горячий кофе добавить половину желатина и перемешать до полного растворения.')
        bot.send_photo(message.chat.id, photo=photo3, caption = 'Молоко вскипятить, добавить 70 г сахара и снять с огня. В горячее молоко добавить оставшийся желатин и перемешать до полного растворения. ')
        bot.send_photo(message.chat.id, photo=photo4, caption = 'В стаканы или креманки налить кофе с желатином слоем примерно 1-2 см. Поставить в холодильник до полного застывания. У меня кофейный слой застыл примерно за 40 минут. На застывший кофейный слой налить молоко с желатином также слоем 1-2 см и снова отправить в холодильник для застывания.')
        bot.send_photo(message.chat.id, photo=photo5, caption = 'Таким образом заполнить стаканы до верха, давая застыть каждому слою. Молочно-кофейное желе готово! Приятного аппетита!')
        bot.send_message(message.chat.id, 'Как приготовите, пришлите мне фото готового блюда. Буду очень рад!🥰')

bot.polling(none_stop=True)

