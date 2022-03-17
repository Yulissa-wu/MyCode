01.撰寫一select敘述，查詢Table: DEPT，列出所有資料
        select * from DEPT
        
02.撰寫一select敘述，查詢Table: EMP，列出所有員工的員工姓名(ENAME)、職稱(JOB)、到職日(HIREDATE)、及員工編號(EMPNO)，員工編號需顯示在第一欄
        select EMPNO, ENAME, JOB, HIREDATE from EMP
        
03.撰寫一select敘述，查詢Table: EMP，列出所有到職日(HIREDATE) ，同樣的到職日不重複顯示
        select distinct HIREDATE from EMP
        
04.續第02題，將select敘述加上別名
        select ENAME EmployeeName, 
               JOB Title, 
               HIREDATE HireDate, 
               EMPNO EmployeeNo
        from EMP
        
05.撰寫一select敘述，查詢Table: EMP，列出員工姓名(ENAME)串接職稱(JOB)，中間用逗號和空白隔開(', ')，並加上別名 NAMEandTITLE
        select concat(ENAME,', ', JOB) NAMEandTITLE from EMP

06.列出薪資不介於1000到2000元的員工之姓名和薪資
        select ENAME, SAL from EMP
        where SAL between 1000 and 2000
        
07.列出到職日為1981年的員工之姓名、職稱、到職日，並依到職日遞減排序
      select ENAME, JOB, HIREDATE
      from EMP
      order by
          HIREDATE desc
          
08.列出薪資超過2000元 且 部門編號為10或30 的員工之姓名、薪資，並依序取別名為"EMPLOYEE_NAME"、"SALARY"
      select ENAME EMPLOYEE_NAME, SAL SALARY
      from EMP
      where SAL > 2000 and (DEPTNO = 10 or DEPTNO = 30)
      
09.列出有獎金(獎金 不是null，也不是0)的員工之姓名、薪資、獎金，並排序，排序依據為薪資加上獎金
      select ENAME, SAL, COMM
      from EMP
      where COMM is not null and COMM != 0
      order by 
          SAL + IFNULL(COMM, 0)
          
10.列出員工姓名最後一個字是"S"的員工之姓名、職稱
      select ENAME, JOB
      from EMP
      where ENAME like '%S'
      
11.列出職稱為CLERK、SALESMAN，且薪資不等於1100、1300、1500的員工之姓名、職稱、薪資
      select ENAME, JOB, SAL
      from EMP
      where 
	        (JOB = 'CLERK' or JOB = 'SALESMAN') and
	        (SAL != 1100 and SAL !=1300 and SAL !=1500)
          
12.列出獎金大於薪資1.05倍的員工之姓名、薪資、獎金
      select ENAME, SAL, COMM
      from EMP
      where
	  COMM > SAL * 1.05
	  
13.請列出公司每年需發出薪資總和 (不含獎金)
      select SUM(SAL * 12)
      from EMP
      
14.請列出公司平均月薪
      select AVG(SAL)
      from EMP
      
15.請列出各部門編號、部門每月發出薪資總和，並依部門編號遞增排序
      select DEPTNO, SUM(SAL)
      from EMP
      group by DEPTNO
      order by 
      	  DEPTNO asc
	  
16.請列出職稱、該職稱平均薪資、該職稱人數
      select JOB, AVG(SAL), COUNT(JOB)
      from EMP
      group by JOB 
      
17.請列出部門編號、部門最低薪資、部門最高薪資
      select EMPNO, MIN(SAL), MIN(SAL)
      from EMP
      group by EMPNO
      
18.請列出到職年、到職年當年人數
      select YEAR(HIREDATE), COUNT(*)
      from EMP
      group by YEAR(HIREDATE)

19.請列出部門編號、部門平均薪資，只顯示部門平均薪資大於2500的部門
      select EMPNO, AVG(SAL)
      from EMP
      group by EMPNO
            having AVG(SAL) > 2500
	    
20.請列出到職年、到職年當年人數，只顯示到職年當年人數等於1的資料
      select YEAR(HIREDATE), COUNT(*)
      from EMP
      group by YEAR(HIREDATE)
      having COUNT(*) = 1
      
21.請列出各部門編號、部門每月發出薪資總和，只顯示部門每月發出薪資總和小於10000的部門，並依部門編號遞減排序
      select DEPTNO, SUM(SAL)
      from EMP
      group by DEPTNO
      having SUM(SAL) < 10000
      order by DEPTNO desc
      
