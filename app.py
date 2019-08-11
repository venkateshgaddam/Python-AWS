from flask import Flask
from flask import render_template

app = Flask(__name__)

dynamoDbData=[
    {
        'service_request_id':1678,
        'request_type':'RDS-Oracle',
        'instanceName':'AZV-DBO2S-DPPL1'
    },
    {
        'service_request_id':1679,
        'request_type':'RDS-MySQL',
        'instanceName':'AZV-DBO2S-DCPS1'
    },
    {
        'service_request_id':1680,
        'request_type':'AURORA-MYSQL',
        'instanceName':'AZV-DBO2S-DCPS1'
    },
    {
        'service_request_id':1681,
        'request_type':'AURORA-POSTGRE',
        'instanceName':'AZV-DBO2S-DSCR1'
    }

]

@app.route('/helloworld')
def hello_world():
    return 'Hello World!'

@app.route('/')
@app.route('/home')
def Home():
    return render_template('Home.html',data=dynamoDbData,Title='Page Data')


@app.route('/about')
def test():
    return render_template('About.html',Title='About')


if __name__ == '__main__':
    app.run(debug=True)
