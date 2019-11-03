

#### windows 下 MySQL下载与配置

```
1.1. 下载：

我下载的是64位系统的zip包：

下载地址：https://dev.mysql.com/downloads/mysql/

下载zip的包

1.2. 配置环境变量：

变量名：MYSQL_HOME

变量值：C:\Program Files\Java\mysql-8.0.13-winx64

path里添加：%MYSQL_HOME%\bin;

1.3. 生成data文件：

以管理员身份运行cmd

进入C:\Program Files\Java\mysql-8.0.13-winx64\bin 下

执行命令：mysqld --initialize-insecure --user=mysql  

1.3.2. MySQl无法启动服务--Can't connect to MySQL server on localhost (10061)解决方法:
      1.windows健+R   弹出运行对话框。输入regedit打开注册表编辑器
      2.打开：k计算机名\HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\
        修改imagepath：为本机的路径 C:\Program Files\Java\mysql-8.0.13-winx64\bin\mysqld.exe

1.4. 启动服务：
执行命令：net start mysql  启动mysql服务，若提示：服务名无效...(后面有解决方法==步骤：1.5）；

1.5. 解决启动服务失败（报错）：
提示：服务名无效

解决方法：

执行命令：mysqld --install  即可（不需要my.ini配置文件 注意：网上写的很多需要my.ini配置文件，其实不需要my.ini配置文件也可以，我之前放置了my.ini文件，反而提示服务无法启动，把my.ini删除后启动成功了）

1.6. 登录mysql:
登录mysql:(因为之前没设置密码，所以密码为空，不用输入密码，直接回车即可）

C:\Program Files\Java\mysql-8.0.13-winx64\bin>mysql -u root -p

Enter password: ******

1.7. 查询用户密码:
查询用户密码命令：mysql> select host,user,authentication_string from mysql.user;

1.8. 设置（或修改）root用户密码：
设置（或修改）root用户密码：

mysql> ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY '123456';

#'123456',此处引号中的内容是密码，自己可以随便设置

Query OK, 1 row affected, 1 warning (0.00 sec)

Rows matched: 1  Changed: 1  Warnings: 1

mysql> flush privileges;  #作用：相当于保存，执行此命令后，设置才生效，若不执行，还是之前的密码不变

Query OK, 0 rows affected (0.01 sec) 

1.9. 退出mysql:
mysql> quit

Bye
--------------------- 
作者：tao10180 
来源：CSDN 
原文：https://blog.csdn.net/tao10180/article/details/83781842 
版权声明：本文为博主原创文章，转载请附上博文链接！
```



### Django数据库笔记

### 1.MySQL驱动程序安装

常见的驱动程序介绍：

       	1. MySQL-python: 是对c语言操作MySQL数据库的一个简单封装，目前只支持python2.
        	2. mysqlclient: 是MySQL-python的另外一个分支， 支持python3
         	3. pymysql: 是纯python实现的一个驱动， 执行效率没有MySQL-python 快
         	4. MySQL connector/Python: MySQL官方推出的使用纯python链接MySQL的驱动， 因为纯Python开发的，效率不高

### 2.操作数据库

#### Django配置链接数据库：

​	

```
DATABASES = {
    'default': {
        # 数据库引擎（mysql 或者 oracle )
        'ENGINE': 'django.db.backends.mysql',
        # 数据库名字
        'NAME': 'django_db1',
        # 连接mysql数据库的用户名
        'USER': 'root',
        # 连接mysql数据库的密码
        'PASSWORD': 'root',
        # mysql数据库的主机地址
        'HOST': '127.0.0.1',
        # mysql数据库的端口号
        'port': '3306',
    }
}
```

Django中操作数据库	

​	有两种方式： 第一种就是使用原生sql语句， 第二种就是使用ORM模型操作

​	第一种：

```
from django.db import connection


cursor = connection.cursor()
# 插入数据
cursor.execute("insert into book(id, name, author) values(null, '%s', '%s')" % (name, author))
# 查询数据
cur.execute("select id, name, author from book")
books = cur.fetchall() 
# 删除数据
cursor.execute("delete from book where id='%s'" % book_id)
# 更新数据
cursor.execute("update book set name='%s', author='%s' where id='%s'" % (name, author, book_id))
book = cursor.fetchone()

'''
flush privileges;  提交
'''
```