22.請列出職稱、該職稱平均薪資、該職稱人數，只顯示職稱平均薪資大於2000且職稱人數小於2的資料
      select JOB, AVG(SAL), COUNT(*)
      from EMP
      group by JOB
      having AVG(SAL) > 2000 and COUNT(*) < 2
      
23.請列出部門編號、部門最低薪資、部門最高薪資，且過濾掉最低薪資大於1200的資料
      select DEPTNO, MIN(SAL), MAX(SAL)
      from EMP
      group by DEPTNO
      having MIN(SAL) <= 1200
      
24.請列出所有員工的員工編號、姓名、職稱、部門編號及部門名稱
      select e.EMPNO, e.ENAME, e.JOB, d.DEPTNO, d.DNAME
      from EMP e
	   join DEPT d
           on e.DEPTNO = d.DEPTNO
		
25.請列出所有部門編號為30 且 職稱為"SALESMAN"之部門名稱、員工姓名、獎金
      select DEPTNO
      from EMP e1
      join EMP e2
      on e.DEPTNO = d.DEPTNO
      where e1.JOB = SALESMAN and e2.DEPTNO = 30

26.請列出薪水等級為"B"的員工之員工編號、員工姓名、薪資
      select s.LEVEL, e.EMPNO, e.ENAME, e.SAL 
      from SAL_LEVEL s
	 join EMP e
            on e.DEPTNO = d.DEPTNO
      where s.LEVEL = B
	
27.請列出部門編號、部門名稱及部門人數
      select d.DEPTNO, d.DNAME, COUNT(*)
      from DEPT d
      join EMP e
      	on e.DEPTNO = d.DEPTNO
      group by EMPNO

28.請列出每個主管之姓名、直屬下屬人數、直屬下屬平均薪資，並依 直屬下屬人數遞減、主管姓名遞增 排序
      select e1.ENAME, COUNT(*), AVG(e2.SAL)
      from EMP e1
      join EMP e2
        on e1.EMPNO = e2.MGR
      group by e1.ENAME
      order by COUNT(*) desc, e1.ENAME asc

29.請列出薪資比所有SALESMAN還低的員工
      select *
      from EMP
      where SAL < (select MIN(SAL) from EMP where JOB = 'SALESMAN');
      
30.請列出到職年(到職日之年)最早的兩年，那兩年到職的員工，並依到職日排序
      select distinct year(HIREDATE)
      from EMP
      order by year(HIREDATE)
      limit 2
      ------
      select ENAME
      from EMP
      where year(HIREDATE) in (1980 or 1981)
      ------
      select ENAME
      from EMP
      where year(HIREDATE) in (select * from (select distinct year(HIREDATE)
      from EMP
      order by year(HIREDATE)
      limit 2)as A)     
      
31.請列出主管的主管是KING 的員工，找出king,king無主管，找出主管的主管是king的
      select EMPNO from EMP -- 先找出king的員工編號=7839 
      where ENAME = "KING"
      -------
      select EMPNO
      from EMP 
      where MGR = (select EMPNO from EMP
      where ENAME = "KING")
      -------
      select ENAME
      from EMP
      where MGR in (select EMPNO
      from EMP 
      where MGR = (select EMPNO from EMP
      where ENAME = "KING"))

32.請列出部門內員工薪資有3種薪資等級之部門名稱、部門所在地
      select * from SAL_LEVEL
      select * from EMP
      select * from DEPT
      e.DEPTNO, COUNT(distinct s.LEVEL) 
           
      select d.DNAME, d.LOC
      from EMP e
	join SAL_LEVEL s
	on e.SAL between SAL_MIN and SAL_MAX
      join DEPT d
        on e.DEPTNO = d.DEPTNO
      group by DEPTNO
      having COUNT(distinct s.LEVEL) = 3

33.請列出跟員工姓名最後一字元是S的員工同部門，該部門薪資最低的員工之部門名稱、姓名、薪資
      select distinct DEPTNO
      from EMP
      where ENAME like '%S'
      -----
      select DEPTNO, MIN(SAL)
      from EMP
      where DEPTNO = 20 or DEPTNO = 30
      group by DEPTNO
      -----
      select d.DNAME, e.SAL, e.ENAME
      from EMP e
	join DEPT d
      on e.DEPTNO = d.DEPTNO
      where e.DEPTNO = 20 and e.SAL = 800.00 or e.DEPTNO = 30 and e.SAL = 950.00
      -----
      select DEPTNO, MIN(SAL)
      from EMP
      where DEPTNO in (select distinct DEPTNO
      from EMP
      where ENAME like '%S')
      group by DEPTNO
      
