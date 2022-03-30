from flask import Flask, request, render_template, jsonify
app = Flask(__name__)
call_cnt = 0
ending = [0, 0, 0, 0, 0, 0, 0, 0]
#home page
@app.route('/', methods=['GET', 'POST'])
def home():
    global call_cnt
    call_cnt = 0
    global ending
    ending = [0, 0, 0, 0, 0, 0, 0, 0]
    return render_template('home.html')

#call video
@app.route('/01', methods=['GET'])
def video_01():
    return render_template('p_01.html')
@app.route('/02', methods=['GET'])
def video_02():
    global ending
    ending[0] = 1
    return render_template('p_02.html')
@app.route('/03', methods=['GET'])
def video_03():
    return render_template('p_03.html')
@app.route('/04', methods=['GET'])
def video_04():
    return render_template('p_04.html')
@app.route('/05', methods=['GET'])
def video_05():
    return render_template('p_05.html')
@app.route('/06', methods=['GET'])
def video_06():
    global ending
    ending[1] = 1
    return render_template('p_06.html')
@app.route('/07', methods=['GET'])
def video_07():
    global ending
    ending[2] = 1
    return render_template('p_07.html')
@app.route('/08', methods=['GET'])
def video_08():
    global ending
    ending[3] = 1
    return render_template('p_08.html')
@app.route('/09', methods=['GET'])
def video_09():
    return render_template('p_09.html')
@app.route('/10', methods=['GET'])#pay more attention to handle circle
def video_10():
    global call_cnt
    call_cnt += 1
    if call_cnt == 1:
        return render_template('p_10.html')
    elif call_cnt == 2:
        return render_template('p_11.html')
    else:
        call_cnt -= 1
        return render_template('p_12.html')
@app.route('/11', methods=['GET'])
def video_11():
    return render_template('p_11.html')
@app.route('/12', methods=['GET'])
def video_12():
    return render_template('p_12.html')
@app.route('/13', methods=['GET'])
def video_13():
    return render_template('p_13.html')
@app.route('/14', methods=['GET'])
def video_14():
    return render_template('p_14.html')
@app.route('/15', methods=['GET'])
def video_15():
    return render_template('p_15.html')
@app.route('/16', methods=['GET'])
def video_16():
    global ending
    ending[4] = 1
    return render_template('p_16.html')
@app.route('/17', methods=['GET'])
def video_17():
    return render_template('p_17.html')
@app.route('/18', methods=['GET'])
def video_18():
    global ending
    ending[6] = 1
    return render_template('p_18.html')
@app.route('/19', methods=['GET'])
def video_19():
    global ending
    ending[7] = 1
    return render_template('p_19.html')
@app.route('/20', methods=['GET'])
def video_20():
    global ending
    ending[5] = 1
    return render_template('p_20.html')
@app.route('/21', methods=['GET'])
def video_21():
    return render_template('p_21.html')
@app.route('/22', methods=['GET'])
def video_22():
    return render_template('p_22.html')
@app.route('/end', methods=['GET'])
def end():
    return render_template('end.html')
@app.route('/achievement_judge', methods=['GET'])
def achievement_judge():
    global ending
    return jsonify(
        {
            'ending0': ending[0],
            'engind1': ending[1],
            'ending2': ending[2],
            'ending3': ending[3],
            'ending4': ending[4],
            'ending5': ending[5],
            'ending6': ending[6],
            'ending7': ending[7],
        }
    )
if __name__ == '__main__':
    app.run()