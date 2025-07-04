#引入需要用到的硬件库
import sensor, lcd, time
import image

#读取时钟
clock = time.clock()

sensor.reset()#初始化摄像头
sensor.set_pixformat(sensor.RGB565)#设置摄像头格式
sensor.set_framesize(sensor.QVGA)#设置分辨率
#sensor.set_hmirror(enable) #设置水平镜像
#sensor.set_vflip(enable) #设置垂直翻转

sensor.run(1)#开始运行，也可以不调用，上面设置完成后，摄像头会自动开始运动
sensor.skip_frames()#摄像头刚启动时，图像质量还没稳定，所以要跳过一些图像，默认跳过10帧

lcd.init()#初始化lcd

while(True):
    fps =clock.fps()#获取当前显示帧率
    clock.tick()

    img = sensor.snapshot()#抓取一张照片
    img.draw_string(0,210,("%2.1f fps" %(fps)), color=(0,0,255), scale=2)#显示字符串
    #("%2.1f fps" %(fps))是python的格式化语法，作用是把fps（当前帧率）格式化位小数并拼接字符串
    #%2.1f表示保留一位小数，总宽度至少为2位
    img.draw_rectangle(0,0,30,30,color=(0,0,255),fill=False)#显示色块/方框 fill：是否填充

    lcd.display(img)#在lcd屏幕显示

    #lcd.rotation(2) #旋转屏幕方向
