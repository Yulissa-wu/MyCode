
　　　　　　　　　1.建立虛擬機(AWS-EC2 or GCP-Compute Engine，此次使用AWS-EC2)
　　　　　　(2-1、2-2擇一做)
　　　　　　　　　2-1.在創建虛擬機時填入UserData下載docker
　　　　　　　　　2-2-1.創建虛擬機後再mobaXterm填入Public IP address(EC2虛擬機介面勾選虛擬機->Connect)、Specify username、Use private key
　　　　　　　　　2-2-2.重開機後Docker version
           容器
　　　　　　　　　3.docker ps -a：查看docker容器一覽，status Exited容器關閉
         　　　　4.docker run 
                5.docker rm <container ID>
                6.docker search <映像檔名稱>
                7.docker images：查看docker映像檔一覽
                



