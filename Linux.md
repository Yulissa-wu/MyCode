      <<查詢>>	
      1. man：查詢指令功能
      2. man -k：以關鍵字查詢指令
      3. apropos：以關鍵字查詢指令
      4. info：查詢指令功能
      5. whatis：查詢指令功能
      6. help：查詢指令功能


	1. ifconfig：查詢網路介面卡設定
	2. su：切換帳號成超級使用者（root）
	3. yum -y install 套件名：下載套件
	4. tree 目錄名稱：樹狀圖
	5. tmux：一個終端機視窗多個分割


	1. mkdir：新增目錄
	2. rmdir：刪除空目錄
	3. touch：新增、修改時間戳記
	4. rm：刪除檔案或目錄
	5. cp：複製檔案或目錄
	6. mv：移動檔案或目錄


	1. wc：計算字數
	2. cat/tac/nl：顯示檔案內容（正向/反向/顯示行號）
	3. head/tail：顯示指定的檔案從頭/從尾開始的行數
	4. more/less：分頁顯示檔案內的資料（檔案內容）
	5. >導出：將放在左邊的東西導出到右邊（覆蓋/附加）
	6. <導入：將放在右邊的東西導入左邊
	7. |管線：把前一個指令的stdout當作後一個指令的stdin
	8. tee：同時將資料流送到終端機、檔案
	9. `指令`/$(指令)：嵌入的指令會優先執行


	1. tr：取代/刪除字元
	2. seq 開始 間隔 結尾：產生序列數字
	3. sort 檔案：將檔案內的資料排序，並顯示在螢幕上
	4. uniq：將相鄰的檔案內容去重複並顯示（不會更動到檔案內容）
	5. split/cat：檔案分割/合併
	6. paste/join：檔案內容左右合併
	7. cut剪下：剪切需要的部分


	1. echo $PATH：檢視環境變數組成的所有路徑
	2. which 指令：找出指令在哪個資料夾下
	3. whereis 指令：搜尋二進位檔案、原始碼、說明文件
	4. type 指令：顯示指令/檔案類型
	5. file 檔案或目錄：顯示文字檔、目錄、執行檔類型
	6. locate 檔名關鍵字：關鍵字搜尋檔案的路徑名稱
	7. find 搜尋路徑 選項：尋找檔案位置


	1. grep：在檔案內搜尋字串
	2. chmod：變更檔案權限
	3. chown：更改檔案擁有者
	4. chgrp：更改檔案群組


	1. tar -zcvf file1.tar.gz dir1：壓縮
	2. tar -zxvf file1.tar.gz：解壓縮


	1. /etc/passwd：紀錄系統帳號相關資訊
	2. su：切換成root，使用root密碼登入
	3. sudo -i：切換成root，使用當前使用者密碼登入
	4. sudo：暫時使用root權限執行指令
	5. useradd：新增帳號
	6. usermod：修改帳號
	7. userdel：刪除帳號
	8. users/who/w：顯示目前登入系統的帳號
	9. group 帳號：查詢帳號的群組
	10. id 帳號：查詢帳號的ID
	11. lastlog：列出每個帳號最近登入時間
	12. last：顯示系統登入紀錄
	13. passwd：更改帳號的密碼
	14. chage：更改密碼期限


	1. groupadd：新增群組
	2. groupmod：修改群組
	3. groupdel：移除群組


	1. pstree：以樹狀結構檢視程序
	2. ps：檢視系統中有哪些程序正在執行
	3. top：動態觀察程序的變化
	4. kill：終止程序
	5. killall：依名稱終止程序
	6. pkill：依部分名稱終止程序
	7. xkill：強制終止視窗程序


	1. jobs：查詢背景程序
	2. fg：將程序切換至前景執行
	3. bg：將程序切換至背景執行


	1. at：一次性的工作排程
	2. crontab：循環性的工作排程


	1. systemctl 動作 服務名稱：管理系統服務運行


	1. ping：顯示連線是否建立
	2. traceroute：顯示封包歷程
	3. netstat：檢視本機的網路連線狀況


	1. wget：檔案下載工具


	1. export：檢視所有環境變數值
	2. echo $變數名稱：印出單一變數值
	3. 變數=變數值：創建變數
	4. 單引號：印出原始字串
	5. 雙引號：印出字串
	6. unset 變數名稱：移除變數
	7. read 變數名稱：讀取來自鍵盤輸入的變數值


	1. help：
	2. alias：設定別名
	3. unalias：移除別名
	4. source：手動套用設定檔
	5. inode：檔案記憶體位置
	6. In -s：為檔案、目錄新增連結