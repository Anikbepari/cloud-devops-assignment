<<<<<<< HEAD
import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def SayHello():
    return f"{os.environ.get('MSG')}"

if __name__ == '__main___':
    app.run(debug=True, port=5000, host='0.0.0.0')

=======
import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def SayHello():
    return f"{os.environ.get('MSG')}"

if __name__ == '__main___':
    app.run(debug=True, port=5000, host='0.0.0.0')

>>>>>>> 362b2fc3fdaa515230f4e5c970b18a4f9a0824d0
