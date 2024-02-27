import numpy as np
import matplotlib.pyplot as plt

class sandbox():
    def progress_bar(progress, total,name):
        percent = int(100 * (progress / total))
        bar = "=" * percent + '-' * (100 - percent)
        print(f"\r{bar}| {name} {percent:.2f}%", end="\r")

    def f(x):
        return x**2 - 1/8 * x**4

    def train(x,y):  # Added self as the first argument
        for deg in [1, 2, 3]:
            reg = np.polyfit(x, y, deg=deg)  # Fit polynomial model
            y_predicted = np.polyval(reg, x)  # Evaluate model predictions
            MSE = np.mean(((y - y_predicted) ** 2))  # Calculate Mean Squared Error

            print(f"deg={deg} | MSE={MSE:.5f}")  # Print degree and MSE

            plt.figure(figsize=(10,6))
            plt.plot(x,y, "ro", label="Some data")
            plt.plot(x, np.polyval(reg, x), label=f"deg={deg}")
            plt.show()

    def test():
        pass

    def run():
        # sequence
        X = [1,2,3,4,5,6,7,8,9,10,11,12,13]
        Y = [sandbox.f(x) for x in X]
        #bets = 1_000_000
        trained_model = sandbox.train(X, Y)

        #attempts = 10_000
        #results = sandbox.test()

        #print(f"\r ACCURACY {round((results/attempts * 100),5)}% ", end="\r")

sandbox.run()
#rl = np.array([np.array([epoch() for _ in range(15)]) for _ in range(50)])
