public class TicketSystem {
    
    private Cinema[] cinemas;
    private String[] names_cinemas;
    private Session[] films;

    TicketSystem(){
        this.cinemas = new Cinema[0];
        this.names_cinemas = new String[0];
        this.films = new Session[0];
    }

    public int getCountCinema(){
        return cinemas.length;
    }

    public Cinema[] getAllCinemas(){
        return cinemas;
    }

    public Session[] getFilms(){
        return films;
    }
    
    public void setFilms(Session session){
        int new_leght_films = films.length + 1;
        Session[] time = new Session[new_leght_films];
        for (int i = 0; i < new_leght_films - 1; i++){
            time[i] = films[i];
        }
        time[films.length] = session;
        films = time;
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

    // Проверака существует фильм с таким названием или нет
    public boolean FindeFilm(String name){
        boolean finde = false;
        for (int i = 0 ; i < films.length; i++){
            if (films[i].getName().equals(name)){
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

    // Получения кинотеатра по индексу
    public Cinema getCinemaInd(int id_cinema){
        return cinemas[id_cinema];
    }

    
}
