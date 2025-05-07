package com.example.Windows;

import java.sql.SQLException;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import com.example.DBmanager.BookManager;
import com.example.DBmanager.UsersBooksManager;
import com.example.Models.Book;

import javafx.beans.property.SimpleIntegerProperty;
import javafx.beans.property.SimpleStringProperty;
import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.geometry.Insets;
import javafx.geometry.Pos;
import javafx.scene.Scene;
import javafx.scene.control.Alert;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.SplitPane;
import javafx.scene.control.TableColumn;
import javafx.scene.control.TableView;
import javafx.scene.control.TextArea;
import javafx.scene.layout.BorderPane;
import javafx.scene.layout.Priority;
import javafx.scene.layout.VBox;
import javafx.stage.Stage;

public class HomeView extends BorderPane {

  private final String userId;
  private final ObservableList<Map<String, Object>> booksData = FXCollections.observableArrayList();
  private TableView<Map<String, Object>> booksTable;
  private Map<String, Object> selectedBook;
  private TextArea bookDetailsArea = new TextArea();

  public HomeView(Stage primaryStage, String userId) {
    this.userId = userId;

    setPadding(new Insets(15));

    // ===== Основной SplitPane =====
    SplitPane splitPane = new SplitPane();
    splitPane.setDividerPositions(0.5);
    
                     // ===== ЛЕВАЯ ПАНЕЛЬ (Список книг) =====
    VBox leftPanel = new VBox(10);
    leftPanel.setPadding(new Insets(10));
    
    // Заголовок
    Label booksLabel = new Label("Список книг");
    booksLabel.setStyle("-fx-font-size: 18px; -fx-font-weight: bold;");
    
    // Таблица книг
    booksTable = new TableView<>(booksData);
    booksTable.setColumnResizePolicy(TableView.CONSTRAINED_RESIZE_POLICY);
    
    // Колонки таблицы
    TableColumn<Map<String, Object>, String> titleCol = new TableColumn<>("Название");
    titleCol.setCellValueFactory(data ->
            new SimpleStringProperty(String.valueOf(data.getValue().getOrDefault("title", ""))));
    
    TableColumn<Map<String, Object>, String> statusCol = new TableColumn<>("Статус");
    statusCol.setCellValueFactory(data ->
            new SimpleStringProperty(String.valueOf(data.getValue().getOrDefault("status", ""))));
    
    TableColumn<Map<String, Object>, String> dataStartCol = new TableColumn<>("Начало чтения");
    dataStartCol.setCellValueFactory(data ->
            new SimpleStringProperty(String.valueOf(data.getValue().getOrDefault("dataStart", ""))));
    
    TableColumn<Map<String, Object>, String> dataEndCol = new TableColumn<>("Конец чтения");
    dataEndCol.setCellValueFactory(data ->
            new SimpleStringProperty(String.valueOf(data.getValue().getOrDefault("dataEnd", ""))));
    
    TableColumn<Map<String, Object>, Integer> idBookColumn = new TableColumn<>("IDBook");
    idBookColumn.setCellValueFactory(data ->
            new SimpleIntegerProperty((Integer) data.getValue().get("idBook")).asObject());
    idBookColumn.setVisible(false); // скрываем колонку
    
    // Добавляем колонки в таблицу
    booksTable.getColumns().addAll(titleCol, statusCol, dataStartCol, dataEndCol, idBookColumn);
    
    // Заполняем таблицу данными
    refreshBooksTable();
    
    // Обработка выбора строки
    booksTable.getSelectionModel().selectedItemProperty().addListener(
            (obs, oldSelection, newSelection) -> selectedBook = newSelection
    );
    
    leftPanel.getChildren().addAll(booksLabel, booksTable);
    VBox.setVgrow(booksTable, Priority.ALWAYS);

    
                  // ===== ПРАВАЯ ПАНЕЛЬ (Действия) =====
    VBox rightPanel = new VBox(20);
    rightPanel.setPadding(new Insets(10));
    rightPanel.setAlignment(Pos.TOP_CENTER);
    
    // Информация о пользователе
    Label userLabel = new Label("Пользователь: " + userId);
    userLabel.setStyle("-fx-font-size: 18px; -fx-font-weight: bold;");
    
    // Кнопки
    VBox buttonsPanel = new VBox(15);
    buttonsPanel.setAlignment(Pos.CENTER);
    
    // Кнопка "Добавить"
    Button addButton = new Button("Добавить книгу");
    addButton.setStyle("-fx-font-size: 14px; -fx-pref-width: 200px; -fx-pref-height: 40px;");
    addButton.setOnAction(e -> handleAddBook(primaryStage));
    
    // Кнопка "Обновить"
    Button updateButton = new Button("Редактировать");
    updateButton.setStyle("-fx-font-size: 14px; -fx-pref-width: 200px; -fx-pref-height: 40px;");
    updateButton.setOnAction(e -> handleUpdate(primaryStage));
    
    // Кнопка "Удалить"
    Button deleteButton = new Button("Удалить книгу");
    deleteButton.setStyle("-fx-font-size: 14px; -fx-pref-width: 200px; -fx-pref-height: 40px;");
    deleteButton.setOnAction(e -> handleDeleteBook());
    
    // Добавляем кнопки
    buttonsPanel.getChildren().addAll(addButton, updateButton, deleteButton);
    
                            // ===== Подробная информация о книге =====
    bookDetailsArea.setPromptText("Подробная информация о книге");
    bookDetailsArea.setEditable(false);
    bookDetailsArea.setWrapText(true); 
    bookDetailsArea.setPrefHeight(200); 
    booksTable.getSelectionModel().selectedItemProperty().addListener((obs, oldSelection, newSelection) -> {
      selectedBook = newSelection;
      if (newSelection != null) 
        updateBookDetails(); 
      else
        bookDetailsArea.clear();
    });

    // Кнопка "Выход"
    Button exitButton = new Button("Выйти");
    exitButton.setStyle("-fx-font-size: 14px; -fx-pref-width: 100px; -fx-pref-height: 20px;");
    exitButton.setOnAction(e -> handleExit(primaryStage));

    // Добавляем на правую панель
    rightPanel.getChildren().addAll(userLabel, buttonsPanel, bookDetailsArea, exitButton);
    
    // ===== Сборка интерфейса =====
    splitPane.getItems().addAll(leftPanel, rightPanel);
    setCenter(splitPane);    
  }

