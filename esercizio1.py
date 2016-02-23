#with the fascinating programming of a. iorio & s. tirone
import pylab
import numpy

#setting initial values
T = 1
n_array = [2,4,9,49,99, 499]
w = 2*numpy.pi/T
t = numpy.linspace(-2, 2, 1000)
g = dict()

for n in n_array:
	#making the arrays c_k, w_k
	c_karray = []
	w_karray = []

	for k in range(1, n, 2):
	    c_k = 2/(k*numpy.pi)
	    w_k = k*w
	    c_karray.append(c_k)
	    w_karray.append(w_k)

	#make g(t)
	g[n] = []

	#doing the sum for each t and populate g(t)
	for i in t:
		g_i = ([(c_k*numpy.sin(w_k*i)) for c_k, w_k in zip(c_karray, w_karray)])
		g[n].append(sum(g_i))

#plotting in a cutie way
n_plots = len(n_array)
cols = 2
rows = n_plots/cols

pylab.figure(1)
pylab.suptitle("Square waveform simulation", fontsize=14)

for h, n in zip(range(1, n_plots+1,1), n_array):
	pylab.subplot(rows, cols, h)
	pylab.plot(t/T, g[n], label='n = %d' % n) #setting period as x-unit
	pylab.legend(prop={'size':10})
	pylab.locator_params(nbins=4)
	pylab.grid()

	#not really elegant, but less boring...
	if (h==3):
		pylab.ylabel('Simulated Signal [arb.un.]', size='large')
	if (h==5) or (h==6):
		pylab.xlabel('Time [T]', size='large')

pylab.show()