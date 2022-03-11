
　　　　　　　　　1.建立虛擬機(AWS-EC2 or GCP-Compute Engine，此次使用AWS-EC2)
　　　　　　(2-1、2-2擇一做)
　　　　　　　　　2-1.在創建虛擬機時填入UserData下載docker
　　　　　　　　　2-2-1.創建虛擬機後再mobaXterm填入Public IP address(EC2虛擬機介面勾選虛擬機->Connect)、Specify username、Use private key
                      sudo yum update -y：更新yum的套件庫清單 
　　　　　　　　　　　　sudo yum install -y git：安裝git
　　　　　　　　　　　　sudo amazon-linux-extras install docker -y：用amazon linux的擴展套件安裝docker
　　　　　　　　　　　　sudo yum install docker -y：安裝docker
　　　　　　　　　　　　sudo service docker start：啟用docker
　　　　　　　　　　　　sudo systemctl enable docker：常駐docker
　　　　　　　　　　　　sudo usermod -a -G docker ec2-user：新增EC2使用者到docker的群組
　　　　　　　　　　　　sudo curl -L"https://github.com/docker/compose/releases/download/1.29.0/docker-compose-$(uname-s)-$(uname -m)" -o /usr/local/bin/docker-compose：下載docker-compose
　　　　　　　　　　　　sudo chmod +x /usr/local/bin/docker-compose：更改docker-compose的執行權限
　　　　　　　　　　　　sudo ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose：設定軟連結，讓docker在任何使用者都可以操作
                      
　　　　　　　　　2-2-2.重開機後Docker version
           容器
　　　　　　　　　3.docker ps -a：查看docker容器一覽，status Exited容器關閉
         　　　　4.docker run --name <要取的名字>：建立容器並取名
                5.docker rm <容器 ID>
                6.docker search <映像檔名稱>
           映像檔
                7.docker images：查看docker映像檔一覽
           docker-compose
                8.下載docker-compose
                9.docker-compose --version
                

