# README #

----------------------

# RU

Исходный код для Python3 бота для Telegram.

В настоящее время бот доступен по имени @music_downloader_python_bot в Telegram на постоянной основе.
Пользователь может прислать боту название песни, которую он желает скачать.
Бот в автоматическом режиме делает запросы пользователям с помощью Telegram API, сохраняет их и делает соответствующий запрос на сайте свободного распространения музыки zaycev.net/.
Далее, выбирает самую релевантную песню и отсылает пользователю ссылку на нее.

Исходный код бота разделен на несколько модулей. 
Модуль link_cutter отвечает за сокращение спаршенных ссылок на скачивание
Модуль telegram_bot_helper работает с получением и отправлением сообщений между сервером и пользователем.
Модуль get_request - это интерфейс работы с POST- и GET- http-запросами на основе модуля flask.

В данный момент бот работает в урезанной бета-версии, а именно, Telegram-кнопки на скачивание mp3-файлов внутри диалогов с пользователем появляются не всегда. 
Данный баг будет устранен в последующих версиях путем скачивания на сервер общего доступа самих mp3-файлов песен и отправки их напрямую через бота как прикреплленный документ.

----------------------

# EN

The source code for the Python3 bot for Telegram.

Currently, the bot is accessible by the name @music_downloader_python_bot in Telegram on a permanent basis.
The user can send to the bot the name of the song he wants to download.
The bot automatically makes inquiries to users using the Telegram API, saves them and makes an appropriate request on the free music distribution site zaycev.net/.
Next, selects the most relevant song and sends the user a link to it.

The bot source code is divided into several modules. 
The link_cutter module is responsible for reducing parsed download links
The telegram_bot_helper module works with receiving and sending messages between the server and the user.
The get_request module is the interface for working with POST and GET-http requests based on the flask module.

At the moment the bot is working in a stripped-down beta version, namely, the Telegram buttons for downloading mp3 files inside the dialogs with the user do not always appear.
This bug will be fixed in next versions by downloading mp3 files of songs themselves to the public server and sending them directly via bot as an attached document.

----------------------

(c) Sodikov M., DIHT MIPT 2018.
