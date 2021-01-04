from flask import *  
app = Flask(__name__)  

def ingest_file(filename, column):
    values = []
    with open(filename, "r") as file:
        header = file.readline()
        header_fields = header.split()
        number_of_columns = len(header_fields)
        if column not in header_fields:
            raise ValueError
        else:
            number_of_columns = len(header_fields)
            column_index = header_fields.index(column)

        for line in file:
            line_fields = line.split()
            if len(line_fields) == 6:
                values.append(line_fields[column_index])
            # else:
            #     print("invalid line: " + line)
    return values

def process_data(values):
    counts = {"0": 0, "1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0, "9": 0}
    for item in values:
        counts[str(item)[0]] += 1

    results = []
    for item in counts.values():
        percentage = int(round((item/len(values))*100))
        results.append(percentage)
    return results

@app.route('/')  
def upload():  
    return render_template("file_upload_form.html")  
 
@app.route('/success', methods = ['POST'])  
def success():
    if request.method == 'POST': 
        f = request.files['file']
        f.save(f.filename)
        column = request.form['column']

        results = ingest_file(f.filename, column)
        percentages = process_data(results)
        bar_labels=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        bar_values=percentages
        return render_template('bar_chart.html', 
                               title='Leading Digit Distribution', 
                               max=100, labels=bar_labels, values=bar_values)

if __name__ == '__main__':  
    app.run(debug=True,host='0.0.0.0')