### 3.ORM模型介绍

随着项目越来越大， 采用原生SQL语句的方式代码中会出现大量的问题

1. SQL语句重复利用不高， 越复杂的SQL语句条件越多， 代码越长， 会出现很多相近的SQL语句.

   2. 很多SQL语句是业务逻辑拼出来的， 数据库需要修改，就要修改这些逻辑，容易漏掉对某些SQL语句的更改。
    3. 写SQL容易忽略web安全问题， 造成未知的隐患

ORM, 全称 Object Relational Mapping 叫做关系映射。通过把表映射成类， 把字段映射为属性， ORM执行队形操作的时候最终还是会把对应的操作转换为数据库原生语句。优点：

1. 易用性：较少重复的SQL语句概率
2. 性能损耗小：开发效率高， 代码可读性好
3. 设计灵活：可以轻松写出复杂的查询
4. 可移植性：很轻松的更换数据库

##### ORM模型的创建和映射：

创建ORM模型

```
    orm 模型一般都放在 ‘app'的’models.py'文件中
    需要在settings.py的'INSTALLED_APP' 中进行安装
```

```
from django.db import models

# Create your models here.
class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, null=False)
    author = models.CharField(max_length=100, null=False)
    price= models.FloatField(null=False, default=0)

# 1 makemigrations命令 生成迁移脚本文件
# python manage.py makemigrations
# 2 migrate命令 将生成的迁移脚本文件映射到数据库
# python manage.py migrate
```

##### ORM对数据库的基本操作

##### ORM 增删改查：

```
ORM对数据库的基本操作

添加数据
    book = Book(name='三国演义', author='罗贯中', price=199)
    book.save()
查找数据
    2.1. pk根据主键进行查找
    book = Book.objects.get(pk=1)
    print(book)
    2.2 根据其他条件进行查找
    books = Book.objects.filter(name='西游记').first()
    print(books)

删除数据
    book = Book.objects.get(pk=2)
    book.delete()

修改数据
    book = Book.objects.get(pk=3)
    book.price = 300
    book.save()
```

### 4 ORM模型常用字段

#### 模型常用属性

##### AutoField

```
# 整型
```



##### BigAutoField

```
# 长整型
```

##### BooleanField:

```
# 在定义字段的时候，如果没有指定null=True, 那么默认情况下， null=False
# 就是不能为空
# 如果要使用可以为null的BooleanField, 那么应该使用NullBooleanField (可以为空)
# 来代替BooleanField
```



##### CharField

```
# CharField, 默认必须定义max_length属性， 如果超过254个字符， 就不建议使用了
# 就推荐使用TextField,
```

##### DateField

```
# 时间类型， 在数据库层是time类型， 在python中是datetime.time类型
```



##### EmailField

```
# 类似于CharField, 在数据库层也是一个varchar类型， 最大长度是254个字符
```

##### FileField

```
# 用于存储文件的， 参考后面文件上传章节
```

##### ImageField

```
# 用于存储图片文件的， 参考后面图片上传章节
```

##### FloatField

```
# 浮点类型， 映射到数据库是float类型
```

##### IntegerField

```
# 整型， 值区间 -2147483648 -- 2147483647
```

##### BigIntegerField

```
# 大整型， 值区间 -9223372036854775808 -- 9223372036854775807
```

##### PositiveIntegerField

```
# 正整型， 值区间 0 -- 2147483647
```

##### SmallIntegerField

```
# 小整型， 值区间 -32768 -- 32767
```

##### PositiveSmallIntegerField

```
# 正小整型， 值区间 0 -- 32767
```

##### TextField

```
# 大量的文本类型， 映射到数据库是longtext 类型
```

##### UUIDField

```
# 只能存储uuid,格式的字符串， uuid是一个32位的全球唯一的字符串， 一般用来做主键
```

##### URLField

```
# 类似于CharField, 只不过只能来存储url格式的字符串， 并且默认的max_length是200
```



#### Field的常用参数：

```
null = True 或者 False
```



### 5.外键和表关系：

#### 5.1外键：

在MySQL中， 表有两种引擎， 一种是InnoDB，另外一种是myisam。 如果使用的是InnoDB引擎， 是支持外键约束的， 外键的存在使得ORM框架在处理表关系的时候异常的强大， 因此这里我们首先来介绍下外键在Django中的使用。

