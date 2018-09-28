# -*- coding: utf-8 -*-

import random


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

# name = getRandomStr(50,100)


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


# 生成NSData类
def addNSData():
    line = '- (NSData *)' + getRandomStr(15,20) + ':(NSString *)' + getRandomStr(15,20) + ' {\n   '
    dataName = getRandomStr(15,20)
    string = 'NSData *' + dataName + ' = [@"' + getRandomStr(50,100) + '"' + ' dataUsingEncoding:NSUTF8StringEncoding]' + ';\n   return '+ dataName + ';\n}'
    return line+string


# 生成NSArray类
def addNSDictionary():
    line = '- (NSDictionary *)' + getRandomStr(15,20) + ':(NSArray *)' + getRandomStr(15,20) + ' {\n   '
    dictName = getRandomStr(15,20)
    dictString = 'NSDictionary *' + dictName + ' = @{\n'
    for i in range(1,10):
        element = '      @"' + getRandomStr(15,20) + '" : ' + '@"' + getRandomStr(50,100) + '",\n'
        dictString += element

    dictString += '  };\n    return ' + dictName + ';\n}'
    return line + dictString


# 生成UIImage类
def addUIImage():
    line = '- (UIImage *)' + getRandomStr(15, 20) + ':(UIImage *)' + getRandomStr(15, 20) + ' {\n   '
    dataName = getRandomStr(15, 20)
    imageName = getRandomStr(15, 20)
    string = 'NSData *' + dataName + ' = [@"' + getRandomStr(50,100) + '"' + ' dataUsingEncoding:NSUTF8StringEncoding]' + ';\n   '
    string += 'UIImage *' + imageName + ' = [UIImage imageWithData:' + dataName + '];\n   '
    string += 'return '+ imageName + ';\n}'

    return line+string + '\n\n'


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









