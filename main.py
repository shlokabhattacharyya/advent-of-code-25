import time

import day01
import day02
import day03
import day04
import day05


# answers are a list of [[func, expected], [func, expected]] where func returns the answer for that part of the question.
def verify(day, answers):
    now = time.time()

    for i, pair in enumerate(answers):
        got = pair[0]()
        expected = pair[1]
        print(f"day {day}.{i+1}: got {got}, expected {expected} {'✅' if got == expected else '❌'}")

    total_ms = round((time.time() - now)*10000)/10
    print(f"time taken: {total_ms}ms")
    print("")

    return total_ms

if __name__ == "__main__":
    total_ms = 0

    total_ms += verify(1, day01.answers)
    total_ms += verify(2, day02.answers)
    total_ms += verify(3, day03.answers)
    total_ms += verify(4, day04.answers)
    total_ms += verify(5, day05.answers)

    print(f"took a total of {round(total_ms*100)/100}ms")
