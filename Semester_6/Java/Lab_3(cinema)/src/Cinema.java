public class Cinema {
    private CinemaHall[] cinema;
    private String name;
    
    // Конструктор
    Cinema(String name){
        this.name = name;
        cinema = new CinemaHall[0];
    }

    // Геттеры и сетер
    public int getCountCinemaHall(){
        return cinema.length;
    }

    public String getNameCinema(){
        return name;
    }

    public CinemaHall getCinemaHall(int id){
        return cinema[id];
    }

    public void setCinemaHall(int count_row, int count_colum){
        CinemaHall hall = new CinemaHall(count_row, count_colum);
        int new_leght_cinema = cinema.length + 1;
        CinemaHall[] time = new CinemaHall[new_leght_cinema];
        for (int i = 0; i < new_leght_cinema - 1; i++){
            time[i] = cinema[i];
        }
        time[cinema.length] = hall;
        cinema = time;
    }

  
}
