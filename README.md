# pytest文件
用于**简陋**的后端测试的，效果可能**有限**  

# 如何同时测试后端的多个端口
在根目录下的.env开头的文件中加入自己的4个后端端口
然后运行
```bash
npm run dev:all
```
若只想运行某一个端口
```
npm run dev:port1
npm run dev:port2
npm run dev:port3
npm run dev:port4
```

# 代码
目前分成了四个组件：图片viewer,输入框和step按钮,checkpoints,导出按钮  

所有的API(fetch请求)都写在了App.vue中(纯新手，这样感觉比较好传参..)  

## 已完成的端口
1,2,3,4,5,6,7,8,9,10

## 效果不佳的端口


## 问题
待Test=False再测试一回
