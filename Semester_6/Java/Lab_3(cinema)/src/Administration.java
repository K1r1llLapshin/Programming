import java.util.Scanner;

public class Administration {
    Scanner in = new Scanner(System.in);
    TicketSystem ticketSystem = new TicketSystem();

    public void Interface(){
        while (true){
            int count_cinema = ticketSystem.getCountCinema();
            
            System.out.println("Количество кинотеатров: " + Integer.toString(count_cinema));
            for (int i = 0; i < count_cinema; i++){
                System.out.println(Integer.toString(i) + ") " + ticketSystem.getCinema(i).getNameCinema());
            }

            System.out.println("\n1. Создать кинотеатр \n2. Перейти в кинотеатр \n3. Выйти из админ аккаунта");
            int var = in.nextInt();
            
            if (var == 1){
                System.out.print("Введите название кинотеатра: ");
                String name = in.next();

                if (ticketSystem.FindeNameCinema(name))
                    System.out.println("Кинотеатр с таким названием сущёствует! Попробуйте ещё раз.");
                else
                    ticketSystem.setCinema(name);
                }

            else if (var == 2){
                System.out.print("Введите название кинотеатра: ");
                String name = in.next();

                if (!ticketSystem.FindeNameCinema(name))
                    System.out.println("Кинотеатр с таким названием не сущёствует! Попробуйте ещё раз.");
                else{
                    Cinema cinema = ticketSystem.getCinema(name);
                    InterfaceCinema(cinema);
                }
            }

            else if (var == 3)
                break; 

            else
                System.out.println("Неизвестная команда. пропробуйте ещё раз.");
                  
        }
    }

    public void InterfaceCinema(Cinema cinema){
        while (true){ 
            int count_cinema_hall = cinema.getCountCinemaHall();

            System.out.println("Количество залов: " + Integer.toString(count_cinema_hall));
            for (int i = 0; i < count_cinema_hall; i++){
                System.out.println("Зал №" + Integer.toString(i+1) + ' ' + Integer.toString(cinema.getCinemaHall(i).getCountPlace()));
            }

            System.out.println("\n1. Создать зал \n2. Перейти в зал \n3. Назад");
            int var = in.nextInt();

            if (var == 1){
                System.out.print("Введите количество рядов: ");
                int row = in.nextInt();
                System.out.print("Введите число мест в ряду: ");
                int colum = in.nextInt();
                cinema.setCinemaHall(row, colum);
            }

            else if (var == 2){
                System.out.print("Введите номер зала: ");
                int num = in.nextInt();
                
                if (num - 1 >= count_cinema_hall  || num - 1 < 0)
                    System.out.println("Зал с таким номером не сущёствует! Попробуйте ещё раз.");
                else{
                    CinemaHall hall = cinema.getCinemaHall(num - 1);
                    InterfaceCinemaHall(hall);
                }
            }

            else if (var == 3)
                break;
            
            else
                System.out.println("Неизвестная команда. пропробуйте ещё раз.");
        }
    }

    public void InterfaceCinemaHall(CinemaHall hall){
        while (true) { 
            hall.DrawCinemaHall();
            System.out.println("1. Поменять конфигурацию ряда \n2. Поменять конфигурацию места \n3. Забронировать сеанс \n4. Назад");
            int var = in.nextInt();
            if (var == 1){
                
            }

            else if (var == 2){

            }

            else if (var == 3){

            }

            else if (var == 4)
                break;
            
            else
                System.out.println("Неизвестная команда. пропробуйте ещё раз.");

        }
    }

}
