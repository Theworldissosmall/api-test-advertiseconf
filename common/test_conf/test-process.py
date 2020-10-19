import threading
import time

'''直接调用'''

def hello(name):
    print("Hello %s"%name)
    time.sleep(3)

if __name__ == "__main__":
    t1=threading.Thread(target=hello,args=("zhangsan",)) #生成线程实例
    t2=threading.Thread(target=hello,args=("lisi",))

    t1.setName("aaa")   #设置线程名
    t1.start()  #启动线程
    t2.start()
    t2.join()   #join  等待t2先执行完
    print("Hello")
    print(t1.getName()) #获取线程名