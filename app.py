from flask import Flask, render_template, jsonify, request
import sudoku_logic

app = Flask(__name__)

# Keep a simple in-memory store for current puzzle and solution
CURRENT = {
    'puzzle': None,
    'solution': None
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/new')
def new_game():
    difficulty = request.args.get('difficulty', 'medium').lower()
    
    # Map difficulty to number of clues
    difficulty_map = {
        'easy': 50,
        'medium': 35,
        'hard': 25
    }
    
    # Fall back to explicit clues parameter if provided
    if 'clues' in request.args:
        try:
            clues = int(request.args.get('clues'))
        except ValueError:
            clues = difficulty_map.get(difficulty, 35)
    else:
        clues = difficulty_map.get(difficulty, 35)
    
    puzzle, solution = sudoku_logic.generate_puzzle(clues)
    CURRENT['puzzle'] = puzzle
    CURRENT['solution'] = solution
    return jsonify({'puzzle': puzzle, 'solution': solution})

@app.route('/check', methods=['POST'])
def check_solution():
    if not request.is_json:
        return jsonify({'error': 'Request must be JSON'}), 400
        
    data = request.json
    board = data.get('board')
    solution = CURRENT.get('solution')
    
    if solution is None or board is None:
        return jsonify({'error': 'No game in progress or board data missing'}), 400
        
    incorrect = []
    try:
        size = getattr(sudoku_logic, 'SIZE', 9)
        for i in range(size):
            for j in range(size):
                if board[i][j] != 0 and board[i][j] != solution[i][j]:
                    incorrect.append([i, j])
    except (IndexError, TypeError):
        return jsonify({'error': 'Invalid board format'}), 400
        
    return jsonify({'incorrect': incorrect})

@app.route('/hint', methods=['GET'])
def get_hint():
    """Optional endpoint to provide a hint coordinate if managed server-side."""
    solution = CURRENT.get('solution')
    puzzle = CURRENT.get('puzzle')
    
    if solution is None or puzzle is None:
        return jsonify({'error': 'No active game'}), 400
        
    # Find an un-filled or incorrect cell from the solution
    return jsonify({'solution': solution})

if __name__ == '__main__':
    app.run(debug=True)