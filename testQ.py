
import matplotlib.pyplot as plt
h, v0, g = 3000, 200, 9.8	#设置参数值
t=eval(input())		#读取时刻t
xt=v0*t				#计算横坐标
yt=h-1/2*g*t**2		#计算纵坐标
plt.plot(xt,yt,'ro')
plt.grid('on') 
plt.show()
