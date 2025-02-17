import Figures.Bishop;
import Figures.Figure;
import Figures.King;
import Figures.Knight;
import Figures.Pawn;
import Figures.Queen;
import Figures.Rook;

public class Board{
    private Figure fields[][] = new Figure[8][8];

    public void init(){
        this.fields[1] = new Figure[]{
            new Pawn('w', "P"), new Pawn('w', "P"), new Pawn('w', "P"), new Pawn('w', "P"), 
            new Pawn('w', "P"), new Pawn('w', "P"), new Pawn('w', "P"), new Pawn('w', "P")};
        this.fields[6] = new Figure[]{
            new Pawn('b', "P"), new Pawn('b', "P"), new Pawn('b', "P"), new Pawn('b', "P"), 
            new Pawn('b', "P"), new Pawn('b', "P"), new Pawn('b', "P"), new Pawn('b', "P")};
        this.fields[0] = new Figure[]{new Rook('w', "R"), new Knight('w', "N"), new Bishop('w', "B"), new Queen('w', "Q"), 
            new King('w', "K") ,new Bishop('w', "B"), new Knight('w', "N") ,new Rook('w', "R")};
        this.fields[7] = new Figure[]{new Rook('b', "R"), new Knight('b', "N"), new Bishop('b', "B"), new Queen('b', "Q"), 
            new King('b', "K") ,new Bishop('b', "B"), new Knight('b', "N") ,new Rook('b', "R")};

    }  
    public String GetCell(int row, int col){
        Figure figure = this.fields[row][col];
        if(figure != null)
            return " " + figure.GetColor() + figure.GetName() + " ";
        return "    ";
    }

    public void printBoard() {
        System.out.println(" +----+----+----+----+----+----+----+----+");
        for (int i = 7; i > -1; i--) {
            System.out.print(i);    
            for (int j = 0; j < 8; j++) {
                System.out.print("|" + GetCell(i, j));
            }
            System.out.println("|");
            System.out.println(" +----+----+----+----+----+----+----+----+");
        }
        for (int j = 0; j < 8; j++) {
            System.out.print("    " + j);  
        }
        System.out.println();  
    }
}      


