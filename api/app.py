from flask import Flask, jsonify
import psycopg2
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)

def get_db_connection():
    try:
        # Update the connection details based on your primary DB server configuration
        connection = psycopg2.connect(
            host='primary-db',
            port='5432',
            dbname='mydatabase',
            user='postgres',
            password='mysecretpassword'
        )
        app.logger.info('Database connection successful')
        return connection
    except Exception as e:
        app.logger.error('Database connection error: %s', e)
        raise e

@app.route('/users', methods=['GET'])
def get_users():
    try:
        connection = get_db_connection()
        cursor = connection.cursor()

        # Fetch users from the primary DB server
        query = "SELECT * FROM users;"
        cursor.execute(query)
        users = cursor.fetchall()

        # Prepare the response
        user_list = []
        for user in users:
            user_dict = {
                'name': user[0],
                'street': user[1],
                'city': user[2],
                'state': user[3],
                'date': user[4].strftime('%Y-%m-%d')
            }
            user_list.append(user_dict)

        connection.close()

        return jsonify(user_list)

    except Exception as e:
        app.logger.error('Error: %s', e)
        return jsonify({'error': str(e)})

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'OK'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
