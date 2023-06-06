
'''
Exercici 1

Reprodueix l'exemple fent servir diferents freqüències per la sinusoide. Al menys considera f_x = 4 kHz, a banda d'una freqüència pròpia en el marge audible. 
Comenta els resultats.

'''	

import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf
import sounddevice as sd      					# Importem el mòdul sounddevice per accedir a la tarja de so

from numpy.fft import fft 


# APARTAT 1 - fx = 440 Hz


T = 2.5										# Durada de T segons
fm = 8000                              		# Freqüència de mostratge en Hz
fx = 440                               		# Freqüència de la sinusoide
A = 4                                  		# Amplitud de la sinusoide
pi = np.pi                             		# Valor del número pi
L = int(fm * T)                      		# Nombre de mostres del senyal digital
Tm =1 / fm                              	# Període de mostratge
t = Tm * np.arange(L)                    	# Vector amb els valors de la variable temporal, de 0 a T
x = A * np.cos(2 * pi * fx * t)      		# Senyal sinusoidal
sf.write('so_exemple1.wav', x, fm)   		# Escriptura del senyal a un fitxer en format wav

Tx = 1 / fx                                 # Període del senyal
Ls = int(fm * 5 * Tx)                       # Nombre de mostres corresponents a 5 períodes de la sinusoide

plt.figure(0)                             # Nova figura
plt.plot(t[0:Ls], x[0:Ls])                # Representació del senyal en funció del temps
plt.xlabel('t en segons')                 # Etiqueta eix temporal
plt.title('5 periodes de la sinusoide')   # Títol del gràfic
plt.show()                                # Visualització de l'objecte gràfic. 

sd.play(x, fm)                	# Reproducció d'àudio

N = 5000                        # Dimensió de la transformada discreta
X = fft(x[0:Ls],N)              # Càlcul de la transformada de 5 períodes de la sinusoide


k = np.arange(N)                      # Vector amb els valors 0≤  k<N

plt.figure(1)                         # Nova figura
plt.subplot(211)                      # Espai per representar el mòdul
plt.plot(k,abs(X))                    # Representació del mòdul de la transformada
plt.title(f'Transformada del senyal de Ls={Ls} mostres amb DFT de N={N}')   # Etiqueta del títol
plt.ylabel('|X[k]|')                  # Etiqueta de mòdul
plt.subplot(212)                      # Espai per representar la fase
plt.plot(k,np.unwrap(np.angle(X)))    # Representació de la fase de la transformad, desenroscada
plt.xlabel('Index k')                 # Etiqueta de l'eix d'abscisses 
plt.ylabel('$\phi_x[k]$')             # Etiqueta de la fase en Latex
plt.show()                            # Per mostrar els grafics





# PROVES I EXERCICIS A FER

# APARTAT 1 - fx = 4000 Hz


T = 2.5  										# Durada de T segons
fx = 4000										# Freqüència de mostratge en Hz
fm = 8000										# Freqüència de la sinusoide
A = 4											# Amplitud de la sinusoide
pi = np.pi 										# Valor del número pi
L = int(fm * T)									# Nombre de mostres del senyal digital
Tm = 1 / fm 									# Període de mostratge
t = Tm * np.arange(L) 							# Vector amb els valors de la variable temporal, de 0 a T
x = A * np.cos(2 * pi * fx * t)					# Senyal sinusoidal
sf.write('so_exemple2.wav', x, fm)				# Escriptura del senyal a un fitxer en format wav


Tx = 1 /fx 										# Període del senyal
Ls = int(fm * 5 * Tx)							# Nombre de mostres corresponents a 5 períodes de la sinusoide

plt.figure(0)									# Nova figura
plt.plot(t[0:Ls], x[0:Ls])						# Representació del senyal en funció del temps
plt.xlabel("t en segons")						# Etiqueta eix temporal
plt.title("5 periodes de la sinusoide")			# Títol del gràfic
plt.show()										# Visualització de l'objecte gràfic.

sd.play(x, fm)              					# Reproducció d'àudio



# Domini transformat. Analitzant en freqüència fent servir la Transformada Discreta de Fourier

N = 5000 										# Dimensió de la transformada discreta
X = fft(x[0:Ls],N)								# Càlcul de la transformada de 5 períodes de la sinusoide

k = np.arange(N)								# Vector amb els valors 0≤  k<N

plt.figure(1)									# Nova figura
plt.subplot(211)								# Espai per representar el mòdul
plt.plot(k,abs(X))								# Representació del mòdul de la transformada
plt.title(f'Transformada del senyal de Ls={Ls} mostres amb DFT de N={N}')	# Etiqueta del títol
plt.ylabel('|X[k]|')							# Etiqueta de mòdul
plt.subplot(212)								# Espai per representar la fase
plt.plot(k, np.unwrap(np.angle(X)))				# Representació de la fase de la transformad, desenroscada
plt.xlabel('Index k')							# Etiqueta de l'eix d'abscisses 
plt.ylabel('$\phi_x[k]$')						# Etiqueta de la fase en Latex
plt.show()										# Per mostrar els grafics





# APARTAT 1 - fx = 40 Hz

T = 2.5  										# Durada de T segons
fx = 40											# Freqüència de mostratge en Hz
fm = 8000										# Freqüència de la sinusoide
A = 4											# Amplitud de la sinusoide
pi = np.pi 										# Valor del número pi
L = int(fm * T)									# Nombre de mostres del senyal digital
Tm = 1 / fm 									# Període de mostratge
t = Tm * np.arange(L) 							# Vector amb els valors de la variable temporal, de 0 a T
x = A * np.cos(2 * pi * fx * t)					# Senyal sinusoidal
sf.write('so_exemple3.wav', x, fm)				# Escriptura del senyal a un fitxer en format wav


