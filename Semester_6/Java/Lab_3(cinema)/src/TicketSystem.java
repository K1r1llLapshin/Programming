public class TicketSystem {
    
    private Cinema[] cinemas;
    private String[] names_cinemas;
    TicketSystem(){
        this.cinemas = new Cinema[0];
        this.names_cinemas = new String[0];
    }

    public int getCountCinema(){
        return cinemas.length;
    }
    
    // Создание кинотеатра
    public void setCinema(String name){
        Cinema new_Cinema = new Cinema(name);
        int new_lenght = cinemas.length + 1;
        Cinema[] time = new Cinema[new_lenght];
        String[] time_name = new String[new_lenght];

        for (int i = 0; i < new_lenght - 1; i++ ){
            time[i] = cinemas[i];
            time_name[i] = names_cinemas[i];
        }
        time[new_lenght - 1] = new_Cinema;
        time_name[new_lenght - 1] = name;
        cinemas = time;
        names_cinemas = time_name;
    }

    // Проверака существует кинотеатр с таким названием или нет
    public boolean FindeNameCinema(String name){
        boolean finde = false;
        for (int i = 0 ; i < names_cinemas.length; i++){
            if (names_cinemas[i].equals(name)){
                finde = true;
                break;
            }
        }
        return finde;
    } 

    // Получения кинотеара 
    public Cinema getCinema (String name_cinema){
        int i = 0; 
        while(!cinemas[i].getNameCinema().equals(name_cinema))
            i++;
        return cinemas[i];
    }

    // Получения зала в кинотеатре
    public CinemaHall getCinemaHall(int id_cinemaHall, Cinema cinema){
        return cinema.getCinemaHall(id_cinemaHall);
    }


}
