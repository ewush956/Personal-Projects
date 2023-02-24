#include <iostream>
using namespace std;

void build_board(char board[][3]);
void select_move(char board[][3], char& turn);
void print_board(char board[][3]);
bool check_winner(char board[][3]);
void print_win_screen(char turn);
int main(){

    char turn = 'X';
    // true for X false for O
    bool game_over = false;
    char board[3][3];

    build_board(board);
    while (!game_over) {
	select_move(board, turn);
	print_board(board);
	
	if (check_winner(board)) game_over = true;

    }
    print_win_screen(turn);
    return 0;
}

void build_board(char board[][3]){
    for (int column = 0; column < 3; column++){
	for (int row = 0; row < 3; row++){
	    board[row][column] = '-';
	}
    }
    return;
}
void select_move(char board[][3], char& turn){
    int row;
    int column;
    
    cout << "enter row: ";
    cin >> row;
    cout << endl << "enter column: ";
    cin >> column;
    cout << endl << endl;
/*
    if (row < 1) {
	cout << "Too low!!" << endl;
	select_move(board, turn);
    }
    if (row > 3) {
	cout << "Too High!!" << endl;
	select_move(board, turn);
*/
    
    if (turn == 'X') {
	board[row - 1][column - 1] = 'X';
	turn = 'O';
    }
    else {
	board[row - 1][column - 1] = 'O';
	turn = 'X';
    }
    cout << "turn: " << turn << endl;
    return;   
}
void print_board(char board[][3]){

    for (int row = 0; row < 3; row++){
	for (int column = 0; column < 3; column++){
	    cout << "|";
	    cout << board[row][column];
	}
	cout << endl;
    }
    
    return;
}
bool check_winner(char board[][3]){
    //Check columns
    bool winner = false;
    for (int column = 0; column < 3; column++){
	char pos0,
	    pos1,
	    pos2;
	pos0 = board[0][column];
	pos1 = board[1][column];
	pos2 = board[2][column];

	if ((pos0 == pos1) && (pos0 == pos2)){
	    if (pos0 != '-' || pos1 != '-' || pos2 != '-'){
		winner = true;
		cout << "column";
	    }
	}
	
    }
    //Check row
    for (int row = 0; row < 3; row++){
	char pos0,
	    pos1,
	    pos2;
	pos0 = board[row][0];
	pos1 = board[row][1];
	pos2 = board[row][2];

	if ((pos0 == pos1) && (pos0 == pos2)){
	    if (pos0 != '-' || pos1 != '-' || pos2 != '-'){
		winner = true;
		cout << "row";
	    }
	}
	
    }
    if ( board[0][0] == board [1][1] &&
	 board[0][0] == board [2][2] &&
	 board[0][0] != '-') winner = true;

    if ( board[0][2] == board [1][1] &&
	 board[2][0] == board [1][1] &&
	 board[1][1] != '-') winner = true;

    return winner;
}
void print_win_screen(char turn){

    if (turn == 'X') turn = 'O';
    else turn = 'X';
    
    cout << endl << endl
	 << "Winner is: " << turn;
    return;
}
