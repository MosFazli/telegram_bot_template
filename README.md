### telegram_bot_Template
# Telegram bot template with flask, The help file is also available for free use on the pythonanywhere site

## Lets Start
First thing first you should register or login in [http://](https://www.pythonanywhere.com/)

If this is the first time you are using this site or you do not have an account, follow the steps below in order
![image](https://user-images.githubusercontent.com/69136464/185737678-75313085-5e7d-4d32-aea9-de7c067b6e69.png)

You can also using Beginner: Free account
![image](https://user-images.githubusercontent.com/69136464/185737732-faeb70fa-6686-4dfb-b9c4-548d4f6f2426.png)

Fill out the form below
![image](https://user-images.githubusercontent.com/69136464/185737870-541c53f6-ed67-4725-b546-b2d699d3a3c5.png)

and Done! your account has been created. Site is refresh and Tour is started, you can skip tour.
![image](https://user-images.githubusercontent.com/69136464/185737984-998652ee-a323-4582-b358-514fab2b472d.png)


# OK, now you have an account, Let's do the next steps
Select the "Web" tab from the top menu and click on the "Add a new web app" field on the opened page.
![image](https://user-images.githubusercontent.com/69136464/185738200-b2f00e35-cdef-4720-a7e7-c824a8aa2a69.png)


After that choose next >>
![image](https://user-images.githubusercontent.com/69136464/185738264-0b1c67e3-6512-4538-a6ac-990e22fc05cc.png)

choose Flask App
![image](https://user-images.githubusercontent.com/69136464/185738282-f4fc9212-8019-4743-81bf-01d5011664b3.png)

and select a version of Python, for example I using lastest version in here, Version 3.9
![image](https://user-images.githubusercontent.com/69136464/185738317-be38d47b-e92e-491e-af8f-eedc30467197.png)

in the next step, Enter Path of your File, This is optional, but i suggest enter Good name
![image](https://user-images.githubusercontent.com/69136464/185738379-9e1f3c9b-8a68-4613-b485-c25ec5c22936.png)

after you created web app, you should see a page like this
![image](https://user-images.githubusercontent.com/69136464/185756421-99854fbc-c833-4c7c-a613-6517a8d08c34.png)
this is web app settings and you should configure your app from this page in future

now you go to Files tab from top menu
![image](https://user-images.githubusercontent.com/69136464/185756481-a9ae0c7a-e21d-4f5c-915b-8708f9baa1cb.png)

and go to your Flask web application folder and delete flask_app.py and in new page that opened, it's named Are you sure?, click OK
![image](https://user-images.githubusercontent.com/69136464/185756578-4a803f32-3f02-4cdf-a1ac-80efe9f268d3.png)

now from Upload a file button, upload main.py that you downloaded from Github
![image](https://user-images.githubusercontent.com/69136464/185756638-d2c748c3-890e-4d5b-9600-0934ff3be2eb.png)
![image](https://user-images.githubusercontent.com/69136464/185756672-26f51e9b-a1cf-4ce4-a499-466c92027838.png)
and wait a little to upload, and done, you should see directory like this:
![image](https://user-images.githubusercontent.com/69136464/185756701-cdf233f9-233e-424c-b80d-e18fd54ce24b.png)

now set change main.py file with click on that and change your bot Token to YOUR_BOT_TOKEN variable
![image](https://user-images.githubusercontent.com/69136464/185757180-31f6bdc8-aecf-4aad-b6d3-3714f393a152.png)
should be like this:
![image](https://user-images.githubusercontent.com/69136464/185757211-1eac1fdd-03da-47c8-9215-cd2e8cb195d2.png)
and save file

now go back to Web tab from top bar, in the Code section, click on WSGI configuration file to go for config Bot
![image](https://user-images.githubusercontent.com/69136464/185756870-a3ae969d-70f3-4b43-a612-dff85e676f8d.png)
just change flask_app variable to main, save file and come back to Web tab:
![image](https://user-images.githubusercontent.com/69136464/185756981-139770ba-876b-45ff-a297-298e8bc37276.png)
![image](https://user-images.githubusercontent.com/69136464/185757727-660f13a0-c88e-414d-8019-571c60498d64.png)


almost done, you should just set webhook.
in set webhook, you tell telegram that this bot following this url, or web app
Format of URL like this:
https://api.telegram.org/bot{my_bot_token}/setWebhook?url={url_to_send_updates_to}
you should change {my_bot_token} to your token and {url_to_send_updates_to} to your web app in pythonanywhere
for example, your token is 5494036016:AAFo3IOj2K7QTqq_n7hy5S5V4aDKM2wS7P0 and your web app is http://mostafafazli.pythonanywhere.com
the url is:
https://api.telegram.org/bot5494036016:AAFo3IOj2K7QTqq_n7hy5S5V4aDKM2wS7P0/setWebhook?url=http://mostafafazli.pythonanywhere.com
