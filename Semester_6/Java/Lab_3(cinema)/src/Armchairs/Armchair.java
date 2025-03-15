package Armchairs;

public abstract class Armchair {
    private int[] position;
    private String type;
    private boolean booked;
    private int price;

    Armchair(int[] position, String type, boolean booked, int price){
        this.type = type;
        this.booked = booked;
        this.position = position;
        this.price = price;
    }

    public void SetPosition(int[] position){
        this.position = position;
    }

    public int[] GetPosition(){
        return position;
    }

    public void SetType(String type){
        this.type = type;
    }

    public String GetType(){
        return type;
    }

    public void SetBooked(boolean booked){
        this.booked = booked;
    }

    public boolean GetBooked(){
        return booked;
    }

    public void SetPrice(int price){
        this.price = price;
    }

    public int GetPrice(){
        return price;
    }
}
