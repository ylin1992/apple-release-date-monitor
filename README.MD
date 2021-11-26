# MacBook Pro Release Date Monitor
- This project provides a web-crawler keeping searching the release date of 14-inch 2021 MacBook Pro in Taiwan.
- A feed showing the current releasing status is updated to user via email in every two hours.
- Once the status is changed, a notification email will be delivered to the user immediately.

## Hosting
The project is hosted on Heroku, but user is also allowed to run it locally.

## Getting started
1. **Python 3.6**: Install Python 3.6 by following the instructions from [Python website](https://www.python.org/downloads/)
2. **Dependencies**: Install packages by ```pip3 install -r requirements.txt```
3. **Setup up environment variables**: Go to ```setup.sh``` and fill in the required fields by the following instructions.
- Run locally: 
    - If you are running the crawler locally, fill in ```SENDER_EMAIL``` (your sender email), ```SENDER_PWD``` (your sender password) and ```RECEIVER_EMAIL``` (account receving notifications). Email-sending feature is implemented by SSL if we run locally.
    - [Download a chromedriver](https://chromedriver.chromium.org/) and put it in the root directory
    ***Note***: Please make sure your are using the same driver version of google chrome installed in your computer.
- Hosted on Heroku: Complete the instructions abovementioned and create a [SendGrid](https://sendgrid.com/) account, filling your api key in the ```SENGRID_API_KEY``` field. For the rest part of the deployment, refer to [Deploy on Heroku section](Deploy-on-Heroku)

## Run the program
### Run locally
- Run the program by the following command:
```
python3 main.py
```
- Check the result, the result will be like:
```
[FETCH 1]: 推出日期，敬請期待。
[FETCH 2]: 推出日期，敬請期待。
[FETCH 3]: 推出日期，敬請期待。
[FETCH 4]: 推出日期，敬請期待。
[FETCH 5]: 推出日期，敬請期待。
```
### Deploy on Heroku
- Create an app on Heroku and set it as an remote repository
```
heroku git:remote -a <YOUR_HEROKU_APP_NAME>
```
- At the ```Settings -> Buildpacks``` tag, add the following buildpacks:
    - ```heroku/python```
    - ```https://github.com/heroku/heroku-buildpack-google-chrome```
    - ```https://github.com/heroku/heroku-buildpack-chromedriver```
- If you are not using a paid dynos subscription, it is recommended using [SendGrid](https://sendgrid.com/) as an email-sending service provider
    - Create an account
    - Create an API
    - Copy the key and save it wisely ***You will not be granted to look up the key again, make sure you have had the key safely saved before closing the page***
    - Paste the key into ```SENDGRID_API_KEY``` in ```setup.sh```
    - Run ```git push heroku main``` to build and run code on Heroku

### Stop and relaunch the program
By setting worker number to zero, the program stops:
```
heroku ps:scale worker=0
```
On the contrary, start the program by setting worker number > 0 (depending on your Heroku subscription plan)
```
heroku ps:scale worker=1
```