Tx = 1 / fx 										# Període del senyal
Ls = int(fm * 5 * Tx)							# Nombre de mostres corresponents a 5 períodes de la sinusoide

plt.figure(0)									# Nova figura
plt.plot(t[0:Ls], x[0:Ls])						# Representació del senyal en funció del temps
plt.xlabel("t en segons")						# Etiqueta eix temporal
plt.title("5 periodes de la sinusoide")			# Títol del gràfic
plt.show()										# Visualització de l'objecte gràfic.

sd.play(x, fm)              					# Reproducció d'àudio



# Domini transformat. Analitzant en freqüència fent servir la Transformada Discreta de Fourier

N = 5000 										# Dimensió de la transformada discreta
X = fft(x[0:Ls],N)								# Càlcul de la transformada de 5 períodes de la sinusoide

k = np.arange(N)								# Vector amb els valors 0≤  k<N

plt.figure(1)									# Nova figura
plt.subplot(211)								# Espai per representar el mòdul
plt.plot(k,abs(X))								# Representació del mòdul de la transformada
plt.title(f'Transformada del senyal de Ls={Ls} mostres amb DFT de N={N}')	# Etiqueta del títol
plt.ylabel('|X[k]|')							# Etiqueta de mòdul
plt.subplot(212)								# Espai per representar la fase
plt.plot(k, np.unwrap(np.angle(X)))				# Representació de la fase de la transformad, desenroscada
plt.xlabel('Index k')							# Etiqueta de l'eix d'abscisses 
plt.ylabel('$\phi_x[k]$')						# Etiqueta de la fase en Latex
plt.show()										# Per mostrar els grafics



'''  ---------------------------------------------------------------------------------------------------------

 EXERCICI 2 - fx = 440.

 Modifica el programa per considerar com a senyal a analitzar el senyal del fitxer wav que has creat (x_r, fm = sf.read('nom_fitxer.wav'))

- Insereix a continuació una gràfica que mostri 5 períodes del senyal i la seva transformada.

- Explica el resultat del apartat anterior.

''' 


x_r, fm = sf.read('so_exemple1.wav')				# llegim l'arxiu .wav creat anteriorment amb fx de 440 Hz

fx = 440 											# Utilizada la de la introducció
L = int(fm * T)
Tm = 1 / fm
t = Tm * np.arange(L)

Tx = 1 / fx
Ls = int(fm * 5 * Tx)
plt.figure(0)
plt.plot(t[0:Ls], x_r[0:Ls])
plt.xlabel("t en segons")
plt.title("5 periodes de la sinusoide")
plt.show()

X = fft(x_r[0:Ls],N)

k = np.arange(N)
plt.figure(1)
plt.subplot(211)
plt.plot(k,abs(X))
plt.title(f'Transformada del senyal de Ls={Ls} mostres amb DFT de N={N}')
plt.ylabel('|X[k]|')
plt.subplot(212)
plt.plot(k,np.unwrap(np.angle(X)))
plt.xlabel('Index k')
plt.ylabel('$\phi_x[k]$')
plt.show() 



# APARTAT 2 - fx = 4000 Hz


x_r, fm = sf.read('so_exemple2.wav')				# llegim l'arxiu .wav creat anteriorment amb fx de 4000 Hz

fx = 4000 											# Utilizada la de la introducció
L = int(fm * T)
Tm = 1 / fm
t = Tm * np.arange(L)

Tx = 1 / fx
Ls = int(fm * 5 * Tx)
plt.figure(0)
plt.plot(t[0:Ls], x_r[0:Ls])
plt.xlabel("t en segons")
plt.title("5 periodes de la sinusoide")
plt.show()

X = fft(x_r[0:Ls],N)

k = np.arange(N)
plt.figure(1)
plt.subplot(211)
plt.plot(k,abs(X))
plt.title(f'Transformada del senyal de Ls={Ls} mostres amb DFT de N={N}')
plt.ylabel('|X[k]|')
plt.subplot(212)
plt.plot(k,np.unwrap(np.angle(X)))
plt.xlabel('Index k')
plt.ylabel('$\phi_x[k]$')
plt.show() 


# APARTAT 2 - fx = 40 Hz


x_r, fm = sf.read('so_exemple3.wav')				# llegim l'arxiu .wav creat anteriorment amb fx de 40 Hz

fx = 40 											# freq a 40 Hz
L = int(fm * T)
Tm = 1 / fm
t = Tm * np.arange(L)

Tx = 1 / fx
Ls = int(fm * 5 * Tx)
plt.figure(0)
plt.plot(t[0:Ls], x_r[0:Ls])
plt.xlabel("t en segons")
plt.title("5 periodes de la sinusoide")
plt.show()

X = fft(x_r[0:Ls],N)

k = np.arange(N)
plt.figure(1)
plt.subplot(211)
plt.plot(k,abs(X))
plt.title(f'Transformada del senyal de Ls={Ls} mostres amb DFT de N={N}')
plt.ylabel('|X[k]|')
plt.subplot(212)
plt.plot(k,np.unwrap(np.angle(X)))
plt.xlabel('Index k')
plt.ylabel('$\phi_x[k]$')
plt.show() 
