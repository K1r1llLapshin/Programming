package Figures;

public abstract class Figure {
    private String name;
    private char color;

    public Figure(char color, String name){
        this.color = color;
        this.name = name;
    }

    public void SetName(String name){
        this.name = name;
    }

    public String GetName(){
        return name;
    }

    public char GetColor(){
        return color;
    }

    public boolean canMove(int row, int col, int row1, int col1){
        return (row >= 0 && row < 8) && (row1 >= 0 && row < 8) 
            && (col >= 0 && col < 8) && (col1 >= 0 && col1 < 8)
            && (col != col1) && (row != row1);
    }

    public boolean canAttack(int row, int col, int row1, int col1){
        return this.canMove(row, col, row1, col1);
    }
}
