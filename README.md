# train01
20191122_ui_test

Definition	定义
PO 即 page object 页面对象，
1.是一种设计模式,用来管理维护一组页面元素的对象库。
2.在PO下,应用程序的每一个页面都有一个对应的Page类.
3.每一个Page类维护着该页面的元素集和操作这些元素的方法.
4.和面向对象的特性相同。面向对象的特性：封装、继承、多态。


Subject		主题
设计模式之PO设计模式在UI自动化上的应用

 

Disadvantages of traditional script	传统脚本的弊端
1.测试脚本未分离，维护成本高，牵一发而动全身。
2.可扩展性差，复用性低，只针对某个问题做解决方案。

Advantage	优势
二次封装，使开发者专注于变化的参数。
1.代码可读性强，掌握函数后，只专注于变化的参数，并作修改。
2.可维护性高，每次只改写特定的几个参数，不改内部函数。
3.复用性高，针对不同场景，封装了简便易用的函数，可直接调用，或任意搭配。

PO的核心要素：
1.在PO模式中抽象封装成一个BasePage类，该基类应该拥有一个只实现webdriver实例的属性。
2．每个一个page都继承BasePage，通过driver来管理本page中元素，将page中的操作封装成一个个的方法。

设计的原则
1.抽象每一个页面
2.页面中元素不暴露,仅报错操作元素的方法
3.页面不应该有繁琐的继承关系
4.页面中不是所有元素都需要涉及到,核型业务元素做建模使用
5.把页面划分功能模块,在Page中实现这些功能方法
