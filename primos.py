import os
from flask import Flask


app = Flask(__name__)


@app.route('/')
def primos():
    num_primos = "2, 3, "
    num = 4
    cont = 1
    while cont < 99:
        divisores = 0
        for i in range(1, num+1):
            if num % i == 0:
                divisores += 1
        if divisores == 2:
            if cont < 98:
                num_primos = num_primos + str(num) + ', '
            else:
                num_primos = num_primos + str(num) + '.'
            cont += 1
        num += 1
    return num_primos


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
