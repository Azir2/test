from flask import Flask, render_template, request, jsonify
import pymysql

app = Flask(__name__)

# Database configuration
db_config = {
    'host': 'gz-cynosdbmysql-grp-2vvyiml3.sql.tencentcdb.com',
    'port': 22956,
    'user': 'root',
    'password': 'itsits123.',
    'db': 'coordinates_db',
    'charset': 'utf8mb4',
}

# Connect to the database
connection = pymysql.connect(**db_config)

@app.route('/')
def index():
    return render_template('coordinates.html')

@app.route('/upload_coordinates', methods=['POST'])
def upload_coordinates():
    data = request.get_json()
    coordinates = data.get('coordinates', [])

    if not coordinates:
        return jsonify({'error': '未提供坐标'}), 400

    try:
        with connection.cursor() as cursor:
            # Replace `coordinates_table` with your table name
            sql = "INSERT INTO coordinates_table (latitude, longitude) VALUES (%s, %s)"
            cursor.executemany(sql, coordinates)
            connection.commit()
    except Exception as e:
        return jsonify({'error': str(e)}), 500

    return jsonify({'success': '坐标上传成功'})

if __name__ == '__main__':
    app.run()
