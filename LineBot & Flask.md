<h1>LineBot</h1>

    Providers->Create->輸入Provider Name
<img src="https://user-images.githubusercontent.com/97188330/159474601-ee157718-1622-4d26-b147-000cf4685c68.png" width="500" height="250" alt="MySQL"/><br/>
    
    Channels分頁->Create a new channel->Messaging API
<img src="https://user-images.githubusercontent.com/97188330/159476935-8fbbc7b2-e97f-42d7-8b16-d80b8d2b9952.png" width="500" height="250" alt="MySQL"/><br/>

    Channels Name：LineBot機器人名稱
    Channel Description：機器人描述
    Category：頻道分類
    Subcategory：頻道子分類
    ->Create
    
    紀錄開發過程重要的欄位資訊：
    <<Basic settings分頁>>
    1.Channel secret
    <<Messaging API分頁>>
    1.Webhook URL
    2.Channel access token

<h1>Heroku</h1>

    Term of Service->Accept
    New -> Create New App
    Deploy using Heroku Git -> Heroku CLI -> Install Heroku CLI
    開啟power shell -> 輸入heroku
    Setting -> Buildpacks -> Add buildpack -> Python
    
    heroku login
    git init
    heroku git:remote -a Heroku_App_Name
    
    修改config.ini：
    [line-bot]
    channel_access_token = Your_Channel_access_token
    channel_secret = Your_Channel_Secret
    cd <目錄>
    pip3 install -r requirement.txt
    python3 <要執行的檔案>
    
<h1>Flask</h1>

    webhook
<img src="https://user-images.githubusercontent.com/97188330/159490793-8a498af3-8cc7-4b5e-895d-7eb4ec3e74a3.png" width="700" height="500" alt="MySQL"/><br/>
    
此聊天機器人 app 需要一個 channel access token 以進行 API call，以及一個 webhook URL 以接收來自 LINE Platform 的 webhook payload。
