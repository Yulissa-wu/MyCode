<h1>製作開機磁碟</h1>

           1. 插入 microSD
           2. 使用 SD Memory Card Formatter 格式化 microSD
           3. 下載 Raspberry Pi OS with Desktop
           4. 使用 Etcher 燒錄 Raspberry Pi OS 至 microSD

<h1>Raspberry Pi 3+</h1>
<img src="https://user-images.githubusercontent.com/97188330/157580453-fab0518d-36d2-4de5-960d-09e73c6a2893.jpg" width="500" height="350" alt="MySQL"/><br/>
<h1>實機使用</h1>
<img src="https://user-images.githubusercontent.com/97188330/157582359-b9448838-311c-4069-99db-2889381cd738.jpg" width="500" height="350" alt="MySQL"/><br/>
<h1>MQTT</h1>

<h4>Server(LocalComputer、VM) MQTT Broker</h4>
          1. 登入 console.cloud.google.com
          2. 建立並切換至新專案
          3. 啟用 Compute Engine
          4. Compute Engine > VM 執行個體 > 建立執行個體
                  名稱 mqtt
                  區域 us-central1/ 區域 us-central1-c
                  機器類型 e2-micro
                  開機磁碟 > 作業系統 Ubuntu/ 版本 Ubuntu 18.04 LTS
                  管理、安全性、磁碟、網路、單獨租用 > 網路 > 網路標記 mqtt
                  網路介面 > 外部 IP > 建立 IP 位址 > mqttip
          5. 虛擬私有雲網路 > 防火牆 > 建立防火牆規則
          6. 名稱 mqttfw
          7. 相符時執行的動作 >目標標記 mqtt
          8. 來源 IP 範圍 0.0.0.0/0
          9. 通訊協定和埠 > 指定的通訊協定和埠 > tcp 1883
          10. (optional) DNS 指向外部 IP 位址 (mqttip)
          11. SSH 連線 GCE VM 執行個體 mqtt
          12. sudo apt-get update; sudo apt-get install -y mosquito; sudo timedatectl set-timezone Asia/Taipei
                                <h4>MQTT Subscriber</h4>
          1. pip install paho-mqtt
          2. import paho.mqtt.client as mqtt
             def on_connect(client, userdata, flags, rc):
                 print("Connected with result code "+str(rc))
                 client.subscribe("rollcall/#")
             def on_message(client, userdata, msg):
                 print(msg.topic+" "+str(msg.payload))
          3. YOUR_BROKER = 'YOUR_BROKER'
            client = mqtt.Client()
            client.on_connect = on_connect
            client.on_message = on_message
            client.connect(YOUR_BROKER, 1883, 60)
            client.loop_forever()
      <h4>Client MQTT Publisher</h4>
          1. from time import strftime
             from paho.mqtt import publish
             YOUR_BROKER = 'YOUR_BROKER'
             topic = 'rollcall'
             msg = f'Mary sign in on {strftime("%Y/%m/%d-%H:%M:%S")}'
             publish.single(topic, msg, hostname=YOUR_BROKER)
             msgs = [['rollcall/register', f'Jerry on {strftime("%Y/%m/%d-%H:%M:%S")}'],
                    ['rollcall/signin', f'Eric on {strftime("%Y/%m/%d-%H:%M:%S")}']
                    ]
             publish.multiple(msgs, hostname=YOUR_BROKER)
