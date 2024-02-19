from flask import Flask

FAI = Flask(__name__)

@FAI.route('/web1')

def web1():
    return 'First Flask project'

if __name__ == '__main__':
    FAI.run(debug=True)

