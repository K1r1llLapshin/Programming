import java.util.Objects;

public class Book {
    private String title;
    private String author;
    private int year;
    
    // Коструктор 
    public Book(String title, String author, int year) {
        this.title = title;
        this.author = author;
        this.year = year;
    }

    // Гетеры
    public String getTitle() {
        return title;
    }

    public String getAuthor() {
        return author;
    }

    public int getYear() {
        return year;
    }

    // Переопределили функцию toString()
    @Override
    public String toString() {
        return "Название книги: " + title + "\n"
             + "Автор книги: " + author + "\n"
             + "Год издания: " + year + "\n";
    }
    
    // Переопределили функцию equals
    @Override
    public boolean equals(Object o) {
        if (this == o) return true; // В случае если этот тот же объект
        if (o == null || getClass() != o.getClass()) return false;
        Book book = (Book) o;
        return year == book.year &&
                Objects.equals(title, book.title) &&
                Objects.equals(author, book.author);
    }


    // Переопределили функцию hashCode()
    @Override
    public int hashCode() {
        return Objects.hash(title, author, year);
    }
}
