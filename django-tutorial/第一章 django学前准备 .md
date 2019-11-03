

### 安装virtualenv

virtualenv 是用来创建虚拟环境的软件， 我们可以通过pip 或者pip3来安装

```
pip install virtualenv

pip3 install virtualenv
```



### 创建虚拟环境

创建虚拟环境非常简单，通过以下命令

```
virtualenv [虚拟环境的名字]
```

### 进入虚拟环境

虚拟环境创建好后， 那么可以进入这个虚拟环境中， 然后安装第三方包，

进入虚拟环境一般分两种， 第一种windows, 第二种linux

1. windows 进入虚拟环境：进入虚拟环境的scripts文件夹中

2. linux进入虚拟环境：source/path/to/virtualenv/bin/activate 一旦你进入这个虚拟环境中，

   你安装包， 卸载包都是在这个虚拟环境中， 不会影响到外部环境

### 退出虚拟环境

通过命令可以完成：deactivate

### 创建虚拟环境的时候指定python解释器

在电脑的环境变量中，一般是不会去更改一些环境变量的顺序的， 也就是说比如

你的python2/Scripts在python3/Scripts的前面， 那么你不会经常更改他们玩的位置， 但是、

这时候我确实想创建虚拟环境的时候用python3这个版本， 这时候可以通过-p参数来指定

具体的python解释器

```
virtualenv -p c:\Python36\python.exe
```



### virtualenvwrapper

virtualenvwrapper 这个软件包让我们管理虚拟环境变得更加简单， 不再跑到某个目录下

通过virtualenv 来创建虚拟环境， 并且激活的时候也要跑到具体的目录下去激活

#### 安装 virtualenvwrapper:

1. *nix: pip install virtualenvwrapper
2. windows: pip install virtualenvwrapper-win

#### virtualenvwrapper 基本使用：

1. 创建虚拟环境：

   ```
   mkvirtualenv my_env
   ```

2. 切换到某个虚拟环境

   ```
   workon my_env
   ```

3. 退出当前虚拟环境

   ```
   deactivate
   ```

4. 删除某个虚拟环境

   ```
   rmvirtualenv my_env
   ```

5. 列出所有虚拟环境

   ```
   lsvirtualenv
   ```

6. 进入虚拟环境所在的目录

   ```
   cdvirtualenv
   ```

#### 修改 mkvirtualenv 的默认路径

在我的电脑-右键-属性-高级系统设置-环境变量-系统变量 中添加一个参数WORKON_HOME，将这个

参数的值设置为你需要的路径 

#### 创建虚拟环境的时候指定Python版本

在使用 mkvirtuakenv 的时候， 可以指定 --python 的参数来指定具体的python路径

```
mkvirtualenv --python==c:Python36\python.exe my_env
```



## 学前准备

1. 安装python3.6

2. 安装 virtualenvwrapper, 这个是用来创建虚拟环境的包， 使用虚拟环境可以让我们的包管理更加方便

3. 虚拟环境相关操作：

   创建虚拟环境： mkvirtualenv --python=[’python3.6文件所在路径‘][虚拟环境名]

   进入虚拟环境：workon [虚拟环境名]

   退出虚拟环境：deactivate

4. 首先进入虚拟环境 workon django-env, 然后通过 pip install django==2.0

5. 安装pycharm profession 2017 (专业版)， community(社区版)不能用于网页开发

6. 安装最新 MySQL, windows版的MySQL下载地址：https://dev.mysql.com/downloads/windows/installer/5.7.html, 如果是其他操作系统， 来这个页面选择具体的MySQL进行下载：http://dev.mysql.com/downloads/mysql/

7. 安装 pymysl, 这个库是python 来操作数据库的， 没有它， django就不能操作数据库，pip install pymysql

   ​

