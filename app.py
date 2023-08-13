from flask import Flask, request, jsonify

app = Flask(__name__)

def perform_operation(operation, num1, num2):
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return "Cannot divide by zero"
        return num1 / num2
    elif operation == 'exponentiate':
        try:
            n = pow(num1,num2)
            return n
        except:
            return "Result out of range"
    else:
        return "Invalid operation, try: add|subtract|multiply|divide|exponentiate"

@app.route('/<operation>', methods=['GET'])
def addition(operation):
    print(operation)
    try:
        num1 = float(request.args.get('num1'))
        num2 = float(request.args.get('num2'))
    except:
        return {"error": "'num' parameter must be a number"}
    
    result = perform_operation(operation, num1, num2)

    response = {
        'input_numbers': [num1,num2],
        'operation': operation,
        'result': result
    }
    return jsonify(response)
