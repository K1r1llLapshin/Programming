import java.time.LocalDate;
import java.time.LocalTime;
import java.time.Duration;
import java.util.Scanner;

public class Administration {
    private Scanner in = new Scanner(System.in);
    private TicketSystem ticketSystem = new TicketSystem();

    public void Interface() {
        while (true) {
            int countCinema = ticketSystem.getCountCinema();

            System.out.println("\nКоличество кинотеатров: " + countCinema);
            for (int i = 0; i < countCinema; i++) {
                System.out.println((i + 1) + ") " + ticketSystem.getCinemaInd(i).getNameCinema());
            }

            System.out.println("\n1. Создать кинотеатр \n2. Перейти в кинотеатр \n3. Выйти из админ аккаунта");
            int var = in.nextInt();

            switch (var) {
                case 1:
                    createCinema();
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

    private void createCinema() {
        System.out.print("Введите название кинотеатра: ");
        String name = in.next();

        if (ticketSystem.FindeNameCinema(name)) {
            System.out.println("Кинотеатр с таким названием существует! Попробуйте ещё раз.");
        } else {
            ticketSystem.setCinema(name);
            System.out.println("Кинотеатр успешно создан.");
        }
    }

    private void enterCinema() {
        int countCinema = ticketSystem.getCountCinema();
        if (countCinema == 0) {
            System.out.println("Кинотеатров не существует! Попробуйте ещё раз.");
            return;
        }

        System.out.print("Введите название кинотеатра: ");
        String name = in.next();

        if (!ticketSystem.FindeNameCinema(name)) {
            System.out.println("Кинотеатр с таким названием не существует! Попробуйте ещё раз.");
        } else {
            Cinema cinema = ticketSystem.getCinema(name);
            InterfaceCinema(cinema);
        }
    }

    private void InterfaceCinema(Cinema cinema) {
        while (true) {
            int countCinemaHall = cinema.getCountCinemaHall();

            System.out.println("\nКоличество залов: " + countCinemaHall);
            for (int i = 0; i < countCinemaHall; i++) {
                System.out.println("Зал №" + (i + 1) + ' ' + cinema.getCinemaHall(i).getCountPlace() + " мест");
            }

            System.out.println("\n1. Создать зал \n2. Перейти в зал \n3. Назад");
            int var = in.nextInt();

            switch (var) {
                case 1:
                    createCinemaHall(cinema);
                    break;
                case 2:
                    enterCinemaHall(cinema);
                    break;
                case 3:
                    return; 
                default:
                    System.out.println("Неизвестная команда. Попробуйте ещё раз.");
            }
        }
    }

    private void createCinemaHall(Cinema cinema) {
        System.out.print("Введите количество рядов: ");
        int row = in.nextInt();
        System.out.print("Введите число мест в ряду: ");
        int colum = in.nextInt();
        cinema.setCinemaHall(row, colum);
        System.out.println("Зал успешно создан.");
    }

    private void enterCinemaHall(Cinema cinema) {
        int countCinemaHall = cinema.getCountCinemaHall();
        if (countCinemaHall == 0) {
            System.out.println("Залов не существует! Попробуйте ещё раз.");
            return;
        }

        System.out.print("Введите номер зала: ");
        int num = in.nextInt();

        if (num < 1 || num > countCinemaHall) {
            System.out.println("Зал с таким номером не существует! Попробуйте ещё раз.");
        } else {
            CinemaHall hall = cinema.getCinemaHall(num - 1);
            InterfaceCinemaHall(hall);
        }
    }

    private void InterfaceCinemaHall(CinemaHall hall) {
        while (true) {
            System.out.println();
            hall.Draw();
            System.out.println("\n1. Поменять конфигурацию ряда \n2. Поменять конфигурацию места \n3. Забронировать сеанс \n4. Назад");
            int var = in.nextInt();

            switch (var) {
                case 1:
                    configureRow(hall);
                    break;
                case 2:
                    configureSeat(hall);
                    break;
                case 3:
                    InterfaceSession(hall);
                    break;
                case 4:
                    return;
                default:
                    System.out.println("Неизвестная команда. Попробуйте ещё раз.");
            }
        }
    }

    private void configureRow(CinemaHall hall) {
        System.out.print("Введите номер ряда: ");
        int numRow = in.nextInt();
        if (numRow < 1 || numRow > hall.getCountRow()) {
            System.out.println("Ряда с таким номером нет. Попробуйте ещё раз.");
            return;
        }

        String type = selectType(hall);
        if (type == null) return;

        int price = inputPrice();
        boolean booked = inputBookedStatus();

        hall.setRowConfigurationArmchairs(numRow - 1, type, price, booked);
    }

    private void configureSeat(CinemaHall hall) {
        System.out.print("Введите номер ряда: ");
        int numRow = in.nextInt();
        System.out.print("Введите номер места: ");
        int numCol = in.nextInt();

        if (numRow < 1 || numRow > hall.getCountRow() || numCol < 1 || numCol > hall.getCountColum()) {
            System.out.println("Ряда или места с таким номером нет. Попробуйте ещё раз.");
            return;
        }

        String type = selectType(hall);
        if (type == null) return;

        int price = inputPrice();
        boolean booked = inputBookedStatus();

        int[] coor = {numRow - 1, numCol - 1};
        hall.setConfigurationArmchairs(coor, type, price, booked);
        System.out.println("Конфигурация места успешно изменена.");
    }

    private String selectType(CinemaHall hall) {
        while (true) {
            System.out.println("Введите тип места: ");
            String[] typeArmchair = hall.getTypesArmchairs();
            for (int i = 0; i < typeArmchair.length; i++) {
                System.out.println((i + 1) + ". " + typeArmchair[i]);
            }
            int numType = in.nextInt();
            if (numType < 1 || numType > typeArmchair.length) {
                System.out.println("Неизвестная команда. Попробуйте ещё раз.");
            } else {
                return typeArmchair[numType - 1];
            }
        }
    }

    private int inputPrice() {
        System.out.print("Введите стоимость места: ");
        return in.nextInt();
    }

    private boolean inputBookedStatus() {
        while (true) {
            System.out.println("Введите свободно место (0 - да, 1 - нет): ");
            int num = in.nextInt();
            if (num == 0 || num == 1) {
                return num == 0;
            }
            System.out.println("Неверная команда. Попробуйте ещё раз.");
        }
    }

    private void InterfaceSession(CinemaHall cinemaHall) {
        while (true) {
            System.out.println("\n1. Создать новый сеанс \n2. Просмотреть существующие сеансы \n3. Назад");
            int num = in.nextInt();

            switch (num) {
                case 1:
                    createSession(cinemaHall);
                    break;
                case 2:
                    viewSessions(cinemaHall);
                    break;
                case 3:
                    return;
                default:
                    System.out.println("Неизвестная команда. Попробуйте ещё раз.");
            }
        }
    }

    private void createSession(CinemaHall cinemaHall) {
        while (true) {
            try {
                System.out.print("Введите название сеанса: ");
                String name = in.next();
    
                LocalDate date = null;
                while (date == null) {
                    System.out.print("Введите дату сеанса (гггг-мм-дд): ");
                    String dateInput = in.next();
                    try {
                        date = LocalDate.parse(dateInput);
                    } 
                    catch (Exception e) {
                        System.out.println("Ошибка: некорректный формат даты. Используйте формат гггг-мм-дд.");
                    }
                }
    
                LocalTime sessionStart = null;
                while (sessionStart == null) {
                    System.out.print("Введите время начала сеанса (чч:мм): ");
                    String timeInput = in.next();
                    try {
                        sessionStart = LocalTime.parse(timeInput);
                    } 
                    catch (Exception e) {
                        System.out.println("Ошибка: некорректный формат времени. Используйте формат чч:мм.");
                    }
                }

                int durationMinutes = 0;
                while (durationMinutes <= 0) {
                    System.out.print("Введите длительность сеанса в минутах: ");
                    try {
                        durationMinutes = in.nextInt();
                        if (durationMinutes <= 0)
                            System.out.println("Ошибка: длительность должна быть положительным числом.");
                        
                    } 
                    catch (Exception e) {
                        System.out.println("Ошибка: введите целое число.");
                        in.next();
                    }
                }
                Duration duration = Duration.ofMinutes(durationMinutes);
    
            
                Session newSession = new Session(name, date, sessionStart, duration);
    
                if (!cinemaHall.isSessionUnique(newSession)) {
                    System.out.println("Ошибка: сеанс с таким названием, датой и временем уже существует.");
                } else if (cinemaHall.isSessionOverlapping(newSession)) {
                    System.out.println("Ошибка: сеанс пересекается по времени с другим сеансом.");
                } else {
                    cinemaHall.setSession(newSession);
                    System.out.println("Сеанс успешно создан!");
                    break; 
                }
            } 
            catch (Exception e) {
                System.out.println("Произошла ошибка: " + e.getMessage());
            }
        }
    }

    private void viewSessions(CinemaHall cinemaHall) {
        Session[] sessions = cinemaHall.getSessions();
        if (sessions.length == 0) {
            System.out.println("Сеансов нет.");
        } else {
            int i = 1;
            for (Session session : sessions) {
                System.out.println(Integer.toString(i) + ") ");
                session.Draw();
                i++;
            }
        }
    }
}
