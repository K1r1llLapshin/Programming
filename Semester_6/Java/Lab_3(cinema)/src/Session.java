import java.time.LocalDateTime;
import java.time.Duration;

public class Session {

    private String name;
    private LocalDateTime sessionStart; // Дата и время начала сеанса
    private Duration duration; // Длительность сеанса

    // Конструктор
    public Session(String name, LocalDateTime sessionStart, Duration duration) {
        this.name = name;
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

    public void setSessionStart(LocalDateTime sessionStart) {
        this.sessionStart = sessionStart;
    }

    public LocalDateTime getSessionStart() {
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
               this.sessionStart.equals(session.getSessionStart()) &&
               this.duration.equals(session.getDuration());
    }

    // Метод для вывода информации о сеансе
    public void Draw() {
        System.out.println("Название: " + name);
        System.out.println("Дата и время начала: " + sessionStart);
        System.out.println("Длительность: " + duration.toMinutes() + " минут");
    }

}