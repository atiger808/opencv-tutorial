### 2.1第一个django项目

```
创建项目
1. 通过命令行方式： 首先进入到安装的虚拟环境， 然后执行命令：
    django-admin startproject [项目名称]
2. 通过pycharm 的方式

运行项目：
1. python manage.py runserver， 这样可以在本地访问你得到网站， 默认端口号8000，
2. pycharm: 直接点击右上角的绿色三角箭头
注意：用pycharm 运行项目， 要避免一个项目运行多次
      在项目配置中， 把'只用单一实例' 那个选项勾选上

改变端口号：
1. 在终端运行时加上端口号： python manage.py runserver 9000, 这样可以通过9000端口来访问

让同局域网中的其他电脑访问本机的项目
1. 那么需要指定ip地址为 0.0.0.0
   示例为：python manage.py runserver 0.0.0.0:8000
   然后 修改 setting.py 文件 ALLOWED_HOSTS = ['192.168.43.117'] IP地址为本机ip地址
   注意： 关闭电脑防火墙
```

#### 项目结构分析

```
1. manage.py
    以后和项目交互基本上都是基于这个文件， 一般都是在终端输入 python manage.py [子命令]
2. setting.py
    保存项目的所有配置信息
3. urls.py
    用来做url 与视图函数映射的， 以后来的一个请求， 就会从这个文件中找到视图函数
4. wsig.py
    专门用来做部署的， 不需要修改
```

#### 视图函数

```
1. 视图函数的第一个参数必须是request, 这个参数绝对不能少
2. 视图函数的返回值必须是 'django.http.response.HttpResponseBase' 的子类的对象
```

#### url传参数

```
url 映射
1. 为什么会去urls.py 文件中寻找映射呢？
   是因为 setting.py 文件配置了 ROOT_URLCONF 为 urls.py. 所有django
   会去 urls.py 中寻找
2. 在 urls.py 中我们所有的映射， 都应该放在 urlpatterns 这个变量中
3. 所有的映射不是随便写的， 而是使用 path 函数或者是 re_path 函数进行包装的

url 传参数
1. 采用在url中使用变量的方式， 在path的第一个参数中， 使用 '<参数名>'的方式产地
   参数， 然后在视图函数中也要写一个参数，视图参数中的参数必须和 url 中的参数保持一致
   ， 不然就找不到这个参数， 另外， url 中可以传递多个参数
2. 采用查询字符串的方式： 在url中， 不需要单独的匹配查询字符串的部分， 只需要视图
   函数中使用'request.GET.get('参数名称')' 的方式来获取， 示例：
   '''
   def author_detail(request):
        author_id = request.GET.get('id')
        text = '作者的id是：%s' % author_id
        return HttpResponse(text)
   '''
   因为查询字符串使用的是 GET 请求， 所以我们通过request.GET 来获取参数，
   并且因为 GET 是一个类似字典的数据类型， 所有获取值跟字典的方式是一样的

```

#### url 命名

```
为什么需要url 命名？
  因为url是经常变化的， 如果在代码中写死可能会经常改代码，给url 取个名字
  以后使用url的时候就使用它的名字进行反转就可以了， 就不需要写死utl

如何给一个url指定名称
  在path 函数中， 传递一个name参数就可以指定。 示例代码如下：
  '''
  urlpatterns = [
    path('', views.index, name='index'),
    path('signin/', views.login, name='login'),
]
  '''

应用命名空间
  在多个app之间， 有可能产生同名url, 这个时候为了避免反转url的时候产生混淆， 就使用
  应用命名空间来区分， 只要在app的urls.py 中定义一个 app_name 的变量， 来指定这个应用的
  命名空间即可， 示例代码如下：
  '''
  #应用命名空间
  app_name = 'font'

   urlpatterns = [
       path('', views.index, name='index'),
       path('signin/', views.login, name='login'),
   ]
   '''
   以后在做反转的时候就可以使用 '应用命名空间: url名称' 的方式进程反转
   示例代码如下：
   '''
   login_url = reverse('font:login')
   '''
```