34.請新增以下資料至資料表DEPT
      50, 'Software', 'Taipei'
      insert into DEPT(DEPTNO, DNAME, LOC)
      value(50, 'Sofrware', 'Taipei');
      
35.請新增以下資料至資料表EMP的欄位 EMPNO, ENAME, JOB, MGR,
      HIREDATE, SAL, DEPTNO
      8888, 'Lee', 'PM', null, NOW(), 3500, 50
      insert into EMP(EMPNO, ENAME, JOB, MGR, HIREDATE, SAL, DEPTNO)
      value(8888, 'Lee', 'PM', null, NOW(), 3500, 50);
      
36.請修改資料表EMP的資料..
      員工8888的主管改為7839
      員工9999的主管改為8888
      提示: 可配合case運算式，將2個敘述合併成1個敘述！
      update EMP
      set MGR = 7839
      where EMPNO = 8888;
      update
      set MGR= 8888
      where EMPNO = 9999;
      
37.請刪除員工編號為8888的員工之資料
      delete from EMP
      where EMPNO = 8888
      
38.請修改資料表EMP的資料..
      員工9999的主管改為7839，薪水改為4000
      select * from EMP 
      update 
      set MGR = 7839
      where EMPNO = 9999;
      update
      set SAL = 4000
      where EMPNO = 9999;
  
39.請啟用交易控制模式，執行以下動作..
刪除除了老闆以外的所有員工之資料
查詢確認是否已刪除
還原
      set autocommit = off;
      delete from EMP where MGR is null;
      select * from EMP;
      rollback;
      set autocommit = on;
      
如果MGR是null的話就顯示

40.請開啟單一交易控制，執行以下動作..
修改除了老闆以外的所有員工，獎金+1000、薪水+15%
查詢確認是否已修改
送交

      start transaction;
      update 
      set COMM = 1000, SAL = 1.15
      where MGR is null;
      select * from EMP;
      commit;
      
41.今天公司空降了一位主管ERIC，員工編號: 6666，職稱: MANAGER，主管: 7839，
薪資: 3500，部門編號: 50
另外原本就在職的2位員工7499、7844調至部門編號50，且主管改為6666
請開啟單一交易控制，將上述動作在一個交易內完成
      start transaction;
	insert into EMP(ENAME, EMPNO, JOB, MGR, SAL, DEPTNO)
	select ERIC, 6666, MANAGER, 7839, 3500, 50
	from EMP
		update EMP
		set DEPTNO = 50
		where EMPNO = 7499;
		update EMP
		set DEPTNO =50
		where EMPNO = 7499;
		
42.請新建 會員資料表MEMBER，欄位描述如下..
      CREATE TABLE `EXAMPLE`.`MEMBER` (
        `ID` INT NULL AUTO_INCREMENT COMMENT '編號',
        `USERNAME` VARCHAR(50) NULL COMMENT '帳號',
        `PASSWORD` VARCHAR(50) NULL COMMENT '密碼',
        `PASS` BIT(1) NULL DEFAULT 0,
        `CREATE_DATE` DATETIME NULL COMMENT '建立日期',
        `LAST_UPDATE_DATE` DATETIME NULL,
       PRIMARY KEY (`ID`));
       
43.請對資料表MEMBER的欄位PASSWORD之後加入一欄位..
      ALTER TABLE `EXAMPLE`.`MEMBER` 
      ADD COLUMN `NICKNAME` VARCHAR(50) NULL COMMENT '暱稱' AFTER `PASSWORD`;
      
44.請修改資料表MEMBER的欄位
USERNAME、PASSWORD: not null、長度100
LAST_UPDATE_DATE: 預設值NOW()、註解"最後修改日期"
      ALTER TABLE `EXAMPLE`.`MEMBER` 
      CHANGE COLUMN `USERNAME` `USERNAME` VARCHAR(100) NOT NULL COMMENT '帳號' ,
      CHANGE COLUMN `PASSWORD` `PASSWORD` VARCHAR(100) NOT NULL COMMENT '密碼' ,
      CHANGE COLUMN `LAST_UPDATE_DATE` `LAST_UPDATE_DATE` DATETIME NULL DEFAULT NOW() COMMENT '最後修改日期' ;
      
45.請將資料表MEMBER的欄位USERNAME設為唯一鍵
      ALTER TABLE `EXAMPLE`.`MEMBER` 
      ADD UNIQUE INDEX `USERNAME_UNIQUE` (`USERNAME` ASC);
      
