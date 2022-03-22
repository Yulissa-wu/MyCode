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
    channel_access_token = Your_Channel_access_token
    channel_secret = Your_Channel_Secret
    
    
