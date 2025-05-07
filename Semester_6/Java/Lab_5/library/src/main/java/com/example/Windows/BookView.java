package com.example.Windows;

import java.sql.SQLException;
import java.time.LocalDate;
import java.util.List;
import java.util.Map;

import com.example.DBmanager.BookManager;
import com.example.DBmanager.UsersBooksManager;
import com.example.Models.Book;

import javafx.geometry.Insets;
import javafx.geometry.Pos;
import javafx.scene.control.Alert;
import javafx.scene.control.Button;
import javafx.scene.control.ComboBox;
import javafx.scene.control.DatePicker;
import javafx.scene.control.Label;
import javafx.scene.control.TextArea;
import javafx.scene.control.TextField;
import javafx.scene.layout.HBox;
import javafx.scene.layout.VBox;
import javafx.stage.Stage;

public class BookView extends VBox{

    private final TextField titleField = new TextField();
    private final TextField authorField = new TextField();
    private final TextField pagesField = new TextField();
    private final ComboBox<String> genreBox = new ComboBox<>();
    private final ComboBox<String> statusBox = new ComboBox<>();
    private final DatePicker startDatePicker = new DatePicker();
    private final DatePicker endDatePicker = new DatePicker();
    private final TextArea descriptionArea = new TextArea();
    private final String whatFunction;
    private  int bookId; 

    BookView(String userId, String whatFunction) {
        super(10);
        setPadding(new Insets(25));
        this.whatFunction = whatFunction;
        // Поля ввода
        titleField.setPromptText("Введите название книги");
        
        pagesField.setPromptText("Введите количество страниц");

        authorField.setPromptText("Введите автора");

        genreBox.getItems().addAll("Фантастика", "Роман", "Детектив", "Научная", "Биография", "Фентези", "Поэзия", "Драма", "Графический роман", "Комедия");
        genreBox.setPromptText("Выберите жанр");


        statusBox.getItems().addAll("Читаю", "Прочитано", "Отложено");
        statusBox.setPromptText("Выберите статус");

        startDatePicker.setPromptText("Дата начала");

        endDatePicker.setPromptText("Дата окончания");

        descriptionArea.setPromptText("Введите описание");
        descriptionArea.setPrefRowCount(3);
        descriptionArea.setWrapText(true);

        // Контейнер для кнопок
        HBox buttonBox = new HBox(10);
        buttonBox.setAlignment(Pos.CENTER);
 
        // Кнопка "Сохранить"
        Button saveButton = new Button("Сохранить");
        saveButton.setOnAction(e-> handleAdd(userId));

        // Кнопка "Назад"
        Button backButton = new Button("Назад");
        backButton.setOnAction(e ->{Stage stage = (Stage) backButton.getScene().getWindow(); stage.close();});

        buttonBox.getChildren().addAll(saveButton, backButton);

        // Основной layout
        this.getChildren().addAll(
            new Label("Название:"), titleField,
            new Label("Автор:"), authorField,
            new Label("Количество страниц:"), pagesField,
            new Label("Жанр:"), genreBox,
            new Label("Статус:"), statusBox,
            new Label("Дата начала:"), startDatePicker,
            new Label("Дата окончания:"), endDatePicker,
            new Label("Описание:"), descriptionArea,
            buttonBox
        );

    }

    BookView(String userId, Map<String, Object> information){
        this(userId, "UpdateBook");
        bookId = (int) information.get("bookId");
        titleField.setText((String)information.get("title"));
        authorField.setText((String)information.get("author"));
        pagesField.setText(String.valueOf(information.get("pages")));

        genreBox.setValue((String)information.get("genre"));
        statusBox.setValue((String)information.get("status"));

        if (information.get("dateStart") != null && !information.get("dateStart").toString().isEmpty()) 
            startDatePicker.setValue(LocalDate.parse((String) information.get("dateStart")));
        else
            startDatePicker.setValue(null);

        if (information.get("dateEnd") != null && !information.get("dateEnd").toString().isEmpty())
            endDatePicker.setValue(LocalDate.parse((String) information.get("dateEnd")));
        else
            endDatePicker.setValue(null);
        
        descriptionArea.setText((String)information.get("description"));
 
    }
    
    private void showError(String message) {
        Alert alert = new Alert(Alert.AlertType.WARNING);
        if (whatFunction.equals("AddBook"))
            alert.setTitle("Ошибка добовления книги");
        else
            alert.setTitle("Ошибка изменения книги");

        alert.setHeaderText(null);
        alert.setContentText(message);
        alert.showAndWait();
    }

    private void handleAdd(String userId) {
        String title = titleField.getText();
        if (title == null || title.trim().isEmpty()) {
            showError("Вы не ввели название книги");
            return;
        }
        String author = authorField.getText();
        if (author == null || author.trim().isEmpty()) {
            showError("Вы не ввели автора");
            return;
        }
        String pagesText = pagesField.getText();
        int pages;
        try {
            if (pagesText == null || pagesText.trim().isEmpty()) {
                showError("Вы не ввели количество страниц");
                return;
            }
            pages = Integer.parseInt(pagesText.trim());
            if (pages < 0) {
                showError("Количество страниц не может быть меньше 0");
                return;
            }
        } 
        catch (NumberFormatException e) {
            showError("Количество страниц должно быть числом");
            return;
        }

        
        String genre = genreBox.getValue() != null ? genreBox.getValue() : "";
        String status = statusBox.getValue() != null ? statusBox.getValue() : "";
        String startDate = startDatePicker.getValue() != null ? startDatePicker.getValue().toString() : "";
        String endDate = endDatePicker.getValue() != null ? endDatePicker.getValue().toString() : "";
        String description = descriptionArea.getText() != null ? descriptionArea.getText() : "";
        
        Book book = new Book(title, author, genre, pages);

        UsersBooksManager usersBooksManager = new UsersBooksManager();
        BookManager bookManager = new BookManager();
        
        try {
            usersBooksManager.connect("library.db");
            bookManager.connect("library.db");
            int Id;
            Stage stage = (Stage) titleField.getScene().getWindow();

            if (whatFunction.equals("AddBook")){
                Boolean isBook1 = bookManager.exists("books", "title", title);
                Boolean isBook2 = bookManager.exists("books", "author", author);
                Boolean isBook3 = bookManager.exists("books", "pages", String.valueOf(pages));
                Boolean isBook4 = bookManager.exists("books", "genre", genre);
                if(!(isBook1 &&  isBook2 && isBook3 && isBook4)){
                    bookManager.addBook(book);
                    Id = bookManager.getBookId(book);
                    usersBooksManager.addUserBook(userId, Id, status, startDate, endDate, description);
                    stage.close();
                }
                else{
                    Id = bookManager.getBookId(book);
                    List<Integer> bookIds = usersBooksManager.getBooksId(userId);
                    Boolean isBookUser = bookIds.contains(Id);

                    if(!isBookUser){
                        usersBooksManager.addUserBook(userId, Id, status, startDate, endDate, description);
                        stage.close();
                    }
                    else
                        showError("У вас уже есть такая книга");
                }
            }   
            else{
                    bookManager.updateBook(book, bookId);
                    usersBooksManager.updateUserBook(userId, bookId, status, startDate, endDate, description);
                    stage.close();     
            }

        }
        catch (SQLException e) {
            System.err.println("Ошибка базы данных: " + e.getMessage());
        }
        finally {
            usersBooksManager.close();
            bookManager.close(); 
        }    
   }
}


