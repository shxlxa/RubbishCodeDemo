# SpamCodeDemo
Add rubbish code for iOS object-c project

用python脚本，给iOS代码添加随机生成的垃圾代码

由于同一个项目需要为不同的客户生成不同UI的app，而这样直接提交审核会在苹果机审代码时被以马甲包的名义拒掉，而且后果很严重，基本上这个bundle ID就废了，因此，需要对app的代码进行一些处理：
# 在项目中增加垃圾代码混淆

>添加垃圾代码的逻辑是，用`python`随机生成各种垃圾代码，循环遍历需要添加代码的文件，读取文件内容，在适当的位置添加垃圾代码

话不多说，上代码:
### 一、在`addRandomUI.py`文件中，有以下函数
#### 1.生成一个随机长度的有大小写字母组成的字符串
```python
# 产生一个satrtIndex到endIndex位长度的随机字符串
def getRandomStr(satrtIndex,endIndex):
numbers = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
# random.choice()从列表中返回一个随机数
final = (random.choice(numbers))
# 从(50,100)列表中取出一个随机数
index = random.randint(satrtIndex, endIndex)
for i in range(index):
final += (random.choice(numbers))
return final
```
#### 2.生成NSString类，NSArray类等等
```python
# 生成NSString类
def addNSString():
line = '- (NSString *)' + getRandomStr(15,20) + ':(NSString *)' + getRandomStr(15,20) + ' {\n   '
stringName = getRandomStr(15,20)
string = 'NSString *' + stringName + ' = @"' + getRandomStr(50,100) + '";\n   return '+ stringName + ';\n}'
return line+string + '\n\n'

# 生成NSArray类
def addNSArray():
line = '- (NSArray *)' + getRandomStr(15,20) + ':(NSArray *)' + getRandomStr(15,20) + ' {\n   '
arrayName = getRandomStr(15,20)
arrayString = 'NSArray *' + arrayName + ' = @[\n'
for i in range(1,15):
element = '     @"' + getRandomStr(50,100) + '",\n'
arrayString += element
arrayString += '  ];\n    return ' + arrayName + ';\n}'
return line + arrayString
```

#### 3.随机调用生成的垃圾代码
```python
# 随机调用(addNSString(),addNSArray(),addNSData(),addNSDictionary(),addUIImage())中的某个函数
def addRandomClass():
index = random.randint(1, 5)
if index == 1:
string = addNSString()
elif index == 2:
string = addNSArray()
elif index == 3:
string = addNSData()
elif index == 4:
string = addNSDictionary()
else:
string = addUIImage()
return string
```

### 二、在`addRubbishCode.py`文件中
>有了addRandomUI.py可以根据需要随机生成垃圾代码，现在的问题就是把这些代码插入到适当的位置，还要保证能运行不出错误

先来看几个函数：
#### 1.由于.h文件和.m文件最后都有`@end`，我们就把垃圾代码添加在最后一个`@end`前面，下面函数获取文件中 `@end` 的总数量
```python
# 获取文件中 @end 的总数量
def GetMFileEndCount(file_path,old_str):
file_data = ""
print('filePath------'+file_path)
Ropen=open(file_path,'r')#读取文件
flagCount = 0
for line in Ropen:
if old_str in line:
flagCount += 1
return flagCount 
```

### 2.向.h文件中添加属性代码
```python
#.h文件添加废代码
def HFileAddCode(file_path,old_str,endTotalCount):
# .h文件里属性的类型从这个数组里随机选
classArray = ['NSString', 'UILabel', 'NSDictionary', 'NSData', 'UIScrollView', 'UIView', 'UITextView',
'UITableView', 'UIImageView']
file_data = ""
Ropen=open(file_path,'r')
flagCount = 0
for line in Ropen:
nameStr = addRandomUI.getRandomStr(6, 10)
className = random.choice(classArray)

if old_str in line:
flagCount += 1
if flagCount==endTotalCount:
file_data += '\n@property(nonatomic,strong) '+className +' *'+nameStr+';\n'
file_data += line
else:
file_data += line
file_data += '\n'
Ropen.close()
Wopen=open(file_path,'w')
Wopen.write(file_data)
Wopen.close()
```
### 3.向.m文件添加垃圾代码
```python
#.m文件添加垃圾代码
def MFileAddCode(file_path,old_str,endTotalCount):

file_data = ""
print('filePath------'+file_path)
Ropen=open(file_path,'r')#读取文件
flagCount = 0
for line in Ropen:
if old_str in line:
flagCount += 1
# 在最后一个 '@end' 前面加上垃圾代码
if flagCount==endTotalCount:
file_data += addRandomUI.addRandomClass() + '\n\n'
file_data += line
else:
file_data += line
Ropen.close()
Wopen=open(file_path,'w')
Wopen.write(file_data)
Wopen.close()
```

### 4.循环遍历指定文件夹中的文件
```python
# 循环递归遍历文件夹
def traverse(file_dir):
fs = os.listdir(file_dir)
for dir in fs:
tmp_path = os.path.join(file_dir, dir)
if not os.path.isdir(tmp_path):
addCode(tmp_path)
else:
# 是文件夹,则递归调用
traverse(tmp_path)
```

### 5.主调用函数
>可以在这里做相关配置  
>`codeCount` ：每个文件中添加的代码数量  
`file_prefix` ：主工程目录  
`file_dirs`： 要添加垃圾代码文件所在的文件夹路径

```python
def addRubbish():
global codeCount
# 每个文件中添加的代码数量
codeCount = 5
# 主工程目录
file_prefix = '../RubbishCodeDemo/'
# 要添加垃圾代码文件所在的文件夹路径
file_dirs = ['ViewControllers',"Views","Models"]
for dir in file_dirs:
file_dir = file_prefix + dir
traverse(file_dir)
```

### 三、其他
#### 1.注意点
>对于那些model文件，需要添加垃圾代码的，需要在model中先导入`UIKit`框架

#### 2. `github`下载链接，欢迎提意见，有帮助的可以`star`一下
[https://github.com/shxlxa/RubbishCodeDemo](https://github.com/shxlxa/RubbishCodeDemo)
- 使用方法：进入到python脚本文件夹, `python3 addRubbishCode.py`运行脚本

#### 3.工程只是加了垃圾代码，还不能通过审核，还需要批量修改类名，给类名添加前缀和后缀，请参考 [https://my.oschina.net/FEEDFACF/blog/1627398](https://my.oschina.net/FEEDFACF/blog/1627398)
>我自己通过加垃圾代码和修改类名这两个方法之后，用同一份代码已经上架了6个app
#### 参考文章：[https://blog.csdn.net/u013857988/article/details/79656048](https://blog.csdn.net/u013857988/article/details/79656048)
