
import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;


public class Library {
    private List<Book> books;
    private Set<String> authors;
    private Map<String, Integer> booksCountByAuthor;

    // Коструктор
    public Library() {
        this.books = new ArrayList<>();
        this.authors = new HashSet<>();
        this.booksCountByAuthor = new HashMap<>();
    }

    public void addBook(Book book) {
        if (!books.contains(book)) {
            books.add(book); // добовляем книгу
            String author = book.getAuthor();
            authors.add(author); // добовляем автора
            booksCountByAuthor.put(author, booksCountByAuthor.getOrDefault(author, 0) + 1); // увеличиваем счётчик книг автора
            System.out.println("Книга успешно добавлена");
        }
        else
            System.out.println("Книга уже есть");
    }

    public void removeBook(Book book){
        if (!books.contains(book))
            System.out.println("Такой книги нет");
        else{
            String author = book.getAuthor();
            books.remove(book); // удаляем книгу
            int count = booksCountByAuthor.getOrDefault(author, 0) - 1; // уменьшаем счётчик книг автора
            if (count <= 0) {
                booksCountByAuthor.remove(author); // удаляем счетчик книг автора
                authors.remove(author); // удаляем автора
            } 
            else 
                booksCountByAuthor.put(author, count); // изменяем количество книг у автора
        }
    }

    public List<Book> findBooksByAuthor(String author){
        List<Book> result = new ArrayList<>();
        
        for(Book book: books)
            if(book.getAuthor().equals(author))
                result.add(book);
        
        return result;
    }

    public List<Book> findBooksByYear(int year){
        List<Book> result = new ArrayList<>();
        
        for(Book book: books)
            if(book.getYear() == year)
                result.add(book);
        
        return result;
    }

    public void printAllBooks(){
        for(Book book: books)
            System.out.println(book.toString());
    }

    public void printUniqueAuthors() {
        if (authors.isEmpty()) {
            System.out.println("В библиотеке нет авторов");
            return;
        }

        System.out.println("=== Уникальные авторы ===");
        for (String author : authors) {
            System.out.println(author);
        }
    }

     public void printAuthorStatistics() {
        if (authors.isEmpty()) {
            System.out.println("В библиотеке нет авторов");
            return;
        }

        System.out.println("=== Статистика по авторам ===");
        for (String author : authors) {
            int count = booksCountByAuthor.getOrDefault(author, 0);
            System.out.println(author +":" + count);
        }
    }
}

