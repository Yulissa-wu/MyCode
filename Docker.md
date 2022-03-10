<h5>1.建立虛擬機(AWS-EC2、GCP-Compute Engine)</h5>
<h5>2.在創建虛擬機時填入UserData</h5>

      #!/bin/bash
      yum update -y
      yum install -y git
      amazon-linux-extras install docker
      yum install docker -y
      service docker start
      systemctl enable docker
      usermod -a -G docker ec2-user
      curl -L
      "https://github.com/docker/compose/releases/download/1.29.0/docker-compose-$(uname
      -s)-$(uname -m)" -o /usr/local/bin/docker-compose
      chmod +x /usr/local/bin/docker-compose
      ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose
