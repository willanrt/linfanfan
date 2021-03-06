##手动创建一个表格
CREATE TABLE `data1` (
  `id` bigint(20) DEFAULT NULL,
  `name` text,
  `grade` bigint(20) DEFAULT NULL,
  `class1` double DEFAULT ,
  `class2` double DEFAULT NULL,
  `class3` double DEFAULT NULL,
  `class4` double DEFAULT NULL,
  `class5` double DEFAULT NULL,
  `class6` double DEFAULT NULL,
  `class7` double DEFAULT NULL,
  `class8` double DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
-- NULL允许为空
-- not null 不允许为空
-- DEFAULT 默认值


####查
select * from data1   -- 读取表格
select id,name from data1  -- 读取其中多列
select id,name from data1 where name = '王' -- 读取特定的行

###增加一行　INSERT INTO 表名 （列名,列名1,列名2...）VALUES(数值,数值1,数值2,数值3)
insert into data1 (id,name,grade,class1,class2,class3,class4,class5,class6,class7,class8)
VALUES(99999,'zhou',2020,100,100,100,100,100,100,100,100)

SELECT * from data1 where name="zhou"

##删除行 delete from 表名 where 字段=值  //  alter table 表名 drop column 列名;
delete from data1 where id = 99999
##删除表
drop table 表名;

##修改
-- UPDATE 表名 SET 字段1=值1,  #注意语法，可以同时来修改多个值，用逗号分隔
--            字段2=值2,
--            WHERE CONDITION; #更改哪些数据，通过where条件来定位到符合条件的数据
UPDATE data1 set grade=2019 where id=99999

select * from data1 where id=99999
