public class TicketSystem {
    private Cinema[] cinemas;
    TicketSystem(){
        this.cinemas = new Cinema[0];
    }

    public int FindeCinema (Cinema[]cinemas, String name_cinema){
        int i = 0; 
        while(!cinemas[i].getNameCinema().equals(name_cinema))
            i++;
        return i;
    }

    // Для админа
    public void setCinema(String name){
        Cinema new_Cinema = new Cinema(name);
        int new_lenght = cinemas.length + 1;
        Cinema[] time = new Cinema[new_lenght];

        for (int i = 0; i < new_lenght - 1; i++ )
            time[i] = cinemas[i];

        time[new_lenght - 1] = new_Cinema;
        cinemas = time;
    }

    
    public void setCinemaHall(String cinema_name, int count_row, int count_colum){
        int i = FindeCinema(cinemas, cinema_name);
        cinemas[i].setCinemaHall(count_row, count_colum);
    }

    public void setSesion(String cinema_name, int id_cinima_hall, String name, int start, int duration){
        Session session = new Session(name, start, duration);
        int i = FindeCinema(cinemas, cinema_name);
        cinemas[i].getCinemaHall(id_cinima_hall).setSesion(session);
    }

    public void setConfigurationArmchairs (String cinema_name, int id_cinima_hall, int[] position, boolean booked, int price, String type){
        int i = FindeCinema(cinemas, cinema_name);
        cinemas[i].getCinemaHall(id_cinima_hall).setConfigurationArmchairs(position, type, price, booked);
    }

    public void setRowConfigurationArmchairs (String cinema_name, int id_cinima_hall, int row, boolean booked, int price, String type){
        int i = FindeCinema(cinemas, cinema_name);
        cinemas[i].getCinemaHall(id_cinima_hall).setRowConfigurationArmchairs(row, type, price, booked);
    
    
    //Для юзера

}