  private Map<String, Object> getAllInformation(){
    Map<String, Object> information = new HashMap<String,Object>();
    UsersBooksManager usersBooksManager = new UsersBooksManager();
    BookManager bookManager = new BookManager();
    int bookID = (int) selectedBook.get("idBook");
    try {
      usersBooksManager.connect("library.db");
      bookManager.connect("library.db");
      List<List<String>> userBooks = usersBooksManager.getUserInformation(userId);
      Book book = bookManager.getBook(bookID);
      for (List<String> userBook : userBooks) {
        if(userBook.get(0).equals(Integer.toString(bookID))){
          information.put("status",userBook.get(1));
          information.put("dateStart",userBook.get(2));
          information.put("dateEnd",userBook.get(3));
          information.put("description", userBook.get(4));
          break;
        }
      }
      information.put("title",book.getTitle());
      information.put("author",book.getAuthor());
      information.put("genre",book.getGenre());
      information.put("pages",book.getPages());
      information.put("bookId", bookID);    
    }
    catch (SQLException e) {
      System.err.println("Ошибка при работе с базой данных: " + e.getMessage());
    } 
    finally {
      usersBooksManager.close();
      bookManager.close();
    }
    return information;
  }

  private void refreshBooksTable() {
    UsersBooksManager usersBooksManager = new UsersBooksManager();
    BookManager bookManager = new BookManager();

    try {
      usersBooksManager.connect("library.db");
      bookManager.connect("library.db");

      booksData.clear();

      List<List<String>> userBooks = usersBooksManager.getUserInformation(userId);

      for (List<String> userBook : userBooks) {
        int bookId = Integer.parseInt(userBook.get(0));
        Book book = bookManager.getBook(bookId);

        Map<String, Object> bookData = new HashMap<>();
        bookData.put("title", book.getTitle());
        bookData.put("status", userBook.get(1));
        bookData.put("dataStart", userBook.get(2));
        bookData.put("dataEnd", userBook.get(3));
        bookData.put("idBook", bookId);

        booksData.add(bookData);
      }

    } 
    catch (SQLException e) {
      System.err.println("Ошибка при работе с базой данных: " + e.getMessage());
    } 
    finally {
      usersBooksManager.close();
      bookManager.close();
    }
  }

