
<h1>架構</h1>

* Monolithic Server單體式系統架構

      將資料庫與快取置於同一個伺服器內
      
<img src="https://user-images.githubusercontent.com/97188330/215191264-24432a5b-372f-4a7b-bc8e-47087d32f0c6.png" width="700" height="280" alt="MySQL"/><br/>      
    
* Microservice微服務

      各服務互相拆開
      
<img src="https://user-images.githubusercontent.com/97188330/215177514-dcc8b85c-799d-48b2-a8c3-454eb58ee203.png" width="1000" height="480" alt="MySQL"/><br/>

<h1>前端</h1>

* CSR - Client-Side Rendering（客戶端渲染）

      較適合靜態網頁，渲染時依照客戶端環境取決速度
        
* SSR - Server-Side Rendering（伺服器端渲染）

      較適合動態網頁，渲染時透過伺服器獲取資料，依照伺服器處理速度來取決速度
      
<h1>後端</h1>

* 網域名稱系統(DNS)

      將網址轉為IP、防止DDos攻擊、快取機制
      
* 反向代理

      可以做到附載平衡(處理大量請求，決定哪些請求接收/不接收，如果同一個API短時間一直發送請求的阻擋)
      SSL避免請求被竊聽/竄改(進反向代理前HTTPS->進反向代理後HTTP)
      根據不同網址決定對應哪些服務(API伺服器、Web伺服器、靜態網頁)
      
* 快取

      用於存放不常變動且產生成本較高的資料
      
* 資料庫

      存放較常變動的資料    
      
<h1>AI</h1>

* 運算引擎

      雲服務運算引擎        
      
* AIOT

* Queue
      透過