```
django-admin startproject name .
pip install mysqlclient
如果报错在 则下载 mysqlclient-1.3.13-cp36-cp36m-win_amd64
 网址：'https://www.lfd.uci.edu/~gohlke/pythonlibs/' ，然后pip install 下
创建应用  python manage.py startapp user, 并把user这个包添加到setting.py文件的INSTALLED_APPS下面
创建model(创建数据库)
安装pymysql  命令; pip install pymysql
迁移命令
创建models  python manage.py makemigrations
执行迁移命令生成数据库表 python manage.py migrate


Django 后台管理
1, 创建管理员
管理员名称 admin
密码       poo14755
python manage.py createsuperuser
2, 本地化
setting.py中设置语言， 时区
语言名称可以查看django\contrib\admin\locale 目录
3, 启动服务器
python manage.py runserver
4, 登录后台页面
5，注册应用模块

路由
编写WSGI框架项目中， 路由功能就是实现url模式匹配和处理函数之间的映射
对于django也是如此， 路由配置要在项目中的urls.py中配置， 也可以多级配置
在每一个应用中， 建立一个urls.py文件配置路由映射
url函数
url(regex, view, kwargs=None, name=None), 进行模式匹配
regex: 正则表达式， 与之匹配的ull 会执行对应的第二个参数view
view: 用于执行与正则表达式匹配的url 请求
kwargs: 视图使用的字典类型参数
name: 用来反向获取url
urls.py 内容如下
```




```
1 变量
	语法：{{content}}
2 模板标签
	if/else标签
	基本格式如
	{% if condition %}
		....display
	{% endif %}
条件也支持and, or, not
注意， 因为这些标签是断开的， 所以不能像python一样使用缩进就可以表示出来， 必须有个结束标签
例如: endif, endfor
  for 标签
  <url>
      {% for athlete in athlete_list %}
          <li>{{ athlete.name}}</li>
      {% endfor %}
  </url>
  {% for person in person_list %}
      <li> {{  person.name }}</li>
  {% endfor %}
```

```
变量                      说明
forloop.counter           当前循环从1开始计数
forloop.counter0          当前循环从0开始计数
forloop.recounter         从循环的末尾开始倒计数到1
forloop.recounter0        从循环的末尾开始倒计数到0
forloop.first             第一次进入循环
forloop.last                  最后一次进入循环
forloop.parentloop        循环嵌套时， 内层当前循环的外层循环

给标签增加一个reversed使得该列表反向迭代
{% for athlete in athlete_list reversed %}
...
{% empty %}
... 如果被迭代的列表是空的或者不存在， 执行empty 
{% endfor %}

可以嵌套使用{% for %}标签
{% for athlete in athlete_list %}
	<h1>{{ athelete.name }} </h1>
	<ul>
	{% for sport in athlete.sports_played %}
		<li> {{ sport }} </li>
	{% endfor %}
	</ul>
{% endfor %}

ifequal/ifnoequal 标签
{% ifequal %} 标签比较两个值， 当它们相等， 显示在{% ifequal %} 和 {% endifequal %} 之中所有值
下面的例子比较两个模板变量user 和 currentuser
  {% ifequal user currentuser %}
      <h1> welcome </h1>
  {% endifequal %}
和 {% if %}类似， {% ifequal %} 支持可选的{% else %}标签
  {% ifequal section 'sitenews' %}
      <h1> Site News </h1>
   { else }
   	  <h1> No News Here </h1>
  {% endifequal %}
 其他标签
 csrf_token 用于跨站请求伪造保护， 防止跨站攻击
 {% csrf_token %}
 
3 注释标签
 单行注释 {# #}
 多行注释 {% comment %}...{% endcomment %}
```

4 过滤器

```
模板过滤器可以在变量被显示前修改它

语法{{变量|过滤器}}
过滤器使用管道字符|, 例如{{name|lower}}, {{name}} 变量被过滤器lower处理后， 文档大写转换为小写

过滤管道可以被套接， 一个过滤管道的输出又可以作为下一个管道的输入， 例如{{my_list|first|upper}},
将列表第一个元素装换为大写

过滤器参数
有些过滤器可以传递参数， 过滤器的参数跟随冒号之后并且总是以双引号包含。
例如：{{bio|truncatewords:"30"}}, 截取显示变量的前30 个词。
{{my_list|join:","}}, 将my_list的所有元素使用，逗号连接起来
其他过滤器
过滤器          说明                               举例
first           取列表的第一个元素
last            取列表最后一个元素
yesno           变量可以是True, False, None,       {{value | 
											   yesno:"yeah, no, maybe"}}
			   yesno的参数给定逗号分隔的三个值， 
			   返回3个值中的一个。
			   True多应第一个
			   False对应第二个
			   None对应第三个
			   如果参数只有2个， 
			   None等效False处理
add             加法。参数是负数就是减法            数字加{{value | add:"100"}}
											  列表合并{{mylist | add: newlst}}
divisibleby     能否被整除                         {{value | divisibleby:"3"}}， 能
											  被3整除返回True
addslashes      在反斜杠，单引号或者双引号前面加反斜杠 {{value| addslashes}}
length          返回变量的长度                       {% if my_list | length>1 %}
default         变量等价False则使用缺省值             {{value | default:"nothing"}}
default_if_none 变量为None使用缺省值                  {{value | default_if_none:"nothing"}}


```

