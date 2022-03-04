   <h1>Git專案開發管理</h1>
          

          〚 - 指令操作 - 〛
          
            --SSH
          git config user.name：顯示使用者名稱
          git config user.email：顯示使用者信箱
          git config user.name "your_name"：設定本地端使用者名稱
          git config user.email "your_name@example.com"：設定本地端使用者信箱
          git config --global user.name "your_name"：設定全域使用者名稱
          git config --global user.email "your_name@example.com"：設定全域使用者信箱位置
              使用 --global 的參數，表示對於所有的 git project 都會採用這組預設值
          ls ~/.ssh
              公鑰：有.pub的是公鑰，公鑰用來上鎖
              私鑰：沒有.pub的是私鑰，私鑰用來解鎖
          eval `ssh-agent -s`：啟動SSH agant
          ssh-add ~/.ssh/id：把私鑰加入ssh agent，每次在開鎖github才可以不用一直帶著私鑰
          cat ~/.ssh/ 公鑰.pub：複製公鑰所有內容
                              setting->SSH and GPG keys->new SSH key->paste->take a SSH key's name

          git add：將working directory的檔案add到staging area
          git commit "版本敘述"：將staging area的檔案commit到localrepo
          
          git commit –am "版本敘述"：git add + git commit
          
          git reflog：查看log變更歷史紀錄
          gir reset 版本編號 --模式
              mixed：預設模式，拆除commit後，將檔案留在working directory
              soft：拆除commit後，將檔案留在stagine area
              hard：拆除commit後，將檔案刪除
          git restore . ：git reset到指定版本編號後，將模式刪除的檔案還原
          git revert：再做一個新的 Commit，來取消你不要的 Commit
             
          git checkout 版本編號/分支名稱：將分支節點移動到指定版本/切換到指定分支
          git branch 分支名稱：新增分支
          git branch –d 分支名稱：刪除分支
          git merge 分支名稱：將指定分支合併至當前分支
          git rebase：重新定義指定分支的基底節點
          
          git push origin 本地分支名稱：將localrepo的檔案複製一份到remoterepo
          git pull origin 遠端分支名稱：將remoterepo的檔案複製一份到localrepo
          git clone 網址：利用HTTPS、SSH將GitHub上專案下載下來
          
          git status：查看working directory的狀態
          git log：查看版本相關紀錄
          
            --版本控制
                    目錄底下有.git就代表受到git的版本控制
          git rm --cached：將檔案移除版本控制
          .gitignore：touch .gitgnore，vim gitgnore可將不想要被版本控制的檔案輸入進去
          
          〚 - 分支涵義 - 〛
          
          Develop：所有程式開發的基礎，不會在此分支進行commit
          Feature：新功能開發皆透過feature分支進行，commit的時候的commit message為feature/some-function
          Master：現在的main，不會對此分支進行commit，用來放穩定、可上線的版本
          Release：用來做上線最後測試，測試完會合併到main、Develop
          Hotfix：線上版本出現緊急問題在main分支另開分支修復後，再合併回main、Develop
<img src="https://user-images.githubusercontent.com/97188330/156694877-9fc82c86-82c0-49d2-9bca-37e2610381e2.png" width="1000" height="330" alt="MySQL"/><br/>