1. 类定义为 class ForeignKey(to, on_delete, **options)。 第一个参数值引用的是哪个模型， 第二个参数是在使用外键引用的模型数据被删除了， 这个字段该如何处理， 比如有一个CASCADE， SET_NULL等， 这里以一个实际案例来说明。 比如有个User 和一个Article 两个模型， 一个User可以发表多篇文章， 一个Article只能有一个Author， 并且通过外键进行引用， 那么相关的示例代码如下：

```
class User(models.Model):
	username = models.CharField(max_length=20)
	password = models.CharField(max_length=100)

class Article(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField()
	
	author = models.ForeignKey("User", on_delete=models.CASCADE)
```

以上使用 ForeignKey 来定义模型之间的关系， 即在article的实例中可以通过author属性来操作对应的User模型， 这样使用起来非常方便， 实例代码如下：

```
article = Article(title='abc', content='123qwe')
author = User(username='张三', password='123456')
article.author = author
article.save()

```

2. 如果想引用另外一个app的模型， 那么应该在传递to参数的时候， 使用app.model_name进行指定， 以上示例为例， 如果User 和 Article不是在同一个app 中， 那么引用的时候示例代码如下：

```
class User(models.Model):
	username = models.CharField(max_length=20)
	password = models.CharField(max_length=100)

class Article(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField()
	
	author = models.ForeignKey("user.User", on_delete=models.CASCADE)
```

3. 如果模型的外键引用的是本身自己这个模型， 那么to参数可以为 ‘self', 或者是这个模型的名字， 在论坛开发中， 一般评论都可以进行二级评论， 即可以针对另外一个评论进行评论， 那么定义模型的时候就需要使用外键来引用自身， 代码如下：

```
class Comment(models.Model):
	content = models.TextField()
	orign_comment = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
	# 或者
	# orign_comment = models.ForeignKey('Comment', on_delete=models.CASCADE, null=True)
```



##### 外键删除操作：

如果一个模型使用的外键， 那么在对方那个命被删除后， 该进行什么样的操作， 可以通过 on_delete 来指定， 可以指定的类型如下：

1. CASCADE: 级联操作， 如果外键对应的那条数据被删除了， 那么这条数据也会被删除
2. PROTECT: 受保护， 即只要这条数据引用了外键的那条数据， 那么不能删除外键的那条数据
3. SET_NULL:  设置为空， 如果外键的那条数据被删除了， 那么在本条数据上就将这个字段设置为空。 如果设置这个选项， 前提是要指定这个字段可为空
4. SET_DEFAULT: 设置默认值, 如果外键的那条数据被删除了， 那么本条数据将这个字段设置为默认值， 如果设置这个选型， 前提是要指定这个字段为默认值
5. SET()： 如果外键那条数据被删除了， 那么将会获取SET函数中的值作为这个外键的值。 SET函数可以接受一个调用的对象（比如函数或方法),  如果是可以调用的对象， 那么会将这个对象调用的结果作为值返回去
6. DO_NOTHING: 不采取任何行为， 一切全看数据库级别的约束

#### 5.2表关系：

表之间的关系是通过外键来进行关联的， 表之间的关系无非就三种关系： 一对一， 一对多， 多对多

##### 一对多：

1. 应用场景： 比如文章和作者之间的关系。 文章只能有一个作者写， 但是一个作者可写多篇文章， 文章和作者的关系就是典型的一对多的关系
2. 实现方式： 一对多或者多对一， 都是ForeignKey来实现的， 还是以文章与作者的案例进行讲解：

```
class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=100)

class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    
    author = models.ForeignKey("User", on_delete=models.CASCADE)

```

#####    2.1添加文章

```
article = Article(title='闰土', content=r'1gwvwvwvw11111111wd')
author = User(username='admin', password='111')
author.save()
article.author = author
article.save()
```

##### 并且以后如果想要获取某个用户的所有文章， 可以通过article_set来实现 示例代码如下：

```
user = User.objects.first()
articles = user.article_set.all()
for article in articles:
	print(article)
```

##### 2.2添加文章， 如果现想要将文章添加某个分类， 可以使用一下方式：

```
category = Category.objects.first()
article = Article('title'='111', content='qqqqqq')
article.author = FrontUser.objects.first()

category.articles_set.add(article, bulk=False)
```

