package Figures;

public class Bishop extends Figure {

    public Bishop(char color, String name){
      super(color, name);
    }
  
    @Override
    public boolean canMove(int row, int col, int row1, int col1){
       return super.canMove(row, col, row1, col1);
      }
  
    @Override
    public boolean canAttack(int row, int col, int row1, int col1){
       return super.canAttack(row, col, row1, col1);
    }
}
