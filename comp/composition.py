class mydate:
	def __init__(self,dd,mm,yy):
		self.dd=dd
		self.mm=mm
		self.yy=yy
	def __str__(self):   #automatically invoked
		return str(self.dd)+'-'+str(self.mm)+'-'+str(self.yy)
	def key(self):
		return self.yy*365+self.mm*30+self.dd

ob=mydate(15,8,1947)
#print(ob)
print(ob.key())



class myevent:
	def __init__(self,dd,mm,yy,detail):
		self.date=mydate(dd,mm,yy)
		self.detail=detail
	def __str__(self):               #automatically invoked
		return str(self.date)+'->'+self.detail
	def key(self):
		#return self.detail
		return self.date.key()

e=myevent(15,8,1947,'independence day')
print(e)
print(e.key())