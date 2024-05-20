import matplotlib.pyplot as pl

if __name__ == '__main__':
    y01 = [0.53899024, 0.67930037, 0.78378745, 0.84233241, 0.89311158, 0.88542331, 0.90292339]
    SNR = [0,3,6,9,12,15,18]
    
    # pl.plot(SNR,y01,'bo',SNR,y01)
    
    # pl.xlabel('SNR, dB')
    # pl.ylabel('BLEU(1-grams)')
    # pl.title('Rayleigh Fading channel')
    # pl.xlim(min(SNR),max(SNR))

    # pl.show()

    y11 = [0.60711777, 0.75727145, 0.83526361, 0.89197901, 0.91549998, 0.92940773, 0.92803982]
    y12 = [0.4848381,  0.68886172, 0.75556871, 0.82907291, 0.87055164, 0.87728947, 0.88486143]
    y13 = [0.41760923, 0.60320102, 0.71430683, 0.78418767, 0.81635434, 0.83351709, 0.83447743]
    y14 = [0.3758477301243779, 0.5513889622638848, 0.6791147140362426, 0.738276030831145, 0.775154801057932, 0.7855812583529225, 0.7890007027454364]
    pl.figure(figsize=[12, 3])
    
    pl.subplot(1, 4, 1)
    pl.plot(SNR,y11,'bo',SNR,y11)
    pl.xlabel('SNR, dB')
    pl.ylabel('BLEU(1-grams)')
    pl.grid()
    pl.title('Rician channel')
    pl.ylim(0,1)
    pl.xlim(min(SNR),max(SNR))

    pl.subplot(1, 4, 2)
    pl.plot(SNR,y12,'bo',SNR,y12)
    pl.xlabel('SNR, dB')
    pl.ylabel('BLEU(2-grams)')
    pl.grid()
    pl.title('Rician channel')
    pl.ylim(0,1)
    pl.xlim(min(SNR),max(SNR))
    
    pl.subplot(1, 4, 3)
    pl.plot(SNR,y13,'bo',SNR,y13)
    pl.xlabel('SNR, dB')
    pl.ylabel('BLEU(3-grams)')
    pl.grid()
    pl.title('Rician channel')
    pl.ylim(0,1)
    pl.xlim(min(SNR),max(SNR))
    
    
    pl.subplot(1, 4, 4)
    pl.plot(SNR,y14,'bo',SNR,y14)
    pl.xlabel('SNR, dB')
    pl.ylabel('BLEU(4-grams)')
    pl.grid()
    pl.title('Rician channel')
    pl.xlim(min(SNR),max(SNR))
    pl.ylim(0,1)
    
    # pl.plot(SNR,y11,'bo',SNR,y11)
    # pl.xlabel('SNR, dB')
    # pl.ylabel('BLEU(1-grams)')
    # pl.title('Rician channel')
    # pl.xlim(min(SNR),max(SNR))
    # pl.show()
   
    y21 = [0.49806338, 0.8322574,  0.92799939, 0.93621025, 0.93777584, 0.93851196, 0.93883513]
    y22 = [0.26410709, 0.72498843, 0.87540947, 0.88640929, 0.88805711, 0.88904494, 0.88916681]
    y23 = [0.15310784, 0.6365255,  0.82732693, 0.84094146, 0.84362299, 0.84437113, 0.84461711]
    y24 = [0.0881179,  0.55759539, 0.77904386, 0.79583771, 0.79781573, 0.79812927, 0.79843169]
    pl.figure(figsize=[12, 3])
    
    pl.subplot(1, 4, 1)
    pl.plot(SNR,y21,'bo',SNR,y21)
    pl.xlabel('SNR, dB')
    pl.ylabel('BLEU(1-grams)')
    pl.grid()
    pl.title('AWGN channel')
    pl.xlim(min(SNR),max(SNR))
    pl.ylim(0,1)

    pl.subplot(1, 4, 2)
    pl.plot(SNR,y22,'bo',SNR,y22)
    pl.xlabel('SNR, dB')
    pl.ylabel('BLEU(2-grams)')
    pl.grid()
    pl.title('AWGN channel')
    pl.xlim(min(SNR),max(SNR))
    pl.ylim(0,1)
    
    pl.subplot(1, 4, 3)
    pl.plot(SNR,y23,'bo',SNR,y23)
    pl.xlabel('SNR, dB')
    pl.ylabel('BLEU(3-grams)')
    pl.grid()
    pl.title('AWGN channel')
    pl.xlim(min(SNR),max(SNR))
    pl.ylim(0,1)
    
    pl.subplot(1, 4, 4)
    pl.plot(SNR,y24,'bo',SNR,y24)
    pl.xlabel('SNR, dB')
    pl.ylabel('BLEU(4-grams)')
    pl.grid()
    pl.title('AWGN channel')
    pl.xlim(min(SNR),max(SNR))
    pl.ylim(0,1)
    
   
    y31 = [0.53899024, 0.67930037, 0.78378745, 0.84233241, 0.89311158, 0.88542331, 0.90292339]
    y32 = [0.24778430208663652, 0.4914229168474284, 0.6234316810259233, 0.7366962725503247, 0.804935637949179, 0.8514473008129537, 0.8592001236058964]
    y33 = [0.20934288965575593, 0.39952964604732644, 0.5591322791842337, 0.6846490884136012, 0.7587716340920249, 0.8087580100576972, 0.8179758996846151]
    y34 = [0.16160327443105685, 0.3657794905851055, 0.5201967550825642, 0.6355342463590606, 0.7101006008808349, 0.7513193230221504, 0.7845047935474156]
    pl.figure(figsize=[12, 3])
    
    pl.subplot(1, 4, 1)
    pl.plot(SNR,y31,'bo',SNR,y31)
    pl.xlabel('SNR, dB')
    pl.ylabel('BLEU(1-grams)')
    pl.grid()
    pl.title('Rayleigh Fading channel')
    pl.ylim(0,1)
    pl.xlim(min(SNR),max(SNR))

    pl.subplot(1, 4, 2)
    pl.plot(SNR,y32,'bo',SNR,y32)
    pl.xlabel('SNR, dB')
    pl.ylabel('BLEU(2-grams)')
    pl.grid()
    pl.title('Rayleigh Fading channel')
    pl.ylim(0,1)
    pl.xlim(min(SNR),max(SNR))
    
    pl.subplot(1, 4, 3)
    pl.plot(SNR,y33,'bo',SNR,y33)
    pl.xlabel('SNR, dB')
    pl.ylabel('BLEU(3-grams)')
    pl.grid()
    pl.title('Rayleigh Fading channel')
    pl.ylim(0,1)
    pl.xlim(min(SNR),max(SNR))
    
    
    pl.subplot(1, 4, 4)
    pl.plot(SNR,y34,'bo',SNR,y34)
    pl.xlabel('SNR, dB')
    pl.ylabel('BLEU(4-grams)')
    pl.grid()
    pl.title('Rayleigh Fading channel')
    pl.xlim(min(SNR),max(SNR))
    pl.ylim(0,1)
    
    
    pl.show()
    
    