使用bulk=False

那么Django会自动的保存article, 而不需要再添加category之前先保存article

或者是另外一种解决方式是， 在添加到category.article_set 之前， 先将article保存到数据库中， 但是如果article_category不能为空， 那么久产生一种死循环了， article没有category, 不能保存， 而将article添加到category_article_set中， 又需要article之前已经存储到数据库中的

如果是上面的需求， 建议使用bulk=False解决方案

### 6.增删改查操作



### 7查询操作

查找是数据库操作中一个非常重要的技术， 查询一般就是使用filter, exclude以及get 三个方法。 我们可以在调用这些方法的时候传递不同 的参数实现查询， 在orm层面， 这些查询条件都是使用field + ___ +condition, (即字段的名字+两个下划线+查询规则)的方式来使用的， 常用的查询条件如下:

#### exact:

精确的提供条件， 如果提供的是一个None， 那么在SQL层面就是解释为NULL。示例代码如下：

```
article = Article.ojects.get(id__exact=2)
article = Article.objects.get(id__exact=None)
```

print(article.query) 会打印出sql语句

以上的两个查找翻译成sql语句如下：

```
select .... from article where id=2
select .... from article where id IS NULL
```

#### iexact:

使用like进行查找示例代码如下：

```
article = Article.objects.filter(title__iexact='hello world')
```

以上的查找翻译成sql语句如下：

```
select .. from article where id like ..
```

#### contains:

```
contains  包含的意思  区分大小写
article = Article.objects.filter(title__contains='hello world')
```

#### icontains:

```
icontains  包含的意思  不区分大小写
```

### 聚合函数：

* 聚合函数都是放在 django.db.models 下面

* 聚合函数不能单独的执行， 需要放在一些可以执行聚合函数的方法下面去执行 比如：

  ```
  result = Book.objects.aggregate(Avg('price'))
  ```

* 聚合函数执行完成后， 给这个聚合函数的值取个名字， 取名字的规则，默认是”field+__+聚合函数名字“, 如果不想使用默认名字， 那么可以在使用聚合函数时候传递关键字参数进去， 参数的名字就是聚合函数执行完成的名字， 示例代码如下：

  ```
  result = Book.objects.aggregate(avg=Avg('price'))
  ```

​       以上传递了关键字参数 avg=Avg('price'), 以后Avg聚合函数的名字就叫做avg

* 'aggregate'： 这个方法不会返回一个“QuerySet'对象， 而是返回一个字典， 这个字典的key就是聚合函数的名字1



1. Avg: 求平均值， 比如想要获取所以图书的平均价格， 代码如下：

```
from django.db.models import Avg
result = Book.objects.aggregate(my_avg=Avg('price'))
print(result)
```



### 8.QuerySet API

#### 返回新的QuerySet的方法：

#### filter/exclude/annotate: 过滤/排除满足条件的/给模型添加新的字段

在使用QuerySet进行查找的时候， 可以提供的各种操作， 比如过滤完后还有根据某个字段进行排序， 那么这一系列的操作我们可以通过一个非常流畅的 ’链式调用‘ 的方法来进行， 比如要从-文章表中获取标题为123， 并且提取后要将结果根据发布的时间进行排序：

```
articles =Article.objects.filter(title='123').order_by('create_time')
```

可以看出order_by 方法是在filter执行后调用的， 这说明filter返回的对象是一个拥有order_by方法的对象， 而对象正是一个新的QuerySet对象， 因此可以使用order_by方法

下面介绍那些返回新的QuerySet对象的方法：

1. filter: 将满足条件的数据提取出来，  返回一个新的QuerySet对象

2. exclude:  排除满足条件的数据， 返回一个新的QuerySet， 示例代码：

   ```
   articles = Article.objects.exclude(title__contains='hello')
   ```

​        以上代码的意思是提取那些标题不包含hello的图书

3. annotate:  给QuerySet中的每个对象添加一个使用的查询方式(聚合函数， F表达式， Q表达式， Func表达式等) 的新字段， 示例代码如下：

   ```
   articles = Article.objects.annotate(author__name=F("author__name"))
   ```

​      以上代码将在每个对象中添加一个 author__name 字段， 来显示这个文章的作者的年龄

