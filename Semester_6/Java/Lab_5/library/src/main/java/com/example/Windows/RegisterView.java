package com.example.Windows;

import java.io.IOException;
import java.sql.SQLException;

import com.example.DBmanager.UserManager;

import javafx.geometry.Insets;
import javafx.geometry.Pos;
import javafx.scene.Scene;
import javafx.scene.control.Alert;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.PasswordField;
import javafx.scene.control.TextField;
import javafx.scene.layout.ColumnConstraints;
import javafx.scene.layout.GridPane;
import javafx.scene.layout.HBox;
import javafx.scene.layout.VBox;
import javafx.stage.Stage;
;

public class RegisterView extends VBox {
    private final TextField loginField = new TextField();
    private final PasswordField passwordField = new PasswordField();
    private final UserManager db = new UserManager();

    RegisterView(Stage primaryStage) {
        // Основные настройки layout
        setAlignment(Pos.CENTER);
        setSpacing(20);
        setPadding(new Insets(20));

        // Создание элементов интерфейса
        Label titleLabel = new Label("Регистрация");
        titleLabel.setStyle("-fx-font-size: 20px; -fx-font-weight: bold;");

        // Сетка для полей ввода
        GridPane inputGrid = new GridPane();
        inputGrid.setHgap(10);
        inputGrid.setVgap(10);
        inputGrid.setAlignment(Pos.CENTER);

        // Настройка колонок
        ColumnConstraints col1 = new ColumnConstraints();
        col1.setHalignment(javafx.geometry.HPos.RIGHT);
        col1.setMinWidth(100);

        ColumnConstraints col2 = new ColumnConstraints();
        col2.setHalignment(javafx.geometry.HPos.LEFT);
        col2.setMinWidth(200);

        inputGrid.getColumnConstraints().addAll(col1, col2);

        // Добавление полей ввода в сетку
        inputGrid.add(new Label("Логин:"), 0, 0);
        loginField.setPromptText("Введите логин");
        inputGrid.add(loginField, 1, 0);

        inputGrid.add(new Label("Пароль:"), 0, 1);
        passwordField.setPromptText("Введите пароль");
        inputGrid.add(passwordField, 1, 1);

        // Панель кнопок
        HBox buttonBox = new HBox(20);
        buttonBox.setAlignment(Pos.CENTER);

        Button nextButton = new Button("Далее");
        nextButton.setStyle("-fx-min-width: 100px; -fx-base: #0096c9;");
        nextButton.setOnAction(e -> handleNext(primaryStage));

        Button backButton = new Button("Назад");
        backButton.setStyle("-fx-min-width: 100px;");
        backButton.setOnAction(e -> handleBack(primaryStage));

        buttonBox.getChildren().addAll(nextButton, backButton);

        // Добавление всех элементов в основной layout
        getChildren().addAll(titleLabel, inputGrid, buttonBox);
    }

    private void showError(String message) {
        Alert alert = new Alert(Alert.AlertType.ERROR);
        alert.setTitle("Ошибка регистрации");
        alert.setHeaderText(null);
        alert.setContentText(message);
        alert.showAndWait();
    }

    private void showHomeScreen(Stage primaryStage, String login) throws IOException {
        HomeView homeView = new HomeView(primaryStage, login);
        Scene scene = new Scene(homeView, 1000, 500);
        primaryStage.setScene(scene);
    }

    private void showLoginScreen(Stage primaryStage) throws IOException {
        LoginView loginView = new LoginView(primaryStage);
        Scene scene = new Scene(loginView, 1000, 500);
        primaryStage.setScene(scene);
    }



    private void handleNext(Stage primaryStage) {
        String login = loginField.getText().trim();
        String password = passwordField.getText().trim();

        if (login.isEmpty() || password.isEmpty()) {
            showError("Логин и пароль не могут быть пустыми");
            return;
        }

        try {
            db.connect("library.db");
            boolean userExists = db.addUser(login, password);

            if (userExists) {
                showHomeScreen(primaryStage, login);
            } 
            else 
                showError("Пользователь с таким логином уже существует");
            
        } 
        catch (SQLException e) {
            System.err.println("Ошибка базы данных: " + e.getMessage());
        } 
        catch (IOException e) {
            System.err.println("Ошибка загрузки интерфейса: " + e.getMessage());
        } 
        finally {
            db.close();
        }
    }

    private void handleBack(Stage primaryStage) {
        try {
            showLoginScreen(primaryStage);
        } 
        catch (IOException e) {
            System.err.println("Ошибка загрузки интерфейса входа: " + e.getMessage());
        }
    }

 
}