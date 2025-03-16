import java.time.LocalDateTime;
import java.time.LocalTime;

import Armchairs.Armchair;
import Armchairs.DefaultArmchair;
import Armchairs.MassageChair;

public class CinemaHall {
    private Armchair[][] hall;
    private Session[] sessions;
    private String[] typeArmchair = {"DefaultArmchair", "MassageChair"};
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

    // Геттеры
    public int getCountPlace(){
        return count_colum * count_row;
    }

    public Armchair[][] getHall(){
        return hall;
    }

    public int getCountRow(){
        return count_row;
    }

    public int getCountColum(){
        return count_colum;
    }

    public String[] getTypesArmchairs(){
        return typeArmchair;
    }
    
    public Session[] getSessions(){
        return sessions;
    }

    public boolean HallAll(){
        int count = 0;
        for(int i = 0; i < count_row; i++)
            for(int j = 0; j < count_colum; j++)
                if(hall[i][j].GetBooked())
                    count++;
        if(count == getCountPlace())
            return true;
        else
            return false;
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


    // Задние сеанса для данного зала
    public void setSession(Session session){
        int new_lenght = sessions.length + 1;
        Session[] time = new Session[new_lenght];
        for (int i = 0; i < new_lenght - 1; i++ )
            time[i] = sessions[i];
        time[new_lenght - 1] = session;
        sessions = time;
    }

    // Проверка на уникальность сеанса
    public boolean isSessionUnique(Session newSession) {
        for (Session session : sessions) {
            if (session.equalSession(newSession)) {
                return false; 
            }
        }
        return true; 
    }

    // Проверка на пересечение по времени
    public boolean isSessionOverlapping(Session newSession) {
    LocalDateTime newSessionStart = newSession.getSessionStart();
    LocalDateTime newSessionEnd = newSessionStart.plus(newSession.getDuration());

    for (Session session : sessions) {
        LocalDateTime existingSessionStart = session.getSessionStart();
        LocalDateTime existingSessionEnd = existingSessionStart.plus(session.getDuration());

        // Проверяем пересечение по времени
        if (newSessionStart.isBefore(existingSessionEnd) && newSessionEnd.isAfter(existingSessionStart)) {
            return true; // Сеансы пересекаются
        }
    }
    return false; // Пересечений нет
}
   
    // Изображение зала
    public void Draw(){
        
        for (int i = 0; i < count_row; i++){
            for (int j = 0; j < count_colum; j++){
                String booked = "X";
                if(!hall[i][j].GetBooked())
                    booked = " ";
                switch (hall[i][j].GetType()) {
                    case "DefaultArmchair":
                        System.out.print("[" + booked +"] ");
                        break;
                    case "MassageChair":
                        System.out.print("{" + booked +"} ");
                        break;
                    default:
                        break;
                }  
            }
            System.out.println();
        }
        System.out.println("[ ] - обычное место \t{ } - масажное кресло \t [X] / {X} - занятые места");
    }

}