4.  order_by: 指定查询的结果根据某个字段进行排序， 如果要倒叙排序， 那么可以在字段前加个符号。 示例代码如下：

   ```
   根据创建的时间进行正序排序
   articles = Article.objects.order_by('create_time')
   根据创建的时间进行倒叙排序
   articles = Artcle.objects.order_by('-create_time')
   首先根据创建时间排序， 如果时间相同， 则根据作者的名字进行排序
   articles = Article.objects.order_by('create_time', 'author_name')
   根据图书销量从大到小进行排序
   books = Book.objects.annotate(order_nums=Count('bookorder')).order_by('-order_nums')
   ```

​        一定要注意的一点：多个order_by, 会把前面排序的规则给打乱， 而使用后面的排序方式， 代码如下：

```
article = Article.objects.order_by('create_time').order_by('author__name')
```

​	它会根据作者的名字进行排序， 而不是根据创建时间

​	当然， 也可以在模型定义中 在’Meta' 类中定义‘ordering', 来默认的排序方式：

```
class Meta:
    db_table = 'book_order'
    # 默认根据create_time 从大到小进行排序，如果create_time相等， 则根据price从大到小排序
    ordering = ['-create_time', '-price']
```

5. values:       




### 9.form表单：

##### CharField:

参数：

 * max_length: 这个字段的长度
* min_length: 这个字段的最小长度
* requried: 这个字段是否是必须的
* error_messages:  在某个条件验证失败的时候， 给出错误信息 

##### EmailField:

用来接受邮件， 会自动验证邮件是否合法

错误信息key: requried, invalid

##### IntegerField:

用来接受整类型， 如果验证通过， 会将这个字段的值转换为整类型

参数：

- max_length: 最大值
- min_length: 最小值

错误信息的key: requried, invalid, max_value, min_value



##### FloatField:

用来接受浮点类型， 如果验证通过， 会将这个字段的值转换为浮点类型

参数：

* max_length: 最大值
* min_length: 最小值

错误信息的key: requried, invalid, max_value, min_value



##### URLField:

用来接受 url 格式的字符串

错误信息key: requried, invalid

### 常用的验证器：

需要引入一下： from django.core import validators

在验证某个字段的时候， 可以传递一个 validator 参数来指定验证器， 进一步对数据进行过滤， 验证器有很多，但是很多验证器我们其实可以通过这个Field或者一些参数就可以指定了， 比如EmailValidator, 我们可以通过EmailField来指定， 比如MaxValueValidator, 我们可以通过max_value参数来指定， 以下是常用的验证器：

1.  MaxValueValidator: 验证最大值

2. MinValueValidator: 验证最小值

3. MinLengthValidator: 验证最小长度

4. MaxLengrhValidator: 验证最大长度

5. EmailValidator: 验证是否是邮箱格式

6. URLValidator: 验证是否是url格式

7. RegexValidator: 如果需要更加复杂的验证， 那么我们可以通过正则表达式的验证器： RegexValidator. 比如现在要验证手机号格式是否合格：

   ```
   from django.core import validators
   class MyForm(forms.Form):
   	telephone = forms.Charfield(vallidators=[validators.RegexValidator("1[345678]\d{9}", message='请输入正确格式的手机号！'])
   ```

### 自定义验证：

有时候对一个字段验证，不是一个长度， 一个正则表达式能够写清楚的， 还需要其他复杂的验证逻辑， 那么我们可以对某个字段，进行自定义验证， 比如注册的表单验证， 我们想验证手机号是否被注册过， 那么这时候需要在数据库中进行判断猜知道， 对某个字段进行验证的验证方式， 定义一个方法， 这个方法的名字定义规则是: clean_fieldname。 如果验证失败， 那么抛出一个验证错误， 示例：

```
class MyForm(forms.Form):
	telephone = forms.CharField(validators=[validators.RegexValidator('1[345678]\d{9}', message='请输入正确格式的手机号！')])
	
	def clean_telphone(self):
		telphone = self.cleaned_data.get('telphone')
		exists = User.objects.filter(telphone=telphone).exists()
		if exists:
			raise forms.ValidationError('手机号已经有存在！')
		return telphone
```






### 12.pycharm 连接数据库:

mysql驱动下载地址: https://dev.mysql.com/downloads/connector/j/