46.請將資料表MEMBER的欄位USERNAME的唯一鍵約束移除
      ALTER TABLE `EXAMPLE`.`MEMBER` 
      DROP INDEX `USERNAME_UNIQUE` ;
      
47.請將資料表MEMBER的欄位CREATE_DATE移除
      ALTER TABLE `EXAMPLE`.`MEMBER` 
      DROP COLUMN `CREATE_DATE`;
      
48.請新建資料表 MEMBER2、MEMBER3，2個資料表的結構跟資料須與資料表MEMBER一樣
      create table MEMBER2
      as
      select * from MEMBER

      create table MEMBER3
      as
      select * from MEMBER
      
49.請將資料表MEMBER2改名為MEMBER_HIS
      alter table MEMBER2 rename to MEMBER_HIS;
      
50.請將資料表MEMBER3截斷(truncate)
      truncate table MEMBER3
      
51.請將資料表MEMBER3的儲存引擎改為MyISAM
      alter table MEMBER3 engine MyISAM;
      
52.請將資料表MEMBER3移除
      drop table MEMBER3
      
53.請授予使用者william 對資料庫EXAMPLE底下所有資料表的所有權限
      grant all
      on EXAMPLE.*
      to 'william'@'%'

54.請撤銷william 對資料庫EXAMPLE底下所有資料表的所有權限
      revoke all
      on EXAMPLE.*
      from 'william'@'%';
      
55.請新建一個View，名為V_DEPT_ECOUNT，列出部門編號、部門人數
      create view V_DEPT_ECOUNT
      as
      select d.DEPTNO, COUNT(e.DEPTNO)
      from EMP e
	right join DEPT d
		on d.DEPTNO = e.DEPTNO
      group by d.DEPTNO;
      
56.請新建一個View，名為V_DEPT_ECOUNT2，基底資料表為第01題建立的檢視表
V_DEPT_ECOUNT，並將欄位依序命名為DEPARTMENT_NO、EMPLOYEE_COUNT
      create view V_DEPT_ECOUNT2(DEPARTMENT_NO, EMPLOYEE_COUNT)
      as 
      select * from V_DEPT_ECOUNT;

57.請撰寫一select敘述，用第02題建立的檢視表V_DEPT_ECOUNT2，join資料表DEPT，列出部門名稱、部門人數
      select DNAME, COUNT(*)
      from V_DEPT_ECOUNT2 v2
	join DEPT d
		on v2.DEPARTMENT_NO = d.DEPTNO
      group by DEPTNO
      
58.請新建一個View，名為V_EMP10，其內含有部門編號10的所有員工資料，並加上with check option限制DML
      create view V_EMP10
      as
	select * from EMP
	where DEPTNO = 10
      with check option
      
59.請修改檢視表V_DEPT_ECOUNT2，將欄位命名依序改為、EMP_COUNT，其餘部分不變
      alter table EMP engine INNODB;


      alter view V_DEPT_ECOUNT2(EMP_COUNT, DEPT_NO)
      as
      select EMPLOYEE_COUNT, DEPARTMENT_NO from V_DEPT_ECOUNT2
      with cascaded check option;

60.請移除檢視表V_DEPT_ECOUNT2
      drop view V_DEPT_ECOUNT2
      
61.請替資料表DEPT的欄位DNAME，新建唯一索引，並取出適當的Index名稱
      drop index IDX_DEPT_DNAME on DEPT;

      select DNAME from DEPT

      create unique index IDX_DEPT_DNAME
      on DEPT(DNAME);
      
62.請替資料表EMP的欄位(DEPTNO, ENAME)，新建複合索引，Index名稱為
IDX_EMP_DEPTNO&ENAME
      create index `IDX_EMP_DEPTNO&ENAME`
      on EMP(DEPTNO, ENAME);

63.請新建一個資料表PERSON，欄位描述如下..
並同時替欄位NAME加上一般索引
      create table PERSON(
			NAME varchar(50) not null, 
                        ID int not null,
			primary key PK_PERSON_ID(ID),
                        index IDX_PERSON_NAME(NAME)
					);
					
64.請使用alter table敘述，替資料表DEPT的欄位(DNAME, LOC)加入複合索引
      alter table DEPT
      add index `IDX_DEPT_LOC&DNAME`(LOC, DNAME);
      
65.請移除第04題建立的索引
      drop index `IDX_DEPT_LOC&DNAME` on DEPT
