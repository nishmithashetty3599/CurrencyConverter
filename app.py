#!flask/bin/python
from flask import Flask, jsonify
from flask import request

app = Flask(__name__)
@app.route('/convert/<int:i>', methods=['GET'])
def convert(i):
    dollar=0
    euro=0
    while(i>0):
        rupee=i;
        dollar = 0.014*i
        euro=0.012*i
        cad=0.018*i
        pound=0.010*i
        aud=0.019*i
        #print(f"{dollar,euro,cad} is the dollor, euro and cad value")
        result={
            "Rupee":rupee,
            "Dollar": dollar,
            "Euro": euro,
            "Canadian Dollar":cad ,
            "Pound sterling":pound,
            "Australian Dollar":aud

              }
        return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
