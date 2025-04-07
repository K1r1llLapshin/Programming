import java.util.List;

public class LibraryTest {

    public void Print(){
        Library library = new Library();
        
        // Создаем тестовые книги
        Book book1 = new Book("Война и мир", "Лев Толстой", 1869);
        Book book2 = new Book("Анна Каренина", "Лев Толстой", 1877);
        Book book3 = new Book("Преступление и наказание", "Федор Достоевский", 1866);
        Book book4 = new Book("1984", "Джордж Оруэлл", 1949);
        Book book5 = new Book("Скотный двор", "Джордж Оруэлл", 1945);
        
        // Тестируем добавление книг
        System.out.println("=== Тестируем добавление книг ===");
        library.addBook(book1);
        library.addBook(book2);
        library.addBook(book3);
        library.addBook(book4);
        library.addBook(book5);
        
        // Попытка добавить существующую книгу
        library.addBook(book1);
        
        System.out.println();
        
        // Тестируем вывод всех книг
        System.out.println("=== Все книги в библиотеке ===");
        library.printAllBooks();
        
        System.out.println();
        
        // Тестируем поиск по автору
        System.out.println("=== Тестируем поиск по автору (Лев Толстой) ===");
        List<Book> tolstoyBooks = library.findBooksByAuthor("Лев Толстой");
        for (Book book : tolstoyBooks) {
            System.out.println(book);
        }
        
        System.out.println();
        
        // Тестируем поиск по году
        System.out.println("=== Тестируем поиск по году (1949) ===");
        List<Book> books1949 = library.findBooksByYear(1949);
        for (Book book : books1949) {
            System.out.println(book);
        }
        
        System.out.println();
        
        // Тестируем вывод уникальных авторов
        library.printUniqueAuthors();
        
        System.out.println();
        
        // Тестируем статистику по авторам
        library.printAuthorStatistics();
        
        System.out.println();
        
        // Тестируем удаление книги
        System.out.println("=== Тестируем удаление книги ===");
        library.removeBook(book3);
        System.out.println("После удаления 'Преступление и наказание':\n");
        library.printAllBooks();
        
       
        // Проверяем статистику после удаления
        System.out.println("=== Статистика после удаления ===\n");
        library.printAuthorStatistics();
        System.out.println();
        
        // Попытка удалить несуществующую книгу
        System.out.println("=== Попытка удалить несуществующую книгу ===");
        Book nonExistentBook = new Book("Несуществующая книга", "Неизвестный автор", 2000);
        library.removeBook(nonExistentBook);
    }
    
}