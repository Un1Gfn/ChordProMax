#!/dev/null

from flask import Flask, request, make_response, send_file, Response
from subprocess import run
from time import time
from io import BytesIO

app = Flask(__name__)

@app.route('/', methods = ['POST',])
def hello_world():
    # data = request.form
    data = request.get_data()
    assert type(data) == bytes
    print(data.decode())
    p = run([
        "/opt/homebrew/opt/perl/bin/chordpro",
        "--diagrams=none",
        "-o", "/dev/stdout",
        "-",
    ], input=data, capture_output=True)
    assert p.returncode == 0
    assert p.stderr == b''
    assert type(p.stdout) == bytes
    # print(p)
    # print(p.stdout)

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
