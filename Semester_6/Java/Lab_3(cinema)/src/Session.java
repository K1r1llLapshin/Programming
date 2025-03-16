import java.time.LocalTime;
import java.time.LocalDate;
import java.time.Duration;

public class Session {

    private String name;
    private LocalDate date; 
    private LocalTime sessionStart;
    private Duration duration; 

    // Конструктор
    public Session(String name, LocalDate date, LocalTime sessionStart, Duration duration) {
        this.name = name;
        this.date = date;
        this.sessionStart = sessionStart;
        this.duration = duration;
    }

    // Геттеры и сеттеры
    public void setName(String name) {
        this.name = name;
    }

    public String getName() {
        return name;
    }

    public void setDate(LocalDate date) {
        this.date = date;
    }

    public LocalDate getDate() {
        return date;
    }

    public void setSessionStart(LocalTime sessionStart) {
        this.sessionStart = sessionStart;
    }

    public LocalTime getSessionStart() {
        return sessionStart;
    }

    public void setDuration(Duration duration) {
        this.duration = duration;
    }

    public Duration getDuration() {
        return duration;
    }

    // Метод для сравнения двух сеансов
    public boolean equalSession(Session session) {
        return this.name.equals(session.getName()) &&
               this.date.equals(session.getDate()) &&
               this.sessionStart.equals(session.getSessionStart()) &&
               this.duration.equals(session.getDuration());
    }

    // Метод для вывода информации о сеансе
    public void Draw() {
        System.out.println("Название: " + name);
        System.out.println("Дата: " + date);
        System.out.println("Начало сеанса: " + sessionStart);
        System.out.println("Длительность: " + duration.toMinutes() + " минут");
    }
}