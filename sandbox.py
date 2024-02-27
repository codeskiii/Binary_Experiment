import numpy as np
import os

class sandbox():
    def train(bets: int, model_0: list, ans: list):  # Added self as the first argument
        for bet in range(bets):
            a = np.random.choice(ans)

            if a == 1:
                model_0.append(1)
            elif a == 0:
                model_0.append(0)

            print("TRAINING", (bet / bets) * 100, "%")

        print("TRAINING ENDED")
        return model_0

    def test(trained_model: list, attempts: int, ans: list):
        score = 0
        for attempt in range(attempts):
            a = np.random.choice(ans)
            s = np.random.choice(trained_model)

            if a == s:
                score += 1

            print("TESTING", (attempt / attempts) * 100, "%")

        print("TESTING ENDED")
        return score

    def run():
        model_0 = [0, 1]
        # 1 - 2/3   0 - 1/3
        ans = [1, 1, 0, 0, 0]
        bets = 100_000
        trained_model = sandbox.train(bets, model_0, ans)

        attempts = 25_000
        results = sandbox.test(trained_model, attempts, ans)

        print("ACCURACY", (results / attempts) * 100, "%" )

sandbox.run()
#rl = np.array([np.array([epoch() for _ in range(15)]) for _ in range(50)])
