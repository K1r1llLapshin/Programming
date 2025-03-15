import Armchairs.Armchair;
import Armchairs.DefaultArmchair;
import Armchairs.MassageChair;

public class CinemaHall {
    private Armchair[][] hall;
    private Session[] sessions;
    private int count_row;
    private int count_colum;

    // Конструктор 
    CinemaHall(int count_row, int count_colum){
        this.hall = new Armchair[count_row][count_colum];
        this.count_colum = count_colum;
        this.count_row = count_row;
        this.sessions = new Session[0];
        for (int i = 0; i < count_row; i++) {
            for (int j = 0; j < count_colum; j++) {
                int[] coordinates = {i, j};
                hall[i][j] = new DefaultArmchair(coordinates, "DefaultArmchair", false, 200);
            }
        }
    }

    // Конфигурации мест всего ряда
    public void setRowConfigurationArmchairs(int row, String type, int price, boolean booked){
        for (int i = 0; i < count_colum; i++){
            int[] coordinates = {row, i};
            switch (type) {
                case "DefaultArmchair":
                    hall[row][i] = new DefaultArmchair(coordinates, type, booked, price);
                    break;
                case "MassageChair": 
                    hall[row][i] = new MassageChair(coordinates, type, booked, price);
                default:
                    break;
            }
        }
    }

    // Конфигурация конкретного места 
    public void setConfigurationArmchairs(int[] position, String type, int price, boolean booked){    
        switch (type) {
            case "DefaultArmchair":
                hall[position[0]][position[1]]= new DefaultArmchair(position, type, booked, price);
                break;
            case "MassageChair": 
                hall[position[0]][position[1]]= new MassageChair(position, type, booked, price);
            default:
                break;
        }
    }

    // Обновленеи информации конкретного места
    public void UpdataConfiguarationArmchairs(int[] position, int price, boolean booked){
        hall[position[0]][position[1]].SetBooked(booked);
        hall[position[0]][position[1]].SetPrice(price);
    }

    // Задние сеанса для данного зала
    public void setSesion(Session session){
        int new_lenght = sessions.length + 1;
        Session[] time = new Session[new_lenght];
        for (int i = 0; i < new_lenght - 1; i++ )
            time[i] = sessions[i];
        time[new_lenght - 1] = session;
        sessions = time;
    }

   

    public void DrawCinemaHall(){
        for (int i = 0; i < count_row; i++){
            for (int j = 0; j < count_colum; j++){
                switch (hall[i][j].GetType()) {
                    case "DefaultArmchair":
                        System.out.print("DA ");
                        break;
                    case "MassageChair":
                        System.out.print("MC ");
                        break;
                    default:
                        break;
                }  
            }
            System.out.println();
        }
    }

}
