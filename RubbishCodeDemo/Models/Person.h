//
//  Person.h
//  RubbishCodeDemo
//
//  Created by aoni on 2018/9/28.
//  Copyright © 2018年 cft. All rights reserved.
//

#import <Foundation/Foundation.h>

// 对于model需要导入 UIKit 框架，可以给model一个baseModel基类，在基类 import <UIKit/UIKit.h>
#import <UIKit/UIKit.h>

@interface Person : NSObject

@property (nonatomic, copy)   NSString  *name;

@property (nonatomic, assign) float height;


@end
