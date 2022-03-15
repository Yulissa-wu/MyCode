<h1>設定heroku APP</h1> 

      New -> Create New App
      Deploy using Heroku Git -> Heroku CLI -> Install Heroku CLI
      開啟power shell -> 輸入heroku
      Setting -> Buildpacks -> Add buildpack -> Python
      More -> View log

      heroku login
      git init
      heroku git:remote -a Heroku_App_Name
<h1>增加付款資訊</h1>

      Account Setting->Billing->Billing Information->Add Credit Card
<h1>heroku add-ons</h1>  
<img src="https://user-images.githubusercontent.com/97188330/158340374-c760d886-1cff-4986-a223-c0905f993b5a.png" width="1300" height="500" alt="MySQL"/><br/>

      在heroku add-ons選擇ClearDB MySQL->Install ClearDB MySQL->Submit Order Form
<img src="https://user-images.githubusercontent.com/97188330/158340762-b21ccd0c-a213-4003-855b-b0d04e650c1c.png" width="1300" height="500" alt="MySQL"/><br/>
     
      點擊resources下的Add-ons的ClearDB MySQL 
<h1>獲得資料庫相關資訊</h1>
<img src="https://user-images.githubusercontent.com/97188330/158341424-8eb28b1a-a459-48e7-af0d-de2c2c5860f2.png" width="1100" height="300" alt="MySQL"/><br/>
<img src="https://user-images.githubusercontent.com/97188330/158341942-c1e49b91-c3ad-4d92-894b-968ba3ade3d8.png" width="1100" height="400" alt="MySQL"/><br/>
      
      點擊資料庫名稱->Community Edition->System Information，獲得Access Credentials
      
<h1>佈署在MySQL-workbench上</h1>
<img src="https://user-images.githubusercontent.com/97188330/157156330-47185940-f240-41dd-a7f9-74452fa5f510.png" width="700" height="450" alt="MySQL"/><br/>
      
      heroku login->heroku config，獲得host與database，輸入到workbench做連接
