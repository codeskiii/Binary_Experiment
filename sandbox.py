import numpy as np
import os

class sandbox():
    def train(bets, ssp, asp):
        for bet in range(bets):
            a = np.random.choice(asp)

            s0 = np.random.choice(ssp)
            s1 = np.random.choice(ssp)
            s2 = np.random.choice(ssp)

            if a == s0:
                asp.append(s0)
            elif a == s1:
                asp.append(s1)
            elif a == s2:
                asp.append(s2)

            print("TRAINING", (bet / bets) * 100, "%")

        print("TRAINING ENDED")
        return asp

    def test(trained_model: list, attempts: int, asp: list):
        score = 0
        for attempt in range(attempts):
            a = np.random.choice(trained_model)
            s = np.random.choice(asp)

            if a == s:
                score += 1

            print("TESTING", (attempt / attempts) * 100, "%")

        print("TESTING ENDED")

        return score

    def run():
        asp = [0, 1]

        ssp = [1, 1, 1, 1, 0]
        bets = 50_000
        trained_model = sandbox.train(bets, ssp, asp)

        attempts = 5_000
        results = sandbox.test(trained_model, attempts, asp)

        print("ACCURACY", (results / attempts) * 100, "%" )

sandbox.run()
#rl = np.array([np.array([epoch() for _ in range(15)]) for _ in range(50)])
