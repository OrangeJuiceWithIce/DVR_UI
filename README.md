# pytest文件
用于**简陋**的后端测试的，效果可能**有限**

# 代码
目前分成了四个组件：图片viewer,输入框和step按钮,checkpoints,导出按钮

所有的API(fetch请求)都写在了App.vue中(纯新手，这样感觉比较好传参..)

# 逻辑
## 三种step
### 1.explore:
一开始会默认进行一次 ps:如果要先加载已有的checkpoint可以修改下这一步的逻辑，位于App.vue的.mount()部分
如果没有提供query，并选择了所有的高斯，则会进行explore.
### 2.text guide
提供了query并选择了所有的高斯
### 3.text and region guide
提供了query并只选择了部分高斯，

#### 如果只选择了部分高斯而没有提供query，则要求提供query