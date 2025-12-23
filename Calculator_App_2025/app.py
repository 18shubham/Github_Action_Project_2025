from flask import Flask, request, jsonify, render_template_string
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# HTML Frontend
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Calculator App</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 20px;
        }

        .calculator {
            background: white;
            border-radius: 20px;
            box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
            padding: 30px;
            max-width: 400px;
            width: 100%;
        }

        h1 {
            text-align: center;
            color: #667eea;
            margin-bottom: 30px;
            font-size: 28px;
        }

        .input-group {
            margin-bottom: 20px;
        }

        label {
            display: block;
            margin-bottom: 8px;
            color: #333;
            font-weight: 500;
        }

        input[type="number"] {
            width: 100%;
            padding: 12px;
            border: 2px solid #e0e0e0;
            border-radius: 8px;
            font-size: 16px;
            transition: border-color 0.3s;
        }

        input[type="number"]:focus {
            outline: none;
            border-color: #667eea;
        }

        .operations {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 10px;
            margin-bottom: 20px;
        }

        button {
            padding: 15px;
            border: none;
            border-radius: 8px;
            font-size: 18px;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s;
            color: white;
        }

        .btn-add { background: #4CAF50; }
        .btn-subtract { background: #FF9800; }
        .btn-multiply { background: #2196F3; }
        .btn-divide { background: #F44336; }

        button:hover {
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
        }

        button:active {
            transform: translateY(0);
        }

        .result {
            background: #f5f5f5;
            padding: 20px;
            border-radius: 8px;
            text-align: center;
            margin-top: 20px;
            min-height: 60px;
            display: flex;
            align-items: center;
            justify-content: center;
        }

        .result-text {
            font-size: 24px;
            font-weight: 600;
            color: #667eea;
        }

        .error {
            color: #F44336;
        }

        .loading {
            color: #999;
        }
    </style>
</head>
<body>
    <div class="calculator">
        <h1>🧮 Calculator</h1>
        
        <div class="input-group">
            <label for="num1">First Number</label>
            <input type="number" id="num1" placeholder="Enter first number" step="any">
        </div>

        <div class="input-group">
            <label for="num2">Second Number</label>
            <input type="number" id="num2" placeholder="Enter second number" step="any">
        </div>

        <div class="operations">
            <button class="btn-add" onclick="calculate('add')">➕ Add</button>
            <button class="btn-subtract" onclick="calculate('subtract')">➖ Subtract</button>
            <button class="btn-multiply" onclick="calculate('multiply')">✖️ Multiply</button>
            <button class="btn-divide" onclick="calculate('divide')">➗ Divide</button>
        </div>

        <div class="result" id="result">
            <span class="result-text">Result will appear here</span>
        </div>
    </div>

    <script>
        async function calculate(operation) {
            const num1 = parseFloat(document.getElementById('num1').value);
            const num2 = parseFloat(document.getElementById('num2').value);
            const resultDiv = document.getElementById('result');

            if (isNaN(num1) || isNaN(num2)) {
                resultDiv.innerHTML = '<span class="result-text error">Please enter valid numbers!</span>';
                return;
            }

            resultDiv.innerHTML = '<span class="result-text loading">Calculating...</span>';

            try {
                const response = await fetch('/calculate', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({
                        num1: num1,
                        num2: num2,
                        operation: operation
                    })
                });

                const data = await response.json();

                if (data.error) {
                    resultDiv.innerHTML = `<span class="result-text error">${data.error}</span>`;
                } else {
                    resultDiv.innerHTML = `<span class="result-text">Result: ${data.result}</span>`;
                }
            } catch (error) {
                resultDiv.innerHTML = '<span class="result-text error">Error connecting to server!</span>';
            }
        }

        // Allow Enter key to trigger calculation
        document.getElementById('num1').addEventListener('keypress', function(e) {
            if (e.key === 'Enter') calculate('add');
        });
        document.getElementById('num2').addEventListener('keypress', function(e) {
            if (e.key === 'Enter') calculate('add');
        });
    </script>
</body>
</html>
'''

# Calculator functions
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return None
    return x / y

# Routes
@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE)

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        data = request.get_json()
        num1 = float(data['num1'])
        num2 = float(data['num2'])
        operation = data['operation']

        operations = {
            'add': add,
            'subtract': subtract,
            'multiply': multiply,
            'divide': divide
        }

        if operation not in operations:
            return jsonify({'error': 'Invalid operation'}), 400

        result = operations[operation](num1, num2)

        if result is None:
            return jsonify({'error': 'Cannot divide by zero!'}), 400

        return jsonify({'result': result})

    except (KeyError, ValueError, TypeError):
        return jsonify({'error': 'Invalid input'}), 400

if __name__ == '__main__':
    print("Calculator app running on http://127.0.0.1:5000")
    app.run(host='0.0.0.0', port=5000)
