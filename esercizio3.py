import pylab
import numpy

#setting initial values
f_Ta = 50
f_Tb = 25e3
w_Ta = 2*numpy.pi*f_Ta
w_Tb = 2*numpy.pi*f_Tb

f_array = [0.05e3, 0.1e3, 0.4e3, 1.6e3, 6.4e3, 12.8e3]

g_a = dict()
g_b = dict()

#setting accuracy
n = 99

for f in f_array:
    T = 1/f 
    w = 2*numpy.pi*f
    t = numpy.linspace(-2*T, 2*T, 1000)

    #making the lists
    c_karray = []
    w_karray = []
    Aa_karray = []
    phia_karray = []
    Ab_karray = []
    phib_karray = []

    #populating them
    for k in range(1, n, 2):
        c_k = 2/(k*numpy.pi)
        w_k = k*w
        Aa_k = 1/(numpy.sqrt(1+(w_k/w_Ta)**2))
        phia_k = numpy.arctan(-w_k/w_Ta)
        Ab_k = 1/(numpy.sqrt(1+(w_Tb/w_k)**2))
        phib_k = numpy.arctan(w_Tb/w_k)
        c_karray.append(c_k)
        w_karray.append(w_k)
        Aa_karray.append(Aa_k)
        phia_karray.append(phia_k)
        Ab_karray.append(Ab_k)
        phib_karray.append(phib_k)

    #making g_a(t)
    g_a[f] = []

    #doing the sum for each t and populating g(t)
    for i in t:
    	ga_i = ([(A_k*c_k*numpy.sin(w_k*i+phi_k)) for A_k, c_k, w_k, phi_k in zip(Aa_karray, c_karray, w_karray, phia_karray)])
    	g_a[f].append(sum(ga_i))

    g_b[f] = []

    for i in t:
        gb_i = ([(Aa_k*Ab_k*c_k*numpy.sin(w_k*i+phia_k+phib_k)) for Aa_k, Ab_k, c_k, w_k, phia_k, phib_k in zip(Aa_karray, Ab_karray, c_karray, w_karray, phia_karray, phib_karray)])
        g_b[f].append(sum(gb_i))



#plotting in a cutie way
n_plots = len(f_array)
cols = 2
rows = n_plots/cols

pylab.figure(1)
pylab.suptitle("Integrator output waveforms simulation", fontsize=14)

for h, f in zip(range(1, n_plots+1, 1), f_array):
    pylab.subplot(rows, cols, h)
    pylab.plot(t*f, g_a[f], label='f = %d Hz' % f) #period set as x-unit
    pylab.legend(prop={'size':10})
    pylab.locator_params(nbins=4)
    pylab.grid()

    #not really elegant, but less boring...
    if (h==3):
        pylab.ylabel('Simulated Signal [arb.un.]', size='large')
    if (h==5) or (h==6):
        pylab.xlabel('Time [T]', size='large')

pylab.figure(2)
pylab.suptitle("Integrator + differentiator output waveforms simulation", fontsize=14)

for h, f in zip(range(1, n_plots+1, 1), f_array):
    pylab.subplot(rows, cols, h)
    pylab.plot(t*f, g_b[f], label='f = %d Hz' % f) #period set as x-unit
    pylab.legend(prop={'size':10})
    pylab.locator_params(nbins=4)
    pylab.grid()

    #not really elegant, but less boring...
    if (h==3):
        pylab.ylabel('Simulated Signal [arb.un.]', size='large')
    if (h==5) or (h==6):
        pylab.xlabel('Time [T]', size='large')

pylab.show()