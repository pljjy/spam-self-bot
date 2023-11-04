# Telegram bot for spamming all users in a group
It takes every user from a group that you need and sends them text message that you need

*BUT* When it sends the message to about 30 people, it stops because of the PeerFlood error, pyrogram.errors.PeerFlood didn't fix it at all, so if you want to 
spam a lot, you may need several accounts. If you know the solution for PeerFlood let me know, that would be great

## How to use
1. install python 3.11+ If you are not familiar with python and installing it using windows via installer from python.org,
 you need to check the box, when you are installing you should: 
        make sure Add python.exe to path is checked > choose customize installation > make sure pip is checked
2. cd to this project, `pip install -r requirements.txt`
3. remove .template from the file api_ids.template
4. add your [api id and api hash](https://core.telegram.org/api/obtaining_api_id) to the file api_ids. Make sure that api id (the one that should only contain numbers) 
is in the first line and api hash is in the second line
5. run `python3.11 main.py`
6. It will ask you to login to your telegram account, dw it's a pyrogram thing (the library that the bot uses), it will only ask you one time and neither I nor pyrogram will get
your information, you need it so the bot can "login" into your account to do things
7. type '.gu' in a group you want to get users that you want to spam. The message will be instantly deleted, *and* you may need to wait some time until it collects every user 
*ALSO* every time you type .gu it rewrites all the data in the file with user ids
8. type '.sp' to start sending your message to all the users you collected. If it stops with an error PeerFlood (or something like that) then you may need to wait, I have no idea how much you 
need to wait because I haven't found any way to handle that exception
