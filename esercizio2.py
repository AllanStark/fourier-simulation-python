import pylab
import numpy

#setting initial values
R = 330
C = 0.1e-6
f_T = 1/(2*numpy.pi*R*C)
w_T = 2*numpy.pi*f_T

f_array = [0.2e3, 0.4e3, 1.6e3, 6.4e3, 12.8e3, 25.6e3]

#setting accuracy
n = 99

g = dict()

for f in f_array:
    T = 1/f
    w = 2*numpy.pi*f
    t = numpy.linspace(-2*T, 2*T, 1000)

    #making the lists
    c_karray = []
    w_karray = []
    A_karray = []
    phi_karray = []

    #populating them
    for k in range(1, n, 2):
        c_k = 2/(k*numpy.pi)
        w_k = k*w
        A_k = 1/(numpy.sqrt(1+(w_k/w_T)**2))
        phi_k = numpy.arctan(-w_k/w_T)
        c_karray.append(c_k)
        w_karray.append(w_k)
        A_karray.append(A_k)
        phi_karray.append(phi_k)

    #making g(t)
    g[f] = []

    #doing the sum for each t and populating g(t)
    for i in t:
    	g_i = ([(A_k*c_k*numpy.sin(w_k*i+phi_k)) for A_k, c_k, w_k, phi_k in zip(A_karray, c_karray, w_karray, phi_karray)])
    	g[f].append(sum(g_i))

#plotting in a cutie way
n_plots = len(f_array)
cols = 2
rows = n_plots/cols

pylab.figure(1)
pylab.suptitle("Shark fin waveform simulation", fontsize=14)

for h, f in zip(range(1, n_plots+1, 1), f_array):
    pylab.subplot(rows, cols, h)
    pylab.plot(t*f, g[f], label='f = %d Hz' % f) #period set as x-unit
    pylab.legend(prop={'size':10})
    pylab.locator_params(nbins=4)
    pylab.grid()

    #not really elegant, but less boring...
    if (h==3):
        pylab.ylabel('Simulated Signal [arb.un.]', size='large')
    if (h==5) or (h==6):
        pylab.xlabel('Time [T]', size='large')

pylab.show()