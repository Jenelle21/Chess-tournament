from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponseBadRequest
import chess
import chess.engine
import json

initial_position = chess.Board()
engine = chess.engine.SimpleEngine.popen_uci("/Users/jenellep/goinfre/.brew/Cellar/stockfish/15.1/bin/stockfish")


def chessboard(request):
    context = {
        'board': str(initial_position.fen().split()[0])
    }
    # engine.quit()
    return render(request, 'chess_engine/chessboard.html', context)


def make_move(request):
    if request.method == 'POST':
        # Get the source and destination squares from the request
        data = json.loads(request.body.decode('utf-8'))
        source_square = data['source']
        destination_square = data['target']

        # Validate the move
        if source_square != destination_square:
            move = chess.Move.from_uci(source_square + destination_square)
            result = ''
            data = {'position': initial_position.fen().split()[0], 'result': result}

            if initial_position.turn == chess.BLACK:
                ai_move = engine.play(initial_position, chess.engine.Limit(time=2.0))
                initial_position.push(ai_move.move)
                data = {'position': initial_position.fen().split()[0], 'result': result}
            else:
                if move in initial_position.legal_moves:
                    # Make the move and update the game position
                    initial_position.push(move)
                    info = engine.analyse(initial_position, chess.engine.Limit(time=2.0))
                    print("Score:", info["score"])
                    if initial_position.is_game_over():
                        if initial_position.is_checkmate():
                            winner = 'Black' if initial_position.turn == chess.WHITE else 'White'
                            result = f"{winner} wins by checkmate"
                        elif initial_position.is_stalemate():
                            result = "Game drawn by stalemate"
                        else:
                            result = "Game drawn by agreement or other reason"
                        engine.quit()
                    data = {'position': initial_position.fen().split()[0], 'result': result}
        return JsonResponse(data)
    return redirect('chessboard')