  private void updateBookDetails(){
    Map<String, Object> information = getAllInformation();
    StringBuilder details = new StringBuilder();
    details.append("Название: ").append(information.getOrDefault("title", "")).append("\n");
    details.append("Статус: ").append(information.getOrDefault("status", "")).append("\n");
    details.append("Автор: ").append(information.getOrDefault("author", "")).append("\n");
    details.append("Жанр: ").append(information.getOrDefault("genre", "")).append("\n");
    details.append("Количество страниц: ").append(information.getOrDefault("pages", "")).append("\n");
    details.append("Дата начала чтения: ").append(information.getOrDefault("dateStart", "")).append("\n");
    details.append("Дата окончания чтения: ").append(information.getOrDefault("dateEnd", "")).append("\n");
    details.append("Описание: ").append(information.get("description")).append("\n");
    bookDetailsArea.setText(details.toString());
  }



  private void handleAddBook(Stage primaryStage) {
    Stage addBookStage = new Stage();
    addBookStage.setTitle("Добавление книги");
    BookView addBookView = new BookView(userId, "AddBook");
    addBookStage.setScene(new Scene(addBookView, 400, 600));
    addBookStage.initOwner(primaryStage);
    addBookStage.setOnHidden(e -> refreshBooksTable());
    addBookStage.showAndWait(); 
  }
 
  private void handleDeleteBook() {
    if (selectedBook == null) {
      Alert alert = new Alert(Alert.AlertType.WARNING);
      alert.setTitle("Ошибка");
      alert.setHeaderText(null);
      alert.setContentText("Выберите книгу для удаления");
      alert.showAndWait();
      return;
    }

    else{
      UsersBooksManager usersBooksManager = new UsersBooksManager();
      BookManager bookManager = new BookManager();
      int bookID = (int) selectedBook.get("idBook");
      try {
        usersBooksManager.connect("library.db");
        bookManager.connect("library.db");
        
        usersBooksManager.deleteUserBook(userId, bookID);
        refreshBooksTable();

        if (!usersBooksManager.exists("users_books", "book_id", bookID))
          bookManager.deleteBook(bookID);    
      }
      catch (SQLException e) {
        System.err.println("Ошибка при работе с базой данных: " + e.getMessage());
      } 
      finally {
        usersBooksManager.close();
        bookManager.close();
      }
    }


  }
  
  private void handleUpdate(Stage primaryStage) {
    if (selectedBook == null) {
      Alert alert = new Alert(Alert.AlertType.WARNING);
      alert.setTitle("Ошибка");
      alert.setHeaderText(null);
      alert.setContentText("Выберите книгу редактикования");
      alert.showAndWait();
      return;
    }
    Map<String, Object> information = getAllInformation();
    Stage updateBookStage = new Stage();
    updateBookStage.setTitle("Редактирование книги");
    BookView updateBookView = new BookView(userId, information);
    updateBookStage.setScene(new Scene(updateBookView, 400, 600));
    updateBookStage.initOwner(primaryStage);
    updateBookStage.setOnHidden(e -> refreshBooksTable());
    updateBookStage.showAndWait(); 
  }

  private void handleExit(Stage primaryStage) {
    try {
      LoginView loginView = new LoginView(primaryStage);
      Scene scene = new Scene(loginView, 1000, 500);
      primaryStage.setScene(scene);
    } 
    catch (Exception e) {
        System.err.println("Ошибка загрузки интерфейса входа: " + e.getMessage());
    }
  }
}
