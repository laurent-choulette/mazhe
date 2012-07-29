from phystricks import *
def MethodeChemin():
	pspict,fig = SinglePicture("MethodeChemin")

	A=Point(-1,1)
	B=Point(1,-1)
	C=Point(-1,-0.5)
	D=Point(1,0.5)
	A.put_mark(0.3,90,"$y=-x$")
	D.put_mark(0.3,45,"$y=x/2$")
	A.parameters.symbol="none"
	D.parameters.symbol="none"
	S1=Segment(A,B)
	S2=Segment(C,D)
	S1.parameters.color="red"
	S2.parameters.color="blue"
	S1.parameters.style="dashed"
	S2.parameters.style=S1.parameters.style

	pspict.DrawGraphs(S1,S2,A,D)

	pspict.axes.no_graduation()
	pspict.DrawDefaultAxes()

	pspict.dilatation(1.5)

	fig.conclude()
	fig.write_the_file()