date: 按指定的格式字符串参数格式化date或者datetime对象， 实例：

```
{{ pub_date|date:"n j, Y"}}
n 1~12月
j 1~31日
Y 2000年
```

练习，

```
<ul>
    {% for k, v in dct.items %}
        {% if forloop.counter0|divisibleby:"2" %}
        <li style="color:#FF0000">{{forloop.counter0}} {{k}} {{v}}</li>
        {% else %}
        <li style="color:#0000ff">{{forloop.counter0}} {{k}} {{v}}</li>
        {% endif %}
    {% endfor %}
</ul>

<ul>
    {% for k, v in dct.items %}
        <li style='color:{{forloop.counter0|divisibleby:"2"|yesno:"red,blue"}}'>{{forloop.counter0}} {{k}} {{v}}</li>
    {% endfor %}
</ul> 

 <ul>
 {% for k, v in dct.items %}
 <li class='{{forloop.counter0|divisibleby:"2"|yesno:"odd, even"}}'>{{forloop.counter0}} {{k}} {{v}}</li>
 {% endfor %}
 </ul>
```



## django用户接口设计之路由配置，视图函数

#### 1 用户功能设计与实现

提供用户注册处理

提供用户登录处理

提供路由配置

#### 2 用户注册接口设计

接受用户通过Post方法提交的注册信息， 提交的数据是json格式数据

检查email是否已存在于数据表中， 如果存爱返回错误的状态码，例如4xx, 如果不存在，

将用户提交的数据存入表中

整个过程都是采用AJAX异步过程， 用户提交json数据， 服务端获取数据后处理， 返回JSON

URL: /user/reg

METHOD: POST

#### 3 路由配置

为了避免项目中的urls.py条目过多， 也为了让应用自己管理路由， 采用多级路由

```
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/$', index),
    url(r'^$', index),
    url(r'^user/', include('user.urls')),
]
```

include函数参数写应用.路由模块， 该函数就会动态导入指定的包的模块， 从模块里面读取urlpatterns

返回三元组， 

url函数第二参数如果不是可调对象， 如果是元组或列表， 则会从路径中除去已匹配的部分， 将剩下部分与应用

中的路由模块的urlpattern进行匹配

```
# 新建user/urls.py
from django.conf.urls import url
from .views import reg

urlpatterns = [
    url(r'^reg$', reg),
]
```

#### 4 视图函数

在user/views.py中编写视图函数reg,  路由做相应的调整

```
import logging
FORMAT = "%(asctime)s %(threadName)s %(thread)d %(message)s"
logging.basicConfig(format=FORMAT, level=logging.INFO)

from django.http import JsonResponse, HttpRequest, HttpResponse, HttpResponseBadRequest
import json
import simplejson

def reg(request:HttpRequest):
    try:
        payload = json.loads(request.body)
        email = payload['email']
        # 数据库中看看email有没有
        return HttpResponse('welcome to django')
    except Exception as e:
        logging.info(e)
        raise HttpResponseBadRequest()  
```

#### 5 测试JOSN数据

使用POST方法， 提交的数据类型为application/json,  json字符串要用双引号

这个数据是登录和注册的， 有客户端提交



	{
	  "password":"abc",
	  "name":"tom",
	  "email":"aas@wdwd.com"
	}


#### 6 JSON数据处理

simplejson 比标准库方便好用， 功能强大

```
pip install simplejson
```

浏览器端提交的数据放在了请求对象的body中， 需要使用simplejson解析， 解析的方式同json模块，但是

simplejson更方便



#### 7 错误处理

Django中有很多异常类， 定义在django.http下， 这些类都继承自HttpResponse.

	# user/views.py中
	from django.http import HttpRequest, HttpResponse, HttpResponseBadRequest, JsonResponse
	import simplejson
	
	def reg(request:HttpResponse):
		print(request.POST)
		print(request.body)
		payload = simple.loads(reqest.body)
		try:
			email = payload['email']
			name = payload['name']
			password = payload['password']
			print(email, name, password)
			return JsonResponse({}) # 如果正常， 返回json数据
		except Exception as e:       # 有任何异常， 都返回
			return HttpResponseBadRequest    # 这里返回实例， 这不是异常类




## Django ORM操作



