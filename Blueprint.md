
<h1>架構</h1>

* Monolithic Server（單體式系統架構）

      將資料庫與快取置於同一個伺服器內
      
<img src="https://user-images.githubusercontent.com/97188330/215191264-24432a5b-372f-4a7b-bc8e-47087d32f0c6.png" width="700" height="280" alt="MySQL"/><br/>      
    
* Microservice（微服務）

      各服務互相拆開
      
<img src="https://user-images.githubusercontent.com/97188330/215177514-dcc8b85c-799d-48b2-a8c3-454eb58ee203.png" width="1000" height="480" alt="MySQL"/><br/>

<img src="https://user-images.githubusercontent.com/97188330/233123792-93387866-4146-4e91-bda3-647b89c44445.png" width="1000" height="200" alt="MySQL"/><br/>

<h1>前端</h1>

* CSR - Client-Side Rendering（客戶端渲染）

      較適合靜態網頁，渲染(將程式碼轉換為可視的圖像或畫面的過程)。時依照客戶端環境取決速度
      >>會用到的技術有：HTML、CSS、JavaScript
        
* SSR - Server-Side Rendering（伺服器端渲染）

      較適合動態網頁，渲染時透過伺服器獲取資料，依照伺服器處理速度來取決速度
      >>會用到的技術有：HTML、CSS、JavaScript、Django、AJAX、MySQL、Nginx、Java
      
<h1>後端</h1>

* 網域名稱系統(DNS)

      將網址轉為IP、防止DDos攻擊
      >>會用到的技術有：Cloudflare DNS、Verisign DNS
      
* 反向代理(Reverse proxy)

      可以做到附載平衡load balancing(處理大量請求，決定哪些請求接收/不接收，如果同一個API短時間一直發送請求的阻擋)
      SSL憑證避免請求被竊聽/竄改(進反向代理前HTTPS->進反向代理後HTTP)
      根據不同網址決定對應哪些服務
      >>會用到的技術有：ngrok
      
* APIserver
 
      >>會用到的技術有：Django、Flask
      
* Webserver

      >>會用到的技術有：Nginx
      
* 快取(Cache)

      用於存放不常變動且產生成本較高的資料
      >>會用到的技術有：Redis
      
* 資料庫(DB Server)

      存放較常變動的資料    
      >>會用到的技術有：MySQL
      
<h1>AI</h1>

* 運算引擎

      透過遠端程式透過API伺服器去呼叫運算引擎內的東西(透過電腦呼叫另一個電腦的服務與元件)
      
      通用AI運算引擎可以處理多種類型的AI任務，比如圖像識別、自然語言處理、聲音識別等。常見的通用AI運算引擎有TensorFlow、PyTorch、Caffe等。
      
      特定AI運算引擎則專門處理某種類型的AI任務，比如語音識別、影像處理、物體追蹤等。這些特定AI運算引擎通常具有更高的效能和更低的延遲，能夠實現更高的實時性。
      常見的特定AI運算引擎有OpenCV、Kaldi、MXNet等。
      >>會用到的技術有：TensorFlow、PyTorch、Caffe、OpenCV、Kaldi、MXNet
      
* AIOT

      Broker
      >>會用到的技術有：

* Queue

      排程
      >>會用到的技術有：
      
<h1>相關資料</h1>

`API`
<a href="https://www.da-vinci.com.tw/tw/blog/api#nav-item-3">API</a>
<br>
`TCP/UDP`
<a href="https://nordvpn.com/zh-tw/blog/tcp-udp-bijiao/">TCP/UDP</a>
<br>
`RPC`
<a href="https://learn.microsoft.com/zh-tw/windows/win32/rpc/how-rpc-works">RPC</a>
<br>
`HTTP/HTTPS`
<a href="https://tw.alphacamp.co/blog/http-https-difference">HTTP/HTTPS</a>
<br>
