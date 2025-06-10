import matplotlib.pyplot as plt
from scipy import signal
import numpy as np

class automatique:
    def __init__(self, func:list):
        # define the transfer function
        self.num: list = func[0] # 0x^2 + 0x + 1
        self.den: list = func[1] # 0x^2 + 3x + 1

        self.sys = signal.TransferFunction(self.num, self.den)
        # Calcul de la réponse en fréquence
        self.w = np.logspace(-2, 2, 1000)
        self.w, self.H = signal.freqresp(self.sys, self.w)

        self.gain_db = 20 * np.log10(np.abs(self.H))
        self.phase_deg = np.angle(self.H, deg=True)

    # réponse indicielle
    def step(self):
        plt.figure(2)
        t,y = signal.step(self.sys)
        plt.plot(t,y)
        plt.title("Réponse indicielle du système")
        plt.grid(which="both")
        plt.xlabel("t[s]")


    # diagramme de Bode
    def bode(self):
        # Plot the magnitude
        plt.figure(figsize=(10, 6))
        plt.subplot(2, 1, 1)
        plt.semilogx(self.w, self.gain_db)  # Bode magnitude plot
        plt.title("Diagramme de Bode d'amplitude")
        plt.xlabel("Fréquence [Rad/s]")
        plt.ylabel("Gain [dB]")
        plt.grid(True, which="both", ls="--")


        # Plot the phases
        plt.subplot(2, 1, 2)
        plt.semilogx(self.w, self.phase_deg)  # Bode phase plot
        plt.title("Diagramme de Bode de phase")
        plt.xlabel('Fréquence [Hz]')
        plt.ylabel('Phase [°]')
        plt.grid(True, which="both", ls="--")
        plt.tight_layout()



    # Diagramme de Black
    def black(self):
        plt.figure(figsize=(8, 6))
        plt.plot(self.phase_deg, self.gain_db)
        plt.xlabel('Phase (°)')
        plt.ylabel('Gain (dB)')
        plt.title('Diagramme de Black-Nichols')
        plt.grid(True)
        plt.axvline(-180, color='r', linestyle='--', linewidth=0.8)
        plt.axhline(0, color='k', linestyle='--', linewidth=0.5)        


    # Diagramme de nyquist
    def nyquist(self):
        plt.figure(figsize=(6, 6))
        plt.plot(self.H.real, self.H.imag, label='Nyquist direct')
        plt.plot(self.H.real, -self.H.imag, '--', color='gray', label='Nyquist conjugué')
        plt.axhline(0, color='black', linewidth=0.5)
        plt.axvline(0, color='black', linewidth=0.5)
        plt.xlabel('Partie réelle')
        plt.ylabel('Partie imaginaire')
        plt.title('Diagramme de Nyquist')
        plt.grid(True)
        plt.axis('equal')
        plt.legend()

    def show(self):
        plt.show()

    def run(self) -> None:
        self.bode()
        self.black()
        self.nyquist()
        self.show()

def test():
    au = automatique()
    au.bode()  
    au.show()

if __name__ == "__main__":
    test()
    pass