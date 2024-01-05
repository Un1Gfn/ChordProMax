#!/dev/null

from flask import Flask, request, make_response
from subprocess import run
from time import time
from sys import stdout
from os import getenv
# from io import BytesIO

TRANSPOSE = {
    'Gb':  "-6",
    'Db': "-11",
    'Ab':  "-4",
    'Eb':  "-9",
    'Bb':  "-2",
    'F':   "-7",
    'C':    "0",
    'G':   "+7",
    'D':   "+2",
    'A':   "+9",
    'E':   "+4",
    'B':  "+11",
    'Fi':  "+6",
    'Ci':  "+1",
}

app = Flask(__name__)

# @app.route('/', methods = ['POST',])
@app.route('/', methods = ['POST',])
def hello_world():

    # lead = request.args.get("lead", default="Unknown Person")
    # subtitle = f"({lead})"
    subtitle = ""

    key = request.args.get("key", default="C")
    assert key in TRANSPOSE

    # time_and_tempo = 4/4 time 114

    # data = request.form
    data = request.get_data()
    assert type(data) == bytes
    # print(data.decode())

    args = [
        getenv('CHORDPRO'),
        "--config=./conf.prp",
        "--diagrams=none",
        "-o", "/dev/stdout",
        "--meta", f"key={key}",
        "--meta", f"subtitle={subtitle}",
        "-x", TRANSPOSE[key],
        "--no-strict",
        "-",
    ]
    print(args)
    stdout.flush()

    p = run(args, input=data, capture_output=True)
    if p.stderr != b'':
        print("\n*******")
        print(p.stderr.decode(), end="")
        print("*******\n")
        stdout.flush()
        raise RuntimeError
    assert p.returncode == 0
    assert type(p.stdout) == bytes

    fn = f"{int(time())}.pdf"
    print(fn)

    response = make_response(p.stdout)
    response.headers.set('Content-Type', "application/pdf")
    response.headers.set('Content-Disposition', "attachment", filename=fn)
    response.headers.set('Access-Control-Allow-Origin', "*")
    return response

    # return Response(
    #     p.stdout,
    #     mimetype="application/pdf",
    #     headers={
    #         'Content-Type': "application/pdf",
    #         'Content-disposition': f"attachment; name={fn}; filename={fn};",
    #     }
    # )

    # return send_file(
    #     BytesIO(p.stdout),
    #     mimetype='application/pdf',
    #     download_name=fn,
    #     attachment_filename=fn,
    #     as_attachment=True
    # )

    # return "<p>OK</p>"
