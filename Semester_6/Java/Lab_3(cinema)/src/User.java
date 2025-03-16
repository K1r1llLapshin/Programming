import java.util.Scanner;

import Armchairs.Armchair;

import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

public class User {

    private Scanner in = new Scanner(System.in);
    private TicketSystem ticketSystem;

    User(TicketSystem ticketSystem)
    {
        this.ticketSystem = ticketSystem;
    }

    public void Interface() {
        while (true) {
            System.out.println("\n1. Найти ближайший сеанс \n2. Перейти в кинотеатр \n3. Выход");
            int num = in.nextInt();
            in.nextLine(); 

            switch (num) {
                case 1:
                    findSession();
                    break;
                case 2:
                    enterCinema();
                    break;
                case 3:
                    return;
                default:
                    System.out.println("Неизвестная команда. Попробуйте ещё раз.");
            }
        }
    }

    private void findSession() {
        Session[] films = ticketSystem.getFilms();
        Cinema[] cinemas = ticketSystem.getAllCinemas();

        if (films.length == 0) {
            System.out.println("Сеансов нет.");
            return;
        }

       
        System.out.println("Доступные фильмы:");
        for (Session session : films) {
            System.out.println("- " + session.getName());
        }

        
        System.out.print("Введите название фильма: ");
        String film = in.nextLine();

        if (!ticketSystem.FindeFilm(film)) {
            System.out.println("Кино с таким названием нет! Попробуйте ещё раз.");
        } else {
            Session nearestSession = null;
            String cinemaName = "";
            int hallNumber = 0;
            LocalDateTime now = LocalDateTime.now();

            for (Cinema cinema : cinemas) {
                for (CinemaHall cinemaHall : cinema.getAllCinemaHalls()) {
                    if (!cinemaHall.HallAll()) {
                        for (Session session : cinemaHall.getSessions()) {
                            if (session.getName().equals(film) && session.getSessionStart().isAfter(now)) {
                                if (nearestSession == null || session.getSessionStart().isBefore(nearestSession.getSessionStart())) {
                                    nearestSession = session;
                                    cinemaName = cinema.getNameCinema();
                                }
                            }
                        }
                    }
                    hallNumber++;
                }
            }

            if (nearestSession != null) {
                System.out.println("\nБлижайший сеанс:");
                System.out.println("Фильм: " + nearestSession.getName());
                System.out.println("Кинотеатр: " + cinemaName);
                System.out.println("Зал: " + hallNumber);
                System.out.println("Время начала: " + nearestSession.getSessionStart().format(DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm")));
                System.out.println("Длительность: " + nearestSession.getDuration().toMinutes() + " минут");
            } else {
                System.out.println("Сеансов на этот фильм не найдено.");
            }
        }
    }

    private void enterCinema() {
        int countCinema = ticketSystem.getCountCinema();
        if (countCinema == 0) {
            System.out.println("Кинотеатров не существует! Попробуйте ещё раз.");
            return;
        }

        System.out.println("Доступные кинотеатры:");
        for (Cinema cinema : ticketSystem.getAllCinemas()) {
            System.out.println("- " + cinema.getNameCinema());
        }

        System.out.print("Введите название кинотеатра: ");
        String name = in.nextLine();

        if (!ticketSystem.FindeNameCinema(name)) {
            System.out.println("Кинотеатр с таким названием не существует! Попробуйте ещё раз.");
        } else {
            Cinema cinema = ticketSystem.getCinema(name);
            InterfaceCinema(cinema);
        }
    }

    private void InterfaceCinema(Cinema cinema) {
        while (true) {
            System.out.println("\n1. Выбрать зал \n2. Назад");
            int num = in.nextInt();
            in.nextLine(); 

            switch (num) {
                case 1:
                    int countCinemaHall = cinema.getCountCinemaHall();
                    for (int i = 0; i < countCinemaHall; i++) {
                        System.out.println("Зал №" + (i + 1) + " " + cinema.getCinemaHall(i).getCountPlace() + " мест");
                    }
                    System.out.print("Выберите зал: ");
                    int hallNumber = in.nextInt();
                    in.nextLine(); 

                    if (hallNumber < 1 || hallNumber > countCinemaHall) {
                        System.out.println("Зал с таким номером не существует! Попробуйте ещё раз.");
                    } else {
                        CinemaHall hall = cinema.getCinemaHall(hallNumber - 1);
                        InterfaceCinemaHall(hall);
                    }
                    break;
                case 2:
                    return;
                default:
                    System.out.println("Неизвестная команда. Попробуйте ещё раз.");
            }
        }
    }

    private void InterfaceCinemaHall(CinemaHall cinemaHall) {
        while (true) {
            cinemaHall.Draw();
            System.out.println("\n1. Выбрать место \n2. Назад");
            int num = in.nextInt();
            in.nextLine(); 

            switch (num) {
                case 1:
                    InterfaceArmchair(cinemaHall);
                    break;
                case 2:
                    return;
                default:
                    System.out.println("Неизвестная команда. Попробуйте ещё раз.");
            }
        }
    }

    private void InterfaceArmchair(CinemaHall cinemaHall) {
        System.out.print("Введите номер ряда: ");
        int numRow = in.nextInt();
        System.out.print("Введите номер места: ");
        int numCol = in.nextInt();
        in.nextLine(); 

        if (numRow < 1 || numRow > cinemaHall.getCountRow() || numCol < 1 || numCol > cinemaHall.getCountColum()) {
            System.out.println("Ряда или места с таким номером нет. Попробуйте ещё раз.");
            return;
        }

        Armchair[][] hall = cinemaHall.getHall();
        if (hall[numRow - 1][numCol - 1].GetBooked()) {
            System.out.println("Место занято. Попробуйте ещё раз.");
        } else {
            hall[numRow - 1][numCol - 1].Draw();
            while (true) {
                System.out.print("\n1. Приобрести \n2. Назад\nВыберите действие: ");
                int num = in.nextInt();
                in.nextLine(); 

                switch (num) {
                    case 1:
                        hall[numRow - 1][numCol - 1].SetBooked(true);
                        System.out.println("Место успешно приобретено!");
                        return;
                    case 2:
                        return;
                    default:
                        System.out.println("Неизвестная команда. Попробуйте ещё раз.");
                }
            }
        }
    }
}
