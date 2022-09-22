import mathimport numpy as npimport soundfile as sffrom matplotlib import pyplot as pltimport sounddevice as sd#Eviatar Cohen - 205913858#Hai Moyal - 205913858def FourierCoeffGen(signal):    # TODO: Implement the FourierCoeffGen function.    pie = np.pi    w_0 = (2 * pie) / N    j = complex(0, 1)    FourierCoeff = []    for k in range(N):        a = 0        for n in range(N):            a=a+ signal[n] * np.exp(-j * w_0 * n * k)        a = a/N        FourierCoeff.append(a)    return FourierCoeffdef DiscreteFourierSeries(FourierCoeff):    # TODO: Implement the FourierSeries function.    pie = math.pi    w_0 = (2 * pie) / N    j = complex(0, 1)    # with the FourierCoeff compute the signal in time    signal = []    for n in range(N):        x = 0        for k in range(N):            x = x + FourierCoeff[k] * np.exp(j * w_0 * n * k)        signal.append(x)    return signal# %% import wav file C:\Users\eviat\Desktop\pyton 1wav_path = "C:/Users/eviat/Desktop/pyton1/about_time.wav"  #in part 3 put in our recording# Insert your path here, you can pick another wav file!signal, fs = sf.read(wav_path)signal = signal[:10 * fs]  # 10 secoundsplt.figure(1)plt.title("Input signal Wave")plt.plot(signal)plt.show()# %% ParametersN = int(512)step = int(N / 4)kk = 0M = 3signal_out = np.zeros(M * len(signal))  # output lengthphase_pre = np.ones(N)last_phase = np.ones(N)current_phase = 0b_k = 0# %%for k in range(0, signal.shape[0] + 1 - N, step):    # Analysis    x = np.multiply(signal[k:k + N], np.hamming(N))    a_k = FourierCoeffGen(x)    print(k)    # TODO: 1. Extract the Frame's phase.    #       2. Find the diff phase    phase = 0    phase_diff = 0    phase = [i/abs(i) for i in a_k] #divide to find phase and add to array    phase_diff = np.divide(phase, phase_pre)    for n in range(M):        current_phase = last_phase * phase_diff        b_k = [abs(i) for i in a_k] * current_phase        last_phase = current_phase        w = np.real(DiscreteFourierSeries(b_k))        z = np.multiply(w, np.hamming(N))        signal_out[kk:kk + N] = signal_out[kk:kk + N] + z        kk = kk + step    phase_pre = phaseplt.figure(2)plt.title("Output signal Wave")plt.plot(signal_out)plt.show()output_path = "C:/Users/eviat/Desktop/pyton1/about_time-m3.wav"  # write your path here!sf.write(output_path, signal_out, fs)sd.play(signal_out, fs)